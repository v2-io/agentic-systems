---
slug: scope-developer-agent
type: scope
status: axiomatic
depends:
  - scope-software
  - obs-software-epistemic-properties
  - def-agent-environment
  - form-agent-model
  - def-observation-function
  - def-action-transition
  - form-complete-agent-state
  - emp-update-gain
  - def-mismatch-signal
  - scope-logogenic-agent
  - def-coupled-update-dynamics
  - obs-context-turnover
stage: draft
---

# Scope: Developer Agent

AAD's developer-scope encompasses human and AI developers acting on a codebase: $X_t = (M_t, G_t)$ where $M_t$ is the developer's understanding of the codebase, and $G_t = (O_t, \Sigma_t)$ decomposes into feature/fix objectives and implementation strategy.

## Formal Expression

*[Scope (scope-developer-agent)]*

A software developer is an actuated adaptive agent ( #def-agent-environment) whose state, environment, and coupling are:

### Environment ($\Omega_t$)

The full state external to the developer's cognition:

| Component | Change driver | Observability |
|-----------|--------------|---------------|
| Codebase source | Developer edits, CI, other developers | High (git, IDE) |
| Runtime behavior | Deployment, config, load, dependencies | Medium (logs, monitoring, tests) |
| User requirements | Stakeholder decisions, market shifts | Low–medium (conversations, tickets) |
| Team knowledge | People joining/leaving, learning | Low (implicit, distributed) |
| Dependency ecosystem | Upstream releases, deprecations, CVEs | Medium (package managers, advisories) |
| Infrastructure state | Cloud changes, scaling events, failures | Medium (dashboards, alerts) |

The full $\Omega_t$ is larger than "the codebase." Many mismatch events (production incidents, requirement changes, dependency breaks) originate outside the codebase proper. Treatments that restrict $\Omega$ to source code systematically underestimate the disturbance rate $\rho$.

### Model ($M_t$)

*[Definition (developer-model)]*

The developer's internal model — the epistemic substate ( #form-agent-model):

**Human developer:**
- Mental model of architecture and module boundaries
- Knowledge of coding conventions and patterns
- Understanding of business domain and requirements
- Expectations about runtime behavior
- Beliefs about which areas are stable vs. volatile
- Trust calibration for other team members' code

**AI agent:**
- In-context understanding from files read this session
- Patterns inferred from code structure
- Instructions from system prompts, memory files, documentation
- Inferences from error messages, test output, tool responses

For AI agents, $M_t$ is more explicitly representable (context window contents plus persistent storage), making it closer to a directly observable quantity — though with a Class 2 / $\kappa_{\text{processing}} \approx 1$ caveat: the goal tokens (system prompt, task description) shape the agent's effective beliefs through joint forward-pass processing rather than separable epistemic processing. The "explicit representability" is a representational convenience for the analyst, not a guarantee of architectural separation. See #scope-logogenic-agent for the Class 2 architectural classification, and #def-coupled-update-dynamics for the coupled update dynamics that replace the factored form for Class 2 agents.

### Objective ($O_t$)

*[Definition (developer-objective)]*

The developer's current objective — what the agent wants:

$$O_t \in \{\text{implement feature } F,\; \text{fix bug } B,\; \text{refactor module } R,\; \text{investigate incident } I,\; \ldots\}$$

$O_t$ induces a value functional $V_{O_t}$ ( #form-objective-functional) over codebase states. For Class 1 (modular) developer-agents — the canonical human-developer case — objective revision occurs via the orient cascade ( #der-orient-cascade) with sequential epistemic-then-purposeful processing: e.g., while implementing feature $F$, the developer discovers a blocking bug and revises $O_t$ from "implement $F$" to "fix blocker, then implement $F$." For Class 2 logogenic developer-agents (LLM-based), the cascade does not hold as a derived result — instead, the coupled update dynamics ( #def-coupled-update-dynamics) apply, with the cascade quantities ($M_t$ update, $\Sigma_t$ revision, $O_t$ feasibility check) recoverable post-hoc from the coupled response by analytical decomposition rather than enforced by the processing architecture.

### Strategy ($\Sigma_t$)

*[Definition (developer-strategy)]*

The developer's implementation plan — how the agent intends to achieve $O_t$:

$$\Sigma_t = \text{plan decomposition of } O_t \text{ into subtasks with dependency and confidence structure}$$

In AAD terms, $\Sigma_t$ is a probabilistic causal DAG ( #def-strategy-dag) whose nodes are subtasks and whose edges carry confidence weights $p_{ij}$ representing the developer's belief that completing subtask $i$ enables subtask $j$. Examples:

- "First understand the data model, then modify the schema, then update the API, then update the UI" — a chain DAG
- "Either refactor the existing handler OR write a new one, then integrate" — an OR-node DAG
- "Add database migration AND update the ORM AND update the tests" — an AND-node

### Observation channels ($\mathcal{O}$)

*[Definition (developer-observation-channels)]*

Two classes of channels, distinguished by trigger:

**Passive channels** (environment-initiated or always-on):

| Channel $k$ | Rate $\nu^{(k)}$ | Noise $U_o^{(k)}$ | Information type |
|-------------|-------------------|---------------------|------------------|
| Compiler/linter | Per-save | Very low | Syntactic/type correctness |
| CI pipeline | Per-push | Low | Integration correctness |
| Runtime logs | Continuous | Medium | System behavior |
| Monitoring alerts | Event-driven | Low–medium | Operational mismatch |
| Bug reports | Sporadic | High | Behavioral mismatch |
| Code review | Per-PR | Medium–high | Quality, convention, intent |

**Active channels** (agent-initiated exploration and probes):

| Channel $k$ | Rate $\nu^{(k)}$ | Noise $U_o^{(k)}$ | Information type |
|-------------|-------------------|---------------------|------------------|
| Code reading | Per-navigation | Variable (depends on code quality — P6) | Architecture, logic, intent |
| Test execution | Per-run | Low | Behavioral correctness |
| Documentation lookup | Per-query | Medium | Design intent, API contracts |
| Colleague query | Per-interaction | Medium–high | Compressed external $M$ |

The distinction matters for gain calibration. Passive channels have well-characterized $U_o$ (compiler output is near-deterministic); active channels have $U_o$ that depends on what is being explored and the quality of the target ( #obs-software-epistemic-properties, P6).

### Action space ($\mathcal{A}$)

*[Definition (developer-actions)]*

Four classes of developer actions, distinguished by purpose:

1. **Exploration** — directed attention to generate observations: read a file, trace a code path, browse git history. These are actions whose purpose is to build $M_t$, not to modify $\Omega_t$.

2. **Interventional probes** — actions that temporarily perturb $\Omega_t$ to learn from the response: run tests, add a print statement, make a speculative change. These are $do(\cdot)$ operations providing Level 2 information ( #def-pearl-causal-hierarchy).

3. **Queries** — accessing pre-compressed external models: ask a colleague, search documentation, consult an AI assistant. These access another agent's $M$ that has already extracted structure from raw observations. A single well-targeted query can carry CIY orders of magnitude higher than individual environment probes ( #def-causal-information-yield).

4. **Environment modification** — changing $\Omega_t$: write/edit/delete code, modify configuration, deploy. A subset of these are *observation-infrastructure investments* — actions that modify $\Omega_t$ in ways that improve future observation quality (write tests, add logging, improve naming). See #der-code-quality-as-observation-infrastructure.

### Mismatch signal ($\delta_t$)

*[Derived (developer-mismatch, from mismatch-signal applied to software)]*

Every moment of developer surprise is a mismatch signal ( #def-mismatch-signal):

| Situation | Prediction $\hat{o}_t$ | Observation $o_t$ | Mismatch $\delta_t$ |
|-----------|------------------------|--------------------|-----------------------|
| Reading unfamiliar code | Expected behavior | Actual implementation | Comprehension gap |
| Running tests | Expected pass | Test failure | Bug or misunderstanding |
| Deploying | Expected behavior | Production error | Integration mismatch |
| Code review | Expected approval | Requested changes | Convention/quality gap |

TST's "comprehension time" ( #def-comprehension-time) is the time spent resolving high $\lVert\delta_t\rVert$ — driving mismatch toward zero through observation. A developer who "doesn't understand the codebase" is one with high $\lVert\delta_t\rVert$.

### Update gain ($\eta^\ast$) instantiation

*[Derived (developer-gain, from update-gain applied to software)]*

The uncertainty ratio principle ( #emp-update-gain) instantiates as:

- **New developer** ($U_M$ high): $\eta^\ast \approx 1$ — trust observations heavily. Read code and believe what you see. Rapid learning but vulnerability to noisy signals (misleading comments, outdated documentation).

- **Experienced developer** ($U_M$ low): $\eta^\ast \ll 1$ — trust the model. When code contradicts the model, suspect the code first. Stable expertise but resistance to genuine changes.

- **After major refactoring** ($U_M$ reset): $\eta^\ast$ spikes — the experienced developer must temporarily behave like a new developer. This is the gain reset after structural change ( #emp-update-gain, gain dynamics).

## Epistemic Status

This is a *definition* — it names the correspondence between software development entities and AAD formal objects. The mapping is exact in the sense that each AAD quantity has a concrete, identifiable software counterpart. The definition itself is not a truth-claim; the substantive claims come from applying AAD's derived results (persistence, tempo, gain dynamics) to this instantiation.

The observation channel tables and action classification are *discussion-grade* taxonomies — useful organizing structures, not exhaustive or formally derived.

## Discussion

**The 100% turnover problem.** For AI agents, the *context-window* component of $M_t$ is reset at each session start, but the effective state is reconstructed from external memory ($\mathcal E_{\text{ext}}$) plus the session-initiating prompt plus the pretrained weights $M_0^{\text{weights}}$ (see #obs-context-turnover, #scope-logogenic-agent). Treating session start as $M_0 \approx 0$ ignores the substantial weights contribution to the effective prior — pretrained knowledge of language, code, and reasoning patterns is preserved across the boundary. In AAD terms: $X_{\tau_{k+1}} = f_{\text{init}}(\mathcal E_{\text{ext}}, p_{k+1}, M_0^{\text{weights}})$, $U_M$ starts elevated (more than continuous-session evolution but less than blank-slate), and $\eta^\ast$ starts elevated correspondingly. The agent rebuilds the session-specific component of $M_t$ through high-$\nu$ observation; the cold-start transient is real but bounded by what survives in weights and externalized state.

Persistent external memory (documentation, CLAUDE.md files, well-structured codebases) determines how much of the prior agent's session-specific $M_t$ survives turnover by converting ephemeral context-window state into persistent environmental state. The quality of this externalization, combined with the weights' contribution, determines the reconstructed model sufficiency $S(M_{\tau_{k+1}})$ — see #obs-context-turnover for the formal sufficiency-discontinuity bound. In information-bottleneck ( #form-information-bottleneck) terms: the externalized memory should retain everything predictively relevant *that the weights do not already encode* while compressing aggressively.

**Channel-specific gain calibration.** When a developer encounters conflicting signals (requirements vs. existing architecture vs. code conventions), the uncertainty ratio principle says: weight each by the channel-specific uncertainty ratio. Clear, well-tested code (low $U_o$) should override vague verbal requirements (high $U_o$). Requirements from a well-understood domain (low $U_o$) should override ambiguous code (high $U_o$). The optimal update is channel-specific, not uniform.

**Developer tempo decomposition.** The developer's adaptive tempo ( #def-adaptive-tempo) decomposes into contributions from the channel classes defined above:

$$\mathcal{T}_{\text{dev}} = \mathcal{T}_{\text{obs}} + \mathcal{T}_{\text{explore}} + \mathcal{T}_{\text{probe}}$$

where each component sums the $\nu^{(k)} \cdot \eta^{(k)\ast}$ products across channels in that class. This decomposition identifies *which kind* of information acquisition is the bottleneck: an AI agent with instant code reading but no test infrastructure has high $\mathcal T_{\text{explore}}$ but near-zero $\mathcal T_{\text{probe}}$ — unable to confirm whether its model is correct.

## Findings

### Developer-Agent as AAD Instantiation

**Brief:** A software developer — human or AI — is identified as an actuated adaptive agent in AAD's full sense: the codebase plus surrounding artifacts form the environment $\Omega_t$, the developer's mental or in-context model is $M_t$, the current feature/fix is $O_t$, and the implementation plan is $\Sigma_t$ as a probabilistic causal DAG. Observation channels (compiler, tests, code reading, colleague queries) and action classes (exploration, interventional probes, queries, environment modification) carry concrete $(\nu, U_o)$ characteristics. The claim is not that AAD describes development *metaphorically* but that the developer-environment loop instantiates AAD's formal objects without relaxation, which is the point that licenses AAD's persistence, gain, and causal-discovery results to apply to software directly rather than by analogy.

**Impact:** Establishes software development as AAD's *privileged high-identifiability calibration laboratory* (the framing in this component's preamble): edge interventions can be literally interventional (tests, deploys, `git bisect`), the chronica $\mathcal C_t$ is partially exteriorized with cryptographic immutability over the committed subset, the causal DAG is partially declared (imports, type dependencies) rather than wholly inferred, and the observation function itself is under agent control. Other AAD application domains require additional transfer assumptions; software does not. This positions the developer-agent scope as the testbed against which AAD's quantitative machinery should be calibrated, with the calibration-lab framing making transfer assumptions to other domains explicit rather than implicit.

**Novelty Claim:** *Claim transfer* of AAD's adaptive-agent formalism into developer-agent software economics. The transfer is provisional pending deeper search. Nominally-comprehensive search at the pillar level surfaced only systems / benchmark / training-environment papers in the developer-agent literature (SWE-agent, SWE-Gym, Ambig-SWE, Demystifying SWE Agents, Long-Context SWE-RL, Agentic Code Reasoning); none formalize software engineering with bounded-rationality, POMDP-control, free-energy, or causal-intervention machinery in the form claimed here.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Developer agents in interactive, partially observed environments | SWE-agent (Yang et al. 2024, published 2024-05, found 2026-04 via Pillar-4 Undermind search) — agent-computer interface design strongly shapes performance; ablation-grade evidence | *empirical instantiation supporting* — confirms the environment has the structure AAD's actuated-agent scope assumes; prior work treats it as design empiricism rather than as scope-condition verification |
| Software repositories as RL training environments | SWE-Gym (Pan et al. 2024, published 2024-12, found 2026-04) — turns repositories and tests into a training environment with verifiers | *empirical instantiation supporting* — provides infrastructure that makes the developer-agent scope operational at scale; does not theorize repositories as partially observed dynamical systems |
| Long-context multi-turn developer agents | Long-Context SWE-RL (Golubev et al. 2025, published 2025-08, found 2026-04) — RL training of multi-turn long-context coding agents | *empirical instantiation supporting* — establishes that the developer-agent loop is a sequential decision setting at engineering-relevant horizons; no formal control-theoretic treatment |
| Underspecification / ambiguity in coding tasks | Ambig-SWE (Vijayvargiya et al. 2025, published 2025-02, found 2026-04) — underspecification creates large performance losses recoverable through interaction | *empirical instantiation supporting* — confirms the specification-bound mechanism is operative for AI developer agents specifically; does not derive the bound |
| When extra agentic machinery pays for itself | Demystifying SWE Agents (Xia et al. 2025, published 2025-06, found 2026-04) — simpler non-agentic pipelines can outperform richer agent scaffolds | *adjacent literature* — cautionary baseline that any developer-agent theory must explain when added scaffolding pays its tempo cost; AAD's tempo / persistence framing supplies one candidate explanation but the connection is not yet formal |
| Code reasoning under agentic execution | Agentic Code Reasoning (Ugare & Chandra 2026, published 2026-03, found 2026-04) | *adjacent literature* — recent work on code reasoning in agentic settings; surfaced too late in Pillar-4 search to assess in detail |
| Active inference in agent-environment loops | Active inference (Friston et al. 2012, 2015) and control-as-inference (Kappen et al. 2009) | *adjacent literature* — adopted as unifying backdrop in AAD generally; not specifically applied to developer agents in the literature surfaced by Pillar-4 search |

**Search Log:**
- 2026-04 (*nominally comprehensive at pillar level, with explicit thin-coverage caveat*, via `ref/Novelty_defense_and_integration.md` Pillar 4): Undermind retrieval covered developer-agent interfaces, training environments, RL pipelines, ambiguity benchmarks, and empirical failure analysis; recommended follow-on search areas — software repository cognition, technical debt as observability, tests as interventions — were not exhausted at this depth, and the report itself records confidence as Low. Current searches did not uncover a prior paper formalizing software-engineering economics with agentic-control tools, but provisional novelty is the honest posture until those follow-on areas are searched directly.

## Working Notes

- The environment table includes "team knowledge" and "dependency ecosystem" which are clearly part of $\Omega_t$ but hard to formalize as observation channels with well-defined $(\nu, U_o)$. These may be better treated as slowly varying background parameters that affect $\rho$ rather than as observable state.
- The tempo decomposition into $\mathcal T_{\text{obs}} + \mathcal T_{\text{explore}} + \mathcal T_{\text{probe}}$ appears in the OUTLINE as a separate gap segment. This definition provides the ingredients; the formal decomposition with its optimization implications deserves its own treatment.
- The strategy DAG instantiation is thin — real developer plans are often implicit, partially formed, and revised continuously. Whether AAD's explicit DAG formalism applies without modification to implicit human planning is an open question. For AI agents with explicit planning steps, the mapping is more direct.
- The distinction between "exploration" and "interventional probe" actions can be blurry. Reading code does not modify $\Omega_t$ and is purely exploratory. Running tests does modify $\Omega_t$ temporarily (process state) and is interventional. But making a speculative code change to see if it compiles is both environment-modifying and exploratory. The classification is useful but not a partition.

*(Source: old-tst-via-tft-mapping.md, "The Agent-Environment Coupling," "The Mismatch Signal," "The Update Gain.")*
