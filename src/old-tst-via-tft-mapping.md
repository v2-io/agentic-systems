# The TFT → Software Development Mapping

**Status**: Working draft. This mapping is the foundation — everything else in
via-tft/ depends on getting this right. Items marked [confident] I believe are solid;
[plausible] means structurally motivated but needs validation; [speculative] means
worth exploring but might not hold.

## The Agent-Environment Coupling

### Environment (Omega)

The "environment" in software development is not just the codebase. It's the full
state external to the developer's mind:

| Component | Changes how? | Observability |
|-----------|-------------|---------------|
| Codebase source | Developer edits, CI, other developers | High (git, IDE) |
| Runtime behavior | Deployment, config, load, dependencies | Medium (logs, monitoring, tests) |
| User requirements | Stakeholder decisions, market shifts | Low-medium (conversations, tickets) |
| Team knowledge | People joining/leaving, learning | Low (implicit, distributed) |
| Dependency ecosystem | Upstream releases, deprecations, CVEs | Medium (package managers, advisories) |
| Infrastructure state | Cloud changes, scaling events, failures | Medium (dashboards, alerts) |

[Confident] The full Omega is much larger than "the codebase." Many mismatch events
(production bugs, requirement changes, dependency breaks) originate outside the
codebase proper. TST's current formulation focuses almost entirely on the codebase as
environment, which systematically underestimates rho.

### Observation Space (O)

Observation channels are how information from Omega *arrives at the agent* — things
the environment tells the developer, as opposed to things the developer actively
seeks. The critical distinction: reading code is not passive observation — it's an
exploration action (see Action Space below). Observations are what flow through
channels that are either always-on or respond to prior actions.

| Channel k | Rate nu^(k) | Noise U_o^(k) | Trigger | Information type |
|-----------|-------------|---------------|---------|------------------|
| Compiler/linter output | Per-save | Very low | Automatic on edit | Syntactic/type correctness |
| Test results | Per-run | Low (deterministic) | Response to probe action | Behavioral correctness |
| CI pipeline results | Per-push | Low | Automatic on commit | Integration correctness |
| Runtime logs/telemetry | Continuous | Medium (sampling, aggregation) | Always-on | System behavior |
| Monitoring alerts | Event-driven | Low-medium | Triggered by anomaly | Operational mismatch |
| Analytics/user data | Slow (hours-days) | High (aggregated, interpreted) | Always-on | Usage patterns, business signal |
| Bug reports | Sporadic | High (user-reported, ambiguous) | Triggered by user experience | Behavioral mismatch |
| Code review feedback | Per-PR | Medium-high (subjective, delayed) | Response to PR submission | Quality, convention, intent |

These are *aisthesis* — the world responding. The developer may have triggered the
response (by running a test, by deploying, by submitting a PR), but the information
content is determined by the environment's state, not by the developer's choice of
where to look.

[Confident] This distinction matters for gain calibration. Observation channel
signals have well-characterized U_o: compiler output is near-deterministic, test
results are deterministic for what they cover, telemetry has known sampling
characteristics. The developer should trust these channels according to their U_o
profile — compiler output almost absolutely (eta* ≈ 1), test results heavily, user
bug reports cautiously.

### Action Space (A)

Developer actions are where the agent exercises choice. The fundamental TFT
distinction applies: actions can be *environment-modifying* (praxis that changes
Omega), *exploratory* (praxis aimed at generating informative observations), or
*query-directed* (accessing pre-compressed external models).

**Exploration actions** (directed attention — choosing what to observe):
- Read a specific file, navigate to a definition, grep for a pattern
- Read documentation, architecture docs, CLAUDE.md
- Trace a code path, follow imports, examine a call graph
- Browse git history for a file or module

These are *not* observations — they are actions whose purpose is to generate
observations (the content of the file, the doc, the history). The developer chooses
*where* to direct attention, and that choice has CIY implications: reading the right
file first is high-CIY; reading irrelevant code is wasted tempo. An AI agent that
reads CLAUDE.md before source code is making a higher-CIY choice than one that starts
with a random file — the memory file is a pre-compressed model (TF-08's query action
insight) with much higher information density per token.

