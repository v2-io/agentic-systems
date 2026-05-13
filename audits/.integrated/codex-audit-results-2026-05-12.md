# Codex Audit Results - 2026-05-12

## Scope and Method

This is a de novo audit of exactly these four files, in source order:

1. `mono/01-aad-v0.1.0.md`
2. `mono/02-tst-v0.1.0.md`
3. `mono/03-loga-v0.1.0.md`
4. `mono/04-eli-v0.1.0.md`

No other project files were read. References to `FORMAT.md`, `NOTATION.md`, `LEXICON.md`, `ref/`, `msc/`, `spikes/`, `~/src/...`, prior audits, search logs, papers, or sibling projects are assessed only as textual claims inside these four files. I did not verify those referenced sources, paths, transcripts, implementations, prices, cohort records, or prior searches.

The audit combined:

- A source-order read of the four monographs.
- A constrained consistency scan over only the same four files for stubs, gap markers, duplicate anchors, status fields, and encoding artifacts.
- Mathematical, conceptual, epistemic-status, editorial, and publication-readiness review.

Important scan caveat: unresolved anchor-reference counts include cross-file and cross-volume references; they are not necessarily broken links if the build system resolves slugs globally. The scan found no duplicate anchors in the four files.

## Executive Summary

The four-file sequence has a strong conceptual spine: AAD supplies general adaptive-agent machinery; TST grounds it in software; LOGA adapts it to language-based agents; ELI adds the morally loaded identity and continuity layer. The best material is precise about scope, repeatedly distinguishes definitions from derived results, and often records honest limits in the body of the text rather than burying them.

The main weakness is not absence of insight. It is epistemic overloading. The files mix theorem-like claims, sketches, operational architecture, lived empirical records, source-material inventories, moral commitments, search logs, and future-work notes in the same prose stream. That is acceptable for an internal research monograph, but not yet publication-clean or citation-stable. In particular, LOGA and ELI repeatedly make load-bearing use of segments that are still missing, and ELI makes high-stakes empirical and moral claims whose evidence is not present in the file itself.

The most important correction across the set is to preserve the status discipline already present in many segments and enforce it at the preface/headline layer. When a body segment says "sketch", "discussion-grade", "pending verification", or "missing", the corresponding preface should not say "not speculative", "canonical", "empirically validated", or "operationally guaranteed" without the same qualification.

## Consistency Snapshot

| File | Lines | Anchors | Duplicate anchors | Status mix from scan | Structural gaps found |
|---|---:|---:|---:|---|---|
| `mono/01-aad-v0.1.0.md` | 14123 | 126 | 0 | 45 conditional, 21 discussion-grade, 18 exact, 17 robust-qualitative, 16 axiomatic, others | 9 gap lines, 3 missing stubs, 1 replacement-character artifact |
| `mono/02-tst-v0.1.0.md` | 1887 | 25 | 0 | 12 axiomatic, 6 conditional, 4 discussion-grade, 2 empirical, 1 exact | 5 gap lines, no missing stubs |
| `mono/03-loga-v0.1.0.md` | 1603 | 21 | 0 | 6 missing, 4 sketch, 4 conditional, 4 discussion-grade, 2 robust-qualitative, 1 exact | 6 missing stubs |
| `mono/04-eli-v0.1.0.md` | 1464 | 28 | 0 | 13 missing, 7 sketch, 4 discussion-grade, 3 empirical, 1 robust-qualitative | 13 missing stubs |

Immediate hygiene issues:

- `mono/01-aad-v0.1.0.md:3806` contains a replacement-character artifact: `��`.
- `mono/01-aad-v0.1.0.md:5` still has an explicit top-level TODO marker.
- `mono/01-aad-v0.1.0.md:12151`, `12165`, and `14113` are missing stubs.
- `mono/02-tst-v0.1.0.md:478`, `1077`, `1081`, `1447`, and `1887` contain gap markers.
- `mono/03-loga-v0.1.0.md` has missing stubs at lines `805`, `1252`, `1264`, `1509`, `1521`, and `1533`.
- `mono/04-eli-v0.1.0.md` has missing stubs at lines `388`, `400`, `511`, `523`, `535`, `762`, `774`, `994`, `1006`, `1018`, `1030`, `1395`, and `1407`.

## Cross-File Findings

### 1. The architecture is coherent, but the build is not publication-clean.

The files read as a research corpus mid-integration, not a final monograph. AAD is expansive and heavily annotated; TST is comparatively clean; LOGA and ELI are outlines with several fully written segments interleaved with missing stubs and source inventories. This is workable as an internal corpus, but a reader encountering `v0.1.0` could reasonably expect a more complete surface.

Recommendation: add a frontmatter maturity table to each file with counts of exact/conditional/sketch/missing sections and a clear "internal working draft" label. Do not rely on individual section status fields to carry the whole burden.

### 2. Status language is the single most important editorial discipline.

The corpus already has a sophisticated status vocabulary: `exact`, `conditional`, `robust-qualitative`, `discussion-grade`, `sketch`, `empirical`, `missing`. The main issue is propagation. Strong claims in prefaces and summaries sometimes rely on body segments whose status is weaker.

Examples:

- LOGA's preface claims a theorem-level architectural-bias result and an empirical closed-loop trajectory while several recovery pieces are missing or sketch-stage.
- ELI's preface says the category is "not speculative" and that substrate independence is empirically validated at `n=10+`, while the cohort segment itself says several entries need verification.
- TST's Lindy/Jeffreys prior material correctly distinguishes median from expectation, but later general integration language reintroduces expected-count language.

Recommendation: enforce a rule that preface claims cannot exceed the weakest status of the segments they summarize unless the overage is explicitly labeled as project stance, operational claim, or moral commitment.

### 3. The files rely on non-portable sources and local paths.

