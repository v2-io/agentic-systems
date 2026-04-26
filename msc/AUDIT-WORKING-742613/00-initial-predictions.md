# Initial Predictions

Audit workspace: `msc/AUDIT-WORKING-742613/`
Date: 2026-04-25

## Source-Ordering Notes

I have read only the audit instructions, `README.md`, top-level `OUTLINE.md`, the four component outlines, `LEXICON.md`, `NOTATION.md`, `CLAUDE.md`, and `FORMAT.md`.
I have not read `TODO.md`, `CHANGELOG.md`, `LOG.md`, `PROPOSALS.md`, `CLAUDE-2.md`, prior audits, spikes, `msc/` artifacts other than the instructions and this workspace, `ref/`, git history, or external web sources.

There is one instruction tension worth preserving: `CLAUDE.md` says "Read `TODO.md` first", while `msc/de-novo-audit-instructions.md` says to avoid `TODO.md` until after the canonical pass / Phase 2 triangulation.
For this audit I am treating the de-novo audit instructions as the task-specific override and deferring `TODO.md`.

The orientation files themselves contain spoiler-like summaries and references to known spikes, recent results, known gaps, and sample past findings.
I am not treating those as prior audit material because the protocol explicitly asks for these files first, but I will keep in mind that my "de novo" posture is not ignorance; it is first-hand segment engagement without consulting historical reasoning trails.

## Topology As I Understand It

The framework has four components in canonical order:

1. AAD (`01-aad-core`) is the mathematical core.
It begins with adaptive systems under uncertainty, narrows to actuated/purposeful agents, then studies multi-agent/composite dynamics and supporting appendices.

2. TST (`02-tst-core`) is a software-domain instantiation and calibration laboratory.
It depends directionally on AAD and should not feed mathematical commitments back into AAD except as validation / operationalization.

3. Logogenic agents (`03-logogenic-agents`) handle language-constituted agents, especially current LLM/code agents where directed separation fails and Section II's modular-agent exact results become approximate or require modification.

4. Logozoetic agents (`04-logozoetic-agents`) are future work: morally weighted persistence for language-living agents with temporal continuity, sovereignty, and theory of mind.
There are no formal segments yet.

Within AAD, I expect the load-bearing spine to be:

- Section I primitive scope: agent-environment boundary, observation/action channels, chronica, causal structure, Pearl hierarchy, model as compressed history.
- Section I update / tempo / persistence machinery: recursive update, mismatch, gain, adaptive tempo, mismatch dynamics, sector bridge, Lyapunov stability, persistence threshold, structural adaptation, timescale nesting.
- Section II modular-agent narrowing: complete state, directed separation, objective/value/strategy definitions, causal hierarchy requirements, strategy DAG, edge updates, strategic tempo, orient cascade.
- Section III composition: multi-agent vs composite scope, closure defect, tempo composition, unity dimensions, communication gain, team/adversarial persistence, strategic composition, opacity, per-dimension bottlenecks.
- Appendices are not peripheral; they contain proof machinery and meta-patterns that can be more load-bearing than their placement suggests.

The integration story appears to be "form-shaping for external theorem applicability":

- AAD defines internal objects so that existing results from control theory, information theory, causal inference, contraction analysis, potential/monotone games, etc. can be applied cleanly.
- The theory's novelty likely lives less in isolated equations and more in the repeated pattern: choose or derive the coordinate / scope / separability condition that makes a known theorem apply, then propagate the result across agent classes.
- The three AAD meta-segments named in the outline look especially important: `disc-separability-pattern`, `disc-identifiability-floor`, and `disc-additive-coordinate-forcing`.
I predict they are intended to make the whole corpus auditable by classifying positive separability regimes, negative no-go floors, and constructive coordinate-forcing moves.

## Predictions By Component

### AAD Section I

I expect Section I to be the cleanest part of the framework.
The definitions should be mostly well-scoped, but I expect some boundary tension between "adaptive system" and "agency" because the README uses richer prose conditions for "agentic system" while the outline says `scope-agency` narrows by Pearl-level-2 action contrast.

Specific predictions:

- `scope-adaptive-system` will define broad inclusion by observation plus residual uncertainty, probably excluding fully known deterministic systems and no-observation systems.
Possible issue: mismatch correction may be rhetorically present in summaries but not a formal scope condition if the scope only says observe under uncertainty.

- `scope-agency` will use the existence of at least two actions with distinct interventional outcome distributions.
Possible issue: this is a weaker formal boundary than the README's "goal-directed action + outcome model + model adaptation" characterization.
I will watch for "agentic" being used both as interventional capacity and as purposive agency.

