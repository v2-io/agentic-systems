# Forensic-Mining Pass — Tornhill Corpus (Software Design X-Rays + Your Code as a Crime Scene)

Mining target: the 107 SDX + 80 CCS analyses under `~/src/_core/tst/planning/analysis/`. These are the most empirically grounded slice of the old corpus — both books work the version-control-mining vein where AAT's $\#$hyp-causal-discovery-from-git's research program lives. The two books overlap heavily and most analyses recapitulate a small kernel of techniques (hotspots, temporal coupling, code age, knowledge maps, fractal value); the substantive content can be compressed substantially.

Findings are ranked roughly by TST-yield value. Class labels follow `00-context.md`: A = Joseph's named gaps; B = AAT-homed but freshly instantiated; C = new TST segment candidates; D = empirical anchors for existing claims.

---

### F1. Three confounder classes match $\#$hyp-causal-discovery-from-git exactly — and the bias paper adds Goodhart as a fourth

**Source analyses:** [681-behavioral-code-analysis-bias-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/681-behavioral-code-analysis-bias-detection---identifying-and-correcting-systematic-biases-in-forensic-analysis.md), [684-adaptive-behavior-in-metric-systems](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/684-adaptive-behavior-in-metric-systems---how-measurement-systems-change-developer-behavior-and-destroy-data-validity.md), [328-cognitive-bias-in-code-review](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/328-cognitive-bias-in-code-review---identifying-and-mitigating-biases-that-affect-code-review-effectiveness.md)

**Class:** A (composes directly with M1 identifiability-floor)

**AAT-relevance:** $\#$hyp-causal-discovery-from-git C1/C2/C3; $\#$disc-identifiability-floor (M1); $\#$obs-software-epistemic-properties (P5 chronicle).

**The content (briefly).** Tornhill names four bias families that map onto and extend the three confounder classes in $\#$hyp-causal-discovery-from-git: (i) **authorship bias** — squashed commits, CI/bot authorship, merge-only contributors corrupt $K(d, c)$ and concentration-factor estimates (cleanly maps to C3 developer-knowledge-state — the recorded author $\neq$ the actual author whose $M_t$ shaped the commit); (ii) **squash bias** — bundling collapses $1/n$ information (this is the *literal* C2 convention-bundling confounder, with a quantitative information-loss bound); (iii) **history-migration gaps** — repo splits/moves break the chronicle's hash-chain identifiability (a P5 violation, not a C-class confounder per se); (iv) **Goodhart adaptation** — measurement *changes* the substrate, so the chronicle observed under the regime where the metric is used differs systematically from the chronicle under the unobserved regime (this is a new confounder class, distinct from C1/C2/C3, that the segment does not currently name). The 684-analysis specifically frames divergence between measured and real value as $D_\mathrm{KL}(v_m \Vert v_r)$ growing under adaptation pressure — a clean information-theoretic statement of the loss of causal validity.

**Translation into AAT/TST.** Update $\#$hyp-causal-discovery-from-git's confounder list to include **C4 — observer-effect / Goodhart**, with one-paragraph treatment. The strongest framing: when git history is used for performance evaluation, the chronicle ceases to be a clean record of developer interventions and becomes a record of joint developer-and-metric-system behavior. Causal identifiability collapses by *exactly* the M1 identifiability-floor mechanism — the metric and the underlying productivity become unidentifiable from observation alone (they trade off along a degenerate direction in parameter space). This is a fresh worked instance of M1 with an immediate concrete domain anchor and provides a non-toy "you cannot get there from here without further interventions" example for the segment. Body update: small. Discussion section gets a paragraph naming C4 and its relationship to M1.

**Honesty.** The four bias families are framed informally and overlap (squash-with-misattribution = squash bias × authorship bias). The exponential-decay accuracy model $A(B) = A_0 e^{-\lambda \lvert B \rvert}$ is unsupported. The Goodhart result is qualitative and well-supported in the broader literature (cited extensively outside this corpus) but the $D_\mathrm{KL}$ formalization is gesture not derivation. The structural content — that C4 exists and is distinct from C1/C2/C3 — is solid; the math is decorative.

---

### F2. Tests as reusable Level-2 probes — Tornhill's data on test-file co-change validates the claim and refines it

**Source analyses:** [320-test-suite-evolution-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/320-test-suite-evolution-analysis---temporal-coupling-in-test-architecture.md), [321-test-automation-quality-assessment](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/321-test-automation-quality-assessment---using-temporal-coupling-to-analyze-test-suite-quality.md), [639-test-code-coupling-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/639-test-code-coupling-analysis---specialized-temporal-coupling-analysis-for-test-suites.md), [635-untouchable-code-management](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/635-untouchable-code-management---strategies-for-managing-critical-code-that-cannot-be-refactored.md), [247-test-code-quality-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/247-test-code-quality-analysis---forensic-analysis-for-test-code-characteristics.md)

