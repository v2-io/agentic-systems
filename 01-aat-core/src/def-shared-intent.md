---
slug: def-shared-intent
type: definition
status: discussion-grade
depends:
  - def-unity-dimensions
  - form-information-bottleneck
  - form-objective-functional
stage: draft
---

# Definition: Shared Intent

When sub-agents within a composite must coordinate, they face a communication problem: transmitting the full purposeful state $G_t = (O_t, \Sigma_t)$ is expensive (high bandwidth, high latency), but acting without any shared purpose wastes coordination potential. The Information Bottleneck (`#form-information-bottleneck`) applied to inter-agent communication predicts an optimal compression: transmit enough of $G_t$ to align behavior, not more. The **shared intent** is the IB-optimal compression of the sender's purposeful state — the minimal sufficient statistic for predicting the jointly optimal coordination behavior. The trade-off parameter controls the regime: at high weight, the agent communicates more detail (approaching full model sharing); at low weight, communication is minimal (approaching independent action).

The IB compression *preferentially preserves* three things, in order: **terminal objectives** (what the agent is trying to achieve — compact, slow-changing), then **high-level strategy** (which approach, not which specific steps — moderate size, moderate change rate), and last **strategic details** (specific edge credences in the strategy DAG — large, change fast, low coordination value). This gives the framework a structural reading of **commander's intent** in military doctrine — the commander communicates *what* to achieve and *why*, not *how*. The framework predicts this pattern *structurally*, from the information-bottleneck trade-off, not as a managerial convention: communicating objectives gives a long shelf life per bit transmitted when objectives change slowly and strategies change fast.

