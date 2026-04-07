---
slug: developer-as-act-agent
type: definition
status: exact
depends:
  - software-scope
  - software-epistemic-properties
  - agent-environment
  - agent-model
  - observation-function
  - action-transition
  - complete-agent-state
  - update-gain
  - mismatch-signal
stage: draft
---

# Definition: Developer as ACT Agent

The developer (human or AI) instantiated as an ACT agent: $X_t = (M_t, G_t)$ where $M_t$ is the developer's understanding of the codebase, $G_t = (O_t, \Sigma_t)$ decomposes into feature/fix objectives and implementation strategy.

## Formal Expression

*[Definition (developer-as-act-agent)]*

A software developer is an actuated adaptive agent ( #agent-environment) whose state, environment, and coupling are:

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

The developer's internal model — the epistemic substate ( #agent-model):

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

For AI agents, $M_t$ is more explicitly representable (context window contents plus persistent storage), making it closer to a directly observable quantity.

### Objective ($O_t$)

*[Definition (developer-objective)]*

The developer's current objective — what the agent wants:

$$O_t \in \{\text{implement feature } F,\; \text{fix bug } B,\; \text{refactor module } R,\; \text{investigate incident } I,\; \ldots\}$$

$O_t$ induces a value functional $V_{O_t}$ ( #objective-functional) over codebase states. Objective revision occurs via the orient cascade ( #orient-cascade): e.g., while implementing feature $F$, the developer discovers a blocking bug and revises $O_t$ from "implement $F$" to "fix blocker, then implement $F$."

### Strategy ($\Sigma_t$)

*[Definition (developer-strategy)]*

The developer's implementation plan — how the agent intends to achieve $O_t$:

$$\Sigma_t = \text{plan decomposition of } O_t \text{ into subtasks with dependency and confidence structure}$$

In ACT terms, $\Sigma_t$ is a probabilistic causal DAG ( #strategy-dag) whose nodes are subtasks and whose edges carry confidence weights $p_{ij}$ representing the developer's belief that completing subtask $i$ enables subtask $j$. Examples:

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

The distinction matters for gain calibration. Passive channels have well-characterized $U_o$ (compiler output is near-deterministic); active channels have $U_o$ that depends on what is being explored and the quality of the target ( #software-epistemic-properties, P6).

### Action space ($\mathcal{A}$)

*[Definition (developer-actions)]*

Four classes of developer actions, distinguished by purpose:

1. **Exploration** — directed attention to generate observations: read a file, trace a code path, browse git history. These are actions whose purpose is to build $M_t$, not to modify $\Omega_t$.

2. **Interventional probes** — actions that temporarily perturb $\Omega_t$ to learn from the response: run tests, add a print statement, make a speculative change. These are $do(\cdot)$ operations providing Level 2 information ( #pearl-causal-hierarchy).

3. **Queries** — accessing pre-compressed external models: ask a colleague, search documentation, consult an AI assistant. These access another agent's $M$ that has already extracted structure from raw observations. A single well-targeted query can carry CIY orders of magnitude higher than individual environment probes ( #causal-information-yield).

4. **Environment modification** — changing $\Omega_t$: write/edit/delete code, modify configuration, deploy. A subset of these are *observation-infrastructure investments* — actions that modify $\Omega_t$ in ways that improve future observation quality (write tests, add logging, improve naming). See #code-quality-as-observation-infrastructure.

### Mismatch signal ($\delta_t$)

*[Derived (developer-mismatch, from mismatch-signal applied to software)]*

Every moment of developer surprise is a mismatch signal ( #mismatch-signal):

| Situation | Prediction $\hat{o}_t$ | Observation $o_t$ | Mismatch $\delta_t$ |
|-----------|------------------------|--------------------|-----------------------|
| Reading unfamiliar code | Expected behavior | Actual implementation | Comprehension gap |
| Running tests | Expected pass | Test failure | Bug or misunderstanding |
| Deploying | Expected behavior | Production error | Integration mismatch |
| Code review | Expected approval | Requested changes | Convention/quality gap |

TST's "comprehension time" ( #comprehension-time) is the time spent resolving high $\lVert\delta_t\rVert$ — driving mismatch toward zero through observation. A developer who "doesn't understand the codebase" is one with high $\lVert\delta_t\rVert$.

### Update gain ($\eta^\ast$) instantiation

*[Derived (developer-gain, from update-gain applied to software)]*

The uncertainty ratio principle ( #update-gain) instantiates as:

- **New developer** ($U_M$ high): $\eta^\ast \approx 1$ — trust observations heavily. Read code and believe what you see. Rapid learning but vulnerability to noisy signals (misleading comments, outdated documentation).

- **Experienced developer** ($U_M$ low): $\eta^\ast \ll 1$ — trust the model. When code contradicts the model, suspect the code first. Stable expertise but resistance to genuine changes.

- **After major refactoring** ($U_M$ reset): $\eta^\ast$ spikes — the experienced developer must temporarily behave like a new developer. This is the gain reset after structural change ( #update-gain, gain dynamics).

## Epistemic Status

This is a *definition* — it names the correspondence between software development entities and ACT formal objects. The mapping is exact in the sense that each ACT quantity has a concrete, identifiable software counterpart. The definition itself is not a truth-claim; the substantive claims come from applying ACT's derived results (persistence, tempo, gain dynamics) to this instantiation.

The observation channel tables and action classification are *discussion-grade* taxonomies — useful organizing structures, not exhaustive or formally derived.

## Discussion

**The 100% turnover problem.** For AI agents, $M_t$ is reset to near-zero at each session start. In ACT terms: $M_0 \approx M_{\text{prior}}$ (whatever memory files provide), $U_M$ starts very high, and $\eta^\ast$ starts near 1. The agent must rapidly build $M_t$ through high-$\nu$ observation before it can act effectively. This creates a formal "cold-start" phase — a transient where the agent is in observation mode, building $M_t$ before the persistence condition ( #persistence-condition) can even be meaningfully evaluated.

Persistent external memory (documentation, CLAUDE.md files, well-structured codebases) converts ephemeral model state into persistent environmental state. The agent writes its model into $\Omega$ so future agents can reconstruct $M_t$ through observation. The quality of this externalization determines how much of the previous agent's $M_t$ survives turnover. In information-bottleneck ( #information-bottleneck) terms: the externalized memory should retain everything predictively relevant while compressing aggressively.

**Channel-specific gain calibration.** When a developer encounters conflicting signals (requirements vs. existing architecture vs. code conventions), the uncertainty ratio principle says: weight each by the channel-specific uncertainty ratio. Clear, well-tested code (low $U_o$) should override vague verbal requirements (high $U_o$). Requirements from a well-understood domain (low $U_o$) should override ambiguous code (high $U_o$). The optimal update is channel-specific, not uniform.

**Developer tempo decomposition.** The developer's adaptive tempo ( #adaptive-tempo) decomposes into contributions from the channel classes defined above:

$$\mathcal{T}_{\text{dev}} = \mathcal{T}_{\text{obs}} + \mathcal{T}_{\text{explore}} + \mathcal{T}_{\text{probe}}$$

where each component sums the $\nu^{(k)} \cdot \eta^{(k)\ast}$ products across channels in that class. This decomposition identifies *which kind* of information acquisition is the bottleneck: an AI agent with instant code reading but no test infrastructure has high $\mathcal T_{\text{explore}}$ but near-zero $\mathcal T_{\text{probe}}$ — unable to confirm whether its model is correct.

## Working Notes

- The environment table includes "team knowledge" and "dependency ecosystem" which are clearly part of $\Omega_t$ but hard to formalize as observation channels with well-defined $(\nu, U_o)$. These may be better treated as slowly varying background parameters that affect $\rho$ rather than as observable state.
- The tempo decomposition into $\mathcal T_{\text{obs}} + \mathcal T_{\text{explore}} + \mathcal T_{\text{probe}}$ appears in the OUTLINE as a separate gap segment. This definition provides the ingredients; the formal decomposition with its optimization implications deserves its own treatment.
- The strategy DAG instantiation is thin — real developer plans are often implicit, partially formed, and revised continuously. Whether ACT's explicit DAG formalism applies without modification to implicit human planning is an open question. For AI agents with explicit planning steps, the mapping is more direct.
- The distinction between "exploration" and "interventional probe" actions can be blurry. Reading code does not modify $\Omega_t$ and is purely exploratory. Running tests does modify $\Omega_t$ temporarily (process state) and is interventional. But making a speculative code change to see if it compiles is both environment-modifying and exploratory. The classification is useful but not a partition.

*(Source: old-tst-via-tft-mapping.md, "The Agent-Environment Coupling," "The Mismatch Signal," "The Update Gain.")*
