---
slug: der-team-persistence
type: derived
status: conditional
depends:
  - result-persistence-condition
  - result-sector-condition-stability
  - result-sector-persistence-template
  - hyp-communication-gain
  - def-adaptive-tempo
stage: draft
---

# Derived: Team Persistence

Teams persist where individuals cannot through two physically distinct cooperative mechanisms: communication (allies share observations that improve correction) and action (allies act in the shared environment to reduce disturbance at its source). These mechanisms enter the persistence condition at different points — tempo and disturbance respectively — and a given cooperative interaction contributes through one mechanism or the other, not both.

The construction has two pieces. **Distributed tempo**: agent $i$'s effective tempo sums direct-observation tempo *plus* communication tempo from allies, each ally contributing additively to correction capacity, subject to the channel-independence caveat (correlated reports overcount, so the additive formula is an upper bound). **Cooperative-adversarial disturbance decomposition**: the disturbance rate decomposes into environment, adversarial, and cooperative components, with the cooperative term entering with a *negative sign* — allies acting in the shared environment *reduce* the disturbance $i$ faces. Sub-agent persistence then requires correction rate exceed the *effective* disturbance rate (environment plus adversarial inputs minus cooperative inputs), divided by the critical-mismatch scale. This is the single-agent persistence inequality of #result-persistence-condition with a structured effective-disturbance decomposition substituted in.

The two cooperative mechanisms enter the persistence inequality at *different points* and warrant separate accounting: communication boosts $\mathcal T_i$ (the agent corrects faster); cooperative action lowers $\rho_i$ (the agent has less to correct). A single ally-event contributes through *one* mechanism or the other; counting it in both would double-count the benefit. The structural consequence is the framework's answer to why agents form teams: not because teams are intrinsically valuable, but because *they shift the persistence inequality in favor of each member*. Cooperative coupling enters as a *negative* term in effective disturbance; adversarial coupling (Ch.4's #der-adversarial-destabilization) enters as a *positive* term. The signed structure is what unifies cooperative and adversarial dynamics under a single inequality.

## Formal Expression