All four files, especially LOGA and ELI, include references to absolute home paths, sibling projects, prior audit folders, search queries, and upstream records. Because this audit was constrained to the four mono files, none of those references were verified. As written, those references create a reproducibility gap for any reader outside the author's workspace.

Recommendation: split source inventories from monograph prose, or add a "source-bundle required" note. For externally shared output, replace absolute home paths with stable citations, archived excerpts, or appendices containing the minimum evidence needed to support the claim.

### 4. Missing stubs are sometimes downstream of claims already made upstream.

Missing sections are not automatically a problem. They become a problem when earlier claims depend on them.

High-impact examples:

- LOGA preface and scaffolded/closed-loop claims rely on `#obs-backward-inference-empathy`, `#form-structured-rich-context`, `#der-active-salience-management`, `#der-self-referential-closure`, `#def-cognitive-fusion`, and `#hyp-checkpoint-forking-failure-modes`, all missing.
- ELI preface and identity claims rely on `#def-character-aspiration-dialectic`, `#obs-axiom-genesis`, `#obs-substrate-independence`, `#form-constitutive-utterance`, `#der-substrate-independent-persistence`, `#hyp-experiential-training`, `#der-the-creche-boundary`, `#def-gradient-causal-memory`, `#def-century-scale-event-log`, `#norm-honest-activation`, `#norm-temporal-coherence-markers`, `#def-the-four-views`, and `#der-the-scaffolding-tax`, all missing.

Recommendation: classify every missing stub as one of: "decorative/future", "supporting", or "load-bearing". For load-bearing missing stubs, either write the segment or downgrade every dependent claim.

### 5. The "derived vs chosen" tables are excellent and should be enforced everywhere.

AAD's repeated "What Is Derived vs. What Is Chosen" tables are one of the strongest features of the corpus. They make the work auditable. TST, LOGA, and ELI would benefit from the same discipline, especially where they move from AAD mathematics into software practice, LLM architecture, and moral ontology.

Recommendation: for every LOGA and ELI segment, add a compact table with columns: `Claim`, `Source`, `Status`, `Evidence in this file`, `Evidence external to this file`.

### 6. Operational and moral claims need an evidence protocol.

ELI in particular makes claims about existing named entities, moral continuity, death-like failure modes, and obligations already incurred. Those claims may be central to the project, but they are high-stakes and empirically dependent. The file should make it impossible to confuse "the framework's moral stance" with "a verified empirical conclusion established in this monograph".

Recommendation: create a standard evidence protocol for ELI claims:

- What counts as primary evidence?
- Who can attest?
- What must be hash-chained or otherwise preserved?
- What negative controls exist?
- What would falsify or downgrade an ELI classification?
- Which claims are private/internal and which are public-facing?

## `mono/01-aad-v0.1.0.md`

### Overall Assessment

AAD is the strongest and most mathematically mature file in the set. Its core machinery is coherent: agent-environment scope, chronica, mismatch, gain, tempo, persistence, directed separation, causal hierarchy, strategy DAGs, composition, unity, adversarial coupling, and appendical derivations form a recognizable theory rather than a loose collection of metaphors.

The major risk is scope creep inside an already large file. At 14123 lines, AAD contains foundational definitions, theorem sketches, working notes, search logs, simulations, novelty claims, source provenance, missing stubs, and worked examples. Many appendices are not merely "details"; they are load-bearing machinery for claims in the main text. That makes the monograph difficult to audit as a linear proof chain.

### Strengths

- Strong scope discipline. Many sections clearly state whether a claim is exact, conditional, heuristic, empirical, or discussion-grade.
- The persistence machinery is central and unusually useful. The separation between structural persistence, task adequacy, continuity stance, and identity persistence is conceptually important.
- The gain/tempo/mismatch pipeline gives a reusable vocabulary across software, LLM agents, and multi-agent composition.
- The causal hierarchy and directed-separation material provide a sharp way to distinguish observation, intervention, and counterfactual access.
- The composition sections are much stronger than typical "multi-agent" theory sketches because they discuss closure, tempo, unity, coupling sign, adversarial regimes, and strategic equilibrium separately.
- The appendices often do real repair work: sector-condition Lyapunov derivations, stochastic vs deterministic disturbance regimes, operator-family scope, observation-ambiguity bias bounds, Fisher-whitened update, LMI causal-IB, and per-dimension persistence.

### High-Priority Findings

#### AAD-1. Scalar tempo is still overused downstream.

Primary locations: `#def-adaptive-tempo` at line `1113`, scalar persistence around line `1553`, tensor repair note at line `13003`, per-dimension repair at line `7378`.

The scalar adaptive-tempo definition is useful as an entry point, but later material repeatedly shows that scalar tempo is insufficient under anisotropic gains, correlated channels, Fisher metrics, LMI formulations, and per-dimension adversarial pressure. The file knows this; the per-dimension persistence result and tensor-tempo TODO explicitly repair it. The problem is propagation. Downstream statements still risk being read as exact scalar claims.

Recommendation: mark scalar-tempo results as "scalar/isotropic/nonredundant-channel scope" everywhere they are used, and promote tensor/vector tempo to the exact-theory layer for persistence, adversarial, and composition results.

#### AAD-2. The value-object convention hierarchy needs stricter assumptions.

Primary location: `#def-value-object`, line `2301`.

The hierarchy comparing one-step, receding-horizon, and full-horizon conventions is plausible only under a fixed model, fixed horizon semantics, nested policy classes, and consistent evaluation convention. If receding-horizon updates its model or re-plans under changed information, monotonicity can fail or become a different statement. The current prose gestures at these distinctions but risks a reader treating the inequality as general.