**Interventional probes** (actions that change Omega temporarily to learn from the response):
- Run a specific test or test suite
- Add a print statement / breakpoint and execute
- Make a speculative change and see if it compiles
- Deploy to staging and observe behavior
- Introduce a deliberate perturbation to test a hypothesis

These are Level 2 (interventional) actions — do(X) and observe the consequence. Their
CIY depends on how informative the system's response is for the developer's current
uncertainty. A targeted test that exercises a suspected bug has very high CIY. Running
the full test suite when you're confident about the change has low marginal CIY.

**Query actions** (accessing external models — TF-08):
- Ask a colleague "why is this designed this way?"
- Search Stack Overflow or documentation
- Ask an AI assistant to explain a module
- Read a PR description or commit message (accessing the *original developer's*
  compressed model of their intent)
- Consult API documentation for a dependency

These access pre-compressed knowledge — another agent's M that has already done the
work of extracting structure from raw observations. As TF-08 notes, a single
well-targeted query can carry CIY orders of magnitude higher than individual
environment probes. The practical implication: asking someone who knows is almost
always higher-CIY than re-deriving from source, *when a reliable source is available*.

**Environment-modifying actions** (changing Omega — the codebase, config, infrastructure):
- Write/edit/delete code
- Refactor (structural adaptation of the codebase)
- Modify configuration
- Deploy to production

**Observation-infrastructure investment** (modifying Omega in ways that improve future
observation channels):
- Write a test (creates a new probe capability — a reusable Level 2 instrument)
- Add logging/tracing (improves the runtime observation channel — lowers U_o)
- Improve naming/comments (lowers U_o for the code-reading exploration channel)
- Add type annotations (lowers U_o for the compiler/type-checker observation channel)
- Write architecture docs (creates a query-action target for future agents)

[Confident] This last category is the most important insight from the corrected
decomposition. These actions don't directly ship features — they invest in the
agent's (and future agents') adaptive capacity. In TFT terms, they raise future T
by lowering future U_o (thus raising eta*) or by creating new observation channels
(raising nu). This is why experienced engineers insist on tests, observability, and
documentation — they're optimizing for adaptive tempo, not for immediate output.

The CIY framework formally justifies prioritizing these investments: they have
high expected future information yield precisely because they compound across every
future interaction with the codebase.

**The code-quality feedback loop.** U_o for the code-reading exploration channel is
*itself a function of past environment-modifying and observation-infrastructure
actions*. Well-written code with good naming has low U_o (exploration yields accurate
model updates). Poorly written code has high U_o (exploration yields inaccurate
or incomplete model updates — the developer reads it but forms a wrong impression).
This means past actions affect future observation quality — a second-order effect
where the agent's environment-modifying praxis shapes the quality of its own future
aisthesis.

[Plausible] This could be modeled as: U_o^(code_reading)(t) = f(quality(codebase_t)),
where quality is itself a function of all past coding actions. The agent faces a
choice: spend time now improving code quality (reducing future U_o, thus raising
future eta*, thus raising future T) or spend time implementing features directly. This
is TST's T-06 (change investment) reframed as a TFT observation-channel investment.

TF-01 allows action-dependent observation (o_t = h(Omega_t, a_{t-1}, epsilon_t)),
which captures the per-action effect (the developer's *current* exploration choice
affects what they see). But the cumulative effect of many past environment-modifying
actions on the observation function h itself is a longer-timescale phenomenon — more
like TF-10's structural adaptation of the observation channel rather than TF-01's
per-step action dependence.

### Model (M_t)

The developer's internal model of the system. This is the hardest part to formalize
because it's cognitive:

**For a human developer**, M_t includes:
- Mental model of architecture and module boundaries
- Knowledge of coding conventions and patterns used
- Understanding of business domain and requirements
- Expectations about runtime behavior
- Beliefs about which areas are stable vs. volatile
- Trust calibration for other team members' code

