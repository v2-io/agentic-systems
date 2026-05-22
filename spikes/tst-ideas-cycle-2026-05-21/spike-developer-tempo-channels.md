---
spike: developer-tempo-channels
date: 2026-05-21
status: spike-grade derivation; candidate segment `#def-developer-tempo-channels` substrate
gap-closed: 02-tst-core/OUTLINE.md Ch.2 (Developer Agent and Time Decomposition) leading `--GAP--` row
related_segments:
  - def-adaptive-tempo
  - deriv-matrix-persistence-condition
  - der-class-coercion-via-wrapping
  - def-causal-information-yield
  - def-pearl-causal-hierarchy
  - scope-developer-agent
  - def-comprehension-time
  - def-implementation-time
  - obs-software-epistemic-properties
  - hyp-causal-discovery-from-git
  - der-code-quality-as-observation-infrastructure
  - impl-developer-agent
substrate:
  - TST-IDEAS.md §A4 (developer-tempo channel decomposition)
  - spikes/tst-mining-2026-05-21/03-pragmatic-mining.md #1 (probe-class typology)
  - spikes/tst-mining-2026-05-21/02-forensic-mining.md F9 (chronicle-derivable channel separation), F2 (tests as reusable Level-2 probes), F11 (mock-complexity blowup as $U_o$ degradation)
sibling-spikes:
  - spike-running-software-agent.md (runtime-tempo decomposition — same structural shape, runtime-domain sibling)
  - spike-software-unmaintainability-bifurcation.md (consumes $\mathcal T_\text{dev}$ as what falls below the persistence threshold)
---

# Spike: Developer-Tempo Channel Decomposition

**Status.** Spike-grade derivation supporting the candidate segment `#def-developer-tempo-channels` under `02-tst-core/` Ch.2. The candidate segment will close the leading `--GAP--` row in Ch.2 of `02-tst-core/OUTLINE.md` (the "Developer tempo as $\mathcal T_\text{obs} + \mathcal T_\text{explore} + \mathcal T_\text{probe}$" gap).

This spike is the reasoning trail. Math that survives lands in the segment when promoted. Per *math-lives-in-segments*, the load-bearing derivations below — the channel decomposition, the per-channel $(\nu, U_o)$ tables, the matrix-Loewner specialization at the developer-agent level, the probe-class typology, and the chronicle-derivable operational definitions — are the candidate segment's content; the *spike-specific* content (the honesty-call work on the W₁/W₂-vs-disposability question, the chronicle-instrumentation-gap analysis, and the sibling-spike coordination notes) is the trail that motivates the body.

## 1. Substrate and claim

The OUTLINE Ch.2 leading-row gap names the decomposition

$$\mathcal{T}_\text{dev} \;=\; \mathcal{T}_\text{obs} \;+\; \mathcal{T}_\text{explore} \;+\; \mathcal{T}_\text{probe}$$

as the candidate-segment shape. The decomposition is already gestured at in `#scope-developer-agent`'s Discussion ("Developer tempo decomposition") and in `#impl-developer-agent`'s "Developer tempo and the unmaintainability threshold" section. Neither carries the per-channel $(\nu^{(k)}, U_o^{(k)})$ tables, the probe-class internal-decomposition of $\mathcal T_\text{probe}$, the chronicle-derivable operationalizations, or the matrix-Loewner specialization — the four operational pieces needed for the candidate segment to do the work the OUTLINE gap names.

The three structural claims the candidate segment will carry:

**(SC-1) Channel decomposition.** The developer's adaptive tempo decomposes as $\mathcal T_\text{dev} = \mathcal T_\text{obs} + \mathcal T_\text{explore} + \mathcal T_\text{probe}$, with each channel having its own $(\nu^{(k)}, U_o^{(k)}, \eta^{(k)\ast})$ profile. The additive form inherits `#def-adaptive-tempo`'s channel-independence assumption (and the same upper-bound caveat under correlated channels).

**(SC-2) Per-channel internal structure.** $\mathcal T_\text{probe}$ further decomposes into a *probe-class typology* with six identifiable classes from practitioner literature (tracer / prototype / e2e / perf / ui / spike-throwaway), each with distinct $(\nu, \eta^\ast)$ signatures. $\mathcal T_\text{obs}$ and $\mathcal T_\text{explore}$ admit similar but less crisp internal decompositions.

**(SC-3) Matrix-Loewner weakest-channel bottleneck.** The developer's *aggregate* tempo is bounded by the *worst* of the three channels under the matrix-Loewner persistence condition `#deriv-matrix-persistence-condition`. A developer with high $\mathcal T_\text{obs}$ and absent $\mathcal T_\text{probe}$ is not "almost-fine on average" — they fail persistence along the probe direction, and aggregate-tempo metrics systematically miss it. This is the developer-agent specialization of `#deriv-matrix-persistence-condition`'s "the weak direction is the bottleneck" result.

## 2. Channel decomposition with per-channel profiles

### 2.1 The three channel classes

The action-class enumeration in `#scope-developer-agent` (exploration / interventional probes / queries / environment modification) already names the substrate for the channels; the candidate segment lifts the *observation-side* triple into the tempo decomposition. Mapping the action classes onto observation channels via the actions' epistemic content:

| Channel | Definitionally | Pearl level | Action-class source |
|---|---|---|---|
| $\mathcal T_\text{obs}$ | Rate of $M_t$-construction from already-existing observable codebase state — reading code, browsing history, inspecting structure, querying documentation, querying colleagues | Level 1 (associational) | Exploration + Queries |
| $\mathcal T_\text{explore}$ | Rate of $M_t$-construction from non-committed speculative interventions on $\Omega_t$ that the developer later either keeps or reverts — speculative edits, scratch branches, throwaway proofs-of-concept that never commit | Level 2 (interventional) on private workspace | Interventional probes (subset) + Environment modification (subset, *uncommitted*) |
| $\mathcal T_\text{probe}$ | Rate of $M_t$-construction from *committed* interventions whose explicit purpose is to test invariants or generate ground-truth verification — running tests, deploying to staging, adding instrumentation, running benchmarks | Level 2 (interventional) on the shared codebase | Interventional probes (subset) + Environment modification (subset, *committed observation-infrastructure*) |

The classification is principled because it tracks two distinct epistemic-content axes: *Pearl level* (Level 1 vs. Level 2 access on the codebase) and *commitment status* (private workspace vs. shared mainline). `#obs-software-epistemic-properties` P5's distinction between $\mathcal C_t$ and $\mathcal C_t^\text{commit}$ is the same axis at the chronicle level — committed work is exact-recorded, uncommitted is not. The three channels are the three combinations of (Pearl-level, commitment-status) that have non-zero developer activity: (Level 1, neither) = $\mathcal T_\text{obs}$; (Level 2, uncommitted) = $\mathcal T_\text{explore}$; (Level 2, committed) = $\mathcal T_\text{probe}$. The fourth combination (Level 1, committed) is empty — code-reading does not produce commits as a side effect.

### 2.2 Per-channel $(\nu, U_o)$ tables

The tables below extend `#scope-developer-agent`'s passive/active observation-channel tables into the three-class structure. Each row is a sub-channel; per-channel tempo $\mathcal{T}^{(k)} = \nu^{(k)} \cdot \eta^{(k)\ast}$ aggregates across sub-channels within a class under channel-independence (`#def-adaptive-tempo` Discussion §"Channel independence assumption" caveat).

**$\mathcal T_\text{obs}$ — Level 1 codebase observation.**

| Sub-channel | $\nu^{(k)}$ | $U_o^{(k)}$ | Information type |
|---|---|---|---|
| Code reading (file open + navigation) | Per-navigation | $U_o(Q)$ per `#der-code-quality-as-observation-infrastructure` | Structure, intent, current state |
| Git history inspection (blame, log, bisect-without-build) | Per-query | Low–medium | Causal-temporal structure (P4) |
| Documentation lookup | Per-query | Medium | API contracts, design intent |
| Colleague query | Per-interaction | Medium–high (trust-dependent, `#def-causal-information-yield` §"Query actions") | Compressed external $M_t$ |
| AI-assistant query (RAG-grounded) | Per-interaction | Medium (trust-dependent + hallucination floor) | Compressed external $M_t$ |
| Compiler/linter output (passive) | Per-save | Very low | Syntactic correctness |
| Code review (incoming) | Per-PR | Medium–high | Convention, intent, quality |

**$\mathcal T_\text{explore}$ — Level 2 private-workspace probes.**

| Sub-channel | $\nu^{(k)}$ | $U_o^{(k)}$ | Information type |
|---|---|---|---|
| Speculative edits (uncommitted) | Per-attempt | Low (deterministic compile-outcome) | Counterfactual: "what breaks if I…" |
| Scratch branches | Per-experiment | Low–medium | Architectural reachability |
| REPL / notebook exploration | Per-evaluation | Low | Runtime semantics, edge cases |
| Throwaway proofs-of-concept | Per-PoC | Medium | Feasibility / "can this work at all" |
| Dry-run / `--dry-run` / staging exec (private workspace) | Per-run | Low–medium | Integration behavior without commitment |

**$\mathcal T_\text{probe}$ — Level 2 committed interventions on the shared codebase.**

The classes here use Pragmatic Programmer's probe-typology (substrate from `spikes/tst-mining-2026-05-21/03-pragmatic-mining.md` #1) lifted into the AAT vocabulary. Each class is a *named probe-class* with characterized signature; the candidate segment can carry the table as the operational content of §"$\mathcal T_\text{probe}$ probe-class decomposition."

| Probe class | $\nu^{(k)}$ | $U_o^{(k)}$ | Target | Disposability |
|---|---|---|---|---|
| Tracer bullet (persistent skeleton) | Per-feature-grade-iteration | Low (production-quality assertions) | Cross-cutting end-to-end path through the architecture | Non-disposable (skeleton survives, fills in) |
| Throwaway prototype | Per-architecture-question | Medium (constants gestural, structure load-bearing) | Constraint discovery on $\Sigma_t$ structure | Strictly disposable ($t_\text{convert} \gt t_\text{reimplement}$) |
| End-to-end integration probe | Per-integration-boundary | Low–medium | Integration-uncertainty between components | Mixed (skeleton retained, mocks shed) |
| Performance benchmark | Per-perf-question | Medium (timing noise) | Stress-response curve, scaling exponents | Often retained as regression-watch suite |
| UI prototype | Per-UX-question | Medium–high (user-mental-model variance) | User mental-model match | Disposable |
| Spike / throwaway exploratory probe | Per-open-question | High variance | Unknown-unknowns at framework or architecture layer | Disposable |
| Unit tests (committed) | Per-CI-cycle | Low (per F2: bounded by mock-complexity blowup F11) | Production-code behavior on tested paths | Retained indefinitely |
| Integration tests (committed) | Per-CI-cycle | Low–medium | Cross-module behavior | Retained indefinitely |
| Production canary | Per-deploy | Low (real traffic) | Full-stack production behavior | Retained as deploy-process probe |