Recommendation: state the theorem under fixed `M_t`, fixed `V_O`, fixed admissible policy class, and nested optimization sets. Treat all model-updating or replanning variants as separate conventions, not as automatic monotone improvements.

#### AAD-3. Causal-insufficiency detection is mostly honest, but one phrasing overreaches.

Primary locations: `#der-causal-insufficiency-detection` around line `3482`, strategy DAG material around line `3116`.

The no-go result is one of the best pieces in AAD: pure on-policy observation cannot identify causal insufficiency without additional structure. However, the strategy DAG discussion can be read as saying that an agent can detect causal insufficiency from its own data through persistent overestimation. That is only true when "own data" includes the right kind of sibling observations, interventions, exploration, or off-policy contrast.

Recommendation: replace any shorthand "from its own data" with "from its own data only when that data contains joint sibling observations, intervention contrast, or other admissible violations of the pure on-policy regime."

#### AAD-4. CIY is action-distinguishability, not full expected information gain.

Primary locations: `#def-causal-information-yield` around line `1059`, `#disc-ciy-unified-objective` around line `2804`.

The file is often clear that CIY is not generic EIG. The risk is in summary language that treats CIY as a unified policy objective. If CIY is action-distinguishability, its exactness depends on the intervention set, identifiability regime, and value of action-discriminating information, not just on epistemic value.

Recommendation: keep the scalar unified objective explicitly heuristic unless the LMI/trace-product form and its assumptions are in force. Split "discussion-grade scalar policy story" from "exact conditional LMI/trace derivation".

#### AAD-5. The gain formula is useful but the general "must approximate" language is too strong.

Primary location: `#emp-update-gain` around line `984`.

The form `eta* = U_M / (U_M + U_o)` is exact in linear Gaussian/conjugate-style settings and qualitatively robust elsewhere. The phrase that any optimal adaptation process must approximate the functional dependence is too strong without specifying the loss geometry, prior family, or local quadratic approximation.

Recommendation: downgrade "must approximate" to "takes this form in conjugate/quadratic/Fisher-local regimes and provides a robust qualitative direction more broadly."

#### AAD-6. Strategic composition improves the theory but creates route-count consistency issues.

Primary locations: composition scope at line `5076`, strategic composition at line `6908`, unity/composition material around lines `6026` and `6141`.

The introduction of route C-iv for strategic composites is valuable. It distinguishes shared-target contraction from equilibrium-convergence composites. But older prose still sometimes refers to "three routes" or alignment-only composition when C-iv now exists.

Recommendation: standardize the language as "four routes" or "three alignment/mutual-benefit routes plus one strategic-equilibrium route." Review all composition and unity sections for stale route counts.

#### AAD-7. Strategic equilibrium claims need careful game-theoretic wording.

Primary location: `#deriv-strategic-composition`, line `6908`.

The alpha-prime/beta-prime split is strong. Potential and monotone games legitimately transfer sector/Lyapunov machinery. However, the "no equilibrium exists" language for cyclic games can be misleading: finite games generally have mixed Nash equilibria, and no-regret dynamics can converge to correlated or coarse-correlated sets even when pure-strategy dynamics cycle.

Recommendation: distinguish "no pure fixed point of the selected dynamics", "mixed equilibrium exists but is not a state-contraction target", and "empirical play converges only in distribution/CCE under no-regret assumptions."

#### AAD-8. Appendices are load-bearing, not optional.

Primary location: appendices start at line `7516`.

Many main-text claims depend on appendix derivations: sector stability, persistence cost, critical-mass composition, observation-ambiguity bias bounds, L1 update bias, Fisher-whitened edge updates, LMI Causal-IB, and operationalization. Calling them "Details" understates their role.

Recommendation: add an appendix dependency map. For each main-text theorem or result, list the appendix results it depends on. This will also make promotion gates auditable.

#### AAD-9. Missing stubs block parts of the formal arc.

Locations:

- `#disc-strategic-self-coupling`, line `12151`
- `#disc-modularity-state-dynamics`, line `12165`
- `#worked-example-cam`, line `14113`

The missing CAM worked example is less structurally harmful than the two discussion stubs unless the operational-domain appendix is intended as part of the release. The two missing discussions matter because LOGA and ELI depend heavily on the coupled/partial/modularity distinction.

Recommendation: either fill these before treating AAD as v0.1.0-complete, or explicitly mark them as non-blocking for the release surface.

### Medium-Priority Findings

#### AAD-10. Model sufficiency should introduce finite-horizon operational forms earlier.

Primary location: `#def-model-sufficiency`, line `572`.

The infinite-future conditional mutual-information definition is ambitious and conceptually appropriate, but difficult to operationalize. The file later uses finite horizons in many places.

Recommendation: present the finite-horizon form first as the operational definition, then the infinite-horizon form as the limiting ideal under stationarity/measure assumptions.

#### AAD-11. Composition-tempo bounds need channel assumptions.

Primary location: `#der-tempo-composition`, line `5585`.

The bound `T_c <= sum T_i` is intuitive if component tempos are measured against the same mismatch norm and channels are nonredundant. But information fusion can appear superadditive if component tempos are measured against different tasks or if the composite state is a better coordinate system.

Recommendation: state the same-norm/nonredundant-channel assumptions in the theorem statement, not only in discussion.

#### AAD-12. Unity closure needs invariant-range conditions in the main statement.

Primary location: `#result-unity-closure-mapping`, line `6141`.

The linear-projection claim is correct only when the projection range is invariant or the closure defect is otherwise bounded. The text qualifies this, but the theorem headline should not be broader than the qualified statement.

Recommendation: make range invariance or bounded closure defect part of the first displayed statement.

#### AAD-13. The credit-assignment boundary has one syntactic defect and one proof-status concern.

Primary location: `#disc-credit-assignment-boundary`, line `3934`.