**For an AI agent (LLM)**, M_t is more explicitly representable:
- In-context understanding from files read this session
- Patterns inferred from code structure
- Instructions from system prompts, CLAUDE.md, memory files
- Inferences from error messages, test output, etc.

[Confident] The AI agent case is actually easier to formalize because M_t is more
observable — it's the agent's context window contents plus whatever persistent storage
it has access to. The human case requires cognitive modeling that TFT (wisely)
abstracts over.

### The 100% Turnover Problem

For AI agents, M_t is *reset to near-zero* at the start of each session. This is not
a gradual degradation but a catastrophic loss. In TFT terms:

- M_0 at session start ≈ M_prior (whatever CLAUDE.md / memory provides)
- U_M starts very high (the agent knows almost nothing about this specific codebase)
- eta* starts near 1 (the agent should trust observations heavily)
- The agent must rapidly build M_t through high-nu observation before it can act
  effectively

[Plausible] This suggests a formal "cold-start" phase in the adapted theory — a
transient period where the agent is in pure observation mode, building M_t before
the persistence condition can even be evaluated. TST's T-05 ("bias toward
comprehension") is the practical prescription for this phase, but TFT can formalize
why: with U_M >> U_o, eta* ≈ 1, so every observation moves the model substantially.
The agent should maximize observation rate (read widely) before attempting actions
that require an accurate model.

**Persistent external memory as M-preservation.** CLAUDE.md files, memory
directories, and well-structured codebases are all mechanisms to *externalize* parts
of M_t so they survive context turnover. In TFT terms, they convert ephemeral model
state into persistent environmental state — the agent writes its model into Omega so
that future agents can observe it and reconstruct M. The quality of this
externalization determines how much of the previous agent's M survives.

[Confident] This reframes the design of AI memory systems as a TFT problem: how to
compress M_t into an observation channel that future agents can absorb with high
fidelity (low U_o) and high speed (high nu). The information bottleneck (TF-03)
applies directly: the externalized memory should retain everything predictively
relevant while compressing aggressively.

## The Mismatch Signal in Software Development

TFT's delta_t = o_t - hat{o}_t (observation minus prediction) instantiates in
software as every moment of surprise:

| Situation | Prediction (hat{o}) | Observation (o) | Mismatch (delta) |
|-----------|-------------------|-----------------|-------------------|
| Reading unfamiliar code | Expected function behavior | Actual implementation | Comprehension gap |
| Running tests | Expected pass | Test failure | Bug or misunderstanding |
| Deploying | Expected behavior | Production error | Integration mismatch |
| Code review | Expected approval | Requested changes | Convention/quality gap |
| Reading requirements | Expected feature scope | Actual stakeholder intent | Requirements mismatch |
| Checking dependency | Expected API stability | Breaking change | Ecosystem mismatch |

[Confident] This mapping is natural and productive. The key insight: TST's
"comprehension time" IS the time spent resolving high delta — driving mismatch toward
zero through observation. A developer who "doesn't understand the codebase" is one
with high ||delta||. A developer who "knows the system well" is one with low ||delta||.

### Mismatch Decomposition (Prop 5.1 Applied)

From TF-05:

    E[||delta||^2] = E[||model_error||^2] + E[observation_noise^2]

In software:
- **Model error (reducible)**: The developer's understanding is wrong — they think
  the function does X but it does Y. Reducible by reading code, running tests,
  asking questions.
- **Observation noise (irreducible)**: The code is genuinely ambiguous — unclear
  naming, missing comments, inconsistent patterns. Irreducible *for this version of
  the codebase* but reducible by improving code quality (changing U_o).