The unit/integration/canary rows are repeated from `#obs-software-epistemic-properties` P3 — they are the *reusable Level-2 probes* the segment names. The first six rows are the *single-use Level-2 probes* from the Pragmatic typology that the framework has not yet surfaced operationally.

### 2.3 The aggregation form

Under channel-independence (`#def-adaptive-tempo`):

$$\mathcal{T}_\text{dev} \;=\; \mathcal{T}_\text{obs} \;+\; \mathcal{T}_\text{explore} \;+\; \mathcal{T}_\text{probe}$$

where

$$\mathcal{T}_\text{obs} = \sum_{k \in \text{obs sub-channels}} \nu^{(k)} \cdot \eta^{(k)\ast}, \quad \mathcal{T}_\text{explore} = \sum_{k \in \text{explore sub-channels}} \nu^{(k)} \cdot \eta^{(k)\ast}, \quad \mathcal{T}_\text{probe} = \sum_{k \in \text{probe-class sub-channels}} \nu^{(k)} \cdot \eta^{(k)\ast}.$$

Cross-class correlation (e.g., a developer who runs tests *while* reading code so the test output shapes reading attention) is the source of the additive form's overcount under `#def-adaptive-tempo`'s redundancy-penalty caveat. The redundancy penalty across the three classes is bounded by the mutual information between the channels' event streams conditioned on the current $M_t$; absent measurement, the additive form is the standard upper bound and the per-class quantities are individually well-defined.

## 3. Matrix-Loewner weakest-channel bottleneck

This is the load-bearing application of `#deriv-matrix-persistence-condition` to the developer-agent — and the operational rewards the candidate segment delivers beyond the additive decomposition.

### 3.1 The scalar reading is unsafe at the developer level

The developer-channel persistence condition reads, at the scalar level (`#result-persistence-condition`):

$$\mathcal{T}_\text{dev} \;\gt\; \frac{\rho_\text{dev}}{\lVert \delta_\text{critical,dev} \rVert}$$