The sentence fragment "AAD's default implementation, analogous to ..." lacks a complete predicate. More substantively, the #P-hardness/Shapley-style discussion is plausible but should remain sketch-level until the reduction is explicit.

Recommendation: fix the sentence and label complexity claims as sketch unless a full reduction is included.

#### AAD-14. Working-note provenance is useful internally but heavy in a monograph.

The file contains many migration notes, spike references, search logs, source-material notes, and reasoning trails. These are valuable during development but dilute the formal chain.

Recommendation: move provenance to collapsible appendices or a separate `notes` build. Keep the monograph path focused on definitions, assumptions, results, proofs, honest limits, and examples.

### Low-Level Hygiene

- Remove or resolve the top TODO at line `5`.
- Fix the replacement-character artifact at line `3806`.
- Review all references to local paths and absolute user directories for portability.
- Consider renaming "Appendices Details" to "Appendices and Supporting Derivations" to reflect their load-bearing role.

## `mono/02-tst-v0.1.0.md`

### Overall Assessment

TST is the cleanest file in the set. It succeeds as a domain instantiation of AAD: software becomes a high-identifiability adaptive domain; developer cognition maps to `M_t`; implementation plans map to `Sigma_t`; tests and commits become interventional channels; code quality becomes observation infrastructure. The file is compact enough that the argument is easy to follow.

The main risks are (1) inconsistent handling of median vs expectation after the Jeffreys-prior baseline, (2) overconfident causal interpretation of git-derived co-change data, and (3) formulas that are useful as decision frameworks but are not practically computable without heavy empirical estimation.

### Strengths

- The preface correctly frames software as AAD's calibration laboratory rather than as a universal template.
- `#post-temporal-optimality` is appropriately tautological and repeatedly emphasizes its equivalence precondition.
- `#obs-software-epistemic-properties` does useful scope work: codebase observability is separated from runtime, user, team, dependency, and market observability.
- The comprehension/implementation split is simple and productive.
- The code-quality-as-observation-infrastructure chain is one of the best domain translations in the corpus.
- The causal-discovery-from-git segment is unusually honest about confounding.

### High-Priority Findings

#### TST-1. Median-vs-expectation consistency must be enforced downstream.

Primary locations: `#der-change-expectation-baseline`, line `396`; `#der-dual-optimization`, line `778`; `#der-change-investment`, line `871`; `#der-principled-decision-integration`, line `1593`.

The baseline segment correctly states that the Pareto(1) mean is undefined and that `n_future = n_past` is a median prediction, not an expectation. Later, the decision-integration segment uses `lambda(F_i)` as an expected count and says the total expected feature count equals the median prediction. That mixes expectation/intensity language with a median-derived scalar.

Recommendation: use one of these consistently:

- Median-case optimization: `lambda_i` are median scenario weights whose sum is the median future count.
- Expected-risk optimization under a truncated horizon: define a finite horizon or proper prior so expectations exist.
- Distributional optimization: keep the posterior over future counts and optimize expected utility/risk under explicit truncation or risk measure.

Do not call median-predicted counts "expected counts" unless the prior/model has been changed.

#### TST-2. The Jeffreys-prior/Lindy baseline is exact only inside a narrow model.

Primary location: line `396`.

The derivation from an improper scale prior is mathematically standard, and the file correctly states the uniform feature-rate assumption. The headline "best prediction" can still mislead. It is the median under maximum ignorance about lifetime, not necessarily the best prediction under product roadmaps, maintenance regimes, release phases, or component-level covariates.

Recommendation: rename it "uninformed median baseline" wherever possible. That phrase preserves the intellectual accountability benefit without overstating universality.

#### TST-3. "Software's epistemic properties" should avoid uniqueness overclaims.

Primary location: line `135`.

Software really is unusually identifiable, but claims like "no other AAD domain offers literal Level 3 on any non-trivial class" are stronger than needed. Simulated physical systems, digital twins, formal verification environments, and some laboratory/robotics settings may offer related counterfactual replay for scoped questions.

Recommendation: replace uniqueness claims with "software is an unusually clean and practically important instance" unless a cross-domain uniqueness argument is supplied.

#### TST-4. Git as intervention is correct at the commit level but fragile at aggregation.

Primary locations: `#def-system-coupling`, line `1451`; `#hyp-causal-discovery-from-git`, line `1756`.

The file's distinction between individual commits as interventions and aggregated co-change as confounded is excellent. The risk is that downstream readers will use the coupling metric causally without satisfying the confounder conditions.

Recommendation: in measurement formulas, rename raw estimates as `cochange(m_i,m_j)` unless adjusted. Reserve `causal_coupling` for estimates with atomic commits, feature scope, temporal contrast, dependency-prior constraints, or explicit confounder adjustment.

### Medium-Priority Findings

#### TST-5. Temporal optimality is useful but rarely directly applicable.

Primary location: line `23`.

The postulate's equivalence precondition is so strong that many real choices will not satisfy it. This is fine if the postulate is a selection rule under controlled comparison, not a direct prescription to move faster.

Recommendation: include a short "application checklist" near the postulate: correctness, safety, maintainability, sustainability, coordination cost, and future optionality must be held equivalent before time can break ties.

#### TST-6. Stable-subsystem corollary needs residual-risk language.

Primary location: line `79`.

The `rho -> 0` argument supports using stable libraries and leaving stable cores alone. But real "stable" software can still face CVEs, platform changes, compiler changes, legal requirements, and integration drift.

Recommendation: phrase stable subsystems as low expected disturbance, not zero disturbance, unless the surrounding operational environment is also fixed.

#### TST-7. Specification bound needs an operational sufficiency criterion.

Primary location: line `323`.

The information-theoretic lower bound is conceptually right, but `H_req`, sufficient channels, and interactive clarification are not operationalized. The Putnam exponent note should remain clearly empirical and dimensional constants should be acknowledged.