[Confident] The zero-mismatch ambiguity (TF-05) is especially important here. A
developer with delta ≈ 0 might have an accurate model (good), might be only looking
at code they already understand (confirmation bias — TST doesn't address this), or
might be reading code so unclear that they can't detect their own misunderstanding
(high U_o masking model error). The third case is pernicious: bad code doesn't just
slow comprehension — it *hides* miscomprehension.

## The Update Gain in Software Development

TF-06's uncertainty ratio principle: eta* = U_M / (U_M + U_o)

**New developer (high U_M)**:
- eta* ≈ 1: Trust observations heavily. Read code and believe what you see.
- Accept that your prior model is nearly empty.
- High gain means rapid learning but also vulnerability to noisy signals (bad code,
  misleading comments, outdated documentation).

**Experienced developer (low U_M)**:
- eta* << 1: Trust your model. Discount surprising observations.
- When code contradicts your model, suspect the code first (it may be buggy).
- Low gain means stable expertise but also resistance to genuine changes.

**After a major refactoring or paradigm shift (U_M reset)**:
- eta* spikes back up: The experienced developer must re-learn.
- TF-06's "gain reset after structural change" is exactly what happens when an
  experienced developer encounters a major rewrite — their old model is suddenly
  unreliable and they must temporarily behave like a new developer.

[Confident] This provides the formal foundation for what experienced developers do
intuitively: they read new code with appropriate skepticism (low eta* for the
observation, trusting their model of how systems "should" work), while new developers
absorb everything uncritically (high eta*). Both behaviors are locally optimal given
their respective U_M.

[Plausible] The earlier agent's observation is worth developing: when a developer
encounters conflicting signals (requirements vs. existing architecture vs. code
conventions vs. domain knowledge), TF-06 says: weight each by the uncertainty ratio
for that channel. Requirements from a well-understood domain (low U_o) should override
ambiguous code (high U_o). Clear, well-tested code (low U_o) should override vague
verbal requirements (high U_o). The optimal update is channel-specific, not
uniform.

## Adaptive Tempo for Software Development

TF-11's adaptive tempo: T = sum_k nu^(k) * eta^(k)*

The developer's tempo decomposes into contributions from observation channels and
from exploration/probe action cycles. The distinction matters because they have
different optimization levers:

**Observation-channel tempo** (information arriving from Omega through always-on or
event-triggered channels):

    T_obs = nu_compiler * eta_compiler + nu_tests * eta_tests +
            nu_monitoring * eta_monitoring + nu_alerts * eta_alerts + ...

These channels have nu determined by infrastructure (how fast tests run, how often
monitoring samples) and eta determined by channel quality (U_o) relative to the
developer's uncertainty (U_M). Optimization: faster CI, better test coverage, richer
telemetry, clearer alert definitions.

**Exploration-action tempo** (information gained from directed attention — the agent
chooses where to look, then processes what it finds):

    T_explore = nu_read * eta_read + nu_query * eta_query + ...

Here nu_read is how fast the developer reads/navigates code, and eta_read depends on
both code quality (U_o) and the developer's current uncertainty about the area being
explored (U_M). nu_query is how fast they can ask and receive answers. Optimization:
IDE navigation tools, AI-assisted search, better documentation (raises eta_query),
cleaner code (raises eta_read).

**Probe-action tempo** (information gained from interventional do(X) → observe):

    T_probe = nu_test_runs * eta_test_results + nu_deploys * eta_staging_obs + ...

Here nu is how frequently the developer performs interventional probes, and eta is
the information gained per probe result. Optimization: faster test execution (raises
nu), better test design (raises eta by testing more informative properties), cheaper
staging environments (raises nu for higher-fidelity probes).

The total tempo is the sum across all three:

    T_developer = T_obs + T_explore + T_probe

[Confident] This three-part decomposition is more productive than TST's aggregate
"comprehension time" because it identifies which *kind* of information acquisition is
the bottleneck. A developer with a fast test suite but poor code quality has high
T_probe but low T_explore — bottlenecked on understanding, not on verification. An AI
agent with instant code reading but no test infrastructure has high T_explore but
near-zero T_probe — bottlenecked on verification, unable to confirm whether its model
is actually correct. A team with good code and good tests but no production telemetry
has high T_explore + T_probe but low T_obs — blind to runtime mismatch.

## Persistence Condition for Codebases

TF-11's persistence threshold: T > rho / ||delta_critical||

Applied to software:

    T_team > rho_total / ||delta_critical||

where:
- T_team is the team's aggregate adaptive tempo (all developers' channels combined)
- rho_total = rho_requirements + rho_dependencies + rho_infrastructure + rho_team_turnover
- ||delta_critical|| is the mismatch level beyond which the team can no longer ship
  working software