with $\rho_\text{dev}$ the rate of incoming codebase-level mismatch events (requirement changes, dependency breaks, integration surprises, bug reports) and $\delta_\text{critical,dev}$ the tolerable mismatch before the developer-agent fails its persistence boundary (cf. `#der-code-quality-as-observation-infrastructure`'s "this codebase is unmaintainable" inequality).

The trap: the scalar form *aggregates* across the three channels and can declare persistence when the developer cannot in fact verify what they have read. Consider a developer with $\mathcal T_\text{obs} = 10$, $\mathcal T_\text{explore} = 5$, $\mathcal T_\text{probe} = 0$ (a codebase with no tests, no staging, no canaries — the developer reads fast and edits fast but has no Level-2 access at all). The scalar sum is $\mathcal T_\text{dev} = 15$, which may exceed the scalar threshold. The matrix-Loewner reading correctly identifies that the *probe direction has zero capacity*: $\delta$-vectors with a probe-channel component cannot be corrected at any rate, and the developer-agent will fail persistence along that direction with probability $1$ over a long enough horizon.

This is `#deriv-matrix-persistence-condition`'s "per-coordinate is unsafe under cross-dimensional correction" specialized to the developer-agent's three-channel structure. The developer's correction operator $\mathcal T_\text{dev}$, expressed in the basis of (obs, explore, probe), is *diagonal* in the channel-independence limit:

$$\mathcal{T}_\text{dev} \;=\; \text{diag}(\mathcal{T}_\text{obs},\; \mathcal{T}_\text{explore},\; \mathcal{T}_\text{probe})$$

The matrix-Loewner condition $\Sigma_\infty^\text{dev} \prec D_{\delta,\text{dev}}$ — with $D_{\delta,\text{dev}} = \text{diag}(\delta_\text{critical,obs}^2, \delta_\text{critical,explore}^2, \delta_\text{critical,probe}^2)$ — then reduces to the per-coordinate form (the diagonal-axis-aligned special case of `#deriv-matrix-persistence-condition` §4.5):

$$\frac{\sigma_{w,k}^2}{2\,\mathcal{T}^{(k)}} \;\lt\; \delta_{\text{critical},k}^2 \quad \text{for } k \in \{\text{obs}, \text{explore}, \text{probe}\}.$$

The *weakest* channel is the binding constraint. The aggregate $\mathcal T_\text{dev}$ does not appear in the binding condition at all; what appears is $\min_k \mathcal{T}^{(k)}$ relative to its own per-channel threshold.

### 3.2 What the matrix-Loewner form predicts about developer-agent failure modes

Three named failure modes follow from the per-channel reading. Each has a corresponding correction prescription distinct from "raise aggregate tempo."

**(F-obs) Comprehension starvation.** $\mathcal T_\text{obs} \approx 0$ with $\mathcal T_\text{explore}, \mathcal T_\text{probe}$ high. Symptom: developer makes rapid changes but cannot describe what the code currently does; speculative edits accumulate without grounding; commits land but the developer cannot explain their own diffs in code review. Failure direction is *interpretation*: the developer's $M_t$ does not reflect the codebase's actual structure. Prescription is not "edit faster" — it is "open the file, read it, ask the question." For AI agents under the AI-maintained-code regime, this is the *normal* failure mode at session start before context fills; the prescription is investment in $\mathcal T_\text{obs}$ sub-channels (RAG grounding, documentation completeness, naming clarity — `#der-code-quality-as-observation-infrastructure`).

**(F-explore) Workspace timidity.** $\mathcal T_\text{explore} \approx 0$ with $\mathcal T_\text{obs}, \mathcal T_\text{probe}$ high. Symptom: developer reads extensively and runs tests on existing code but never tries speculative edits to probe alternatives; architectural decisions are made from $M_t$-as-currently-constituted without counterfactual exploration. Failure direction is *counterfactual reasoning*: the developer's $\Sigma_t$ never widens to include alternatives not directly suggested by reading. Prescription is "open a scratch branch and try the alternative" — Pearl-Level-2 access on private workspace. For AI agents, this is the mode where the agent reads the code, runs the tests, and never speculates on whether a different approach would be cleaner.

**(F-probe) Verification starvation.** $\mathcal T_\text{probe} \approx 0$ with $\mathcal T_\text{obs}, \mathcal T_\text{explore}$ high. Symptom: the canonical case TST-IDEAS §A4 names. Developer reads the code fast, makes speculative edits fast, but cannot *verify* whether the resulting state holds the production invariants. Failure direction is *ground-truth verification*: the developer's posterior on whether their changes actually work is unbounded above by their own model confidence. Prescription is investment in the probe channel — write the test, add the assertion, run the canary, add the contract. The chain `#hyp-causal-discovery-from-git` §"Tests as reusable Level-2 probes" composed with `#der-code-quality-as-observation-infrastructure` says this investment compounds across every future agent who touches the code.

The structural insight worth carrying explicitly: *aggregate-tempo metrics for developer-agent assessment systematically miss directional failures.* A developer-productivity dashboard reporting "X commits per week / Y lines per day" is the scalar-tempo reading. The matrix-Loewner reading says these aggregates are unsafe — they can rise to celebration-grade levels while a particular channel sits at zero and the developer-agent is failing persistence along that direction.

### 3.3 Cross-channel correlation: when the diagonal form fails

`#deriv-matrix-persistence-condition`'s §4 result — per-coordinate is *unsafe* when $\mathcal{T}$ has off-diagonal entries — is also active at the developer-agent level. The diagonal form is an approximation; in practice the three channels couple in three named ways:

- **Reading-while-testing.** Test output shapes which files the developer reads next; reading reveals which tests are missing. $\mathcal T_\text{obs}$ and $\mathcal T_\text{probe}$ have positive off-diagonal coupling: each channel speeds the other when both are present. (Cf. F2 in `02-forensic-mining.md`: tests that co-change with production code are the *symptom* of this coupling.)
- **Speculate-then-test.** A scratch-branch experiment generates a hypothesis about production-code behavior; the developer then writes the committed test that confirms or refutes it. $\mathcal T_\text{explore}$ feeds $\mathcal T_\text{probe}$ — without exploration, the test-writing has no direction.
- **Read-then-speculate.** Code reading generates the candidate counterfactuals worth scratch-branching. $\mathcal T_\text{obs}$ feeds $\mathcal T_\text{explore}$.

The full developer-channel matrix $\mathcal T_\text{dev}$ in the (obs, explore, probe) basis carries off-diagonals from these couplings. The matrix-Loewner condition $\Sigma_\infty^\text{dev} \prec D_{\delta,\text{dev}}$ then has its full force: the binding direction can be *off-axis* in channel space — a 45-degree direction between obs and probe, for instance, corresponding to "interpret what I read by running a quick test." A developer who is fast at reading and fast at running pre-existing tests but slow at the *combination* (reading code that lacks tests, or running tests whose assertions are unclear) fails along the diagonal direction, and per-channel monitoring misses it. The candidate segment should carry this in Discussion as the developer-agent specialization of `#deriv-matrix-persistence-condition` §4's counterexample.

The diagonal form remains the operational baseline — most developer assessments do not have access to off-diagonal coupling estimates — but the Discussion should flag the unsafety so that aggregate-rate metrics are not over-trusted.

## 4. Chronicle-derivable channel separation

Substrate: `spikes/tst-mining-2026-05-21/02-forensic-mining.md` F9. The forensic claim is that the chronicle $\mathcal C_t^\text{commit}$ — `#obs-software-epistemic-properties` P5's exact-recorded committed-state subset — supports *post-hoc separation* of the three channels for projects with mature git history. This is operationally valuable because it converts the candidate segment from a definitional decomposition into one with calibratable estimators from git data alone.

### 4.1 $\mathcal T_\text{probe}$ from test-only-changing commits — the cleanest reconstruction

Define a commit $c$ as *test-only-changing* if every modified file under $c$ lives in a test-suite directory (`test/`, `tests/`, `spec/`, `*_test.go`, `*_test.py`, `test_*.py`, `*.test.js`, etc.). The set of test-only-changing commits over a window $W$ has:

- $\nu_\text{probe}^\text{commit-rate} = \lvert \{c \in W : c \text{ test-only-changing}\} \rvert / \lvert W \rvert$ — the rate of probe-strengthening commits per unit time.
- $U_o^\text{probe}$ estimable from test flakiness rate and from `#meas-coherence-coupling`-derived test-file-vs-production-file co-change matrices (a test that co-changes with arbitrary production code is high-leakage; a test that co-changes only with its narrow target is low-leakage — directly the mock-complexity blowup from F11).

This is *clean* because the filename filter is auditable, deterministic, and content-addressed via `#obs-software-epistemic-properties` P5. The candidate segment can carry the reconstruction without scope caveats beyond "the project's test directory convention is consistent."

### 4.2 $\mathcal T_\text{explore}$ from scratch-branch + revert-rate — murkier but still chronicle-derivable

Two operational proxies for $\mathcal T_\text{explore}$ from git data:

- **Scratch-branch activity.** Branches that never merge to mainline (forensic mining F12 analog at the branch level). Rate: $\nu_\text{explore}^\text{scratch} = \lvert\{\text{branches}_W : \text{no merge to main}\}\rvert / \lvert W \rvert$. Quality $U_o$: the scratch branches' lifetime distribution (short-lived branches that reach deletion quickly = low $U_o$ exploration; long-lived branches that get abandoned without resolution = high $U_o$ "experiment failed to terminate" cases).
- **Revert-rate on main.** Commits later reverted by an explicit revert-commit. Rate: $\nu_\text{explore}^\text{revert}$. The revert is the *committed* signature of an *attempted* probe that did not succeed — i.e., a $\mathcal T_\text{explore}$ event that ended up entering the chronicle when it shouldn't have. High revert-rate is evidence of $\mathcal T_\text{explore}$ activity that *failed to stay in workspace* — a regularization-failure on the exploration channel.

The proxy is murkier than (4.1) because the chronicle's scope (P5) is *committed* state; scratch branches and reverted commits are partial exteriorizations of an inherently uncommitted activity class. Branch-management conventions vary substantially across projects (rebase-only workflows lose much of the scratch-branch signal; trunk-based development with feature-flags loses the merge-or-not signal). The candidate segment should carry these as estimators of a *lower bound* on $\mathcal T_\text{explore}$ — the chronicle sees the spillover; the bulk of explore activity remains private to the developer's workspace by construction.

### 4.3 $\mathcal T_\text{obs}$ requires instrumentation the chronicle alone does not provide — the honest call

This is the load-bearing honesty point from TST-IDEAS §A4. The chronicle records *what was committed*, not *what was read before committing*. Reconstructing $\nu_\text{obs}$ from $\mathcal C_t^\text{commit}$ requires an additional assumption — typically that observation activity scales with commit activity, or with code-review-comment activity for projects with mature PR-review processes.

Three proxies of decreasing fidelity:

- **Code-review duration (highest-fidelity, project-dependent).** For projects with mature code-review tooling (GitHub PRs with timestamps on review approvals, Gerrit with review-iteration durations), the elapsed time between PR-opened and PR-approved is a partial proxy for $\nu_\text{obs}$ on the reviewer side. This requires *tooling beyond git itself* — the chronicle's P5 immutability does not extend to PR-review metadata, which lives outside the hash-chained committed state. The candidate segment must surface this scope distinction.
- **Commit-message comprehension references (medium-fidelity).** Commit messages that reference *prior commits* ("revert of abc123," "follow-on to def456," "addressed in ghi789") evidence that the committing developer had to read the prior commit before producing the new one. Rate: count of comprehension-references per commit. This is auditable from $\mathcal C_t^\text{commit}$ alone but is a *lower bound* — disciplined developers reference; undisciplined developers do not, regardless of whether they read.
- **`git blame` query frequency (instrumentation-dependent).** For projects that instrument developer-side IDE telemetry, the rate of `git blame` queries is a direct proxy. This requires *agent-side instrumentation*, which is generally absent.

The honest framing the candidate segment should carry: **$\mathcal T_\text{obs}$ has a chronicle-derivable lower bound** (from commit-message comprehension references and review-duration proxy) **but the true rate requires explicit instrumentation that the chronicle's P5 immutability does not extend to.** This is a genuine asymmetry across the three channels — $\mathcal T_\text{probe}$ is cleanly reconstructible, $\mathcal T_\text{explore}$ has a lower-bound reconstruction, $\mathcal T_\text{obs}$ requires out-of-chronicle instrumentation that varies across teams. The candidate segment should not pretend otherwise.

A subtle composition with `#obs-software-epistemic-properties` P5's conditional-maximality claim: P5 says $\mathcal C_t^\text{commit}$ is the *unique maximal exteriorized subset* of $\mathcal C_t$ under cryptographic-immutability + universal-retrieval scope. Code-review timestamps and IDE telemetry fail at least one of those conditions (PR-review state is centralized-server-dependent; IDE telemetry has no universal retrieval protocol). So the $\mathcal T_\text{obs}$ measurement gap is *consistent with* P5 rather than evidence against it — P5 names exactly where the chronicle's exact-recording ends, and $\mathcal T_\text{obs}$ is one of the things that ends there.

## 5. Honesty call — probe-disposability is NOT W₁/W₂ goal-blindness

This is the load-bearing honesty work flagged in TST-IDEAS §A4: *the W₁/W₂ analogy for probe disposability needs care — disposability and goal-blindness are structurally different and conflating them is a category error*. The Pragmatic-mining yield in `03-pragmatic-mining.md` #1 explicitly proposed the analogy ("disposable prototypes are W₁; tracer bullets are W₂"), with the qualifier that the load-bearing translation move *needs to be checked carefully*. The check below concludes: **the analogy is misleading enough that the candidate segment should not carry it.** The structural relationship between disposability and the wrapping-regime hierarchy is named explicitly as a *distinction*, not an analogy.

### 5.1 What W₁/W₂ are about

From `#der-class-coercion-via-wrapping`: the W₀/W₁/W₂ hierarchy is about *where directed separation lives* in a wrapped Class-3 component. W₁ enforces directed separation *structurally* at the query boundary — the wrapper's $q_M$ query selector is type-signed to have no $G_W$ argument, so the component's belief-update path is goal-blind by *construction*. W₂ enforces directed separation only *behaviorally* — a single goal-conditioned call's response is parsed into $M_W$ and $G_W$ slots, and the separation is real only insofar as the component complies with the prompted instruction-to-separate. The leakage bound under W₂ is the component's *instruction-following fidelity*; under W₁ it is pretraining-induced *mutual information* between query content and goal content.

The thing being separated is the *belief-update path* from the *goal-conditioning path*. The hierarchy is about what happens *during one cycle* of the wrapper's operation — does $G_W$ enter the $f_M$ computation or not? It is fundamentally about *information flow within a single processing step*.

### 5.2 What probe-disposability is about

Probe-disposability is the practitioner-flagged invariant that $t_\text{convert} \gt t_\text{reimplement}$ — converting a disposable prototype into production code costs more than reimplementing the production code from scratch using what the prototype taught. The invariant is about *cross-temporal contamination*: code written under the disposable-probe register (deferred robustness, deferred correctness, deferred style, deferred edge-cases) cannot be safely promoted into the production register because the deferrals are structurally embedded in the prototype's substance.

The thing being separated is *probe-substrate* from *production-substrate*. The invariant is about *what happens between probe and production* — does prototype code leak into mainline or not? It is fundamentally about *artifact-level isolation across time*.

### 5.3 Why these are structurally different

Three structural disanalogies make the analogy a category error:

**(D1) Different separated quantities.** W₁/W₂ separate *information* (goal-state from belief-update state). Disposability separates *artifacts* (prototype code from production code). Information and artifacts are not the same kind of thing — information can leak through artifact-level commitments; artifacts can carry information faithfully or deceptively. Conflating them treats a wrapping-regime statement and an artifact-isolation statement as instances of the same machinery when they are not.

**(D2) Different temporal scope.** W₁/W₂ are *per-cycle* — they govern what flows during a single $f_M$ computation. Disposability is *cross-cycle* — it governs whether the prototype's residue contaminates a future production cycle. The two operate on different timescales and have different failure modes (within-cycle goal-leakage vs. across-cycle artifact-contamination).

**(D3) Different leakage measure.** The W₁/W₂ leakage bound is a *KL-divergence* on the component's response distribution (`#der-class-coercion-via-wrapping` Theorem 2). The disposability invariant is a *time-comparison* ($t_\text{convert} \gt t_\text{reimplement}$). The first is information-theoretic; the second is cost-comparative. There is no natural reduction between them.

The deeper structural recognition: **disposability is the developer-side analog of `#scope-agent-identity`'s singular-trajectory commitment, not of W₁/W₂.** The agent's identity is grounded in its unique causal trajectory $\mathcal C_t$; the developer's *probe* is *deliberately not* on the production trajectory — that is what disposability means. A disposable prototype is, in `#scope-agent-identity` vocabulary, code that exists on a *forked sandbox trajectory* that the production trajectory does not depend on causally. The "burn it after reading" discipline is the developer's commitment that the sandbox trajectory does *not* flow back into production. This is a much closer structural fit than the W₁/W₂ analogy — both disposability and sandbox-vs-production are about *trajectory isolation*, not information-flow within a single processing step.

### 5.4 What the candidate segment should say instead

The candidate segment should:

1. **State the probe-class typology** as the operational decomposition of $\mathcal T_\text{probe}$, with the six probe-classes carrying their distinct $(\nu, U_o, \text{target})$ signatures. No reference to W₁/W₂.

2. **Name disposability as a probe-specific invariant** ($t_\text{convert} \gt t_\text{reimplement}$ for the disposable classes; $\text{persistent skeleton}$ for the non-disposable tracer class). State it as a *purity guarantee* on the probe's artifact-substrate, distinct from the developer-agent's goal-state.

3. **Flag the structural distinction from W₁/W₂ in Discussion**, briefly: "Probe disposability is structurally distinct from `#der-class-coercion-via-wrapping`'s wrapping-regime hierarchy. The wrapping hierarchy governs per-cycle information flow within a wrapped Class-3 component; probe disposability governs cross-cycle artifact isolation between probe-substrate and production-substrate. Conflating them is a category error; the closer structural analog of disposability is `#scope-agent-identity`'s singular-trajectory commitment specialized to private workspace branches." (One paragraph; the spike here carries the working-out.)

4. **Do not import the W₀/W₁/W₂ vocabulary into the candidate segment.** The probe channel does not need a leakage-regime hierarchy; it needs a class typology and an artifact-isolation invariant. The wrapping-regime machinery is doing real work elsewhere (`#der-class-coercion-via-wrapping` for the AI-agent composite, the sibling spike for the running-software composite); pulling it into the developer-tempo channel decomposition is over-extending its scope.

This is the strengthen-before-soften discipline applied to the analogy itself. The original framing (in mining yield #1) *proposed* the W₁/W₂ mapping; the spike-side work here *strengthened the inquiry* by checking whether the structural mapping holds, and found it doesn't. The honest landing is not "weakened to a metaphor" — it is "the mapping was refuted by the directed-separation-at-information-flow vs. trajectory-isolation-at-artifact-level distinction; the correct structural analog is `#scope-agent-identity`'s singular-trajectory commitment." This is integration-as-replacement (`feedback_integration_is_replacement`): the false analogy is deleted, the true structural relationship is named.

## 6. Sibling-spike coordination

This spike runs in parallel with five others. Two have structural dependencies on this work; one is the runtime-tempo sibling.

### 6.1 Spike 1 — `spike-running-software-agent.md` — runtime-tempo sibling

The running-software-agent spike (TST-IDEAS §A1) carries the candidate segment `#der-runtime-tempo-decomposition` — $\mathcal T_\text{runtime} = \mathcal T_\text{sense} + \mathcal T_\text{decide} + \mathcal T_\text{actuate}$, with matrix-Loewner weakest-channel bottleneck on the runtime side. The structural shape is identical to this spike's developer-side decomposition. Three places the sibling work coordinates:

- **Matrix-Loewner specialization is shared machinery.** Both spikes invoke `#deriv-matrix-persistence-condition` to convert the additive scalar decomposition into a per-channel bottleneck reading. The "weak-direction is the bottleneck" payoff is structurally identical. The sibling spike should cross-reference this spike's §3 derivation rather than re-deriving, and vice versa; the candidate segments can then share Discussion language without duplicating the matrix-Loewner argument in two places.
- **The runtime channels are distinct from the developer channels.** Runtime $\mathcal T_\text{sense}$ (telemetry / health-check / request-stream) ≠ developer $\mathcal T_\text{obs}$ (code-reading / queries) — they have different $(\nu, U_o)$ regimes (runtime is continuous high-frequency; developer is event-driven medium-frequency) and different upstream substrates (runtime sensors are physical; developer observation is cognitive). The candidate segments should not over-unify; the parallel is structural (both decompose into three channels with a matrix-Loewner bottleneck), not content (the channels are doing different work).
- **Composite reading: developer + runtime as joint agent.** TST-IDEAS A2 (the composite developer-agent under AI augmentation) names the composite of developer + AI + running service + tooling. The composite's tempo is a composition of the developer-channel tempo and the runtime-channel tempo, with `#der-tempo-composition`'s Brooks's-Law inequality binding. Neither this spike nor the sibling should carry the composite reading — that lives in the A2 spike. Both should flag the forward-pointer.

**Action item for cross-spike reconciliation:** the matrix-Loewner specialization (§3) should land in *one* of the two candidate segments and be cross-referenced from the other. Recommend it lands in the developer-tempo segment (this spike) because the developer-agent is the high-identifiability calibration substrate (`#obs-software-epistemic-properties`); the runtime-tempo segment cross-references back.

### 6.2 Spike 4 — `spike-software-unmaintainability-bifurcation.md` — consumes $\mathcal T_\text{dev}$

The unmaintainability-bifurcation spike (TST-IDEAS §A3) carries the candidate segment `#hyp-software-unmaintainability-bifurcation` — the codebase enters the *unmaintainable* regime when $\mathcal T_\text{dev}$ falls below the persistence threshold $\rho/\lVert \delta_\text{critical} \rVert$. The bifurcation argument *uses* this spike's $\mathcal T_\text{dev}$ as its left-hand side. Two coordination points:

- **Aggregate-vs-per-channel: which threshold applies?** The bifurcation argument as stated in A3 reads the persistence inequality at the *scalar* $\mathcal T_\text{dev}$ level. This spike's §3 shows the scalar reading is unsafe; the binding inequality is per-channel. The bifurcation spike should be updated to carry both forms — the scalar bifurcation as the operational baseline, the per-channel bifurcation as the sharpening. A codebase can be "scalar-maintainable but per-channel unmaintainable" — Ebbinghaus $U_o^\text{obs}$ decay can push $\mathcal T_\text{obs}$ below threshold while $\mathcal T_\text{probe}$ stays high (a codebase with great tests but unreadable production code). The G2 danger-zone in the bifurcation argument is most cleanly diagnosed as *$\mathcal T_\text{obs}$-channel failure under Ebbinghaus decay*, not aggregate failure.
- **F-obs / F-explore / F-probe failure modes from §3.2 are the bifurcation's failure typology.** The three named failure modes in §3.2 give the bifurcation segment its qualitative content: which channel fails determines what "unmaintainability" *looks like* in practice. The bifurcation spike can adopt the three-failure-mode catalog directly.

**Action item for cross-spike reconciliation:** the bifurcation spike's argument should be lifted from scalar to per-channel form, with this spike's matrix-Loewner reading as the binding constraint. The three named failure modes (F-obs / F-explore / F-probe) can be used to operationalize "unmaintainable" with finer grain than the scalar threshold alone supports.

### 6.3 Coordination assumption to name explicitly

This spike's matrix-Loewner specialization (§3) assumes the developer-channel tempo $\mathcal T_\text{dev}$ composes with $\mathcal T_\text{runtime}$ (the running-software-agent sibling spike) by *additive* aggregation under the same channel-independence caveat that `#def-adaptive-tempo` applies internally. That is: if a developer-agent operates against a running-service composite, the composite-agent's adaptive tempo is the developer's per-channel tempo plus the runtime's per-channel tempo, with the matrix-Loewner bottleneck applying to the *composite* channel structure. The composite has six channels (three developer + three runtime), not three, and the bottleneck binds the worst of six.

This is the composition assumption the A2 spike will need to verify. Naming it here for the sibling reconciliation: **the developer-tempo decomposition (this spike) and the runtime-tempo decomposition (sibling spike 1) are sub-vectors of a joint composite-tempo vector, with matrix-Loewner persistence applying to the joint.** The A2 spike on the composite developer-agent will need to either confirm or refute this composition rule. If it fails to hold (e.g., because developer-channel events couple non-trivially with runtime-channel events under the AI-augmentation regime — a plausible failure mode given AI agents that observe both code and runtime telemetry), the candidate segments will need to surface the failure in Discussion.

## 7. Candidate segment shape

The candidate segment `#def-developer-tempo-channels` under `02-tst-core/` Ch.2:

```yaml
---
slug: def-developer-tempo-channels
type: definition
status: discussion-grade (per-channel decomposition); robust qualitative (matrix-Loewner specialization)
depends:
  - scope-developer-agent
  - def-adaptive-tempo
  - deriv-matrix-persistence-condition
  - obs-software-epistemic-properties
  - def-causal-information-yield
  - der-code-quality-as-observation-infrastructure
  - hyp-causal-discovery-from-git
stage: draft
---
```

Cadence (per `FORMAT.md`):

1. **Title:** Developer-Tempo Channel Decomposition.
2. **One-sentence summary:** The developer-agent's adaptive tempo decomposes into three Pearl-level-and-commitment-status-distinct channels — observation, exploration, and probe — with each having its own $(\nu, U_o, \eta^\ast)$ profile, and aggregate developer-channel persistence bound by the matrix-Loewner weakest-channel condition.
3. **Formal Expression:** §2 above (the three-channel decomposition with per-channel tables) + §3.1 (the matrix-Loewner specialization at the developer level) + §4 (chronicle-derivable operational definitions).
4. **Epistemic Status:** The decomposition is *discussion-grade* as a definitional taxonomy; the matrix-Loewner specialization is *robust qualitative* (lifted from `#deriv-matrix-persistence-condition`'s exact form under the channel-independence caveat); the chronicle-derivable estimators are *empirical* with named scope conditions (probe-channel clean, explore-channel lower-bound, obs-channel out-of-chronicle).
5. **Discussion:** §3.2 (the three named failure modes), §3.3 (cross-channel coupling and when the diagonal form fails), §5.3 (the structural distinction from W₁/W₂), §6 (sibling-spike coordination — composite-agent composition).
6. **Working Notes:** The W₁/W₂ disanalogy strengthening trail (§5 here), the $\mathcal T_\text{obs}$ instrumentation-gap detail (§4.3 here), the cross-spike composition-assumption flag (§6.3 here). These can be removed at `candidate` stage per FORMAT.md Gate 4.

The candidate segment will then close the leading `--GAP--` row in `02-tst-core/OUTLINE.md` Ch.2, leaving the trailing GAP (`#def-developer-tempo-channels` — already named in the OUTLINE row, matching this slug) resolved.

## Working Notes

- **The strongest single content this spike contributes** is §5's negative result: the W₁/W₂ analogy proposed in the original mining yield is a category error, not a metaphor in need of softening. The structural distinction work makes the candidate segment cleaner by removing the temptation to over-unify probe disposability with wrapping-regime leakage. Per *integration is replacement*, the false analogy should be deleted from the segment body (and from `03-pragmatic-mining.md` #1's translation paragraph if that file is re-touched), not kept-softened-with-a-pointer.
- **Math-lives-in-segments check.** The load-bearing math in this spike is (a) the additive channel decomposition (§2.3), (b) the matrix-Loewner specialization at the developer-channel level (§3.1), and (c) the three per-channel failure-mode characterization (§3.2). None of (a)–(c) carries novel theorem-grade derivation beyond what `#def-adaptive-tempo` and `#deriv-matrix-persistence-condition` already prove; the spike's contribution is specialization to the developer-agent's three-channel structure. So the spike does not need an appendix segment in `01-aat-core/` — the math is application of existing AAT machinery, and lands in the candidate TST segment directly.
- **The probe-class typology table (§2.2) is the spike's main operational content.** It carries six named probe-classes from the Pragmatic Programmer mining substrate (substrate citation in frontmatter), each with characterized $(\nu, U_o, \text{target}, \text{disposability})$ signature. The candidate segment will carry the table; the spike's role is to record where the typology came from and the citation-chain to the original analyses.
- **Chronicle-derivable operationalizations (§4) are the bridge to empirical work.** A future cycle could use these as the basis for a calibration exercise on a mature open-source repository — compute $\mathcal T_\text{probe}^\text{commit-rate}$, $\mathcal T_\text{explore}^\text{scratch+revert}$, and a lower-bound $\mathcal T_\text{obs}$ from commit-message comprehension-references, and check whether the matrix-Loewner persistence-bound prediction matches the observed periods of project-maintainability vs. degradation. Empirical work not in scope for this spike; flagged for `TODO.md`.
- **Disposability connection to `#scope-agent-identity` (§5.3 closing point) is the philosophically deepest move in this spike.** The recognition that disposability is the developer-side analog of singular-trajectory commitment (specialized to sandbox vs. production trajectories) gives the practitioner discipline a structural grounding in AAT. This is worth surfacing in the candidate segment Discussion as a forward-pointer to `#scope-agent-identity`; whether it warrants its own appendix in 01-aat-core is a future-cycle judgment call.
- **Sibling-spike action items (§6) are coordination flags, not deliverables for this spike.** This spike does not perform the cross-spike reconciliation; it names the assumptions and recommends where the reconciliation work should land. The composite-agent (A2) spike, when authored, will be the natural place for the composition-rule verification.
- **`$\delta_\text{critical}$ per channel.** This spike's matrix-Loewner reading uses $\delta_\text{critical,obs}$, $\delta_\text{critical,explore}$, $\delta_\text{critical,probe}$ as if they were independently characterizable. In practice, the developer-agent's per-channel critical-mismatch thresholds couple — a stale $M_t$ from low $\mathcal{T}_\text{obs}$ feeds into wrong commits which raise the probe-channel mismatch which raises the verification cost. The candidate segment should carry the *channel-independent threshold approximation* as the default reading with the caveat that the off-diagonal coupling in the $D_\delta$ matrix is a follow-on cycle item. Not in scope here.