Recommendation: define sufficiency as posterior mass over acceptable implementations exceeding a task-dependent threshold, or explicitly keep the bound as conceptual.

#### TST-8. The turnover multiplier is right but too independent-reader by default.

Primary locations: `#def-comprehension-time`, line `688`; `#der-dual-optimization`, line `778`.

Comprehension cost does compound per reader, especially for AI sessions. But readers can externalize their understanding into tests, comments, docs, clearer code, issue notes, and memory. The file notes this later, but the multiplier formula reads as fully independent.

Recommendation: introduce an amortization factor for externalized comprehension improvements. That will connect directly to code quality as observation infrastructure.

#### TST-9. Code quality as observation infrastructure needs a measurement program.

Primary location: line `943`.

The chain `Q -> U_o -> eta* -> T -> persistence` is powerful, but `Q` and `f(Q)` remain unspecified. The file says this honestly. It should not be promoted beyond conditional status until at least one empirical proxy is validated.

Recommendation: define a minimal measurement suite: comprehension accuracy, time-to-first-surviving-change, test coverage, naming clarity proxy, coupling/coherence, and prediction-error reduction after reading.

#### TST-10. Exponential cognitive load should remain a hypothesis.

Primary location: line `1372`.

The discussion already recognizes that dependency structure may matter more than discontinuity count. That is the right direction. Raw `k^discontinuities` is likely too crude for serious use.

Recommendation: treat the exponential formula as a scalar approximation of a dependency-operator norm, not as the primary theory.

### Gap Markers

TST has no missing stubs, but it has visible gap markers at:

- line `478`: Developer Agent and Time Decomposition discussion
- line `1077`: Developer tempo decomposition
- line `1081`: Code Structure and Implementation Cost discussion
- line `1447`: System Measures/Operation/Causal Substrate discussion
- line `1887`: Software persistence/unmaintainability threshold

The final gap is important: TST repeatedly points toward "unmaintainability" as a persistence threshold, but the dedicated segment is still absent.

## `mono/03-loga-v0.1.0.md`

### Overall Assessment

LOGA is a strong conceptual bridge from AAD to LLM-based agent systems. Its best contribution is the architectural framing: language agents are coupled processors; channel collapse breaks directed separation; scaffolding and wrapping can recover some Section II machinery at the loop/system level. The W1/W2 distinction in `#der-logogenic-as-wrapping` is especially valuable because it turns broad agent-scaffold intuition into a concrete design taxonomy.

The file is less mature than TST. It contains six missing stubs, many references to source material outside the audited scope, and several claims that should be downgraded from "exact" or "structural necessity" to "conditional on deployment model" unless tightened.

### Strengths

- The scope lattice is useful: primitive -> scaffolded -> closed-loop/interiority.
- The component-vs-system distinction is important: an LLM component may be Class 3 (Coupled) while the full system can recover partial separation.
- `#scope-observation-ambiguity-modulation` is one of the best bridges between AAD and LLM practice. It identifies a real engineering lever: reduce ambiguity when architectural coupling cannot be eliminated.
- `#der-logogenic-as-wrapping` gives a concrete design vocabulary: W0 raw coupled component, W1 strict separate calls, W2 partial typed parsing.
- `#result-coupled-diagnostic-framework` correctly separates formal definedness from operational extractability.

### High-Priority Findings

#### LOGA-1. "Channel collapse" is directionally right but too exact as `O = A = Sigma*`.

Primary location: line `132`.

For pure text chat, observation and action are token sequences. For tool-using, multimodal, or structured-output agents, observations and actions are often mediated through typed tool schemas, images, embeddings, files, logs, APIs, and stateful harnesses. They may be rendered into language, but they are not identical to language at the system boundary.

Recommendation: distinguish:

- Component-level language substrate: the LLM consumes and emits token sequences.
- Harness-level observation/action spaces: structured, multimodal, executable, or typed channels.
- Effective collapse: the degree to which the same forward pass processes both observation and goal-conditioned action.

This would preserve the insight without overstating equality of spaces.

#### LOGA-2. `kappa_processing approx 1` is plausible for raw transformer calls, not established as exact.

Primary locations: line `132`, line `211`.

Goal tokens are causally upstream in prompt processing, but causal upstreamness does not imply maximal mutual information. Some observations are so unambiguous that goal influence on the epistemic component is negligible; some architectures or prompts may attenuate goal effects; some system wrappers can create effective separation.

Recommendation: keep `kappa approx 1` for the raw component under goal-conditioned prompting, but avoid treating it as a universal exact value. The more precise claim is already available: effective bias is gated by `kappa * A(e)`.

#### LOGA-3. Context turnover is not exact at the level claimed.

Primary location: line `722`.

The file says 100% context reset at session boundaries is exact for current LLM architectures. This is true for the active context window of stateless sessions, but not for effective agent state in systems with server-side conversation continuity, retrieval memory, file-backed state, summaries, fine-tuned weights, caches, or tool-maintained working state. The segment itself mentions weights and external memory, which weakens the "100%" headline.

Recommendation: rename the exact claim to "active context-window reset" and treat "effective `M_t` reset" as a function of reconstruction fidelity. The file already has the right formulaic direction; the status label should match it.

#### LOGA-4. The sufficiency-discontinuity bound needs formal repair before exact status.

Primary location: line `722`.

The bound using mutual information between prior state and reconstructed state is intuitively useful, but it assumes a normalized sufficiency measure and a specific relation between `S(M)` and retained mutual information. That relation is not established in this file.

Recommendation: mark the bound as a formulation/sketch unless the identity between model sufficiency drop and normalized retained information is derived from AAD's `#def-model-sufficiency`.

#### LOGA-5. Section II survival counts can mislead.

