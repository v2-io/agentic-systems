---
slug: detection-latency
type: derivation
status: conditional
depends:
  - edge-update-natural-parameter
  - credit-assignment-boundary
  - strategy-persistence-schema
  - identifiability-floor
  - strategic-dynamics-derivation
  - structural-adaptation-necessity
  - exploit-explore-deliberate
stage: draft
---

# Derivation: Detection Latency Under Accumulated Experience

For a Beta-Bernoulli strategy-edge agent without forgetting, the expected number of cycles required to detect a within-class regime change of observable footprint $\varepsilon$ scales as $\Omega((n_{\min}+1)/\varepsilon)$ with $n_{\min}$ the minimum accumulated pseudo-count on load-bearing edges. The $1/(n+1)$ rate is **structurally forced** — it is the log-odds update magnitude per cycle under #edge-update-natural-parameter's Aczél-Cauchy-FE uniqueness theorem, and no choice of coordinate escapes it. The result sharpens #strategy-persistence-schema's forgetting prerequisite from "required for asymptotic persistence" to "required for detection-latency bounded independently of operating point." The broader myopia observation — that successful, high-capability organizations systematically underinvest in detecting regime changes that would require structural adaptation — admits a complementary decision-theoretic account via #exploit-explore-deliberate's oracle analysis; this segment's contribution is the signal-side lower bound, not the decision-side account.

## Formal Expression

### Setup

An agent with a Beta-Bernoulli strategy DAG per #strategy-persistence-schema / #strategic-dynamics-derivation, credit assignment via the log-odds signal of #credit-assignment-boundary (forced by #edge-update-natural-parameter), and no forgetting ( $\lambda = 1$, pseudo-counts $n_k$ accumulate monotonically). Let $E_{\text{load}}$ denote the load-bearing edges on the current active plan; $n_{\min} = \min_{k \in E_{\text{load}}} n_k$. The agent has been operating with model-class fitness $\mathcal F(\mathcal M)$ near $1$, adaptive reserve $\Delta\rho^\ast \gt 0$, control regret $\delta_{\text{regret}}$ small — a high-operating-point configuration.