For agents with bounded communication capacity (bandwidth-limited channels, finite context windows), the strategy DAG must be summarized for transmission — a 500-node DAG cannot be shared in full; the IB compression identifies which structural features matter for coordination. The same compression is useful for an agent preserving its own state across context boundaries (the language-model 100% context turnover problem) — store the compressed version of the purposeful state, not the full state. The status is honestly *discussion-grade*: the formulation makes several strong assumptions (the sender must know the jointly optimal action, which requires knowing other agents' states; the compression is lossless in the IB sense; the trade-off parameter is fixed rather than dynamically adjusted), and the qualitative prediction (communicate purpose before plans before models) is more robust than the specific IB formulation.

## Formal Expression

*[Definition (shared-intent)]*

Let $G_t^{\text{full}}$ be the source agent's complete purposeful state $(O_t, \Sigma_t)$. Let $G_t^{\text{shared}}$ be the compressed representation communicated to partners. The shared intent is the IB-optimal compression:

$$G_t^{\text{shared}} = \arg\min_{G_s} \left[ I(G_t^{\text{full}}; G_s) - \beta \cdot I(G_s; a_t^{\text{coordinated}}) \right]$$

where $a_t^{\text{coordinated}}$ is the jointly optimal action and $\beta$ controls the complexity-relevance tradeoff. At high $\beta$, the agent communicates more detail (approaching full model sharing). At low $\beta$, communication is minimal (approaching independent action).

The shared intent is the *minimal sufficient statistic* of the sender's purposeful state for predicting the jointly optimal coordination behavior.

## Epistemic Status

*Discussion-grade.* Max attainable: conditional (conditional on the IB framework being appropriate for inter-agent communication). The application of IB to inter-agent communication is structurally motivated — IB compresses optimally given a relevance criterion, and coordination relevance is the natural criterion — but the specific formulation assumes: (1) the sender knows the jointly optimal action (which requires knowing other agents' states), (2) the compression is lossless in the IB sense (real communication introduces noise, delay, and misinterpretation), (3) the $\beta$ parameter is fixed rather than dynamically adjusted. These are strong assumptions. The qualitative prediction (communicate purpose before plans before models) is more robust than the specific IB formulation.

## Discussion

**What gets compressed out.** The IB compression preferentially preserves:
1. Terminal objectives (what the agent is trying to achieve) — these are compact and change slowly
2. High-level strategy (which approach, not which specific steps) — moderate size, moderate change rate
3. Strategic details (specific edge credences in $\Sigma_t$) — large, change fast, low coordination value

**Connection to cognitive cost of $\Sigma_t$.** For agents with bounded communication capacity (bandwidth-limited channels, finite context windows), the DAG must be summarized for transmission. A 500-node strategy DAG cannot be shared in full; the IB compression identifies which structural features of the DAG matter for coordination.

**Organizational communication patterns.** Commander's intent in military doctrine is an empirical instantiation: the commander communicates *what* to achieve and *why*, not *how*. This is IB-optimal if objectives change slowly (low $\nu_O$) and strategies change fast (high $\nu_\Sigma$) — communicating objectives gives a long shelf life per bit transmitted.

## Working Notes
- The IB formulation assumes a single relevance variable ($a_t^{\text{coordinated}}$). In practice, coordination relevance is multi-dimensional: shared intent needs to support action coordination, conflict resolution, resource allocation, and adaptive replanning. A richer relevance variable might be needed.
- How does shared intent interact with 100% context turnover? An AI agent starting a new session needs to reconstruct $G_t^{\text{shared}}$ from persistent storage. The compression from full $G_t$ to shared intent is also useful for $M_t$ preservation ( #disc-m-preservation) — store the compressed version, not the full state.

### Incidental audit gold (lift 2026-05-31)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical / framing material, kept separate from the certified theory-fix findings (the IB-formalization findings F157–F161 from AUDIT-WORKING-526815 are routed for adjudication — see the off-ramp note at the end). **Coverage:** two dirs carry a dedicated reflection (526815, 849201) plus a forward-looking note from the batched 471203. Substrate attribution inferred from voice where not explicit.

#### 1. Candidate Brief prose / pre-prose

- The plain-language definitional payoff, twice converged: shared intent "formalizes what 'Commander's Intent' actually is — the minimal sufficient statistic of the leader's goals needed to predict coordinated action" (Claude, AUDIT-WORKING-849201); "defines the optimal *content* of inter-agent communication" (same). Candidate one-line Brief anchor.

#### 2. Candidate Discussion

- **Coordination does not require full plan transmission.** The clean restatement of the segment's core: "coordination does not require full plan transmission; it requires enough purpose and strategy information for partners to choose compatible actions" — the compression is over $G$ (purpose), not over the full model $M$ (Codex/Claude, AUDIT-WORKING-526815). A candidate sharpening of the "what gets compressed out" Discussion.
- **The honesty-about-its-own-limits is itself worth keeping visible.** Auditors praised the epistemic honesty that the formula "assumes the sender already knows the jointly optimal action $a_{\text{coord}}$ (which would require knowing the receiver's state, defeating the purpose of communication)" — so the math is "a conceptual bound, not a literal algorithm the agent runs" (Claude, AUDIT-WORKING-849201). The Epistemic Status already states this; flagged as a convergence signal that the framing lands.

#### 3. Follow-up items

- **Theory of mind / nested beliefs is missing from the communication vocabulary.** This segment and #hyp-communication-gain "handle inter-agent epistemic unity, but the recursive structure — 'I believe that you believe that I believe …' — is central to multi-agent reasoning (Aumann common knowledge, level-$k$ thinking) and isn't in the framework's vocabulary" (Claude, AUDIT-WORKING-471203, adversarial-creative-challenges "Missing 2"). A candidate scope-extension follow-up shared with #hyp-communication-gain.
- **Richer relevance variable.** The single relevance variable $a_t^{\text{coordinated}}$ is too narrow: real shared intent must support a policy/trajectory distribution, conflict resolution, resource allocation, and replanning — not just one jointly optimal action (Codex/Claude, AUDIT-WORKING-526815). The existing first Working Note already raises this; the auditor's framing names the four coordination sub-tasks explicitly.

#### 4. Readers often ask / wonder

- **How is shared intent actually *encoded* — a vector, a text prompt, a mathematical objective function?** A natural first reader question once the IB-optimal-compression definition lands (Claude, AUDIT-WORKING-849201). Candidate for a one-line concretization or a forward pointer to the implementation-side treatment.

#### 5. Candidate figures

- **Shared intent as a bottleneck.** A bottleneck between full purposeful state $G$ and coordinated behavior, with two emphases marked: the compression is over $G$ (not the full model $M$), and the relevance variable may need to be a policy/trajectory-level object rather than a single coordinated action (Codex/Claude, AUDIT-WORKING-526815).

#### Off-ramp (NOT gold — routed to certified-findings track)

- AUDIT-WORKING-526815 raised IB-formalization findings on this segment that are strengthen-first / scope-tightening candidates, flagged here only so they are not lost: **F157** — the IB optimization is written as $\arg\min$ over representations $G_s$, but standard IB optimizes over an encoder/channel $p(G_s \mid G_{\text{full}})$ (deterministic-encoder ambiguity, inherited from #form-information-bottleneck); **F158** — the relevance variable is too narrow (see follow-up above); **F159** — "high $\beta$ approaches full model sharing" should read "full *purposeful-state* sharing," since the source is $G_t^{\text{full}} = (O_t, \Sigma_t)$, not the epistemic model $M_t$; **F160** — "minimal sufficient statistic" is stronger than the displayed IB tradeoff (IB gives a complexity/relevance optimum for a chosen $\beta$; exact minimal sufficiency requires a separate sufficiency constraint or a limiting regime); **F161** (soft) — the "purpose before plans before models" ordering is plausible but not derived from the displayed objective without assumptions about entropy, change rate, shelf life, and relevance. *These are formalization tightenings, not no-gos; routed for adjudication on the strengthen-first track.*