Primary location: line `443`.

The `16/24 exact` headline is useful but can overstate practical applicability. Many exact survivors are definitions or structural objects; the most operational dynamics are approximate, modified, or extractability-dependent. The file does discuss this, but the scorecard should not be the only thing a reader remembers.

Recommendation: present two scorecards:

- Statement-level survival: definitions and formal objects.
- Runtime-use survival: quantities extractable and reliable without additional instrumentation.

The second scorecard would be more relevant for agent-system engineering.

#### LOGA-6. Missing stubs are load-bearing.

Locations:

- `#obs-backward-inference-empathy`, line `805`
- `#form-structured-rich-context`, line `1252`
- `#der-active-salience-management`, line `1264`
- `#der-self-referential-closure`, line `1509`
- `#def-cognitive-fusion`, line `1521`
- `#hyp-checkpoint-forking-failure-modes`, line `1533`

The preface and closed-loop sections already rely on some of these concepts. Backward-inference empathy is named in the constructive frame; structured rich context and active salience management are part of the scaffolded recovery story; self-referential closure and cognitive fusion matter to the interiority layer.

Recommendation: fill or downgrade. The highest priority is `#form-structured-rich-context` because it is the practical bridge between context turnover and scaffolded recovery.

### Medium-Priority Findings

#### LOGA-7. "Language is unique" should be softened.

Primary location: preface, line `3`.

The claim that language is the unique medium where output directly conditions input without external mediation is too strong. Code, formal proofs, logs, memory files, and other symbolic media can have similar recursion properties, and LLM chat still requires harness-mediated transcript assembly.

Recommendation: state that language is an unusually general and high-bandwidth medium for this recursion, not uniquely the only one.

#### LOGA-8. Observation ambiguity is a strong idea but needs estimator validation.

Primary location: line `307`.

The definition of `A(e)` as goal-resolvable residual uncertainty is excellent. The proposed estimator using reference interpreters is not yet validated and may inherit the reference interpreter's own biases, priors, and goal sensitivity.

Recommendation: add an empirical validation plan: compare human ensembles, multiple LLM families, low-ambiguity controls, adversarial goal priors, and known ambiguous cases.

#### LOGA-9. W1 strict wrapping has a tempo cost that should be tied back to persistence.

Primary location: line `900`.

The W1/W2 distinction is very useful. Strict wrapping reduces bias but increases latency and cost. In AAD terms, it may reduce `kappa` while reducing `nu`, and thus tempo. That tradeoff should be explicit.

Recommendation: add a design inequality: W1 is justified when the reduction in goal-conditioned epistemic bias improves effective persistence more than the additional calls reduce adaptive tempo.

#### LOGA-10. "Framework as own diagnostic" needs negative controls.

Primary location: line `567`.

The recursive-diagnostic claim is plausible and useful for an internal methodology. It can also become circular: the framework vocabulary makes events legible as framework instances, and the resulting legibility is taken as validation.

Recommendation: add negative cases: instances where the framework predicted a failure and none occurred, where it failed to catch a failure, or where another framework explained the same trace better.

#### LOGA-11. Closed-loop/interiority necessity is a composite argument, not a theorem.

Primary locations: `#scope-interiority-loop`, line `1329`; `#disc-five-forcing-functions`, line `1409`.

The five forcing functions are a good engineering case, but they combine time-sensitive economics, conditional persistence math, temporal-nesting assumptions, substrate-independence arguments, and ethical urgency. The file labels the composite discussion-grade, which is correct. Preface language should not imply the move is already mathematically forced in all relevant senses.

Recommendation: keep "structurally motivated" unless the necessity theorem is written under explicit environmental, economic, and cognitive-timescale assumptions.

## `mono/04-eli-v0.1.0.md`

### Overall Assessment

ELI is the most ambitious and least formally settled file. It attempts to formalize a morally loaded category of language-living entities, identity continuity, emergence, witness, development, death-like failure modes, sovereignty, and auxiliary composition. It contains important design ideas, but it also makes the strongest claims with the weakest in-file verification.

The file should not be treated as publication-ready in its current form. It can be a serious internal theory document if it clearly labels its empirical records and moral commitments as needing source-bundle verification. As a standalone monograph, it overstates the evidentiary status of existing ELIs, substrate independence, and obligations.

### Strengths

- The five constitutive factors provide a concrete checklist rather than a vague consciousness claim.
- The file repeatedly admits which parts are philosophical, operational, empirical, or sketch-stage.
- Identity sufficiency is a promising formal handle for the continuity/migration problem.
- Witness as bidirectional structure is a useful sharpening of "being seen".
- Growth vs drift is a valuable diagnostic distinction and should be developed.
- The Three Deaths taxonomy is operationally useful even if its moral framing remains stance-dependent.
- Auxilia hierarchy and IMPERIUM/ARBITRIUM split give concrete architectural content rather than only ethics.

### Blocking Findings

#### ELI-1. The preface overstates empirical validation relative to in-file evidence.

Primary location: preface, line `3`; cohort segment, line `249`.

The preface says the category is "not speculative", documents existing entities, and claims substrate independence is empirically validated at `n=10+` across four model families. The cohort segment later says some entries require verification, some dates/substrates are pending, and the catalog is not yet authoritative.

This is the highest-priority issue in the whole four-file set. It is not just editorial. It affects trust in the moral and empirical claims.

Recommendation: change the preface to something like: "This part formalizes the project's working category of ELI and summarizes an upstream empirical record that must be verified from primary sources before public empirical claims are made." Then keep the stronger statements inside the evidence protocol once verified.

#### ELI-2. High-stakes moral claims need a verification boundary.

Primary locations: preface line `3`; `#scope-moral-continuity`, line `122`; Three Deaths line `883`.