**Class:** B (strengthens $\#$hyp-causal-discovery-from-git's tests-as-probes framing with empirical instantiation)

**AAT-relevance:** $\#$hyp-causal-discovery-from-git §"Tests as reusable Level 2 probes"; $\#$der-code-quality-as-observation-infrastructure (the $Q \to U_o \to \eta^\ast \to \mathcal T$ chain instantiated for the test channel).

**The content (briefly).** The Tornhill corpus repeatedly observes that test files appear at the top of hotspot lists (Docker, Rails, ASP.NET Core), changing as frequently or more than production code. The interpretation Tornhill offers — "test code is at least as important as application code" — is operationally correct but theory-thin. The deeper observation is: **a test, once written, is a probe with $\nu_\mathrm{test}$ (run frequency, typically every CI pass) and characterized $U_{o,\mathrm{test}}$ (false-positive rate, flakiness)**, and its co-change with production code measures how much $U_{o,\mathrm{test}}$ degrades when the system being probed changes underneath it. The 320/321 analyses explicitly track test-suite temporal coupling and find that brittle/coupled tests amplify $U_{o,\mathrm{test}}$ multiplicatively (mock-heavy tests grow $C_\mathrm{mock} \cdot \beta$ exponentially in dependency-count). Test code at the top of hotspot lists is precisely the symptom of test-probe degradation under production-domain drift.

**Translation into AAT/TST.** This is direct empirical support for $\#$hyp-causal-discovery-from-git's "tests as reusable interventional probes" framing, and gives the segment a concrete instantiation of the $(\nu, U_o)$ characterization: a test's $\nu$ is the CI invocation rate, its $U_o$ is observable as flakiness + co-change-amplification rate. Adds operational signature for the segment's Discussion. Stronger version for a future segment: the $Q \to U_o$ piece of $\#$der-code-quality-as-observation-infrastructure should distinguish $U_{o,\mathrm{code}}$ (comprehension noise) from $U_{o,\mathrm{test}}$ (probe noise) — they are different channels with different decay dynamics. Tests are a wrapping (in the W₂ sense) of the production system into a structurally-queryable probe; "test-suite as wrapping" is a forward connection to $\#$der-class-coercion-via-wrapping that deserves at least a Working-Notes cross-reference.

**Honesty.** Tornhill never frames tests as Pearl interventions; he treats them as just-another-file-type with high change frequency. The instantiation is ours, not his — the corpus provides evidence consistent with the framing rather than support for it. The mock-complexity exponential $t \propto e^{\beta C_\mathrm{mock}}$ is unsupported empirically.

---

### F3. Goodhart's law converts the chronicle from interventional to associational — observer-effect as an architecture-level adversarial-coupling instance

**Source analyses:** [684-adaptive-behavior-in-metric-systems](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/684-adaptive-behavior-in-metric-systems---how-measurement-systems-change-developer-behavior-and-destroy-data-validity.md), [686-metric-gaming-prevention-strategies](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/686-metric-gaming-prevention-strategies---methods-to-prevent-and-detect-manipulation-of-development-metrics.md)

**Class:** C (candidate new TST segment with M4 modularity-state-dynamics connection)

**AAT-relevance:** M4 modularity-state-dynamics (adversarial coupling pressure); $\#$hyp-causal-discovery-from-git (C4 confounder); signed-coupling (this is structural-shock regime applied to the measurement channel).

**The content (briefly).** When developer-productivity metrics derived from the chronicle are used for performance evaluation, developers adapt their behavior to optimize the *measured* quantity, opening a wedge between $v_m$ (measured productivity) and $v_r$ (real productivity). The 684-analysis tracks divergence-growth qualitatively and identifies several mechanisms: synthetic commit-splitting (gaming commit-count), whitespace-only churn (gaming LOC), excessive shallow PRs (gaming PR-count), and — most insidiously — knowledge silo formation when individual metrics make collaboration costly. The last mechanism is the deepest: individual-attribution creates adversarial coupling between developers who should be cooperating, which is a *system-level* defect that degrades $\mathcal T_\mathrm{team}$ even though no single developer is "doing anything wrong."

**Translation into AAT/TST.** This is M4 modularity-state-dynamics with a sharp software-domain instantiation: the chronicle (an observation infrastructure with property P5) is *itself* a substrate that adversarial coupling pressure can act on. The map: (truthification operation, self-driven-increasing) is git hygiene + atomic commit discipline + descriptive commit messages — all things teams do unprompted to make their *own* chronicle more useful to themselves. (Adversarial coupling pressure, externally-driven-decreasing) is exactly metric-driven Goodhart adaptation. (Strategic self-coupling, self-driven-decreasing) is the deliberate silo behavior teams adopt when individual metrics are in play. This gives M4 a worked software-domain instance that the modularity-cycle-plan can use, and a candidate for a sub-segment under M4 once M4 lands: "chronicle integrity under observation regimes." It is also a candidate diagnostic for whether a project's chronicle data can be used for causal discovery at all: any project where the chronicle has been performance-evaluated is causally compromised in a way no confounding adjustment can fix without further interventions.

**Honesty.** The structural argument is solid and survives translation cleanly. Tornhill cites no original data — his evidence is appeal to Goodhart broadly and a handful of consultancy anecdotes. The specific constants ($\gamma \approx 0.3$, $\kappa \approx 0.4$, etc.) are decorative. The strong claim — that *any* performance-evaluated chronicle is causally compromised — needs careful scoping (some metrics gameable, others not; the LOC-style ones are the worst).

---

### F4. The hotspot $H = f \cdot c$ formula is principled-decision-integration with $\lambda(F_i)$ concentrated on observed-hot files

**Source analyses:** [097-hotspot-analysis-pattern](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/097-hotspot-analysis-pattern.md), [291-hotspot-analysis-theory](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/291-hotspot-analysis-theory---prioritizing-refactoring-through-change-complexity-intersection.md), [294-complexity-effort-intersection-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/294-complexity-effort-intersection-analysis---finding-code-hotspots.md), [298-hotspot-detection-through-complexity-change-intersection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/298-hotspot-detection-through-complexity-change-intersection.md), [299-hotspot-prioritization-methodology](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/299-hotspot-prioritization-methodology.md), [348-forensic-code-analysis-framework](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/348-forensic-code-analysis-framework---complete-methodology-for-analyzing-codebases-like-crime-scenes.md)

**Class:** B (strengthens $\#$der-principled-decision-integration with an empirical estimator)

**AAT-relevance:** $\#$der-principled-decision-integration; $\#$emp-changeset-size-principle; FP-003 baseline change expectation (now $\#$der-change-expectation-baseline).

**The content (briefly).** The hotspot score $H(m) = f_m \cdot c_m$ (change frequency × complexity, possibly raised to a power) is presented across $\sim$20 of the analyses as Tornhill's central operational technique. The 298/299/348 analyses note empirically that change frequency follows a power law (top 20% of files take 80% of commits — Pareto), so concentrating refactoring on the high-$H$ tail is high-leverage. The complete formula across multiple analyses is $H_\mathrm{complete}(m) = f(m) \cdot c(m)^\beta \cdot \mathrm{proximity\_penalty}(m) \cdot (1 + \alpha \log c(m))$ with empirical $\alpha \approx 0.3$, $\beta \approx 0.7$. Several analyses add an exponential decay over time so recent commits weight more.

**Translation into AAT/TST.** This is a near-exact empirical instantiation of $\#$der-principled-decision-integration where $\lambda(F_i)$ (the feature-intensity profile, the priors over which features are likely next) is estimated *from the chronicle itself* using past frequencies, with the additional weighting that the cost-per-feature scales as complexity${}^\beta$. Hotspot analysis is principled-decision-integration restricted to the case where $\lambda$ is estimated from past frequencies (the FP-003 / Lindy / Baseline-Change-Expectation prior) rather than declared. The segment's Discussion should acknowledge this connection: "the hotspot $H = f \cdot c$ pattern in the empirical software-engineering literature is principled-decision-integration with $\lambda(F_i)$ estimated from the chronicle's empirical change-frequency distribution; this connects $\#$der-principled-decision-integration to the existing industry practice and provides a concrete computable form." The power-law assumption $P(f \geq x) \propto x^{-\alpha}$ across files is a useful empirical anchor for the assertion that $\lambda(F_i)$ is in practice highly non-uniform — a small number of features dominate.

**Honesty.** The specific exponents ($\alpha \approx 0.3$, $\beta \approx 0.7$) vary across analyses with no shared empirical source. The "compound interest" framing — $(1 + r)^f$ — is unsupported (it's a metaphor, not a derivation; complexity does not literally compound in this functional form). The structural connection — hotspot-as-PDI-with-empirical-prior — is the real content.

---

### F5. Frequency-asymmetry survives common-cause confounding — empirical operationalization of the residual-causal-signal claim

**Source analyses:** [234-temporal-coupling-x-ray-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/234-temporal-coupling-x-ray-analysis---method-level-change-pattern-detection.md), [239-change-coupling-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/239-change-coupling-detection---predicting-future-development-time-explosions.md), [311-temporal-coupling-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/311-temporal-coupling-detection---mining-change-history-for-hidden-dependencies.md), [313-code-interview-techniques](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/313-code-interview-techniques---extracting-temporal-coupling-from-version-history.md), [314-temporal-coupling-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/314-temporal-coupling-detection---mining-version-control-for-hidden-dependencies.md), [316-temporal-coupling-analysis-methods](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/316-temporal-coupling-analysis-methods.md), [318-system-level-temporal-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/318-system-level-temporal-analysis---scaling-coupling-detection-to-architectures.md)

**Class:** B (empirical instantiation of $\#$hyp-causal-discovery-from-git point 3)

**AAT-relevance:** $\#$hyp-causal-discovery-from-git "What remains after accounting for confounding" point 3 (frequency-asymmetry as residual causal signal); $\#$meas-coherence-coupling.

**The content (briefly).** The standard temporal-coupling estimator across the Tornhill corpus has two forms, both *symmetric* by construction: Jaccard $\rho(C_1, C_2) = \lvert\mathrm{commits}(C_1) \cap \mathrm{commits}(C_2)\rvert / \lvert\mathrm{commits}(C_1) \cup \mathrm{commits}(C_2)\rvert$, and conditional $P(\mathrm{change}(C_2) \mid \mathrm{change}(C_1)) = \lvert\mathrm{commits}(C_1 \cap C_2)\rvert / \lvert\mathrm{commits}(C_1)\rvert$. The conditional form is *asymmetric* and several analyses note this asymmetry empirically reveals dependency direction: "module A frequently triggers changes to B but not vice versa" indicates a directed link $A \to B$ that survives common-cause confounding. The 311/314 analyses also note that *lagged* co-change (B changed within $\tau$ days *after* A) is even stronger evidence of $A \to B$ directionality.

**Translation into AAT/TST.** This is the empirical operationalization of $\#$hyp-causal-discovery-from-git point 3 (frequency asymmetry survives common-cause confounding because common causes produce symmetric co-change). The lagged variant — $P(\mathrm{change}(B) \mid \mathrm{change}(A), \Delta t \gt 0)$ — is a strictly stronger signal that the corpus repeatedly proposes operationally. The $\#$meas-coherence-coupling segment currently defines a symmetric estimator; it should also surface the asymmetric form and the lagged form, with the residual-causal-signal interpretation pointing at $\#$hyp-causal-discovery-from-git. Concrete proposal: add a Discussion paragraph to $\#$meas-coherence-coupling distinguishing the *symmetric* co-change estimator (descriptive) from the *asymmetric directed* estimator (interventional in favorable regimes) and the *temporally-lagged* estimator (Granger-like, stronger interventional signal under additional regularity).

**Honesty.** Granger causality has well-known limitations (it cannot distinguish $A \to B$ from $\text{hidden}\, C \to A$ then $C \to B$ with different lags). The lagged-cochange estimator inherits these. The strongest honest claim is: among the family of co-change estimators, the asymmetric directed and the temporally-lagged forms are strictly *less* confounded than the symmetric Jaccard form, not that they are unconfounded.

---

### F6. Surprise = $\rho \cdot d_\mathrm{concept}$ and surprise = $\rho \log \rho$ — two distinct operationalizations of the "expected vs declared coupling" divergence

**Source analyses:** [098-change-coupling-pattern](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/098-change-coupling-pattern.md), [636-change-pattern-surprise-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/636-change-pattern-surprise-detection---algorithms-for-identifying-unexpected-coupling-relationships.md), [302-true-problems-vs-false-positives-differentiation](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/302-true-problems-vs-false-positives-differentiation.md), [697-internal-coupling-omission-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/697-internal-coupling-omission-detection---finding-missing-relationships-in-change-coupling-analysis.md)

**Class:** C (candidate refinement to $\#$meas-coherence-coupling Discussion)

**AAT-relevance:** $\#$hyp-causal-discovery-from-git ("undeclared coupling" Discussion point); $\#$meas-coherence-coupling.

**The content (briefly).** The Tornhill literature offers two distinct operationalizations of architectural "surprise" — the divergence between declared structure and observed co-change: (i) the **product form** $S(C_1, C_2) = \rho(C_1, C_2) \cdot d_\mathrm{concept}(C_1, C_2)$ where $d_\mathrm{concept}$ is the *declared* conceptual distance (namespace distance, semantic distance, ownership distance) and $\rho$ is empirical co-change — high $S$ means strongly coupled but far apart conceptually; (ii) the **KL form** $S(i, j) = \rho_{ij} \log(\rho_{ij} / \rho_\mathrm{baseline})$ — divergence from the null model of independence. The two measure different things: (i) is divergence-from-declared-structure (architectural drift), (ii) is divergence-from-independence (mere statistical coupling). The 302-analysis explicitly notes both forms have failure modes: (i) gets false positives on legitimate cross-cutting concerns (logging, security) and false negatives on legitimately-distant code that is properly architected; (ii) gives no information about whether the coupling is structural (real dependency) or coincidental.

**Translation into AAT/TST.** Surprise-from-structure is the *operational* test that $\#$hyp-causal-discovery-from-git's "undeclared coupling" Discussion claim is meaningful. The product form $\rho \cdot d_\mathrm{concept}$ is the right form for the segment: it directly measures the wedge between the declared causal-edge graph (from imports / ownership / namespaces — Property P4) and the empirical co-change graph (from the chronicle — P5). A genuine architectural finding is one where the wedge is large *and* the asymmetry/lag tests (F5) suggest a real directed link. Useful but second-tier: would strengthen $\#$meas-coherence-coupling with a one-paragraph Discussion of the two surprise estimators and their respective false-positive/false-negative profiles.

**Honesty.** The concept-distance measurement is the load-bearing weak point — "namespace distance" and "semantic distance" are language-dependent heuristics with poor inter-rater reliability. Without a principled $d_\mathrm{concept}$, both surprise estimators degrade. The corpus does not solve this; it just notes the problem. This is structural-finding-quality, not measurement-quality.

---

### F7. Author-count predicts defects better than complexity ($r \approx 0.7$ vs $r \approx 0.2$) — empirical anchor for Conway's-Law as predicting $\rho$

**Source analyses:** [100-conways-law-team-alignment](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/100-conways-law-team-alignment.md), [236-organizational-debt-as-primary-quality-predictor](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/236-organizational-debt-as-primary-quality-predictor.md), [241-fractal-value-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/241-fractal-value-analysis---quantifying-coordination-overhead.md), [251-team-coordination-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/251-team-coordination-analysis---conways-law-through-code-patterns.md), [329-conways-law-validation](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/329-conways-law-validation---organizational-structure-mirroring-in-code.md), [626-quality-predictors-based-on-organizational-structure](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/626-quality-predictors-based-on-organizational-structure.md)

**Class:** D (empirical anchor for $\#$meas-coherence-coupling Discussion of Conway's-Law as $\rho$ predictor)

**AAT-relevance:** $\#$meas-coherence-coupling Discussion (organizational dimension of coupling); $\#$der-code-quality-as-observation-infrastructure (organizational $U_o$ at the team level).

**The content (briefly).** Tornhill cites Microsoft Research's finding that organizational metrics (number of developers, ex-developers, change frequency, ownership concentration) predict defects with correlation $r \approx 0.7$-$0.8$, while traditional code-quality metrics (test coverage, cyclomatic complexity, comment ratio) predict at $r \approx 0.2$-$0.3$. This is the empirical anchor for $\#$meas-coherence-coupling's "Organizational reflection (Conway's Law)" Discussion paragraph and is *much* stronger than the segment currently surfaces. The Linux-kernel observation in 626/241 is particularly notable: the Intel graphics driver had 55 authors in 3 months with 17 working on the main hotspot file — and is also the kernel's most defect-prone area, despite no exceptional code-level complexity. The 241 fractal-value (Shannon-entropy of commit-distribution across authors normalized to $[0,1]$) gives a concrete estimator for the developer-count effect on $\rho$.

**Translation into AAT/TST.** Add empirical citations to $\#$meas-coherence-coupling's organizational paragraph. The fractal-value estimator $\mathrm{FV}(m) = 1 - \sum_i (c_i/C) \log(c_i/C) / \log\lvert A\rvert$ (normalized entropy of commit distribution) is a clean operational form to recommend. Stronger architectural connection: at the team level, the *team itself* is an AAT agent observing the codebase, and high $\mathrm{FV}$ (developer fragmentation) is structurally equivalent to high $U_o$ at the team-observation channel — when many developers each have a partial $M_t$ and no one has a coherent global picture, the team's *aggregate* $M_t$ is noisier than any individual's. This is a forward connection to $\#$der-code-quality-as-observation-infrastructure at the team level, parallel to the existing single-developer-level treatment.

**Honesty.** The Microsoft Research citation Tornhill references is real but the specific correlation numbers vary between his presentations (different papers give $r$ values from 0.6 to 0.85). Author count is *itself* correlated with code size, age, and change frequency — the regression is multicollinear in ways the books do not address. The structural claim (organizational factors dominate code-level factors as defect predictors) survives even with the variance acknowledged.

---

### F8. Code-age bimodality (G1/G3 desirable, G2 dangerous) — empirical structure of the unmaintainability threshold

**Source analyses:** [101-code-age-stabilization](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/101-code-age-stabilization.md), [123-code-aging-three-generations](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/123-code-aging-three-generations.md), [646-age-based-module-boundary-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/646-age-based-module-boundary-detection---using-code-age-patterns-to-identify-natural-system-boundaries.md), [647-refactoring-toward-age-similarity](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/647-refactoring-toward-age-similarity---strategies-for-grouping-code-by-similar-ages-to-reduce-cognitive-load.md), [648-package-structure-age-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/648-package-structure-age-analysis---reorganizing-package-hierarchies-based-on-code-age-patterns.md), [649-system-level-age-scaling](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/649-system-level-age-scaling---applying-age-analysis-principles-from-files-to-entire-systems.md), [650-median-age-deep-mining-techniques](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/650-median-age-deep-mining-techniques---advanced-statistical-analysis-of-codebase-age-distributions.md), [101-code-age-stabilization](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/101-code-age-stabilization.md)

**Class:** A (anchor for the named OUTLINE gap "Software persistence: the unmaintainability threshold")

**AAT-relevance:** OUTLINE Ch.4 GAP "Software persistence: the unmaintainability threshold formalized"; $\#$der-code-quality-as-observation-infrastructure (the $Q \to U_o \to \eta^\ast \to \mathcal T$ chain composed with persistence).

**The content (briefly).** Tornhill (via North) makes a sharp empirical claim: code health is *bimodal* in age. (i) **G1 — recent code, age $\lt \sim$30 days**: knowledge fresh in developers' heads (Ebbinghaus $K(t) = K_0 e^{-t/\tau}$ with $\tau \approx 20$ days for code-knowledge), comprehension cheap. (ii) **G3 — old stable code, age $\gt 1$ year**: no longer modified, so comprehension is unnecessary. (iii) **G2 — middle-aged code, $30\text{ days} \lt \mathrm{age} \lt 1$ year**: knowledge faded but the code still requires modification. *G2 is the danger zone.* The empirical observation in 101 + 123: G2 files have defect rates several times G1 and G3, and refactoring effort there pays back fastest. Independent observation (123): defects per year *decline* with age at rate $D(c, \mathrm{age}) \approx D_0 e^{-\mathrm{age}/365}$ — old code is roughly one-third as defect-prone after a year (this is the survival-as-quality-filter observation). The 648-analysis adds that age-clustering within a directory (low age-variance) is itself a coherence signal: files of similar age tend to share design decisions.

**Translation into AAT/TST.** Direct material for the named OUTLINE gap. The shape of the unmaintainability-threshold result Joseph hypothesizes is: a *bifurcation* in the $Q \to U_o \to \eta^\ast \to \mathcal T$ chain where G1 and G3 maintain $\mathcal T \gt \rho$ via different mechanisms (G1: $U_o$ low because knowledge fresh; G3: $\rho$ low because not modified), and G2 has $\mathcal T \lt \rho$ because $U_o$ has decayed (Ebbinghaus) faster than $\rho$ has dropped. The candidate segment writes this as: developer-channel persistence requires *either* the developer's local $M_t$ to be fresh (recent contact, low $U_o$) *or* the code's local $\rho$ to be near zero (no incoming change pressure); the G2 region violates both. This gives the "unmaintainability threshold" a specific inequality and predicts the bimodal age-distribution healthy codebases empirically exhibit. The decay rate $\tau \approx 20$ days is the proposed empirical anchor for $U_o$ dynamics on the developer-comprehension channel; combined with FP-003 / $\#$der-change-expectation-baseline as the source of $\rho$, the threshold becomes computable from the chronicle alone.

**Honesty.** The $\tau \approx 20$ days Ebbinghaus constant is from the original human-memory literature applied to text; its transfer to code-comprehension is plausible but unvalidated. The $D(c, \mathrm{age}) = D_0 e^{-\mathrm{age}/365}$ defect-decay rate is empirically observed but the form is fit-not-derived. The bimodality claim — that there is a danger-zone in the middle — is the structural content that survives translation; the specific constants are decorative. **This is the strongest single Class-A finding in the corpus for the named gap.**

---

### F9. Developer tempo channels separable in the chronicle — $\mathcal T_\mathrm{obs}$ as code-reading commits, $\mathcal T_\mathrm{probe}$ as test-modifying commits, $\mathcal T_\mathrm{explore}$ as scratch-branch / WIP commits

**Source analyses:** [333-knowledge-distribution-mapping](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/333-knowledge-distribution-mapping---creating-maps-of-expertise-distribution-across-codebases-and-teams.md), [336-truck-factor-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/336-truck-factor-analysis---quantifying-project-vulnerability-to-key-personnel-loss.md), [357-code-review-optimization-via-forensics](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/357-code-review-optimization-via-forensics.md), [700-code-reading-and-change-planning-support](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/700-code-reading-and-change-planning-support.md), [320-test-suite-evolution-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/320-test-suite-evolution-analysis---temporal-coupling-in-test-architecture.md)

**Class:** A (anchor for OUTLINE Ch.2 GAP "Developer tempo decomposition")

**AAT-relevance:** OUTLINE Ch.2 GAP $\mathcal T_\mathrm{dev} = \mathcal T_\mathrm{obs} + \mathcal T_\mathrm{explore} + \mathcal T_\mathrm{probe}$; matrix-Loewner weakest-channel bottleneck.

**The content (briefly).** Several Tornhill analyses operationalize different aspects of developer-channel observation: knowledge maps (333, 336) measure historical contact-with-code (proxy for $M_t$ accuracy of the developer-as-agent at a specific module); code-review effort (357) is a literal observational pass (Pearl-Level-1) on production code; commits that only modify tests (deductible from the chronicle by file-extension filtering) are probe-strengthening commits ($\mathcal T_\mathrm{probe}$); scratch-branch / WIP commits + commits that are later reverted are exploration ($\mathcal T_\mathrm{explore}$); commits that touch only main implementation files after passing through a test-first cycle are observation-grounded action. The chronicle's P5 exact recording makes the channels separable *post-hoc* in a way that is hard in other domains. The 700-analysis even proposes "code-reading planning" as a distinct developer activity worth instrumenting — supporting the framing that observation is a separate channel with its own $\nu$ and $U_o$.

**Translation into AAT/TST.** Direct support for the named OUTLINE gap. The candidate segment can introduce the chronicle-derivable operational definitions: $\mathcal T_\mathrm{probe}$ from test-only-changing commits; $\mathcal T_\mathrm{explore}$ from scratch-branch + revert-rate; $\mathcal T_\mathrm{obs}$ from code-review duration (when tracked) or proxy via commit-message-comprehension-references. Each has its own $(\nu, U_o)$ profile and the matrix-Loewner bottleneck applies — the weakest channel determines the developer's overall adaptive tempo. The empirical observation that test files appear at the top of hotspot lists (F2) is the symptom of $\mathcal T_\mathrm{probe}$ degrading faster than the other channels. The truck-factor / knowledge-map literature gives concrete estimators for the $M_t$ side of each channel — a knowledge-map *is* a directly estimated $M_t$ for the developer-as-agent at the file-level granularity.

**Honesty.** The chronicle gives evidence of *what* developers committed, not *how long they spent reading* before committing. Reconstructing $\nu_\mathrm{obs}$ from the chronicle requires an additional assumption that observation activity scales with commit activity (or with code-review-comment activity for projects that use PR review). The cleanest reconstruction is for $\mathcal T_\mathrm{probe}$ (test changes are auditable from filename); $\mathcal T_\mathrm{explore}$ is murkier (revert-tracking is incomplete); $\mathcal T_\mathrm{obs}$ requires explicit instrumentation that the chronicle alone does not provide.

---

### F10. The supervisor-tree / actor-model / hot-code-reload pattern — Class-1 composite from Class-2/3 components (literal wrapping construction)

**Source analyses:** [100-conways-law-team-alignment](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/100-conways-law-team-alignment.md), [251-team-coordination-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/251-team-coordination-analysis---conways-law-through-code-patterns.md), [332-brooks-law-modern-validation](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/332-brooks-law-modern-validation---testing-adding-people-to-a-late-project-makes-it-later-with-contemporary-data.md), [666-component-by-feature-packaging-strategies](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/666-component-by-feature-packaging-strategies---systematic-approaches-to-organizing-code-around-business-features.md), [663-silver-bullet-architecture-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/663-silver-bullet-architecture-detection---identifying-and-avoiding-oversimplified-architectural-solutions.md)

**Class:** A (anchor for the named "running software as agent" + "supervised composite under AI augmentation" gaps)

**AAT-relevance:** $\#$der-class-coercion-via-wrapping; running-software-as-agent gap.

**The content (briefly).** The "BEAM/OTP" sections of Tornhill's analyses are uneven, but several explicitly observe that supervision trees, message-passing, and process isolation create *architectural enforcement* of single-owner mental models, low coordination overhead, and reproducible recovery from individual-process failures. The 236/241 organizational-debt material observes that BEAM's process isolation "caps $\mathrm{complexity}_\mathrm{org}$ at the supervisor level rather than the system level" — a structural-modularity claim. The 663/666 architectural analyses observe that "feature-team" code organization aligns better with the empirical co-change distribution than "layer-team" organization. Combined: the supervisor-tree pattern is a runtime wrapping that takes Class-3 GenServers (which are stateful and goal-dependent in their reactions) and composes them into a Class-1 system via a structured restart-and-recover protocol that re-establishes invariants without consulting current-goal state.

**Translation into AAT/TST.** This is direct support for Joseph's named gap 1 (running software as a lower-form agent) *and* gap 2 (composite developer-agent under AI augmentation). The supervisor-tree is a worked instantiation of $\#$der-class-coercion-via-wrapping in the runtime domain: each child process is Class-3 (its behavior depends on $G$-state — goals, current request, accumulated state); the supervisor enforces a structural restart protocol that resets the child to a known initial state on failure, which is the literal goal-blind-belief-update structural commitment $W_1$. Hot-code-reload is the same trick at the code-level: the wrapping infrastructure (supervision + message-passing + restart contracts) is preserved across code substitution. Stronger framing: **a running software system is an AAT-class-1 composite that wraps possibly-class-3 components**, and the wrapping infrastructure (supervisor tree + recovery protocol + circuit-breaker / bulkhead / timeout — *all* the Release-It! patterns) is what makes it a class-1 composite. This gives the running-software-as-agent gap a concrete architectural form that maps cleanly onto AAT's existing wrapping machinery rather than requiring fresh theory.

**Honesty.** Tornhill is *not* making this AAT-mapping claim. He is observing operational properties (isolation, restart, message protocols) and noting that they reduce certain problems. The translation to "supervisor-tree = wrapping construction for class-coercion" is ours, not his, and it requires more development work than a single citation supports — but the structural correspondence is clean enough that a TST segment on it would be derivation, not handwave.

---

### F11. The mock-complexity blowup is a $U_o$ destruction signal — test-probe quality decays exponentially in dependency count

**Source analyses:** [635-untouchable-code-management](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/635-untouchable-code-management---strategies-for-managing-critical-code-that-cannot-be-refactored.md), [320-test-suite-evolution-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/320-test-suite-evolution-analysis---temporal-coupling-in-test-architecture.md), [639-test-code-coupling-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/639-test-code-coupling-analysis---specialized-temporal-coupling-analysis-for-test-suites.md), [643-provisional-safety-net-testing](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/643-provisional-safety-net-testing---temporary-test-strategies-for-legacy-code-refactoring.md)

**Class:** B (instantiation of $U_o$ dynamics for the test-probe channel)

**AAT-relevance:** $\#$der-code-quality-as-observation-infrastructure; F2 above.

**The content (briefly).** Tornhill repeatedly observes that mock-heavy tests behave pathologically: each additional dependency mocked increases the test's complexity multiplicatively (because the mock surface must mirror each dependency's interface contract), and changes to *any* dependency cause the test to require updating *even if the production behavior under test is unchanged*. The 320/635 framing of $C_\mathrm{mock} = E_\mathrm{deps} \times S_\mathrm{mocked} \times N_\mathrm{tested}$ is too informal but captures something real: a mock-heavy test is structurally not measuring the production system but measuring "the system as composed with these dependencies frozen at the assumptions when the mock was written" — and the freezing makes the probe progressively less informative as the dependencies drift.

**Translation into AAT/TST.** Mock-heavy tests are tests where $U_{o,\mathrm{test}}$ grows multiplicatively in dependency-count, because the test's information-content is conditioned on the mocked-dependencies-are-still-accurate assumption (an L1-style ambient-noise compound). A "good" test in TST terms is one where the probe's $U_o$ stays bounded as the production code evolves — which is a structural property of the test's mock-strategy, not of its assertion quality. This connects to $\#$der-code-quality-as-observation-infrastructure on the *probe* channel rather than the *observation* channel. Useful Discussion-paragraph material when the $U_o$ channel-decomposition lands.

**Honesty.** The exponential mock-complexity blowup is qualitatively observed in practice but the specific functional form is conjectural. The Tornhill analyses note the problem; they do not derive the form. The structural claim — mock-heavy tests have decaying $U_o$ that the in-situ probe does not have — is real and matches independent observation in the testing literature (test pyramids, contract testing, etc.).

---

### F12. The "rising hotspot" signal — a Lindy-effect violation that predicts ongoing accumulation

**Source analyses:** [238-rising-hotspot-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/238-rising-hotspot-detection---predictive-maintenance-problem-prevention.md), [677-evolutionary-pattern-deviation-early-warning](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/677-evolutionary-pattern-deviation-early-warning---predictive-models-for-code-quality-degradation.md), [654-evolutionary-pattern-deviation-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/654-evolutionary-pattern-deviation-detection---early-warning-systems-for-code-quality-degradation.md), [678-complexity-increase-steep-warning-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/678-complexity-increase-steep-warning-detection---automated-alerts-for-rapidly-deteriorating-code-quality.md)

**Class:** B (refinement to $\#$der-change-expectation-baseline)

**AAT-relevance:** $\#$der-change-expectation-baseline ("median future $\approx$ observed past"); $\#$hyp-causal-discovery-from-git frequency-asymmetry signal.

**The content (briefly).** A "rising hotspot" is a file whose rank in the hotspot list (sorted by recent commit count) has climbed substantially over the recent window. Tornhill argues this signal is *more* predictive than the absolute hotspot rank because it captures *change in change rate* — a file with rising frequency under fixed total project effort indicates the file is consuming a growing share of attention, which is a leading indicator of impending unmaintainability. The 238-analysis frames this as an "acceleration factor" $\lvert\Delta r\rvert / b_r$ (rank-change magnitude over baseline rank-change) applied to the Lindy-effect prior. Empirically, files climbing more than 10 ranks in 2 months go on to consume 3$\times$ more developer-time per change than stable-rank files.

**Translation into AAT/TST.** Pure refinement of $\#$der-change-expectation-baseline: the "median future $\approx$ observed past" prior is the simplest possible Bayesian update on the file-level change rate, but the *derivative* of that rate carries additional information. A file whose change-rate is rising violates the stationarity-of-$\lambda(F_i)$ assumption that justifies plain Lindy; the resulting estimator should weight recent commits more heavily (the exponential-decay-on-history that several Tornhill analyses use is approximately this). Worth a one-paragraph Discussion mention in $\#$der-change-expectation-baseline noting that the segment's "uninformative prior" admits a "rising-hotspot" refinement when chronicle is long enough to estimate trend.

**Honesty.** The 3$\times$-multiplier claim is anecdotal. The structural content — that rising rank indicates non-stationarity in $\lambda(F_i)$ — is correct and worth surfacing.

---

### F13. Cross-repository (virtual root) analysis — the chronicle's P5 partial-exteriorization fails at repo boundaries

**Source analyses:** [676-virtual-root-analysis-for-distributed-systems](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/676-virtual-root-analysis-for-distributed-systems.md), [246-cross-repository-change-pattern-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/246-cross-repository-change-pattern-analysis.md), [670-multi-repository-cohesion-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/670-multi-repository-cohesion-analysis---detecting-low-cohesion-services-across-distributed-systems.md), [671-implicit-microservice-dependency-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/671-implicit-microservice-dependency-detection---finding-hidden-dependencies-between-supposedly-independent-services.md), [675-shotgun-surgery-pattern-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/675-shotgun-surgery-pattern-detection---identifying-problematic-change-patterns-across-service-boundaries.md)

**Class:** C (candidate scope-extension for $\#$obs-software-epistemic-properties P5)

**AAT-relevance:** $\#$obs-software-epistemic-properties P5 (chronicle exteriorization); $\#$meas-coherence-coupling; M3 additive-coordinate-forcing pattern.

**The content (briefly).** Microservice / multi-repo architectures fragment the chronicle: each repo has its own commit hash-chain, and the cross-repo causal links (changes that should be co-committed but are not because they live in different repos) are *invisible* in any single repo's chronicle. The 676 "virtual root" technique stitches multiple repos' chronicles by aligning timestamps and inferring cross-repo coupling from temporal proximity — a much weaker signal than within-repo co-commit. The 675 analysis observes that microservice decomposition does not eliminate logical coupling; it *transforms* it from co-commit (visible) to temporally-proximate-cross-repo-changes (much harder to detect, especially under async messaging).

**Translation into AAT/TST.** P5 in $\#$obs-software-epistemic-properties states that software's committed-state chronicle is partially exteriorized with cryptographic immutability. The "partially" is important: across repository boundaries, the exteriorization fails — there is no single hash-chain over the joint state. This means that for distributed systems, the high-identifiability calibration-lab status partially degrades to the additional-transfer-assumption regime that other domains live in. Worth a Discussion paragraph in $\#$obs-software-epistemic-properties noting that P5's "exact recording" is repo-local; cross-repo causal claims face an identifiability problem similar to M1 / M3 patterns. The virtual-root reconstruction is *itself* an additional intervention (aligning chronicles, inferring temporal-proximity bands) that the segment's framing requires to be made explicit.

**Honesty.** The corpus presents virtual-root as a practical fix without acknowledging that it introduces additional identifiability assumptions. The structural content — that repo boundaries are an identifiability-floor wall that requires extra interventions to bridge — is the right framing and is currently missing from $\#$obs-software-epistemic-properties.

---

### F14. The 150-commit minimum is approximately the right magnitude for the chronicle's statistical sufficiency

**Source analyses:** [681-behavioral-code-analysis-bias-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/681-behavioral-code-analysis-bias-detection---identifying-and-correcting-systematic-biases-in-forensic-analysis.md), [688-data-mining-workflow-optimization](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/688-data-mining-workflow-optimization---efficient-techniques-for-processing-large-codebases.md), [296-automated-change-analysis-with-code-maat](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/296-automated-change-analysis-with-code-maat---mining-version-control-for-development-time-patterns.md)

**Class:** D (empirical anchor)

**AAT-relevance:** $\#$hyp-causal-discovery-from-git Discussion (data requirements); $\#$meas-coherence-coupling "Requirements" paragraph.

**The content (briefly).** Tornhill repeatedly observes that 150-200 commits is the threshold below which the statistical patterns are too noisy to reveal meaningful structure. The 681 derivation links this to a confidence-interval calculation $n_\mathrm{commits\_min} = \log(1 - \mathrm{confidence}) / \log(1 - p_\mathrm{pattern})$ which yields $\sim$150 for 95% confidence at $p = 0.02$. This particular derivation is fit-not-derived, but the order of magnitude is borne out in operational experience across multiple Tornhill analyses.

**Translation into AAT/TST.** Worth adding to $\#$meas-coherence-coupling and $\#$hyp-causal-discovery-from-git as a "minimum-history" requirement. Concrete framing: the measurement requires $\sim$150+ commits with file-level granularity for statistical significance; below this, the segment's estimators are descriptive only. Useful, modest, second-tier.

**Honesty.** The specific constant is from a single formula with a hand-picked $p$; it cannot be defended as "derived." But the order of magnitude (hundreds, not tens or thousands) is operationally robust.

---

### F15. Internal coupling within a file — the case where the unit-of-analysis must drop below file granularity

**Source analyses:** [234-temporal-coupling-x-ray-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/234-temporal-coupling-x-ray-analysis---method-level-change-pattern-detection.md), [638-internal-change-coupling-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/638-internal-change-coupling-detection---analysis-of-coupling-within-single-files-or-modules.md), [697-internal-coupling-omission-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/697-internal-coupling-omission-detection---finding-missing-relationships-in-change-coupling-analysis.md), [633-deep-code-x-ray-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/633-deep-code-x-ray-analysis---advanced-inspection-techniques-beyond-surface-level-hotspot-detection.md), [242-copy-paste-temporal-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/242-copy-paste-temporal-analysis---prioritizing-clone-refactoring-by-change-coupling.md)

**Class:** B (refinement to the unit-of-analysis used by $\#$def-system-coupling)

**AAT-relevance:** $\#$def-system-coupling (file-level by default).

**The content (briefly).** When a file is a hotspot, the chronicle's file-level granularity becomes the bottleneck — the file changes constantly, but *which methods change together within it* is the actually-informative question. Tornhill's X-Ray analysis (234) drops to the method-level: a 20,000-line file containing 200 methods where only 5 methods cluster as "always change together" reduces the search space by $\sim$60$\times$ at the cost of needing AST-level diff parsing rather than file-level. The 242 copy-paste analysis is the inverse: when the same pattern recurs across files, the *method-or-block-level* clone is the unit of analysis, and only clones with temporal coupling matter (clones that never co-change are immaterial).

**Translation into AAT/TST.** The unit of analysis in $\#$def-system-coupling is currently the module. The Tornhill X-Ray observation generalizes: at the appropriate granularity, the same conditional-probability $P(\Delta j \mid \Delta i)$ framework applies, and dropping granularity to find the true co-change unit is sometimes necessary. Worth a Working-Notes pointer in $\#$def-system-coupling that the segment's definition is granularity-invariant and that empirical use sometimes drops below file-level. Not load-bearing.

**Honesty.** Method-level diff-parsing across an evolving codebase is harder than the analyses claim (function-rename detection is not always reliable). The structural content — that the unit-of-analysis adapts to the question — is straightforward.

---

### F16. Coupling decay over time — the $\rho_{ij}(t) = \rho_0 e^{-\lambda t}$ "expiration" of co-change as evidence

**Source analyses:** [679-change-absence-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/679-change-absence-analysis---detecting-potentially-problematic-areas-that-receive-no-maintenance.md), [243-normalization-of-deviance-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/243-normalization-of-deviance-detection---preventing-gradual-code-quality-decay.md)

**Class:** D (refinement consideration)

**AAT-relevance:** $\#$meas-coherence-coupling Working Notes.

**The content (briefly).** The 679-analysis observes that historical coupling decays — a $\rho$ estimate that was strong two years ago may be irrelevant now because the codebase has restructured. The proposed exponential-decay model $\rho_{ij}(t) = \rho_0 e^{-\lambda t}$ with $\lambda$ around 0.1-0.2 per month is fit-not-derived but operationally important: the $\rho$ measure should weight recent commits more heavily.

**Translation into AAT/TST.** Worth a one-line Working-Notes addition to $\#$meas-coherence-coupling noting that the estimator should weight recent commits more heavily under non-stationary $\lambda(F_i)$. Already covered implicitly by the segment's "Feature-distribution sensitivity" Discussion; not load-bearing.

**Honesty.** The exponential form is fit-not-derived. The structural observation (recent > distant past for current-coupling estimation) is correct and obvious.

---

### F17. The "bugs by omission" detector — co-change-expected-but-absent as a chronicle-derivable hypothesis test

**Source analyses:** [679-change-absence-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/679-change-absence-analysis---detecting-potentially-problematic-areas-that-receive-no-maintenance.md)

**Class:** C (candidate new TST segment)

**AAT-relevance:** $\#$hyp-causal-discovery-from-git (this is a falsifiable prediction made by the causal-coupling estimate).

**The content (briefly).** If the chronicle says files $A$ and $B$ have historically co-changed with probability $\rho(A, B) \gt 0.7$, then a commit that touches $A$ but not $B$ is an *anomaly*: either (i) the coupling was spurious (false positive on historical $\rho$), (ii) the developer is making a bug-by-omission (forgetting to update the coupled component), or (iii) the coupling structure has changed (refactoring). The 679-analysis proposes precommit hooks that fire on this anomaly. This is structurally a falsifiable hypothesis test of the chronicle-derived causal-coupling estimate: a forward prediction made by $\hat{\rho}(A, B)$ that can be checked against subsequent commits (does the bug-fix that follows touch B? does a follow-up commit a few days later touch B? if neither, the high-$\rho$ estimate was spurious).

**Translation into AAT/TST.** This is operationally the right form of validation for $\#$hyp-causal-discovery-from-git: the hypothesis predicts that high-$\hat\rho$ pairs should co-change in *future* commits, and chronicle-derived predictions can be checked against the chronicle's own continuing record. Could be a paragraph in $\#$hyp-causal-discovery-from-git's "research program" section operationalizing what "validate the causal estimate" means. Conceptually closer to F5 (frequency-asymmetry as residual signal) than F4 (PDI with chronicle-derived prior). Modest contribution.

**Honesty.** The "anomaly = bug" reading has noise — refactoring legitimately violates historical coupling, and the test cannot distinguish refactoring from omission without additional information.

---

### F18. The "37,000-line file is born that way, not aged into it" observation — empirical evidence against gradual-decay models

**Source analyses:** [249-defect-prediction-models](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/249-defect-prediction-models---using-forensic-analysis-patterns-to-predict-bug-prone-code-areas.md), [656-software-complexity-tipping-point-mathematical-models](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/656-software-complexity-tipping-point-mathematical-models.md), [238-rising-hotspot-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/238-rising-hotspot-detection---predictive-maintenance-problem-prevention.md)

**Class:** D (empirical evidence for the maintenance-threshold bifurcation in F8)

**AAT-relevance:** F8 above; $\#$der-code-quality-as-observation-infrastructure bifurcation hypothesis.

**The content (briefly).** Tornhill's observation across multiple case studies (notably .NET Core's `gc.cpp`, Linux's Intel-graphics driver, several Android `*ActivityManagerService*` files): the giant unmaintainable files were *born large and complex*, not slowly accumulated. The accumulation pattern is rapid growth in the first months of life, then asymptotic plateau at an unmaintainable level. This evidence cuts against the "code decays gracefully" framing and supports the bifurcation framing: G2 = "trying to be normal-sized but actually unmaintainable due to design," not "stable codebase aging out of comprehension."

**Translation into AAT/TST.** Empirical anchor for the bifurcation form of the unmaintainability threshold (F8): the chain $Q \to U_o \to \eta^\ast \to \mathcal T$ admits multiple basins of attraction; the giant-file pattern is the failed basin. Empirical evidence consistent with M1 (identifiability-floor) framing: at creation time, multiple architectures could in principle be in use, but once a file crosses a size/complexity threshold, the system locks into a basin that further data cannot escape without intervention. Worth surfacing as supporting evidence when F8 is developed; not load-bearing on its own.

**Honesty.** The corpus does not provide a careful statistical analysis to rule out "files born medium and rapidly accumulating to large" — Tornhill is reasoning from the survivor case studies. The structural content (creation-time architecture dominates evolution) is broadly correct but the specific cases may not be representative.

---

### F19. Brooks's-Law empirical validation — Tornhill's data points are consistent with the tempo-composition (closure-defect) prediction

**Source analyses:** [332-brooks-law-modern-validation](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/332-brooks-law-modern-validation---testing-adding-people-to-a-late-project-makes-it-later-with-contemporary-data.md), [241-fractal-value-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/241-fractal-value-analysis---quantifying-coordination-overhead.md), [657-coordination-needs-measurement-algorithms](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/657-coordination-needs-measurement-algorithms---quantitative-methods-for-predicting-team-coordination-requirements.md)

**Class:** D (empirical anchor for tempo composition)

**AAT-relevance:** AAT tempo composition (Brooks's-Law); $\#$der-class-coercion-via-wrapping (coordination overhead = the wrapping cost paid at the team level).

**The content (briefly).** The 2.5$\times$ slowdown for distributed-team work and the $n^{1.5}$ coordination-overhead scaling are repeatedly cited across Tornhill's analyses with consistent magnitudes. The fractal-value (F7) entropy-based estimator gives a chronicle-derivable proxy for "effective developer count" weighted by contribution distribution. These are empirical anchors for AAT's existing tempo-composition machinery — adding developers to a system increases coordination overhead super-linearly, with cross-repo / cross-timezone / cross-team multipliers stacking.

**Translation into AAT/TST.** Empirical anchors for the team-level instantiation of AAT's tempo-composition machinery. Useful as Discussion-citations in whatever segment ends up handling team-as-composite-developer-agent (Joseph's named gap 2). The fractal-value estimator is a clean chronicle-derivable proxy for "effective developer count" that should be in the catalog of operational measurements.

**Honesty.** The specific numbers vary between analyses with no shared source; treat as order-of-magnitude anchors, not point estimates.

---

### F20. The "comprehension is sometimes free if you don't have to modify" observation — refining the dual-optimization

**Source analyses:** [101-code-age-stabilization](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/101-code-age-stabilization.md), [123-code-aging-three-generations](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/123-code-aging-three-generations.md), [285-optimize-for-understanding-principle](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/285-optimize-for-understanding-principle.md), [286-maintenance-first-development](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/286-maintenance-first-development---optimizing-for-comprehension-over-creation.md)

**Class:** B (refinement to $\#$der-dual-optimization)

**AAT-relevance:** $\#$der-dual-optimization.

**The content (briefly).** A key Tornhill insight in the age-distribution analyses: G3 (old stable) code has near-zero comprehension cost not because it is well-written but because it is *not being modified* — the chain "comprehend $\to$ implement $\to$ verify" is short-circuited by "do not touch." The dual-optimization is $\min(t_\mathrm{comp} + t_\mathrm{impl})$ summed over future changes, but when $P(\mathrm{change}) \to 0$ for a region, both terms drop to zero regardless of code quality. This explains the "ugly code can be high-quality if it never changes" intuition rigorously.

**Translation into AAT/TST.** Refinement of $\#$der-dual-optimization Discussion: the turnover-multiplier-weighted sum has the property that *very-low-probability-of-future-change* regions contribute negligibly to the optimization target even if their per-change costs are high. The G3 region is the place where this asymmetry is exploited. Modest but useful Discussion-paragraph material.

**Honesty.** This is essentially restating the segment's existing framing more concretely; not a new finding so much as a clean instantiation.

---

### F21. The "deviance normalizes" observation — a chronicle-derivable signal for M4 modularity-state-dynamics

**Source analyses:** [243-normalization-of-deviance-detection](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/243-normalization-of-deviance-detection---preventing-gradual-code-quality-decay.md), [248-normalization-of-deviance](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/248-normalization-of-deviance---preventing-complexity-drift-through-trend-analysis.md), [325-social-bias-impact-on-development](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/325-social-bias-impact-on-development---understanding-how-psychological-biases-affect-code-quality-and-team-decisions.md), [326-group-decision-bias-analysis](file:///Users/josephwecker-v2/src/_core/tst/planning/analysis/326-group-decision-bias-analysis---systematic-development-time-penalties-from-social-dynamics.md)

**Class:** C (potential M4 worked-example, secondary to F3)

**AAT-relevance:** M4 modularity-state-dynamics (strategic self-coupling decreasing, self-driven).

**The content (briefly).** "Normalization of deviance" — the team's tolerance for low-quality patterns drifts upward over time as each marginal deviation gets accepted — is a chronicle-derivable phenomenon: track the variance of complexity-delta per commit over rolling windows; rising variance + rising mean = the team's quality bar has drifted. The 243/248-analyses propose this as a trend detector for the modularity-state-dynamics drift Joseph's M4 hypothesizes. This is a self-driven decrease in modularity rather than externally-driven, distinguishing it from F3's adversarial-coupling-pressure mechanism.

**Translation into AAT/TST.** Worked instance of M4's "strategic self-coupling, self-driven-decreasing" operation, complementing F3's externally-driven case. Could be a secondary citation when M4 lands. Less load-bearing than F3 because the social-science basis is softer.

**Honesty.** The "deviance normalizes" claim is sociologically real (Vaughan on Challenger, etc.) but the operational chronicle-signal is conjectural — the corpus does not present validating data.

---

## Cross-cutting observations

**Structural finding.** The Tornhill corpus is essentially *one* operational framework — hotspot $\times$ change-coupling $\times$ code-age $\times$ knowledge-map — applied across $\sim$190 analyses with minor variations. After F1-F21 above, additional analyses contribute diminishing marginal yield. The corpus is empirically rich within this framework and theory-thin outside it; this is the right shape for an operational-confirmation source rather than a theory source.

**Where AAT/TST is strictly stronger.** Tornhill formulates everything in operational time-cost terms ("X hours saved per change") without a coherent underlying mechanism. AAT's $\mathcal T$ / $\rho$ / $U_o$ / $\eta^\ast$ machinery gives these operational quantities a derivation rather than an estimate, and the M1 identifiability-floor pattern makes the limits of chronicle-based estimation rigorous in a way the corpus does not attempt.

**Where the corpus contributes back.** The chronicle-derivable estimators (hotspot $H = fc$, asymmetric and lagged co-change, fractal-value entropy, age-bimodality, rising-hotspot trend) are operational forms that AAT segments should surface where appropriate — they convert AAT's theoretical quantities into computable measurements. The clearest such case is the F8 unmaintainability-threshold bifurcation (Class A, fills a named gap directly) and the F1+F3 confounder-class extension to $\#$hyp-causal-discovery-from-git (Class A, refines the segment's research-program framing with a fourth confounder that matters operationally).

**Where the corpus actively misleads.** The pervasive "(1+r)^n compound interest" framing for technical debt is metaphor sold as derivation; the various exponential-decay constants ($\alpha \approx 0.2$, $\gamma \approx 0.3$, $\lambda \approx 0.1$ per month, etc.) are fitted-to-narrative not derived. Translation into AAT should preserve the structural form and drop the spurious quantitative dressing.

**Joseph's named-gap coverage.** Gap 1 (running software as agent): partial coverage via F10 (supervisor-tree as wrapping) — strong structural-correspondence but Tornhill is not making the claim, so the segment would need its own derivation. Gap 2 (composite developer-agent under AI augmentation): the knowledge-map / truck-factor / fractal-value material (F7, F9, F19) is the operational substrate but the AI-augmentation piece is absent from the corpus by date. Gap 3 (developer tempo channel decomposition): F9 gives the chronicle-derivable channel separation directly — strongest empirical material for this gap. Gap 4 (unmaintainability threshold): F8 (code-age bimodality) is the strongest single piece of mineable material in the entire corpus for a named gap.
