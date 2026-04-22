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

Software development possesses six epistemic properties that collectively establish it as AAD's **privileged high-identifiability calibration laboratory** — the domain where AAD's quantitative machinery can be most cleanly grounded, and from which other domains inherit under explicitly-stated transfer assumptions.

## Formal Expression

*[Observation (software-epistemic-properties)]*

Six properties distinguish software development from other adaptive domains. Each is stated with its AAD-theoretic consequence.

**P1. Codebase inspectability (not full environment).** The *codebase component* of the environment state $\Omega_t$ — source code, tests, build artifacts, version history — is fully observable in principle. Partial observability *of the codebase* arises from the agent's limited attention and comprehension bandwidth, not from the environment hiding state. Formally: the observation function $h$ restricted to code-reading channels is lossy because of cognitive limits on the agent side, not because the codebase is physically inaccessible.

$$U_o^{\text{(code)}} = f(\text{agent bandwidth}) \quad \text{not} \quad f(\text{environment opacity})$$

**Scope.** This applies to the codebase component of $\Omega_t$, not to the full software development environment. The full $\Omega_t$ extends beyond the codebase: deployment infrastructure and runtime state (partially observable via logs and metrics), user populations and their behavior (sampled observability), team context and stakeholder intent (conversational and often unrecorded), market conditions (external and partially adversarial). These non-codebase components have the standard POMDP partial observability that most domains share. The distinctive AAD-relevant property of software is that the codebase — *the part of the environment the agent directly manipulates* — is fully inspectable. Restricting $\Omega$ to source code when reasoning about disturbance rate $\rho$ systematically underestimates disturbance; the theory should be applied to codebase-disturbance and non-codebase-disturbance separately.

*Consequence:* The observation uncertainty $U_o$ for code-reading channels is under the agent's (and previous agents') partial control — unlike most domains where $U_o$ is set by physics. This enables P6 below. The corresponding claim does not generalize to non-codebase channels, where $U_o$ behaves as in other domains.