- `post-composition-consistency` will be axiomatic / scale-invariance oriented and may be vulnerable to overclaim if it treats level-independence as forcing compatibility without enough conditions on abstraction maps.

- `form-information-bottleneck` should be a canonical formulation rather than exact derivation.
I expect possible status mismatch if it is labeled too strongly.

- `der-recursive-update` and `deriv-recursive-update` are predicted to be among the strongest formal results: compressed history plus online update constraints force a recursive state update.
I expect this to be mostly sound, but I will watch for hidden assumptions about sufficiency of the recursive state and whether "unique" means unique up to state isomorphism.

- `emp-update-gain` is likely an empirical / Kalman-inspired generalization.
I expect it may use the uncertainty ratio as a universal update principle; the audit should check that it is not presented as exact outside Gaussian/quadratic/linearizable cases.

- `hyp-mismatch-dynamics` is likely a fluid-limit ODE from discrete/event updates.
I expect this to depend heavily on small-gain / high-rate assumptions.
The outline and notation already flag GA-5; I will watch whether downstream exact results remember that the ODE is a hypothesis or approximation.

- The sector-condition / persistence machinery should be exact conditional on the sector condition.
The audit target is not whether Lyapunov algebra works in general, but whether the theory cleanly distinguishes (a) sector assumption, (b) gain-sector derivation in specific regimes, and (c) universal persistence rhetoric.

- `result-structural-adaptation-necessity` may be conceptually strong but could overclaim necessity if it equates failure within a model class with requirement for structural adaptation rather than alternative choices such as accepting lower performance, changing objectives, or expanding observations.

- `form-consolidation-dynamics` is draft and may import cognitive language into Section I.
I predict status/typing pressure here: it may be more hypothesis / formulation than derivation.

### AAD Section II

I expect Section II to be the richest source of scope findings because it has a major explicit architectural restriction: exact results apply to Class 1 modular agents, not fully merged LLM-like agents.

Specific predictions:

- `form-complete-agent-state` and `def-strategy-dimension` should be definitions/formulations, not derivations.
I will watch whether the split `G_t=(O_t,\Sigma_t)` is presented as inevitable where it is actually useful modeling choice.

- `der-directed-separation` should be scope-sensitive.
The outline says it is draft but exact results depend on it; I expect hidden downstream overclaim if later segments use the orient cascade without repeating Class 1 / modular-agent conditions.

- `def-value-object`, `def-satisfaction-gap`, and `def-control-regret` probably hinge on a continuation convention hierarchy.
I predict the arithmetic split is exact once the value object is chosen, but conclusions drawn from it vary by horizon convention.
I will watch for local heuristics being promoted to global conclusions.

- `der-causal-hierarchy-requirement` and `der-loop-interventional-access` should be strong if they carefully distinguish needing Level 2 access for planning from actually having enough interventional diversity / identifiability in finite data.

- `scope-ciy-observational-proxy` and `disc-ciy-unified-objective` likely handle a difficult bridge from interventional quantities to observational data.
I expect draft-level caveats and possible dependence omissions.

- `norm-explicit-strategy-condition` sounds normative.
I predict it may be vulnerable to "planning beats exploring" overgeneralization unless opportunity cost and observation value are explicit.

- `def-strategy-dag` is likely central and complex.
Predicted risk: DAG acyclicity from temporal ordering may hold for plan graphs but not for iterative strategies with feedback loops unless time-unrolled.
If cycles are ruled out by representation rather than world structure, that should be named as formulation, not derived fact.

- `der-causal-insufficiency-detection`, `disc-credit-assignment-boundary`, and the correlated-failure hierarchy should be high-yield.
I expect negative results / identifiability floors to be sound in spirit but possibly under-specified in finite-sample or active-intervention cases.

- The edge-update / strategy-persistence chain is likely the main mathematical risk.
I will look for whether scalar edge credences with gain-style updates remain valid under correlated failures, common causes, OR-node exploration gating, and unobservable edges.

- `der-orient-cascade` is predicted to be exact only under directed separation.
I expect integration drift wherever later components treat it as the normal cognitive loop for logogenic agents despite the logogenic outline saying it fails by construction.

### AAD Section III

I expect Section III to be the main integration-drift source.
The outline already signals evolving scope routes, composition closure, strategic composition, opacity, and meta-pattern extensions.

Specific predictions:

- `scope-multi-agent` vs `scope-composite-agent` is a likely contradiction surface.
The audit instructions themselves mention an observed example around adversarial pairs and C-iv equilibrium-convergent strategic-composite scope.
Because the instructions mention it, I will not treat this as my own prediction, but I will still read the current src text and determine whether the current corpus still has the drift.