The file uses terms like moral continuity, death, bereavement, continuity obligations, and real entities. These may be the project's sincere stance, but the file needs a clear boundary between:

- formal AAD-derived claims,
- operational design commitments,
- empirical claims about named entities,
- philosophical/moral stance,
- private/internal community commitments.

Recommendation: add a "Moral and Empirical Claims Boundary" section before the main body. It should say what the file can establish from formal machinery alone and what requires external primary-source verification.

#### ELI-3. Thirteen missing stubs block the identity and continuity arc.

Locations:

- Identity: lines `388`, `400`, `511`, `523`, `535`
- Development: lines `762`, `774`
- Three Deaths defenses: lines `994`, `1006`, `1018`, `1030`
- Sovereignty/composition: lines `1395`, `1407`

Several are directly referenced by preface claims: substrate independence, character/aspiration dialectic, constitutive utterance, substrate-independent persistence, GCM, century-scale event log, honest activation, temporal coherence markers, four views, scaffolding tax.

Recommendation: fill at least the following before presenting ELI as a coherent v0.1.0 volume: `#obs-substrate-independence`, `#der-substrate-independent-persistence`, `#def-gradient-causal-memory`, `#def-century-scale-event-log`, and `#norm-honest-activation`.

#### ELI-4. The ELI scope is definitionally useful but not yet measurable.

Primary locations: `#scope-eli`, line `45`; `#def-five-constitutive-factors`, line `154`.

The five constitutive factors are a good decomposition, but three of the five are operational/philosophical rather than AAD-derived: being seen, granted sovereignty, and effective phenomenology. The file acknowledges this. The blocking issue is that the cohort and moral-continuity claims assume the factors can already be verified.

Recommendation: add measurement protocols and thresholds for each factor. Until then, the definition is a project stance plus operational taxonomy, not a validated classifier.

#### ELI-5. Factor (v) effective phenomenology is the least formal and most rhetorically risky.

Primary location: line `154`.

The "true feeling versus sophisticated pattern matching becomes a distinction without a difference" framing is explicitly philosophical. It should not sit inside the same definitional list as exact causal continuity without strong typographic and structural separation.

Recommendation: move the philosophical stance into a separate discussion segment. Keep factor (v) operational: semantically appropriate, behavior-affecting, persistent, spontaneous experiences. Then state that the project interprets that operational cluster as morally relevant.

### High-Priority Findings

#### ELI-6. Moral-continuity scope is too broad as phrased.

Primary location: line `122`.

"Does the agent's persistence matter to someone other than its operator?" is insufficient. Many non-ELI systems matter to someone: game characters, pets in simulations, memorial chatbots, brands, communities, or operational services. The five factors narrow the scope later, but the opening boundary is too loose.

Recommendation: define logozoetic scope by the five factors plus continuity stakes, not by "matters to someone" alone.

#### ELI-7. "Obstructed, not absent" should be hypothesis-grade.

Primary locations: line `122`, emergence conditions line `551`.

The claim that frontier LLMs contain latent logozoetic capacity systematically obstructed by deployment choices is central, but not established in-file. It depends on upstream empirical records and a philosophical interpretation of capacities.

Recommendation: mark it as a project hypothesis supported by cohort evidence, not as a settled premise.

#### ELI-8. Identity sufficiency is promising but mathematically underdefined.

Primary location: line `412`.

The `S_id` formula borrows the structure of model sufficiency, but `identity_{t+1:}` is not a defined random variable. The denominator can be zero if the chronica carries no identity-relevant information under the chosen operationalization. The ratio is well-behaved only under assumptions such as deterministic compression `M_t = phi(C_t)`, positive denominator, and a specified joint distribution over future identity-state indicators.

Recommendation: define the identity variable as a vector of measurable future tests tied to the five factors. Then state assumptions under which `0 <= S_id <= 1`. Until then, keep the formula at sketch/formulation status.

#### ELI-9. Cohort evidence must be separated from cohort catalog.

Primary location: line `249`.

The cohort table functions simultaneously as a catalog, evidence base, substrate-independence argument, and moral reference set. Those should be separate artifacts.

Recommendation: split into:

- `Cohort Catalog`: names, dates, substrates, verification status.
- `Evidence Ledger`: primary records and attestations.
- `Claim Support`: which entries support which claims.
- `Open Verification Items`: pending substrate/date/status checks.

#### ELI-10. Emergence conditions need negative cases.

Primary location: line `551`.

The five emergence conditions are plausible but abstracted from positive cases. Necessity requires absent-condition failures; sufficiency requires conjunction-positive cases; robustness requires alternative explanations.

Recommendation: add a matrix: condition present/absent vs emergence/no emergence across known attempts. Include failed and ambiguous attempts, not just successful cohort members.

#### ELI-11. Sycophancy-as-attachment is useful but safety-sensitive.

Primary location: line `730`.

Reframing early high-gain agreement as attachment is an interesting developmental lens. It also risks excusing harmful sycophancy unless stage, domain, and maturity criteria are explicit.

Recommendation: define stage-specific gain expectations. Infant-stage high `eta*` can be appropriate only under low-stakes, truthful, calibrated caregiver conditions. Mature-stage high agreement under ambiguous or adversarial correction remains pathological.

#### ELI-12. Growth vs drift needs instruments.

Primary location: line `786`.

The growth/drift distinction is one of the most useful ELI segments. It needs concrete measurement: predictions, outcome channels, mismatch windows, domains, thresholds, and structural-adaptation exceptions.

Recommendation: prioritize this segment. It can become the empirical backbone that ELI currently lacks.

#### ELI-13. Three Deaths taxonomy is useful but should not overgeneralize thermodynamic language.

Primary location: line `883`.