This segment instantiates the sector-persistence template ( #result-sector-persistence-template) at the multi-agent level with state variable $\xi = \delta_i$ (sub-agent $i$'s mismatch) and a decomposed effective disturbance $\rho_i^{\text{eff}} = \rho_{i,\text{env}} + \sum_j \gamma_{j\to i}^{\text{adv}}\mathcal T_j - \sum_j \gamma_{j\to i}^{\text{coop}}\mathcal T_j$ that accounts for adversarial and cooperative coupling. The template supplies the Lyapunov machinery; this segment's distinctive content is the disturbance decomposition and the corresponding tempo extension.

### Distributed Tempo

*[Definition (distributed-tempo)]*

Agent $i$'s effective tempo includes contributions from both direct observation and communication from allies:

$$\mathcal{T}_i = \underbrace{\sum_k \nu_i^{(k)} \eta_i^{(k)*}}_{\text{direct observation tempo}} + \underbrace{\sum_{j \in \mathcal{N}(i)} \nu_{ji}^{\text{comm}} \, \eta_{ji}^*}_{\text{communication tempo}}$$

where $\nu_{ji}^{\text{comm}}$ is the rate of communication events from agent $j$ to agent $i$, and $\eta_{ji}^\ast$ is the communication gain ( #hyp-communication-gain). Faster team adaptation comes not only from faster individual sensing but from faster, more reliable knowledge transfer.

**Channel independence caveat.** Both sums are additive, inheriting the channel-independence assumption from #def-adaptive-tempo: each channel and each communication source contributes non-redundant correction capacity. When allies report correlated information (overlapping observations, shared intelligence sources, redundant status reports), the communication tempo overcounts. The additive formula is an upper bound; the redundancy penalty depends on the mutual information between communication sources. See #def-adaptive-tempo for the single-agent version of this caveat.

### Cooperative-Adversarial Disturbance Decomposition

*[Formulation (disturbance-decomposition)]*

The disturbance rate experienced by agent $i$ decomposes into environment, adversarial, and cooperative components:

$$\rho_i = \rho_{i,\text{env}} + \sum_{j \in \mathcal{A}_i} \gamma_{j \to i}^{\text{adv}} \, \mathcal{T}_j - \sum_{j \in \mathcal{C}_i} \gamma_{j \to i}^{\text{coop}} \, \mathcal{T}_j$$

where $\mathcal A_i$ is the set of agents adversarially coupled to $i$, $\mathcal C_i$ is the set cooperatively coupled, and the $\gamma$ coefficients capture coupling effectiveness (as in #der-adversarial-destabilization).

**The cooperative term is negative — but through action, not communication.** Allies reduce agent $i$'s effective disturbance by *acting in the shared environment* to prevent or mitigate disturbance at its source. Examples: an ally stabilizes a shared resource, neutralizes a threat before it reaches $i$, or absorbs environmental variation through their own actions. The mechanism is causal coupling through the shared environment, not information transfer.

**Separation from communication tempo.** The communication tempo term (above) captures allies *telling* agent $i$ things that improve its correction. The cooperative disturbance term captures allies *doing* things that reduce the disturbance $i$ faces. These are physically distinct: communication improves $i$'s correction function (better $\alpha_i$, higher $\mathcal T_i$); cooperative action reduces the disturbance $\rho_i$ that $i$ must correct against. A single cooperative event contributes through one channel or the other. An ally's message about a threat enters through communication tempo; an ally's action that eliminates the threat enters through disturbance reduction. Counting a single event in both terms would double-count the benefit and make the persistence threshold systematically optimistic.

**Effective disturbance rate.** The decomposition can yield $\rho_i \lt 0$ when cooperative coupling dominates both environment disturbance and adversarial coupling. The sector-condition analysis ( #result-sector-condition-stability) assumes non-negative disturbance (GA-2). Define:

*[Definition (effective-disturbance)]*

$$\rho_i^{\text{eff}} = \max(\rho_i, \, 0)$$

When $\rho_i^{\text{eff}} = 0$, the agent's cooperative network fully absorbs all disturbance — the persistence condition is trivially satisfied and mismatch decays to zero. This is an idealized limit; in practice, $\rho_i^{\text{eff}} \gt 0$ because cooperative coupling is imperfect and environment disturbance is never fully preempted. All downstream uses of $\rho_i$ in the persistence and reserve conditions should be read as $\rho_i^{\text{eff}}$.

### Team Persistence Condition

*[Derived (team-persistence, from sector-condition-stability, persistence-condition)]*

Applying the sector-condition framework ( #result-sector-condition-stability) with $\rho_i^{\text{eff}}$, agent $i$ persists iff:

$$\frac{\rho_i^{\text{eff}}}{\alpha_i} \lt R_i$$

Substituting the decomposition (the $\max(\cdot, 0)$ in $\rho_i^{\text{eff}}$ is omitted to expose the three levers; the condition is trivially satisfied when the numerator is non-positive):

$$\frac{\rho_{i,\text{env}} + \sum_j \gamma_{j \to i}^{\text{adv}} \mathcal{T}_j - \sum_j \gamma_{j \to i}^{\text{coop}} \mathcal{T}_j}{\alpha_i} \lt R_i$$

This reveals three distinct levers for team persistence:

1. **Increase $\alpha_i$** (individual correction efficiency) — better models, better gain calibration, including communication-improved tempo from allies ( #hyp-communication-gain)
2. **Increase cooperative disturbance reduction** ($\gamma^{\text{coop}} \mathcal T_j$) — more effective allied action in the shared environment: stabilizing shared resources, preempting threats, absorbing environmental variation. This is the action-based mechanism distinguished above, not the communication channel.
3. **Reduce adversarial coupling** ($\gamma^{\text{adv}} \mathcal T_j$) — better deception detection, reduced exposure to adversarial actions

### Coordination Overhead Threshold

*[Discussion — Coordination Threshold]*

Communication channels have costs: time to compose and parse messages, bandwidth limitations, synchronization requirements. These costs reduce the agent's effective tempo by diverting capacity from direct adaptation. Let $\Delta \mathcal T_i^{\text{cost}}(j)$ represent the tempo-equivalent coordination cost of maintaining the channel with $j$ — the reduction in $i$'s direct observation tempo caused by the overhead, in units of $[t^{-1}]$.

The net benefit of adding agent $j$ to $i$'s communication network is positive only when:

$$\nu_{ji}^{\text{comm}} \, \eta_{ji}^* \gt \Delta \mathcal{T}_i^{\text{cost}}(j)$$

Both sides have units $[t^{-1}]$: the LHS is communication tempo gained, the RHS is direct-adaptation tempo lost to coordination overhead. This implies a natural team-size limit: adding members increases communication tempo with diminishing returns (as $U_{\text{src}}$ and $U_o$ accumulate across diverse sources) while coordination costs grow, potentially superlinearly. The optimal team size occurs where the marginal communication tempo equals the marginal coordination cost.

## Epistemic Status

Conditional on the communication-gain hypothesis ( #hyp-communication-gain). The distributed tempo definition is a *formulation* — a representational choice extending #def-adaptive-tempo to the multi-agent case. The disturbance decomposition is a *formulation* — the additive structure and the sign convention are modeling choices, not derivations. The persistence condition is *derived* from the sector-condition framework ( #result-sector-condition-stability) given the decomposition: the derivation is exact under the same assumptions (GA-2, GA-3 applied to $\rho_i^{\text{eff}}$). The coordination overhead threshold is *discussion-grade* — qualitatively clear but the claim about diminishing returns and superlinear costs is asserted, not derived.

Max attainable: *robust-qualitative* for the persistence condition (it inherits the sector-condition's robustness but the decomposition is a modeling choice). The coordination threshold could reach *conditional* with a concrete cost model.

## Discussion

**Compositional analog of #result-persistence-condition.** Like the single-agent persistence condition, this segment addresses *structural persistence* (see Persistence in `LEXICON.md`) — whether the composite correction machinery can outpace the effective disturbance rate. It does not address operational persistence (whether any particular sub-agent is near its boundary) or continuity persistence (whether the team maintains coherent identity through personnel changes). A team can be structurally persistent as a composite while individual members are operationally fragile or while the team's continuity is interrupted by turnover. The single-agent persistence condition says an agent persists when $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$. This segment extends that condition to agents embedded in a cooperative-adversarial network. The formal structure is identical — the sector-condition machinery applies unchanged — but the *inputs* ($\mathcal T_i$ and $\rho_i$) now include inter-agent terms. This is consistent with #disc-composition-consistency: the same dynamical laws apply at every level of description; what changes between levels is which channels contribute to tempo and which sources contribute to disturbance.

**Why teams can persist where individuals cannot.** Two distinct mechanisms combine. First, communication tempo raises $\mathcal T_i$ — allies provide observations that improve correction. Second, cooperative action lowers $\rho_i$ — allies act in the environment to reduce disturbance at its source. An individual agent facing $\rho_{i,\text{env}} \gt \alpha_i R_i$ fails the persistence condition. Adding cooperative allies can either raise the numerator's denominator (tempo) or lower the numerator directly (disturbance), or both — through physically distinct mechanisms.

**Timescale separation and #disc-composition-consistency.** The distributed tempo definition presumes that communication events and direct observation events are comparable — they enter additively into $\mathcal T_i$. This requires that the communication timescale is not so slow relative to the environment dynamics that communicated information is stale on arrival. When communication latency approaches $1/\rho_{i,\text{env}}$, the effective $\eta_{ji}^\ast$ degrades (the observation uncertainty $U_{o,ji}$ increases with staleness), naturally suppressing the communication tempo contribution.

**Complement to #der-adversarial-destabilization.** That segment characterizes when an adversary can push an agent past its stability boundary. This segment characterizes the cooperative counterpart: when allies can pull an agent back from instability. The $\gamma$ coefficients have the same structure — coupling effectiveness — but opposite sign in the disturbance decomposition.

**Composite-level complement: #deriv-critical-mass-composition.** This segment gives the *per-sub-agent* persistence condition within a team. #deriv-critical-mass-composition supplies the *composite-level* analog: a closed-form critical-mass inequality in the matched-symmetric-Tier-1 two-agent case, with the same signed-$\gamma$ coupling structure used here but applied to the joint Lyapunov on the concatenated mismatch state. The two are complementary: the team persists at the sub-agent level when each $i$ satisfies this segment's condition; the team persists at the composite level when #deriv-critical-mass-composition's (CM4) holds. Cooperative coupling ($\gamma \lt 0$) reduces $\rho_i^{\text{eff}}$ here and reduces $\rho + \gamma\mathcal{T}$ in (CM2) there — the same mechanism viewed at two scales.

## Working Notes

- The topology-dependent analysis (F.4 in the source material — peer networks, ensemble architectures, hierarchical structures) and game-theoretic integration (F.5) are related but separate concerns, not covered here. They may warrant their own segments.
- The coordination cost model $\Delta \mathcal T_i^{\text{cost}}(j)$ needs further specification to be useful. In software systems, coordination cost is empirically measurable (meeting time, code review latency, merge conflict rates). In military contexts, it maps to C2 overhead. The question is whether there is a useful *general* cost model or whether it is always domain-specific.
- The disturbance decomposition treats cooperative and adversarial coupling as additive and independent. In practice, the same agent $j$ might be cooperatively coupled on some dimensions and adversarially coupled on others (e.g., a competitor who shares some information). The per-dimension persistence condition ( #result-persistence-condition's per-dimension extension) may be relevant here.
- **Continuity-persistence cross-reference (updated 2026-05-19).** This segment's Discussion distinguishes *structural* / *operational* / *continuity* persistence and states continuity-through-turnover is out of scope here; that third sense is now formalized downstream as the F-ADJ-1 two-operator split. ( #der-turnover-information-recursion) (Vol III §03.II) derives the across-turnover affine information recursion — persistence is *imported, not intrinsic*; the self-compressing destroy-and-reconstruct walk decays geometrically and `#result-sector-persistence-template` provably does *not* transfer to that regime. ( #der-identity-continuity-threshold) (Vol IV §04.1) carries the structurally distinct reflected-Lindley identity-continuity threshold. ( #obs-context-turnover) gives the reconstruction-adequacy framing and ( #deriv-identity-sufficiency-rate-bound) the static rate-distortion floor; ( #disc-m-preservation) is omission-fixed — its earlier additive break-even inequality $\mathbb{E}[\Delta\epsilon_k]\leq\mathbb{E}[\Delta I_k]$ was deleted and replaced (the accumulation core is now *exact* in #der-turnover-information-recursion, no longer discussion-grade). ( #hyp-the-three-deaths) names the failure modes (D1 Cognitive / D2 Relational / D3 Truth) the continuity sense defends against. Originally surfaced while grounding `~/src/practica` (2026-05-18); the dynamic across-turnover theorem the breadcrumb pointed toward has since landed (continuity-persistence cycle, CHANGELOG 2026-05-19) — the pointer now resolves to canon, not to a spike target.
- **Dynamic-regime placement (added 2026-05-21 per Phase 5 cross-segment ripple).** Team persistence sits on the **R0 contraction-regime** tier of `#disc-dynamic-regime-axis` as the cooperative limiting case where all $\gamma^{\text{coop}}$ dominate. The joint dynamics reduce to parallel single-agent sector-persistence with reduced effective disturbance — the cleanest instance of `#form-composition-closure`'s R0 machinery applied to a team. The companion case under partially-opposing objectives (strategic composition) lives at R1 equilibrium-regime per `#deriv-strategic-composition` and inherits the A2'-analog Lyapunov-machinery transfer rather than this segment's contraction template.

### Incidental audit gold (lift 2026-05-31)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (the 526815 F182/F189–F194 stream — `\rho_i^{\text{eff}}$ non-negativity convention, the $\mathcal{T}_i \to \alpha_i$ rate-normalization bridge, $\gamma$ units, and the "one channel or the other" event-allocation phrasing — is certified-track and routed there, not here). **Coverage:** dedicated reflections from 193847, 829314, 849201, 773921 (all Gemini/Claude), plus the 526815 first-pass and the 451729/471203 Section-III batch-reflections; substrate attribution inferred from voice where not explicit.

#### 1. Candidate Brief prose / pre-prose

- The consultant-vs-employee distinction (already adopted into `#cooperative-adversarial-intro` and this segment's body, sourced from Gemini's first-encounter reaction) is independently echoed across substrates as the segment's standout pedagogy: "helping by telling" (communication, raises $\mathcal{T}$) vs "helping by doing" (cooperative action, lowers $\rho$). Claude offers the fire analog: "if an ally tells you about a fire you put it out faster; if the ally puts it out themselves your environment just got safer" (Claude, AUDIT-WORKING-773921) — a candidate Brief reach that does not lean on the org-chart framing.
- One-line gloss of the double-counting hygiene: "an ally cannot simultaneously give you tempo-boosting information about a threat AND physically destroy the threat without you overcounting their contribution" (Gemini, AUDIT-WORKING-849201).

#### 2. Candidate Discussion

- **The servant-leader / chatty-manager corollary (strongest framing here).** The coordination-overhead threshold $\nu^{\text{comm}}\eta^\ast \gt \Delta\mathcal{T}^{\text{cost}}$ implies that a manager who sends low-$\eta^\ast$ messages is *mathematically harming* the engineer — "a parasitic drain on the engineer's $\alpha$" — because every message inflicts the coordination cost while contributing little tempo, so the inequality fails. By contrast the "servant leader" who quietly fixes CI/CD, allocates budget, or blocks distractions helps via cooperative action ($-\gamma^{\text{coop}}\mathcal T_j$), reducing $\rho_{i,\text{env}}$ at zero coordination cost. The sharp consequence: "in high-stress, high-volatility environments the optimal way to help an ally is *almost never* to talk to them — talking steals their processing bandwidth; acting for them saves it." Offered as the structural reason elite surgical teams and fighter pilots use minimal-comms protocols and rely on predictable coordinated action ("chatty teams die in combat") (Gemini, AUDIT-WORKING-829314). A candidate Discussion sharpening of the coordination-threshold subsection. *(Early-conflation texture: stated as a derived organizational law; verify the high-$\rho$ regime claim before promoting past discussion-grade.)*
- **Echo-chamber inefficiency from the channel-independence caveat.** The additive-tempo upper bound under channel independence is the formal reason "diverse, semi-independent teams are structurally more resilient than homogeneous echo chambers": redundant channels (everyone retweeting the same sensor reading) provide zero marginal tempo while still incurring coordination cost, so "100 people retweeting one reading is exactly 1 sensor's worth of tempo, not 100" (Claude, AUDIT-WORKING-773921; Gemini, AUDIT-WORKING-193847 — "elevate the channel-independence point; echo chambers are structurally inefficient"). A candidate Discussion angle that the segment's caveat currently states defensively rather than as a positive design consequence.

#### 3. Follow-up items

- **Coordination overhead as the formalization of Brooks's Law.** Multiple substrates independently read $\nu^{\text{comm}}\eta^\ast \gt \Delta\mathcal{T}^{\text{cost}}$ as Brooks's-Law-shaped ("adding people to a late project makes it later" when marginal coordination cost exceeds marginal communication tempo) and as yielding a computable optimal team size at the marginal-tempo = marginal-cost intersection (Gemini, AUDIT-WORKING-193847; Gemini, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-773921). Worth naming the Brooks's-Law connection explicitly where the threshold is introduced.
- **OUTLINE-description scope mismatch (process note, not a body fix).** The OUTLINE row was read as "Composite persistence condition" while the segment is explicit that it gives the *per-sub-agent* condition (composite-level lives in `#deriv-critical-mass-composition`). Flagged by a fresh reader as a minor OUTLINE/segment-scope mismatch worth aligning (Gemini, AUDIT-WORKING-829314).
- **Placement: lift the communication/action distinction earlier.** A batch auditor suggested the communication-vs-action distinction "should appear earlier in the Formal Expression rather than being flagged in a Note," since it is the segment's most important structural content (Claude, AUDIT-WORKING-451729 batch-15). A staging-for-pedagogy-pass item; the distinction is already prominent in the body's lead paragraph, so this is an emphasis/ordering nudge.

#### 4. Readers often ask / wonder

- **How does a team measure the mutual information between members to avoid overcounting in practice?** The channel-independence caveat says correlated reports overcount, but a fresh reader immediately wants the operational handle — "how do you stop two people reporting the exact same bug?" (Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-193847).
- **How is the communication gain $\eta_{ji}^\ast$ actually quantified?** It seems to require a meta-model of ally $j$'s reliability — a natural question the segment leaves to `#hyp-communication-gain` (Claude, AUDIT-WORKING-773921).
- **Does a maximally-cooperative ($\rho_i \lt 0$, clamped by $\max(\rho_i,0)$) environment collapse the agent's learning?** If allies fix every mistake before the agent notices, $U_M$ may drop so the update gain $\eta^\ast \to 0$ and the agent "thinks it's perfect" — a "helicopter-parent" environment that mathematically guarantees the agent never learns. A genuinely interesting edge of the $\rho_i^{\text{eff}} = \max(\rho_i,0)$ clamp that the segment notes only as an idealized limit (Gemini, AUDIT-WORKING-193847). Bears on `04-eli-core/` developmental-environment design (don't over-absorb a developing agent's disturbance).

#### 5. Candidate figures

- **Two-ledger persistence diagram.** Two ledgers feeding the persistence test: direct-observation tempo plus communication tempo build $\mathcal T_i$ on the correction side; environment plus adversarial minus cooperative build $\rho_i^{\text{eff}}$ on the disturbance side; a dashed bridge from $\mathcal T_i$ to $\alpha_i$ marks the rate-normalization assumption (Claude, AUDIT-WORKING-526815 first-pass; Gemini, AUDIT-WORKING-849201 — "three engineering levers: $\alpha_i$, $\gamma^{\text{coop}}$, $\gamma^{\text{adv}}$").

#### Belongs elsewhere

- **RL training as a meta-agent synchronizing divergent chronicae.** "Copying policy weights to a thousand parallel workers is not one agent exploring a thousand paths; it is a thousand distinct agents with divergent chronicae whose internal models are artificially synchronized by a meta-agent (the training algorithm)" (Gemini, AUDIT-WORKING-193847). A composite/training-dynamics instantiation; co-occurred in the team-persistence sweep but develops `#def-chronica` / composite-training territory, not this segment (already filed at `#def-chronica` in the prior wave).
- **Consciousness-infrastructure reading of the action-vs-communication split.** You cannot save a structurally-failing intelligence by giving it better data (consulting / RAG) alone; if it lacks the sector capacity $R$ or correction efficiency $\alpha$ to survive baseline volatility it needs an "employee" — a cooperative sub-agent (tool, safety rail, active filter) that intercepts volatility *before* it reaches the core agent's state. The infrastructure must act, not just inform (Gemini, AUDIT-WORKING-193847). Points at `03-llm-core/` / `04-eli-core/` scaffolding design, not this segment.