[Confident] This formalizes what every experienced engineer knows: there's a point
where a codebase becomes "unmaintainable" — where the rate of new complexity exceeds
the team's capacity to comprehend and adapt. TFT's persistence threshold makes this
quantitative (in principle) and identifies the three levers: increase T, decrease rho,
or raise delta_critical (accept lower quality standards).

**The death spiral formalized.** TST's "vicious cycle" (T-06) is:

    Rushed changes → higher U_o (worse code quality) → lower eta_reading
    → lower T_developer → lower T_team → further below persistence threshold
    → more rushed changes (desperate to keep up) → ...

This IS the effects spiral (Cor. A.3.1) applied to a single-agent case where the
agent's own actions degrade its observation channel. The agent is adversarial to its
future self — a self-inflicted version of TF-08's adversarial mirror.

[Plausible] The virtuous cycle is the reverse: principled changes → lower U_o →
higher eta_reading → higher T_developer → further above persistence threshold → more
slack for principled changes → ... This is the agent investing in its own observation
infrastructure, creating a positive feedback loop in adaptive capacity. TFT doesn't
currently model this self-reinforcing dynamic explicitly, but it's a natural extension
of the gain dynamics.

## Structural Adaptation in Software

TF-10's Proposition 10.1: when F(M) < 1 - epsilon, no parametric adaptation can
close the mismatch floor. Structural change is required.

In software, this is: when the architecture cannot accommodate the current
requirements pattern — when every new feature requires touching too many files,
crossing too many boundaries, fighting the existing structure — no amount of
incremental improvement within the current architecture will help. Refactoring (or
rewriting) is required.

**Symptoms of model class inadequacy (TF-10) mapped to software:**

| TFT symptom | Software manifestation |
|-------------|----------------------|
| Persistent irreducible mismatch | Every feature takes too long despite experienced team |
| Gain collapse without performance | Developers "know the codebase" but still can't ship fast |
| Systematic mismatch patterns | The same kinds of changes always cause the same kinds of problems |

[Confident] TST's T-06 (change investment) and C-07.1 (evolution justifies
realignment) are both instances of TF-10's structural adaptation. The investment
calculus in T-06 (accept cost C now to save S per future change when C < n_future * S)
is a specific decision rule for the structural-switch trigger formalized in
Appendix B, section B.6.3.

## Multi-Agent Dynamics in Software Teams

Appendix F's multi-agent coupling applies directly:

**Cooperative coupling**: Team members sharing knowledge through code review, pair
programming, documentation, and conversation. Communication gain eta_ji depends on
trust (U_align), source quality (U_src), and channel noise (U_o). Slack messages are
high U_o; pair programming is low U_o. A new team member is high U_src; a recognized
expert is low U_src.

**Adversarial coupling** (less obvious but real):
- Competing teams modifying shared infrastructure
- Developers with conflicting architectural visions
- AI agents with misaligned objectives modifying shared codebases
- Intentionally obfuscated code (rare in cooperative settings, common in adversarial
  ones like DRM, anti-cheat, or obfuscated malware)
- Hostile PRs or sabotage (extreme but not unheard of)

**The trust meta-model**: A developer's estimate of code quality IS a trust model.
"Alice writes clean code" → low U_src for Alice's modules. "This legacy code is
unreliable" → high U_src for that module. "The API documentation is always outdated"
→ high U_o for that observation channel. These trust estimates update through
experience — exactly TFT's trust calibration as a meta-model (Appendix F.2).

[Plausible] The team-persistence condition from Appendix F.3 applies: a team can
persist in environments where individuals cannot, because cooperative communication
tempo offsets disturbance that would exceed any single developer's capacity. This
formally justifies team structures, knowledge sharing, and communication investment —
not as soft "team culture" but as adaptive-capacity optimization.