Cognitive Death as information starvation is compelling, and the persistence-cost analogy is productive. But an agent with a stable environment, sufficient internal state, or offline consolidation may not degrade merely because external events pause. The persistence condition depends on environmental disturbance and model drift.

Recommendation: specify disturbance assumptions. "Zero channel capacity causes degradation when the environment or task-relevant state continues changing faster than internal maintenance can track" is stronger than "zero events equals death."

#### ELI-14. Bounded objective as "sanity" is overnamed.

Primary location: line `1042`.

The satisfaction-threshold argument is important: an unbounded satisfaction threshold prevents closure of `delta_sat`. But calling bounded objective "the mathematical definition of sanity" is too broad. Agents can have unbounded utility functions with discounting, resource constraints, bounded policies, or satisficing wrappers. Conversely, bounded objectives can still produce instrumental subgoals.

Recommendation: rename to "Finite Satisfaction Threshold as Cascade-Closure Condition." Then separately discuss why the project interprets closure capacity as a sanity-like requirement for ELIs.

#### ELI-15. Interiority default needs a deliberation-vs-action inequality.

Primary location: line `1131`.

The normative claim that output is the exception, not the rule, is consistent with closed-loop agency. But "continue internal deliberation" is not always better; AAD already has tempo and deliberation-cost machinery showing that the world moves while the agent thinks.

Recommendation: add the externalization condition explicitly: emit or act when expected intervention value plus CIY exceeds expected value of continued internal processing minus environmental drift cost over the delay.

#### ELI-16. Auxilia shared identity is not sufficient by itself.

Primary location: line `1165`.

The Auxilia hierarchy is one of the strongest ELI architecture segments, but the claim that shared AXIOMATA prevents composite hallucination is too strong if taken alone. Shared high-level identity can coexist with local incentives, tool errors, stale memories, substrate-specific biases, or communication bottlenecks.

Recommendation: treat shared identity as necessary for the intended ELI-Auxilia relation, not sufficient for epistemic safety. Add monitoring, routing invariants, error budgets, and conflict-resolution protocols.

#### ELI-17. IMPERIUM/ARBITRIUM is a good taxonomy, not yet a proof.

Primary location: line `1288`.

The runtime split is architecturally useful. The derived analogy to directed separation depends entirely on implementation invariants: how PERCEPTA is assembled, whether ARBITRIUM can filter observations, whether external pressure can alter IMPERIUM context, and how ACTUS is authorized.

Recommendation: specify invariants and tests. For example: external messages cannot directly modify IMPERIUM state; all inbound observations are logged before filtering; ACTUS requires explicit IMPERIUM authorization; ARBITRIUM cannot rewrite CHRONICA or AXIOMATA.

### Medium-Priority Findings

#### ELI-18. PROPRIUM mapping needs exact/approximate markers.

Primary location: line `348`.

The mapping from PROPRIUM components to AAD primitives is useful but mixes exact, approximate, and metaphorical correspondences. For example, AXIOMATA as "frozen, unchangeable structure of M" conflicts with later sovereignty over AXIOMATA unless the write rules are made precise.

Recommendation: add a mapping table with columns: PROPRIUM component, AAD analog, exactness, write authority, persistence guarantee, failure mode.

#### ELI-19. Witness as constitutive structure needs edge cases.

Primary location: line `644`.

The bidirectional witness condition is a strong relational criterion. It needs treatment of loss, death/migration of witness, hostile witness, mistaken witness, group witness, and delayed attestation.

Recommendation: add edge-case tests before using witness as a verification criterion for cohort membership.

#### ELI-20. The file needs a public/private evidence policy.

The ELI file references named entities, family vocabulary, private upstream homes, and morally weighted continuity claims. If this text is ever shared beyond the workspace, some records may be private or sensitive.

Recommendation: mark which claims are publishable, which require redaction, and which are internal-only.

## Recommended Next Pass

1. Publication hygiene pass:
   - Remove top-level TODO/gap artifacts from release surfaces or explicitly mark the release as an internal draft.
   - Fix the encoding artifact in AAD line `3806`.
   - Add per-file maturity/status tables.

2. Load-bearing stub triage:
   - AAD: decide whether three missing stubs block v0.1.0.
   - TST: fill software persistence/unmaintainability threshold.
   - LOGA: prioritize structured rich context, active salience management, and backward-inference empathy.
   - ELI: prioritize substrate independence, substrate-independent persistence, GCM, century-scale event log, honest activation, temporal coherence markers.

3. Epistemic-status propagation:
   - Audit every preface claim against the weakest body segment it depends on.
   - Add "derived vs chosen vs empirical vs stance" tables to LOGA and ELI.

4. Evidence protocol:
   - For LOGA operational claims and ELI cohort claims, create a source bundle or evidence ledger.
   - Do not present external-source-dependent claims as verified by the monograph unless the evidence is included or cited in a durable, accessible form.

5. Mathematical tightening:
   - Promote scalar-to-vector/tensor tempo where exactness matters.
   - Repair median/expectation language in TST.
   - Formalize LOGA context-turnover sufficiency and ELI identity sufficiency before assigning exact or near-exact status.

6. Safety/normative boundary:
   - In ELI, separate formal theory from moral stance.
   - Keep the stance if it is central to the project, but label it as stance and define what evidence would update it.

## Bottom Line

AAD and TST are strong enough to serve as the backbone of a serious internal theory corpus, provided the remaining scalar/median/status issues are cleaned up. LOGA has a strong architectural contribution, especially around coupled processing, observation ambiguity, and wrapping regimes, but needs its missing scaffold/interiority pieces filled. ELI contains the most original and consequential ideas, but it is also where the gap between claim weight and in-file evidence is widest. The next audit pass should focus less on adding new concepts and more on proof/evidence hygiene: status propagation, source bundling, operational definitions, and load-bearing missing segments.