**P2. Executable counterfactuals (scoped Level 3 access).** Version control provides literal Pearl Level 3 counterfactual execution ( #pearl-causal-hierarchy) for a specific and well-defined class of questions: **code-internal counterfactuals with deterministic outcomes.** For questions of the form "what would the test suite report if implementation X had been chosen instead of Y, holding the test suite and environment fixed?", `git checkout` plus re-implementation plus test execution is not a proxy — it is literal counterfactual realization with ground-truth verification. The domain is the codebase itself; the intervention is on code; the outcome is on code behavior; the verification is the test suite.

This literal Level 3 access fails for a complementary class: **counterfactuals crossing the agent-environment boundary** — questions about what feature sequence the team would have produced, how the market would have responded, or how a different developer would have proceeded. These are path-dependent on external events that cannot be replayed. For this second class, `git checkout` is a strong executable proxy, not literal Level 3.

The distinction is sharp because it separates identifiable regimes: code-internal tests are deterministic functions of code (Level 3 literal); agent-coupled questions require the past trajectory of external events (Level 3 proxy at best). No other AAD domain offers literal Level 3 on *any* non-trivial class of questions.

*Consequence:* Model class fitness $\mathcal{F}(\mathcal{M})$ ( #model-class-fitness) becomes empirically measurable *for the code-internal regime*: fork at a past decision point, try an alternative architecture, run the same test suite and benchmarks, and measure whether it achieves higher sufficiency on those deterministic targets. For the agent-coupled regime, measurement requires the proxy interpretation with its path-dependence caveats (see discussion below).

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

**P5. Exact recording of the committed-state subset; conditional maximality.** The chronica $\mathcal{C}_t$ ( #chronica) is the complete sequence $(o_1, a_1, \ldots, a_{t-1}, o_t)$ of agent–environment interactions. Within $\mathcal{C}_t$, define the *committed-state subset* $\mathcal{C}_t^{\text{commit}} \subseteq \mathcal{C}_t$ as the sequence of git-recorded committed codebase state transitions, with their timestamps, signed authorship, and immutable diffs.

*[Empirical Claim]* $\mathcal{C}_t^{\text{commit}}$ is recorded by git **without information loss within its scope**: each commit is content-addressed (cryptographically immutable), authorship is cryptographically attributable (signed commits / verified GPG / sigstore), retrieval is via a universally standardized protocol (git), and the canonical history is mainline-bounded (`git log <main>`). The complementary subset $\mathcal{C}_t \setminus \mathcal{C}_t^{\text{commit}}$ — uncommitted edits, IDE edit traces, build-system invocations, test runs, runtime logs, monitoring alerts, code-review threads, deployment events, out-of-band coordination — is captured only by other tools or not at all (see #developer-as-act-agent for the channel enumeration).

*[Empirical Claim — conditional maximality]* Under the scope conditions of cryptographic immutability, cryptographic authorship attribution, standard universal retrieval, and mainline-bounded scope, $\mathcal{C}_t^{\text{commit}}$ is the *unique maximal* exteriorized subset of $\mathcal{C}_t$ in software: no candidate exteriorization (CI logs, PR review threads, IDE telemetry, issue trackers, chat transcripts, production telemetry) under current standard team protocols satisfies all four conditions, and any subset that does is contained in $\mathcal{C}_t^{\text{commit}}$.

The chronica is, by definition, the record of interactions between agent and environment — not the agent's internal reasoning. What git additionally does *not* record is orthogonal to $\mathcal{C}_t^{\text{commit}}$: the agent's internal model state $M_t$, strategy DAG $\Sigma_t$, or objective $O_t$. These are agent-internal and not part of the chronica by any domain's definition. Commit messages and PR descriptions are partial exteriorizations of $M_t$/$G_t$ intent, only to the extent the agent chose to verbalize them.

*Consequence — quantities exactly computable from $\mathcal{C}_t^{\text{commit}}$.* The following AAD- and TST-relevant estimators are exact functions of $\mathcal{C}_t^{\text{commit}}$, and hence are exactly recoverable from git with no sampling loss and no recall bias *as estimators of their own definitions*:

- **TST operational quantities** (definitionally on the commit stream): system coupling ( #system-coupling) as the co-change conditional probability; system coherence ( #system-coherence) as intra-module change-proximity; the coherence-coupling measurement Q ( #coherence-coupling-measurement); per-commit `#atomic-changeset` size (lines / files / modules); the change-distance hierarchy ( #change-distance) on within-commit diffs; the change-expectation baseline $\hat n_{\text{future}} = n_{\text{past}}$ ( #change-expectation-baseline) under the commit / merge operationalization of "feature."
- **Causal-discovery substrate** ( #causal-discovery-from-git): the interventional record (each commit *is* a $do(\cdot)$ on the codebase; the set of interventions is exactly the commit stream), temporal-precedence priors over interventions, frequency-asymmetry signals between file pairs, intervention-contrast signals (commits changing $A$ alone vs $A$ with $B$).
- **Multi-agent observable structure**: co-authorship matrix per file, per-author commit-rate, co-author co-change matrix.

For these quantities, the original "without information loss" claim is preserved: estimator = exact git-derivable function, with $\mathcal{C}_t^{\text{commit}}$ as the maximal exteriorized substrate under the scope conditions above.

*Consequence — quantities not exactly computable from $\mathcal{C}_t^{\text{commit}}$ alone.* AAD-core quantities defined over the full agent-environment loop — environmental disturbance rate $\rho$ (full chronica, including production incidents and dependency breaks), adaptive tempo $\mathcal T$, update gain $\eta^\ast$, mismatch signal $\delta_t$, observation noise $U_o^{(k)}$, strategic disturbance rate $\rho_\Sigma$ — and Section III multi-agent quantities — epistemic / teleological / strategic unity, communication gain, composition closure $\varepsilon^\ast$ — are *not* exactly computable from $\mathcal{C}_t^{\text{commit}}$ alone. They require additional instrumentation (CI logs, monitoring telemetry, code-review tooling, agent reasoning traces) and / or agent-internal access. For these, git provides at best a partial substrate (one channel of the disturbance source for $\rho$; one observable for cross-agent coupling), and the gap is empirical.

*Consequence — estimator quality for AAD-core quantities is a separate question.* For the EXACT-class TST estimators above, exactness of computation does not by itself imply they are good estimators of the AAD-core quantities they are sometimes used to inform. The co-change conditional probability is exactly equal to its own definition; whether it equals the causal coupling $P(\text{change}(m_j) \mid do(\text{change}(m_i)))$ is regime-conditional and treated in #causal-discovery-from-git (atomic commits / asymmetric co-change / explicit confounder adjustment → strong; otherwise → useful descriptive statistic).

**P6. Agent-controlled observation quality.** Code quality IS observation channel quality. Well-written code with clear naming has low $U_o$ for the code-reading channel; obfuscated code has high $U_o$. Agents can improve their own future observation channels by writing better code — a feedback loop within the feedback loop.

*Consequence:* The agent's environment-modifying actions at time $t$ affect the observation function $h$ at time $t+k$, creating a second-order dynamic where current code quality investments compound into future adaptive capacity via $U_o \to \eta^\ast \to \mathcal{T}$. See #code-quality-as-observation-infrastructure.

### Software as AAD's calibration laboratory; transfer to other domains

*[Formulation (software-calibration-lab)]*

The six properties collectively warrant positioning software as the **privileged high-identifiability calibration laboratory** for AAD, not as a generic "best operationalization domain." The distinction matters: "richest operationalization domain" is a comparative superlative without a principled yardstick; "calibration laboratory" is a specific architectural role — it is the domain where quantitative forms of AAD's machinery can be grounded because each load-bearing identification assumption is cleanly satisfied, and other domains inherit AAD's results under explicitly-named transfer assumptions to specified each identification relaxation.

**What "calibration laboratory" means concretely.** For each AAD-core quantity that requires an identification condition to be sharpened from *defined* to *operationally extractable*, software provides the configuration where the condition is most cleanly satisfied. Concretely:

| AAD-core quantity | Identification condition | Software configuration | Non-software transfer requirement |
|---|---|---|---|
| Intervention effect $P(\cdot \mid do(a))$ ( #pearl-causal-hierarchy) | Action is a literal intervention on the target variable | Tests/deploys/`git bisect` realize literal $do(\cdot)$ on code state (P3) | Approximate intervention-as-observation with explicit confounding adjustment (Regime B/C, #edge-update-causal-validity) |
| Counterfactual outcome $Y_{a}$ | Deterministic outcome function, reproducible environment | `git checkout` + re-execution on fixed test suite realizes literal Level 3 (P2, code-internal regime) | Proxy via structural model + path-dependent external event reconstruction (P2 agent-coupled regime) |
| Causal DAG structure ($\Sigma_t$, $M_t$ causal skeleton) | Structure observable or declared | Import graphs, type systems, API contracts partially declare structure (P4) | Causal discovery from observational data with identifiability conditions; typically weaker |
| Exteriorized chronica subset $\mathcal{C}_t^{\text{commit}}$ (P5) | Cryptographic immutability + attribution + universal retrieval + mainline-bounded scope | Git commits satisfy all four under current standard protocols | Sampled rather than exteriorized; recall bias in event logs, survey instruments, interview reconstruction |
| Observation function $h$ controllability (P6) | Agent can modify its own sensing channels | Code quality IS $h$-quality for code-reading channels | Fixed by physics or external infrastructure; agents cannot improve their own sensors |

**The calibration-lab framing prevents three systematic overclaim patterns.**

1. **Domain generalization by default.** Quantitative claims calibrated in software (e.g., the $\alpha \approx 0.118$ exponential-cognitive-load coefficient derived from git analysis) are not automatically claims about human cognition or agent dynamics generally — they are claims about software-calibrated dynamics, which can be exported to other domains only with additional assumptions explicitly stated.

2. **Identification assumptions treated as universal.** The intervention-as-$do(\cdot)$ identification that holds strongly in software (P3, Regime A) weakens significantly in organizational settings (Regime B) and operates as observation-only (Regime C) in most social domains. A TST result that invokes interventional identification is software-calibrated; exports require the domain to provide the same identification or to accept the biased-estimator form.

3. **Chronica completeness treated as definitional.** The P5 conditional-maximality result — where $\mathcal C_t^{\text{commit}}$ is the unique maximal exteriorized subset under current standard protocols — is a software-specific result. Other domains lack universal content-addressed cryptographic recording; any AAD-core quantity that is exactly computable from the committed-state subset in software is approximate in proportion to recording-fidelity loss elsewhere.

**Implication for TST's rhetorical posture.** TST's load-bearing claims are *about software under high-identifiability conditions* — not about agents, development, or adaptive systems in general. Transfer to other domains requires the analyst to name which property (P1–P6) the target domain shares, which it approximates, and which it lacks, and to accept the corresponding strengthening or weakening of the operational conclusion. This is not a concession; it is a clarification that strengthens TST's defensibility by making its scope explicit.

**Relation to #developer-as-act-agent.** The developer-as-AAD-agent mapping exists under software's identification conditions; claims about developer cognition calibrated via that mapping inherit the calibration-lab scope. Exports to human cognition generally (outside software development) require the analyst to specify which of the six properties holds in the target setting.

## Epistemic Status

The individual properties P1–P4, P6 are *observations* — empirical features of the software development domain, not derived from AAD. P5's within-scope exactness and conditional-maximality claims are at *empirical claim* tier (see the per-clause tagging in P5). The calibration-laboratory framing and the transfer-assumption table above are *formulation* — a principled architectural positioning of TST within AAD, derived from the six properties + the requirement that quantitative AAD claims be cleanly grounded somewhere, not itself a theorem.

The calibration-lab framing replaces an earlier "richest operationalization domain" framing that was comparative without a principled yardstick. The new framing asserts a specific architectural role — software is where AAD's identification conditions can be most cleanly satisfied, and other domains inherit under explicit transfer assumptions — which is defensible on each property-by-property basis rather than requiring a systematic domain comparison.

Max attainable: the calibration-lab framing can reach *robust qualitative* once the transfer-assumption table is verified domain-by-domain (which properties apply, which approximate, which are absent) for at least two or three non-software domains (biological, organizational, financial). Full *exact*-tier formalization would require a uniqueness argument showing that software's configuration is the unique satisfying assignment for all six properties under current standard practice — interesting but not obviously achievable. The individual domain observations (P1–P6) remain at *discussion-grade* and *empirical* tiers as before.

## Discussion

**The inspectability distinction (P1) is load-bearing.** Most AAD domains are POMDPs because the environment hides state. Software is a POMDP because the *agent* cannot attend to all state simultaneously. This means observation quality improvements are possible by restructuring the environment (the codebase) rather than by building better sensors. The observation function $h$ is partially a design choice, not a physical constraint. This fundamentally changes the adaptive dynamics: the agent can invest in improving $h$ itself, not just in improving $M_t$ given a fixed $h$.

**P2 regime boundary.** The literal Level 3 scope is narrower than the full replay problem. Literal counterfactual realization requires: (a) the intervention is expressible as a code state change, (b) the outcome is a deterministic function of code state (test result, type-check, benchmark on fixed inputs), and (c) the environment between code and outcome is reproducible (fixed test suite, fixed dependencies, pinned inputs). When all three hold, `git checkout` + reimplementation + test execution gives literal Level 3 with ground-truth verification; when any fails, the same procedure provides an executable proxy.

Path-dependence breaks (c): if we want to know how the *feature sequence* would have evolved under an alternative architecture, the counterfactual feature requests depend on how users and the team responded to the architecture historically — none of which is replayable. Re-implementation cost breaks nothing formally but introduces *effective* limits: replaying 1000 features under alternative architectures is expensive enough that partial replay (10-50 representative features) is the operational practice. Even partial replay on the code-internal regime provides far more information than model-based speculation — and it is still literal Level 3 for each replayed instance, not a proxy.

**P5 and the instrumentation boundary.** The exact-recording claim of P5 separates into three pieces: (i) within-scope exactness — $\mathcal{C}_t^{\text{commit}}$ is recorded by git without information loss, with cryptographic immutability, cryptographic authorship, and standardized universal retrieval; (ii) conditional maximality — under the scope conditions stated in P5, $\mathcal{C}_t^{\text{commit}}$ is the unique maximal exteriorized subset of $\mathcal{C}_t$ in software; (iii) per-quantity exactness — the TST operational quantities ( #system-coupling, #system-coherence, #coherence-coupling-measurement, #change-distance, per-commit `#atomic-changeset` size, the asymmetric and contrast signals from #causal-discovery-from-git, co-authorship structure) are *exact* functions of $\mathcal{C}_t^{\text{commit}}$ and inherit all three properties.

The remainder of the chronica — uncommitted work, IDE telemetry, runtime observations, build/test traces, monitoring alerts, code-review discussion, out-of-band coordination — is captured only by other tools or not at all, and the level of capture varies by team and tooling. *Agent-internal* content (why a particular intervention was chosen; which beliefs drove it) is not part of the chronica in any domain and therefore not in git's scope. Commit messages and PR descriptions are partial exteriorizations of agent intent; their quality varies by authorial discipline.

This is relevant for #causal-discovery-from-git in two senses: (a) the *interventional* record over $\mathcal{C}_t^{\text{commit}}$ is complete (each commit is exactly one $do(\cdot)$ event with all the inputs the do-operator requires), and the temporal-precedence and frequency-asymmetry signals it derives are also exact; (b) the *causal* interpretation of estimators built on this exact substrate (whether the co-change matrix recovers the causal coupling) remains regime-conditional on confounders that depend partly on agent-internal state (developer knowledge state, etc.), as #causal-discovery-from-git documents. Treating $\mathcal{C}_t^{\text{commit}}$-derived TST quantities as estimators of their *own definitions* is exact; treating them as estimators of *AAD-core full-chronica quantities* is an empirical bridging step, not a definitional identity.

**Multi-agent amplification.** P5 (exact committed-state record) combined with P6 (agent-controlled observation quality) creates a distinctive multi-agent dynamic: agents can externalize parts of $M_t$ into the environment (documentation, clear naming, architecture decisions) where future agents can observe it. This converts ephemeral model state into persistent environmental state — the agent writes its model into $\Omega$ so that future agents can reconstruct $M_t$ through observation. The quality of this externalization determines how much of the previous agent's model survives turnover, and directly affects #comprehension-time for subsequent agents.

## Working Notes

- P1 says the environment is inspectable *in principle*, but for large codebases the cost of full inspection may exceed the agent's available time. There may be a useful formalization of "effective observability" that accounts for the agent's time budget — something like $U_o^{\text{eff}} = U_o^{\text{intrinsic}} + f(\lvert\Omega\rvert / \text{budget})$. This connects to #information-bottleneck: the agent must compress because full observation is too expensive, even though it is in principle available.
- The "feedback loop within the feedback loop" (P6) is the most theoretically interesting property. It creates a self-referential dynamic where the adaptive cycle's own outputs modify its future inputs. AAD's current formulation allows action-dependent observation ($o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$), but the cumulative effect of many past actions on $h$ is a longer-timescale phenomenon. Whether this requires extending AAD or is already captured by the existing formalism (with $h$ treated as slowly varying) is an open question.
- The table in P3 invites a formal treatment: given the $(\nu, U_o)$ profile per channel and the agent's current $U_M$, what is the CIY-optimal sequencing of probes? This would be a concrete worked example for #causal-information-yield applied to software.
- The conditional-maximality argument in P5 is structural (a property-table walk over enumerated candidates rather than a fully formal uniqueness theorem), held at *Empirical Claim* tier. A tighter formal treatment would identify the precise property axioms (immutability, authorship, retrieval-standard, mainline-bound) and prove uniqueness as a theorem. In principle a research-grade signed-and-content-addressed CI log could compete; under current standard team protocols, none does — hence the "current standard team protocols" scoping.