At cycle $t_0$, a regime change occurs within the current model class (a true edge probability shifts by $\varepsilon$; the L0 graph remains correct; the agent's model class still suffices). This is case R1 in the spike taxonomy — a within-class drift change. Other regime-change cases (R2 model-class inadequacy; R3 L0→L1 structural transition) are deferred to Working Notes and #identifiability-floor respectively.

### Detection-latency theorem

*[Derived (detection-latency-R1, from edge-update-natural-parameter + strategic-dynamics-derivation)]*

**Proposition.** Under the setup, the expected number of cycles $T_{\text{detect}}$ required for the log-odds coordinate on any load-bearing edge $k \in E_{\text{load}}$ to cross a fixed detection threshold $\Delta\lambda_{\text{detect}}$ in response to the regime change satisfies

$$\boxed{\;\mathbb E[T_{\text{detect}}] \;=\; \Omega\!\left(\Delta\lambda_{\text{detect}} \cdot (n_{\min} + 1) / \varepsilon\right)\;}$$

**Derivation.** The default signal function of #credit-assignment-boundary (under the log-odds coordinate forced by #edge-update-natural-parameter) updates an edge's log-odds credence by

$$\lambda_k^{\text{new}} = \lambda_k + \eta_{\text{edge}} \cdot \iota_k \cdot J_k \cdot (y_G - \hat P_\Sigma) / \lVert\mathbf J\rVert^2$$

with $\eta_{\text{edge}} = 1/(n_k + 1)$ for Beta-Bernoulli (Prop B.4 of #strategic-dynamics-derivation). Per-cycle the expected log-odds update magnitude is bounded:

$$\mathbb E\lvert\Delta\lambda_k\rvert \;\leq\; \frac{\lvert J_k\rvert \cdot \mathbb E\lvert y_G - \hat P_\Sigma\rvert}{\lVert\mathbf J\rVert^2 \cdot (n_k + 1)}$$

Under regime change R1 with observable footprint $\varepsilon$, the expected systematic residual $\mathbb E\lvert y_G - \hat P_\Sigma\rvert = \Theta(\varepsilon)$ as $\varepsilon \to 0$ (the misspecified-edge residual is proportional to the edge's probability shift, via the linearization of the Bernoulli likelihood in a neighborhood of the pre-change parameter). Combining: the per-cycle expected log-odds increment on load-bearing edges is $O(\varepsilon/(n_{\min}+1))$.

For the agent to cross $\Delta\lambda_{\text{detect}}$, expected cycles required is at least $\Delta\lambda_{\text{detect}} / (O(\varepsilon/(n_{\min}+1)))$ = $\Omega(\Delta\lambda_{\text{detect}} \cdot (n_{\min}+1) / \varepsilon)$. $\square$

### The rate is structurally forced

*[Observation (rate-forced-by-aczel)]*

The $1/(n+1)$ scaling is not a property of the specific update rule choice. Per #edge-update-natural-parameter, the log-odds coordinate is the *unique* additive-evidence coordinate satisfying the evidential-additivity axiom — the Aczél 1966 Cauchy-functional-equation uniqueness theorem forces it up to positive affine transformation. In this forced coordinate, the per-cycle increment for Beta-Bernoulli edges is forced to be $O(1/(n+1))$: the Fisher-equivalent statement holds in any sensible coordinate. Rearranging the update to a different scale does not change the rate — it just changes the units in which the rate is measured.

The forcing composition:

1. #edge-update-natural-parameter forces the log-odds coordinate via evidential additivity.
2. In that coordinate, Beta-Bernoulli accumulation gives $\eta_{\text{edge}} = 1/(n+1)$.
3. Therefore the per-cycle update magnitude is structurally forced at $O(1/(n+1))$.

This is the specific link between AAD's constructive meta-pattern ( #additive-coordinate-forcing, via #edge-update-natural-parameter's theorem) and a downstream detection-latency consequence. The rate cannot be escaped without abandoning evidential additivity — which would invalidate the update rule on AAD-internal grounds, not merely operational ones.

### Sharpening the forgetting prerequisite

*[Corollary (forgetting-as-latency-bound, sharpens #strategy-persistence-schema)]*

#strategy-persistence-schema derives the forgetting prerequisite $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$ as required for *asymptotic persistence* — without forgetting, $\alpha_\Sigma = 1/(n+1) \to 0$ and persistence eventually fails. The detection-latency theorem sharpens this to a **load-bearing claim about detection latency on the way to asymptotic failure**:

**Forgetting is required not only for asymptotic persistence, but also for detection latency to be bounded independently of operating point.** Without forgetting, $n_{\min}$ grows monotonically, and $\mathbb E[T_{\text{detect}}]$ grows linearly with $n_{\min}$. With forgetting at rate $\lambda \lt 1$, the effective pseudo-count $n_{\text{eff}} = 1/(1-\lambda)$ is bounded, and the detection latency caps at $\Omega(1/((1-\lambda)\varepsilon))$ regardless of how long the agent has been operating.

This dualizes #strategy-persistence-schema's asymptotic claim: forgetting is operationally load-bearing at every step, not only in the limit. An agent with the right $\lambda$ has bounded detection latency throughout its lifetime; an agent with $\lambda = 1$ has detection latency that grows unboundedly with experience, producing the phenomenon of stability-induced myopia in practice.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| R1 detection-latency theorem $\mathbb E[T_{\text{detect}}] = \Omega((n_{\min}+1)/\varepsilon)$ | #edge-update-natural-parameter log-odds coordinate + #strategic-dynamics-derivation Prop B.4 $\eta_{\text{edge}} = 1/(n+1)$ + Pinsker-type linearization | Derived (conditional on Beta-Bernoulli + log-odds + no forgetting) |
| $1/(n+1)$ rate structurally forced | Composition of #edge-update-natural-parameter's Aczél-Cauchy-FE theorem with Beta-Bernoulli accumulation | Proved (conditional on evidential-additivity axiom) |
| Sharpening of forgetting prerequisite from asymptotic persistence to bounded detection latency | #strategy-persistence-schema + this theorem | Derived |
| R2 model-class inadequacy sub-case (C1-diagnostic blindness under misspecification) | Common-mode-bias argument on $A_O^{(1)}$ vs $V_O(\pi_{\text{current}})$ | Discussion (sketch; see Working Notes) |
| R3 L0→L1 structural transition sub-case | Direct application of #identifiability-floor Instance 1 — already derived there | Reference (not new content) |
| Probability-of-deferral bound | Derivable from the expected-time bound via Markov inequality | Discussion |
| Connection to institutional inertia / Christensen / competency traps | Stability-induced-myopia as a mechanism for the empirical pattern | Discussion |
| Connection to IDT sidecar monitoring (Hafez et al. 2026 89% vs 44%) | On-policy reward-based monitoring is the log-odds accumulator; IDT bi-predictability is a change-detector that bypasses the $1/(n+1)$ rate | Discussion |

## Epistemic Status

*Conditional.* Max attainable: *exact* for R1 under stated scope (Beta-Bernoulli + log-odds forced + no forgetting + linearized residual near pre-change parameter); *robust qualitative* for general exponential-family edge with similar sufficient-statistic accumulation; *discussion-grade* for extensions beyond the Beta-Bernoulli / log-odds specialization.

The R1 theorem is a direct consequence of two derived AAD results ( #edge-update-natural-parameter's forced log-odds coordinate + #strategic-dynamics-derivation's Beta-Bernoulli $\eta_{\text{edge}}$) composed with a standard residual-magnitude argument (Pinsker-type inequality applied to the linearized Bernoulli likelihood). The mathematical core is not novel — what is novel is the AAD-framing: reading the $1/(n+1)$ scaling as *structurally forced* through composition of existing AAD theorems, not contingent on update-rule choice. The rate is unescapable without abandoning evidential additivity.

The forgetting-prerequisite sharpening follows by direct substitution — replace unbounded $n_{\min}$ with bounded $n_{\text{eff}} = 1/(1-\lambda)$ and the latency bound inherits the cap. This is where the segment's most concrete contribution lies: the existing forgetting prerequisite's justification expands from "asymptotic persistence fails without it" to "detection latency is unbounded in operating point without it." Two load-bearing consequences instead of one, from the same $\lambda \lt 1$ condition.

**What this does not establish:**

- R2 (model-class inadequacy) as a full derivation. The sketch argument — that $A_O^{(1)}$ and $V_O(\pi_{\text{current}})$ share common-mode bias under misspecification, so the C1 regret diagnostic under-reports — is qualitatively clear but quantitatively informal. Making it rigorous requires a model of the bias's functional form.
- R3 (L0→L1 transition) as new content. This is #identifiability-floor Instance 1 — a structural no-go, not a latency bound. This segment references it but does not extend it.
- Decision-theoretic consequences. The theorem is about signal latency, not about whether the signal once received yields the right decision. #exploit-explore-deliberate's oracle analysis (which shows deliberation rarely chosen) operates at the decision-theoretic level; the myopia theorem operates at the signal-quality level. An agent with degraded signals + perfect decision rule still defers; this is complementary to the oracle's degraded-decision-with-perfect-signals result.
- Extension beyond Beta-Bernoulli. Gaussian edges admit $1/(n+c)$ scaling with analogous behavior; general exponential-family edges admit scaling following the sufficient-statistic accumulation. The qualitative form — expected detection time monotone in accumulated sufficient statistic — is more general than Beta-Bernoulli; the quantitative $1/(n+1)$ is specific.

## Discussion

**The forcing composition is where the meta-pattern interacts with downstream results.** #additive-coordinate-forcing is an AAD meta-segment naming the Cauchy-FE structural move at three layers (chain / divergence / update). This segment exhibits the specific case where that move's downstream consequences bind: the log-odds forcing at the update layer implies — through Beta-Bernoulli accumulation — a specific detection rate that cannot be escaped via re-parameterization. The meta-pattern's constructive power is visible here as a *negative* downstream consequence (bounded detection rate), which then becomes the positive motivator for forgetting. This is an example of AAD's meta-architecture composing constructively: the forcing move (positive) produces a bound (negative) that sharpens an existing requirement (positive).

**Distinction from adjacent phenomena:**

- #structural-adaptation-necessity characterizes WHEN restructuring is needed at truth (model-class inadequacy). This segment characterizes WHEN (in terms of cycles) the agent's detection signal crosses threshold. The two together say: the agent will eventually detect a structural problem, but the latency can be large at high operating point.
- #exploit-explore-deliberate gives a decision rule over exploit / explore / deliberate given signals. This segment is about signal quality — specifically, a predictable bias in signals as a function of operating point. The two compose: even an oracle's decision rule applied to myopia-biased signals produces deferred action.
- #strategy-persistence-schema's forgetting prerequisite is a condition for asymptotic persistence. The corollary here is a condition for bounded detection latency — the same $\lambda \lt 1$ buys both.
- #identifiability-floor Instance 1 (on-policy L0-insufficiency no-go) is a structural unboundedness result specific to L0/L1 transitions. The R1 detection-latency theorem is a quantitative bound on a broader class of regime changes (within-class drift, not just structural transitions).

**Connection to cross-domain empirical patterns.** Christensen's *Innovator's Dilemma*, Levitt & March competency traps, Hannan & Freeman structural inertia, March exploration/exploitation, and Eldredge-Gould punctuated equilibria all identify empirical patterns of stability-induced myopia across domains. The common story is that successful, mature, capable systems systematically underinvest in detecting regime changes that would require restructuring. The theorem supplies a mechanism: as experience accumulates ($n_{\min}$ grows), per-observation learning rate decays as $1/(n+1)$, expected detection time grows linearly, and the structural-adaptation trigger signal is systematically delayed. The phenomenon is not only decision-theoretic (incentive mis-alignment, short-horizon myopia) — it has a signal-side epistemic component forced by the log-odds coordinate. The signal-side and decision-side stories compose; neither subsumes the other.

**Connection to IDT (Hafez et al. 2026) empirical result.** Hafez et al. 2026 observed 89% vs 44% detection accuracy for Information Digital Twin (IDT) sidecar monitoring vs reward-based monitoring. The AAD-native explanation: reward-based monitoring is the log-odds accumulator — it inherits the $1/(n+1)$ detection rate and is subject to the theorem's latency bound. IDT's bi-predictability and entropy-change measures are structural-information-theoretic tests that bypass the log-odds coordinate entirely; they are change-detectors in the CUSUM / GLR tradition (Page 1954; generalized likelihood ratio tests) rather than Bayesian credence accumulators. The predicted gap between the two monitoring styles grows with accumulated experience — a testable refinement of the 89%/44% observation. A sidecar change-detector is always going to beat the log-odds accumulator on detection latency for within-class drift; the AAD theorem explains why without invoking the specific IDT mechanism.

**The signal side and decision side as complementary.** The fact that the oracle in #exploit-explore-deliberate rarely chose deliberation is usually read as "agents correctly defer when deliberation is expensive and information is limited." This segment's theorem adds: "and the information is limited in a specific quantitative way that scales with operating point." Both are true; neither is contradicted. The detection-latency result does not overturn the oracle analysis; it provides the signal-quality context in which that decision analysis operates.

## Working Notes

- **R2 sharpening (model-class inadequacy).** The argument: under C1 convention, $\delta_{\text{regret}}^{(1)} = A_O^{(1)} - V_O(\pi_{\text{current}})$ where both terms are computed under the current (now misspecified) $M_t$. Both terms bias in the same direction when the model class is structurally wrong; the gap stays small under common-mode bias. A clean version would compute the common-mode bias as a function of #mismatch-decomposition's model-error component, show it is $O(1)$ (not $O(\varepsilon)$) when the misspecification is directional, and derive a convention-dependent detection latency. Candidate one-evening spike.
- **R3 reference, not extension.** The L0→L1 structural-transition case is #identifiability-floor Instance 1 — on-policy detection is forbidden by Bareinboim CHT, not merely slow. The detection-latency theorem here is about within-class drift (R1), which does not hit that no-go. When the regime change *does* involve an L0→L1 transition, the theorem does not apply and the no-go does; the two coexist at different regime-change types.
- **Extension beyond Beta-Bernoulli.** Gaussian edges: $\eta \propto 1/(n+c)$ for the Gaussian-mean update. Exponential-family edges in natural-parameter form: $\eta$ follows sufficient-statistic accumulation. The *qualitative* form (detection time monotone in accumulated sufficient statistic) is general; the *quantitative* $1/(n+1)$ is specific to Beta-Bernoulli. A parametric version of the theorem covering general exponential-family edges would be a clean follow-up.
- **Probability bound.** The expected-time bound implies a probability bound via Markov: $\Pr[\text{detect within } T] \leq T / \mathbb E[T_{\text{detect}}]$. Tighter concentration requires specifying the residual distribution's shape; candidate one-paragraph extension.
- **Testable prediction.** In agents with controlled accumulated experience $n$, detection latency for regime change with fixed observable footprint $\varepsilon$ should scale linearly in $n$. Directly testable in multi-arm bandits with drifting reward distributions, in simulated organizations with commit-log-mediated task environments, in human-subjects studies on noisy-signal regime detection. Each would confirm or refute the $1/(n+1)$ scaling in its native setting.
- **Multi-timescale connection.** The theorem adds empirical content to #temporal-nesting: the slow (structural-adaptation) timescale slows with accumulated fast-timescale state — the two timescales are not independent. The fast one's accumulated state feeds back into the slow one's responsiveness. This is the formal version of the institutional-inertia observation and is adjacent to, but not subsumed by, #multi-timescale-stability's current formulation.
- **Section III analog.** Do larger teams / organizations face proportionally longer detection latency via analogous accumulation? Candidate: team effective detection latency is bounded below by the slowest member's latency (the weakest-dimension version of #per-dimension-persistence). Connects to #team-persistence. Not derived here.
- **Class 2 architectures.** For fully-merged agents (LLMs), the Beta-Bernoulli accumulator is absorbed into the single merged computation — there is no literal edge-credence accumulator. But there *is* an analog at pretraining: token-statistic accumulation. Do LLMs exhibit a myopia analog? This is in the domain of `03-logogenic-agents/`, potentially connecting to `#context-turnover` and the frozen-weights framing.