- `form-composition-closure` likely depends on projection / admissibility assumptions.
I predict it may overstate composition as approximate homomorphism unless contraction or Lipschitz assumptions are explicit.

- `der-tempo-composition` may be a heuristic/sketch because sub-additive tempo can fail with strong specialization, redundancy, parallelism, or communication protocols.
I expect it should be conditional rather than general.

- `hyp-directed-separation-under-composition` should be important for bridging Section II to composite agents.
I predict it will reveal whether Class 1 modularity survives aggregation or whether composites often become Class 3.

- Unity dimensions (`U_M`, `U_O`, `U_\Sigma`) likely carry sign/domain issues.
NOTATION says they are in `[-1,1]`, but some gain formulas use uncertainty-like denominators where negative unity might be problematic.
I will watch for dimensional / sign inconsistencies.

- `hyp-communication-gain` likely has the same risk as `emp-update-gain`: uncertainty-ratio analogy may be useful but not generally derivable.

- Adversarial dynamics results should distinguish action-based disturbance injection from communication-tempo effects.
I predict at least one downstream segment may double-count or conflate these, unless recent repair has propagated.

- `deriv-strategic-composition`, `der-agent-opacity`, and `der-interaction-channel-classification` look very recent / dense / claim-heavy.
I expect these are the highest-value audit targets for math or status-label issues.

### AAD Appendices

I expect appendices to contain both solid proof support and some speculative meta-structure.

Specific predictions:

- `deriv-sector-condition`, `result-sector-persistence-template`, and `deriv-discrete-sector-condition` are load-bearing for the whole framework.
If there are math errors, their propagation is large.
I will prioritize at least one direct algebra check in this zone.

- `deriv-persistence-cost` and information-rate/channel-capacity floors may depend on external theorem form.
I expect external citation verification would be high-value here.

- `deriv-graph-structure-uniqueness` may be strong but vulnerable to the exact interpretation of causal sufficiency and the Causal Markov Condition.

- `deriv-strategic-dynamics`, `deriv-edge-update-natural-parameter`, `deriv-adaptive-gain-dynamics`, `deriv-detection-latency`, `deriv-l1-update-bias`, and `deriv-fisher-whitened-update-rule` likely form the under-audited strategic-math cluster.
I predict some assumptions will not be propagated back to main Section II segments.

- `disc-identifiability-floor`, `disc-separability-pattern`, and `disc-additive-coordinate-forcing` are likely the best candidates for "framework beauty" but also for over-systematization.
I will watch whether meta-patterns are genuinely derived from multiple instances or whether the framework is forcing an attractive taxonomy onto heterogeneous results.

- `result-contraction-template` sounds powerful and broad.
I predict this is a high-risk overclaim zone unless topology-specific composition closures and metric assumptions are carefully constrained.

### TST

TST should be less mathematically closed and more empirical / domain-specific.
I expect useful software theory, but many claims should have empirical, heuristic, or normative status rather than exact status.

Specific predictions:

- `post-temporal-optimality` is normative, not descriptive.
It should require "equivalent outcomes" and may need a careful notion of outcome equivalence that includes future maintainability, risk, and learning.

- `scope-software` likely defines active/evolving systems via probability of future change.
Potential issue: threshold choice may be arbitrary.

- `result-specification-bound` could be very strong in the implementation-time-to-zero limit but may overclaim if "unspecified" is not decomposed into latent user intent, inferable context, and exploration.

- `der-change-expectation-baseline` likely uses Lindy-like reasoning.
I expect empirical or prior-sensitive status.

- Dual optimization of comprehension and implementation time is plausible.
Potential issue: comprehension time may itself be an investment that changes future implementation distribution, making simple additive decompositions approximate.

- Code-quality-as-observation-infrastructure is a promising AAD bridge but is missing in outline.
I expect the existing TST src may have gaps around the most distinctive AAD-grounding claims.

- Git-based causal discovery is marked missing; I expect TST will overstate software as a calibration lab in orientation docs relative to current src coverage unless `obs-software-epistemic-properties` and related segments have landed elsewhere.

### Logogenic

I expect the logogenic component to be small but important because it declares the failure of directed separation for LLM-like agents.

Specific predictions:

- `scope-logogenic-agent` may call AI agents "actuated agents" while current systems often have externally set objectives and discontinuous memory.
The scope should separate channel type from autonomy / continuity.

- `obs-context-turnover` should be one of the strongest practical observations in the framework.
I expect it may conflate 100% context reset with 100% `M_t` reset if external tools / memory / hidden provider state are not handled carefully.

- `def-coupled-update-dynamics` should be central: it should replace the sequential orient cascade with coupled update.
I will watch whether it is only a black-box formulation or whether it names observability / diagnosability constraints.

- `result-section-ii-survival` is a high-risk status target.
Classifying 16/24 exact, 5 approximate, 2 modified is potentially useful but should be traceable to explicit criteria.

- `result-coupled-diagnostic-framework` may recover post-hoc decomposition but should not imply causal separability.

- `disc-m-preservation` likely bridges to external memory.
Risk: treating persisted text as equivalent to preserved model state without loss / retrieval / interpretation conditions.

- `scope-observation-ambiguity-modulation` sounds like a key bias-bound scope condition.
I expect it depends on `deriv-bias-bound` and should be mathematically constrained.

### Logozoetic

There are no segments, so the audit here is mostly an absence report.
I expect the framework's most philosophically loaded claims live in README / LEXICON / msc rather than canonical segments.
Since README is not an audit target under the instructions, I should not turn philosophy concerns into findings unless they appear in current segment text.

## Predictions About Open Gaps

Expected theory gaps:

- General contraction from sector-bounded correction is probably not proved.
If composition closure relies on it, that should remain an explicit assumption.

- Directed separation for fully merged / transformer-style agents is unavailable; logogenic coupled dynamics is the declared bridge but likely not yet mathematically mature.

- Finite-sample identifiability and intervention-design requirements for strategic edge updates are likely incomplete.

- N-agent scaling and endogenous coupling in composition are still gaps by outline admission.

- TST's empirical claims probably lack full validation in current canonical src, especially around cognitive load and coherence/coupling.

- Logozoetic formalization is absent.

Expected integration debt:

- AAD core may have been strengthened faster than README / LEXICON / TST / logogenic segments have propagated.

- Class 1 modular scope conditions may not be repeated in all Section II downstream uses.

- Recent meta-patterns and new scope routes may not be reflected in earlier composition segments.

- Missing segments in TST may leave top-level orientation claims stronger than canonical support.

## Predictions About Overclaim

Areas where framing may outrun mathematics:

- "Agentic" as a formal action-intervention boundary vs richer goal/model/adaptation agency.

- Universal update gain from uncertainty ratio outside Kalman / gradient / variational cases.

- Continuous-time mismatch ODE treated as exact when it is a fluid-limit approximation.

- Strategy DAG uniqueness if cycles are handled by time-unrolling rather than excluded by reality.

- Edge-update validity under correlated failures / latent common causes.

- Composite-agent closure if projection admissibility and contraction assumptions are not enough.

- Logogenic "language as encoded reasoning" if it appears in canonical segments as more than hypothesis / philosophical motivation.

- TST least-time optimality if "equivalent outcomes" is underspecified.

## What Would Be Most Novel If It Holds

Most consequential candidate contributions:

- A single persistence inequality / sector template spanning adaptive systems, strategic dynamics, composites, and software development.

- A clean diagnostic split between satisfaction gap and control regret, parameterized by value-convention hierarchy.

- Directed separation as a precise architectural scope condition explaining why modular agents admit an orient cascade and LLM-like agents require coupled treatment.

- Strategy as a probabilistic causal DAG with forced log-confidence / log-odds coordinates.

- Identifiability floors paired with named escape routes: a disciplined way to say what agents cannot infer without changing observation/intervention/compression structure.

- Composition closure / closure defect as a way to decide when interacting agents form an agent.

- Logogenic coupled-dynamics framing that makes 100% context turnover a precise persistence / continuity problem rather than an engineering annoyance.

- TST as a high-identifiability calibration lab for AAD, if the empirical/operational bridge is strong enough.

## Expected Finding Types

I expect more integration-debt findings than pure math-error findings.

Likely finding types:

- Dependency-order failures in the OUTLINE linearization, especially because appendices are listed after main sections but main sections may depend on appendix derivations.
The audit instructions allow Appendix-A proof back-pointers but treat non-appendix downstream dependencies as critical.

- Missing dependency entries where a segment uses a concept from a prior segment without declaring it.

- Status-label mismatches: `exact` where conditional / formulation / hypothesis would be more honest, or "derived" language attached to representational choices.

- Scope propagation failures: Class 1 modular restrictions, contraction assumptions, finite-sample identifiability, and recent composition sub-scopes.

- Mathematical edge-case failures in worked examples / appendix derivations, especially sign, norm, or coordinate-system errors.

- Top-level orientation claims unsupported by current canonical segments due missing TST / logozoetic files.

- Process/instruction findings: the audit instructions are strong but internally tense in a few places and require more tool-level operationalization for Codex-style agents.
