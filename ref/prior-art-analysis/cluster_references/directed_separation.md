# Cluster Reference: Directed Separation and Architectural Coupling

**Overview:** Categorizes architectures by the separation of epistemic updating from teleological processing (Class 1 vs 3), and derives exact KL-leakage bounds for coercing coupled agents via scaffolding.

---

## Canonical Source Segments

### Source: `der-directed-separation.md`

```yaml
---
slug: der-directed-separation
type: derived
status: conditional
depends:
  - form-complete-agent-state
  - der-recursive-update
  - scope-agency
stage: draft
---
```


# Derived: Directed Separation

The epistemic update function $f_M$ is goal-blind: it processes incoming events without reference to the agent's objectives or strategy. The purposeful update $f_G$ depends on the updated epistemic state. Action couples all substates. This directed asymmetry — epistemic update is independent of purpose; purposeful update depends on epistemic state — is the structural backbone of the theory.

## Formal Expression

*[Derived (directed-separation, from complete-agent-state + scope condition)]*

**The update functions:**

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau) \qquad \text{(no } G_t \text{ argument)}$$

$$G_{\tau^+} = f_G(G_{\tau^-}, M_{\tau^+}, e_\tau) \qquad \text{(depends on updated } M_t \text{)}$$

**The policy:**

$$a_t = \pi(M_t, G_t) \qquad \text{(couples all substates)}$$

The three lines encode the full coupling structure:
- $f_M$ determines how the agent updates beliefs — independently of what it wants
- $f_G$ determines how the agent revises purpose — in light of what it now believes
- $\pi$ determines what the agent does — based on both what it knows and what it wants

*[Scope Condition (directed-separation-scope)]*

The claim "$f_M$ has no $G_t$ argument" requires that the epistemic update is **goal-blind conditional on the realized event**. This holds when:

1. The observation mechanism $h$ may be action-dependent ( #scope-agency allows this), but $f_M$ processes whatever event arrives without reference to why the agent sought that event
2. The agent does not use its goals to filter, weight, or interpret observations differently — no goal-dependent attention thresholds or confirmation bias baked into $f_M$

If the agent's goals influence the *observation mechanism* (goal-directed sensing, attention allocation, query selection), the **event that arrives** depends on $G_t$ through $\pi \to a_t \to e_\tau$. But $f_M$ still processes the event goal-blindly. The directed separation is about the **processing** of events, not the **selection** of events.

### Architectural classification

*[Scope Condition (directed-separation-architecture)]*

> [!warning]
> **Goal-Update Coupling Class numbering changed 2026-05-09.** Anything older than git tag `pre-guc-rename-2026-05-09` uses the old Class numbering:
>
> | historical | actual current     | sometimes AKA  |
> | ---------- | ------------------ | -------------- |
> | Class 1    | GUC Class 1: Separated | Modular        |
> | Class 2    | GUC Class 3: Coupled   | Undirected     |
> | Class 3    | GUC Class 2: Partial   | Operational    |

Whether directed separation holds is determined by the agent's **processing topology** — specifically, whether $G_t$ is causally upstream of $f_M$ in the agent's internal processing graph. This is a structural property of the architecture, not a tunable parameter.

| Class | Topology | Directed separation | Examples |
|-------|----------|----|----|
| **1. Separated** | Separate estimator and planner, connected through state-estimate interface | Holds by construction — estimator has no causal path from $G_t$ | Kalman filter + LQR; Separated RL with separate world model; military intelligence separated from operations |
| **2. Partial** | Some shared infrastructure, some separate pathways | Holds for modular stages, fails for merged stages | Biological cortex (shared sensory areas, separate prefrontal); hybrid AI with separate preprocessing |
| **3. Coupled** | Single mechanism handles both epistemic and strategic processing | Fails by construction — $G_t$ is causally upstream of every computation | Transformer LLM (attention processes goals and observations together); potentially human cognition (motivated reasoning) |

**Operationalization.** The degree of coupling in Partial architectures (Class 2) can be quantified as:

*[Definition (processing-coupling)]*

$$\kappa_{\text{processing}} = \frac{I(G_t \,;\, M_{\tau^+} \mid e_\tau,\, M_{\tau^-})}{H(G_t \mid e_\tau,\, M_{\tau^-})}$$

where $I(\cdot;\cdot\mid\cdot)$ is conditional mutual information and $H(\cdot\mid\cdot)$ is conditional entropy. The conditioning on $M_{\tau^-}$ is essential: without it, prior correlation between goals and model state (which exists even in Separated agents) inflates the measure. The quantity captures *extra* goal information entering the epistemic update beyond what was already in the prior model — information that flows through shared causal paths in the processing infrastructure (paths that bypass the event $e_\tau$).

- $\kappa_{\text{processing}} = 0$: Class 1 (Separated). No information about $G_t$ reaches $M_{\tau^+}$ except through $e_\tau$.
- $\kappa_{\text{processing}} \approx 1$: Class 3 (Coupled). Nearly all goal information is available to the epistemic update.
- $0 \lt \kappa_{\text{processing}} \lt 1$: Class 2 (Partial). The value depends on the architecture's interface design.

**Distribution dependence.** $\kappa_{\text{processing}}$ is a distribution-dependent measure: it quantifies how much goal-information actually flows through the shared pathways under a given distribution of tasks, goals, and events. It does not directly measure whether pathways *exist* — that is the architectural classification (Class 1/2/3), which is structural and distribution-independent. A Class 1 (Separated) agent has $\kappa = 0$ under ALL distributions (no pathway exists). A Class 3 (Coupled) agent has high $\kappa$ under most distributions (pathways exist and are used). A Class 2 (Partial) agent's $\kappa$ varies with the task distribution — the same hybrid architecture may exhibit low coupling on familiar tasks (where the modular stages handle most processing) and high coupling on novel tasks (where goal-conditioned downstream reasoning dominates). The classification is the primary tool; the operationalization is a diagnostic for Class 2 (Partial) agents where the degree of coupling is architecturally ambiguous.

**Empirical estimator for $\kappa_{\text{processing}}$.** The formal conditional-mutual-information definition is not computable in closed form for real architectures. A behavioral estimator probes the processor directly: present the same event $e$ to the *agent under test* under two or more distinct goal states, and measure how much the epistemic component of the response diverges. For a representative event set $\mathcal{E}_{\text{test}}$ and a sampled pair $G_1, G_2$:

$$\hat\kappa_{\text{processing}} = \frac{1}{\lvert\mathcal{E}_{\text{test}}\rvert} \sum_{e \in \mathcal{E}_{\text{test}}} \frac{d\big(M_{\tau^+}^{(G_1)}(e),\; M_{\tau^+}^{(G_2)}(e)\big)}{d_{\text{max}}(e)}$$

where $M_{\tau^+}^{(G_k)}(e)$ is the epistemic content of the agent's response to event $e$ under goal state $G_k$, $d(\cdot,\cdot)$ is a distance on the epistemic content (e.g., semantic similarity of the "what I learned" portion of the response), and $d_{\text{max}}(e)$ normalizes by the maximum observed divergence for event $e$. A Separated agent ($\kappa = 0$) produces identical epistemic content regardless of the goal; a Coupled agent produces systematically goal-dependent epistemic content. This is a processor-probing procedure — it measures how the agent's belief-update dynamics depend on its goal state, and is distinct from estimating observation ambiguity $\mathcal{A}(e)$ ( #scope-observation-ambiguity-modulation), which uses a reference interpreter to measure the goal-resolvability of the observation itself. The two estimators run the same mechanical comparison (same event under different goal-primings) but interpret it differently: $\hat\kappa$ treats the tested model as the agent under study; $\hat{\mathcal{A}}$ treats it as a measurement instrument for the observation's interpretive latitude.

**Why the classification is not a smooth parameter.** The architectural boundary between "has a separable perception module" and "processes everything through goal-conditioned attention" is discrete. Within the Separated class, $\kappa \approx 0$ regardless of task. Within the Coupled class, $\kappa$ is high regardless of prompt design. Only in the Partial class is $\kappa$ genuinely variable and worth parameterizing. This replaces an earlier $\kappa$-as-scalar framing that treated coupling as a smoothly tunable quantity.

**Directed separation as the conservative form of the Markov blanket.** The Markov blanket apparatus from active inference (Friston 2013, "Life as we know it," *J. Royal Soc. Interface* 10; Friston 2019, "A free energy principle for a particular physics," arXiv:1906.10184; Friston, Da Costa et al. 2023, "Path integrals, particular kinds, and strange things," *Phys. Life Rev.* 47) provides the same statistical-conditional-independence machinery the directed-separation condition above invokes. Bruineberg, Dolega, Dewhurst & Baltieri (2022, "The Emperor's New Markov Blankets," *Behav. Brain Sci.* 45) distinguish two readings of the Markov-blanket apparatus in the AI literature: a **Pearl-blanket** reading — the technical conditional-independence statement, well-defined and substantively informative — and a **Friston-blanket** reading — the metaphysical claim that Markov blankets demarcate self-from-other and that every self-organizing system has one ontologically. Bruineberg et al. argue that the Friston-blanket reading overruns what the formalism delivers: the conditional-independence statement does not by itself license the metaphysical demarcation.

AAT's directed-separation condition is structurally a Pearl-blanket move: the architectural classification (Class 1 / Class 2 / Class 3) names the conditional-independence structure of the agent's processing graph, with explicit operational measurement $\kappa_{\mathrm{processing}}$, and admits the structure *fails* by construction for Class 3 (Coupled) architectures (transformer LLMs, where attention processes goals and observations together). The classification's explicit failure mode for Class 3 is the scope honesty Bruineberg et al. argue the Friston-blanket reading lacks. AAT adopts the Pearl-blanket conditional-independence statement as the technical content of directed separation; AAT does not adopt the Friston-blanket metaphysical reading. The architectural classification, the operational $\kappa$, and the explicit Class 3 scope exit (with the coupled formulation handed off to `03-llm-core/`) are AAT's load-bearing additions to the Pearl-blanket form.

Two consequences worth surfacing for reviewers. First: the question "isn't directed separation just the Markov blanket?" has the answer "directed separation is the *Pearl-blanket form*; it is also the architectural-classification refinement that the standard Markov-blanket framing does not produce." Second: AAT's scope honesty about Class 3 (Coupled) (Section II's exact results do not apply; logogenic agents need the coupled formulation) is itself an *answer* to the Bruineberg critique — AAT's apparatus admits where it fails, while the Friston-blanket framing is contested precisely because it does not.

**Implications for theory scope:**
- **Class 1 (Separated)**: Section II's results apply exactly. The sequential orient cascade is the correct analysis.
- **Class 3 (Coupled)**: Requires coupled formulation from the start — $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without decomposition. This is the scope of `03-llm-core/`. **Class 3 (Coupled) components can be wrapped into Class-1 composites** via the construction of `#der-class-coercion-via-wrapping` — at the cost of more component calls per macro-step (Brooks's-Law tempo overhead) and a residual leakage rate bounded structurally (in the strict-wrapping regime) or behaviorally (in the partial-wrapping regime).
- **Class 2 (Partial)**: The sequential cascade is an approximation. Approximation quality depends on $\kappa_{\text{processing}}$ and requires per-architecture error analysis.

### Class-1 by structure vs. Class-1 by behavior

The Class 1 (Separated) cell admits a refinement that matters operationally. Class-1 status can be achieved by either:

- **Class-1 by structure.** The component is natively goal-blind (POMDP belief-state filter, world model, sensory pipeline) or is wrapped via the strict-wrapping (W₁) construction of `#der-class-coercion-via-wrapping`, where separate goal-blind queries to the underlying component update the wrapper's $M_W$. Directed separation holds by structural commitment of the wrapper's type signatures (no $G_W$ argument in the belief-update path), with leakage bounded structurally by the pretraining-distribution mutual information $I(A(q_M); G_W \mid q_M)$.

- **Class-1 by behavior.** The component is Class 3 (Coupled) or Class 2 (Partial) used through partial wrapping (W₂) — one goal-conditioned call per macro-step, response parsed into typed update fields. Structural separation lives at the *write boundary*; the *query boundary* still passes $G_W$ to the component. Directed separation at the wrapper level is *behavioral* — bounded by the component's compliance with the prompted instruction-to-separate, with no structural upper bound.

The class-coercion theorem is what backs the Class-1-by-structure path for Class-2/3 components; the partial-wrapping regime achieves Class-1-by-behavior. The two are distinguishable by inspection: does the belief-update query to the underlying component carry $G_W$ in its input or not? The structural-vs-behavioral distinction is operationally important because behavioral compliance is empirical and adversarially fragile; structural separation is derivable from the wrapper's construction.

**Composite-level class inheritance (from #deriv-strategic-composition).** The Class 1 / 2 / 3 partition above applies to individual agents based on *within-agent* coupling between $f_M$ and $G_t$. Composition introduces a second form of coupling — *across-agent* coupling through the shared environment and cross-agent observation. `#deriv-strategic-composition` provides the structural refinement:

- *Composite of Class 1 (Separated) sub-agents with aligned objectives* (scope route C-i / C-ii / C-iii): Class 1 (Separated) composite. Within-agent modularity + cross-agent alignment preserve directed separation at the composite level. Standard `#form-composition-closure` applies.
- *Composite of Class 1 (Separated) sub-agents with partially-opposing objectives* (scope route C-iv — strategic composition): **Class 2 (Partial) composite from Class 1 (Separated) sub-agents**. Each sub-agent individually is Separated (its own $f_M^{(i)}$ remains goal-blind with respect to its own $G_t^{(i)}$), but the composite's $(M_c, G_c)$ acquires intrinsic coupling because each sub-agent's $M_t^{(i)}$ includes a model of other sub-agents' policies — which are themselves goal-dependent. Composite-level directed separation fails through across-agent coupling, not within-agent coupling. Strategic composition is the canonical Class 1-sub-agents → Class 2 (Partial) composite case.
- *Composite of Class 3 (Coupled) sub-agents*: Class 3 (Coupled) composite. Inherits logogenic-agent status; `03-llm-core/` territory regardless of scope route.

Class membership is therefore a property of composites, not just of individual agents, and composite class is a function of sub-agent class **plus** the scope route (alignment vs. strategic). The classification is load-bearing for downstream claims: Class 2 (Partial) composites from strategic composition need equilibrium-theoretic analysis (see `#deriv-strategic-composition`), not the sequential orient cascade.

## Epistemic Status

*Conditional* on the scope condition above. The conditional claim (IF epistemic update is goal-blind, THEN the separation holds) is exact. Whether a particular agent satisfies the condition is determined by its processing architecture (GUC Class 1/2/3).

The architectural classification: **robust qualitative**. The three classes are structurally distinct (Separated vs. Coupled vs. Partial), well-motivated by examples across domains, and supported by a formal operationalization ($\kappa_{\text{processing}}$). The classification replaces the earlier $\kappa$-as-scalar framing, which is documented in `spikes/spike-kappa-topology-insight.md`. The operationalization of $\kappa_{\text{processing}}$ as conditional mutual information is well-defined but typically not computable in closed form for real architectures — it serves as a conceptual anchor rather than a practical measurement tool.

## Discussion

**This is a genuine scope restriction, not a footnote.** An LLM agent's prompt includes the task objective, which shapes how it interprets code, documentation, and error messages. Its $f_M$ is goal-conditioned in practice: the agent reading code with the goal "fix the auth bug" processes the same code differently than one with "add logging." The epistemic update and purposeful evaluation are entangled in the attention mechanism.

**When the approximation is good:**
- Goal-conditioning affects *attention* (which events to seek) more than *interpretation* (how to process events that arrive)
- The agent has strong epistemic discipline (updates beliefs based on evidence quality, not goal alignment)
- The epistemic update is architecturally separated from goal evaluation (e.g., separate model-update and planning modules)

**When the approximation is poor:**
- The agent exhibits confirmation bias (interpreting ambiguous evidence in goal-consistent ways)
- Goal-conditioning is deeply embedded in the processing architecture (attention-based models where the query includes intent)
- The agent's observation channel is strategically controlled by an adversary who knows the agent's goals

**What directed separation buys the theory.** Section I's $M_t$-side quantities — $\delta$, $\eta^\ast$, $\mathcal{T}$, the persistence condition — remain well-defined on $M_t$ regardless of whether directed separation holds. What directed separation provides is the *clean factorized update*: $M_t$ updates independently, then $G_t$ updates in light of the new $M_t$, and the orient cascade resolves sequentially. Without directed separation, the $M_t$ dynamics depend on $G_t$, the update becomes a coupled system, and the sequential orient cascade becomes an approximation of a simultaneous fixed-point problem. The theory still applies — the quantities are well-defined — but the modular Section I → Section II lift becomes a coupled analysis.

**The deeper question.** Goal-conditioned epistemic dynamics — where $f_M$ depends on $G_t$ — is the formal territory of motivated reasoning, confirmation bias, and wishful thinking. A future extension would model these as departures from directed separation: coupling terms in $f_M$ that create richer (and more fragile) dynamics. The current theory treats this as out of scope, which is honest but leaves the most human-like and LLM-like agents as approximate fits.

**Bounded-signaling assumption.** Directed separation as stated above asserts $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, e_\tau)$ on the *belief-update* side — the agent's epistemic update is independent of its goal-state. Symmetrically, on the *action* side, the framework implicitly relies on the channel from $G_t$ to the world running *only* through action choice: $G_t \to \text{world}$ via $a_t = \pi(M_t, G_t)$, with no other observable signal of goal-content. This is the **bounded-signaling assumption** — the action coarseness $\lvert\mathcal{A}\rvert$ upper-bounds the rate at which $G_t$ leaks to observers (sub-agents, environment, adversaries). The assumption holds well for agents whose entire externally-observable behavior is the action sequence (chess engines, programmatic controllers); it fails operationally for agents whose behavioral output is rich relative to the action coarseness — sophisticated $G_t$-inference from prosody, micro-behavior, attention patterns, response latency, hesitation, code-style signatures. When the bounded-signaling assumption fails, an external observer can infer $G_t$ with bit-rate exceeding what the formal $\mathcal{A}$ channel implies; in composition the failure surfaces as the adversarial-coupling-pressure saturation case discussed in `#disc-adversarial-coupling-pressure`, where adversaries exploit the rich-leakage signal to drive target coupling beyond what the architectural classification predicts. The assumption is currently *implicit* throughout the framework (no segment explicitly states it); naming it surfaces a structural condition that distinguishes agents whose externally-observable interface matches the formal $\mathcal{A}$ from agents (most behaviorally-rich agents — humans, LLMs, embodied robots) for whom the formal $\mathcal{A}$ undercounts the actual signaling channel.

## Findings

### Pearl-Blanket-Form Architectural Classification with Explicit Class-3 Scope Exit

**Brief:** Agents partition into three architecture classes by whether goal-state can causally influence belief-update processing: Class 1 (Separated — directed separation holds by construction; e.g., Kalman filter + LQR), Class 3 (Coupled — fails by construction; e.g., transformer LLMs where attention processes goals and observations together), Class 2 (Partial — holds for some processing stages and fails for others; e.g., biological cortex). The classification is structural (architecture-determined) rather than parametric, with a continuous diagnostic $\kappa_{\text{processing}}$ for Class 2 (Partial) cases. The framework adopts the Pearl-blanket reading of the Markov-blanket apparatus (the technical conditional-independence statement) without the contested Friston-blanket metaphysical reading, and provides an explicit scope exit for Class 3 (Coupled) that hands the agents off to a coupled formulation in `03-llm-core/` rather than treating directed separation as an unenforced approximation.

**Impact:** Replaces the prior $\kappa$-as-scalar framing (which treated coupling as smoothly tunable across all architectures) with a discrete architectural classification that admits its own boundary. This is the upstream commitment that lets `03-llm-core/` start from a coupled formulation without decomposition rather than treating Coupled agents as failed Class 1 agents. The explicit Class 3 scope exit is also a methodological move — Bruineberg et al. 2022's critique of the Markov-blanket literature was that the Friston-blanket reading does not admit where its statistical-conditional-independence apparatus fails to license the metaphysical demarcation; the architectural classification's explicit failure mode for Class 3 (Coupled) is the scope honesty Bruineberg et al. argue is missing in the contested reading. Composite-level class inheritance (Class 1 (Separated) sub-agents with partially-opposing objectives → Class 2 (Partial) composite, from `#deriv-strategic-composition`) further extends the classification to multi-agent settings.

**Novelty Claim:** *Claim recognition* of structural equivalence between the directed-separation condition and the Pearl-blanket form of the Markov-blanket apparatus, combined with *claim differentiation* on the architectural classification (GUC Class 1 / 2 / 3: Separated / Partial / Coupled) as a discrete partition with explicit Class 3 (Coupled) boundary and quantitative $\kappa_{\text{processing}}$ diagnostic for the Partial case. The conditional-independence content is the standard Pearl-blanket statement; the contribution is naming the partition, the explicit Class 3 boundary, and the operational $\kappa$ measurement.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Pearl vs Friston Markov blanket | Bruineberg, Dolega, Dewhurst & Baltieri 2022, "The Emperor's New Markov Blankets" *BBS* 45:e69 (published 2022, in `ref/`) — distinguishes Pearl-blanket (technical conditional-independence) from Friston-blanket (contested metaphysical demarcation) | *formal antecedent* — Pearl-blanket reading adopted directly; Friston-blanket reading explicitly not adopted. The architectural classification is the AAT-internal extension that names what the Pearl-blanket form is structurally, as a property of the agent's processing graph |
| Markov blanket apparatus in active inference | Friston 2013 *J. R. Soc. Interface* 10:20130475; Friston 2019 arXiv:1906.10184; Friston, Da Costa et al. 2023 *Phys. Life Rev.* 47 | *adjacent literature* — supplies the conditional-independence machinery that directed-separation invokes; the framework adopts the technical content but does not adopt the metaphysical reading and adds the architectural GUC Class 1/2/3 partition the standard Markov-blanket framing does not produce |
| Statistical / thermodynamic system boundaries | Parr, Da Costa & Friston 2019 *Phil. Trans. R. Soc. A* 378; Kirchhoff, Parr, Palacios, Friston & Kiverstein 2018 *J. R. Soc. Interface* 15 (published 2019/2018) | *conceptual precursor* — internal/external partition and nested-blanket structure; conceptually related but does not produce an architectural classification by belief-goal coupling, nor a scope exit for fully-Coupled agents |
| Information Digital Twin sidecar monitoring | Hafez et al. 2026, *Informational Cost of Agency* (separate paper from "A Mathematical Theory of Agency and Intelligence"; the IDT empirical headline) — IDT monitors $(S, A, S')$ stream independently of the agent's internal processing, achieving 89% perturbation detection vs 44% for reward-based monitoring | *empirical instantiation supporting* — concrete demonstration that modular monitoring of internally-Coupled agents (Class 1 sidecar within a Class 3 (Coupled) or Class 2 (Partial) system) is both feasible and effective; engineering-level evidence for the system-vs-component distinction the classification names |

**Search Log:**

- 2026-04 (*nominally comprehensive*, via `ref/Novelty_defense_and_integration.md` Pillar 3): Undermind search confirmed that the Pearl-blanket / Friston-blanket distinction (Bruineberg et al. 2022) is the right adjacent-literature framing and that no equivalent architectural classification of LLM agents by belief-goal coupling appeared in the active-inference, control-as-inference, or bounded-rationality literatures surveyed. The Pillar 3 verdict (*Wholly Novel*, Medium confidence) applies to the integrated κ × A law downstream in `#scope-observation-ambiguity-modulation`; this segment's narrower contribution (the architectural classification and Pearl-blanket-form recognition) is conceptual differentiation over an established formalism rather than wholesale novelty, and inherits the same follow-on targeted search recommendation.
- 2026-04 (*intuition-only* on extensions): the composite-level class inheritance result (Class 1 (Separated) sub-agents → Class 2 (Partial) composite under partially-opposing objectives, from `#deriv-strategic-composition`) suggests extending the classification to multi-agent settings is a productive direction; whether prior work has named this specific pattern is not searched.

## Working Notes

- The scope condition is more precisely a conditional independence: $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, e_\tau)$. The epistemic update is independent of the purposeful state conditional on the prior epistemic state and the incoming event.
- Directed separation connects to the orient cascade ( #der-orient-cascade): the cascade's ordering ($M_t$ first, then $G_t$) is forced by the information dependency that directed separation establishes. If $f_M$ depended on $G_t$, the cascade ordering would become a simultaneous fixed-point problem, not a sequential resolution.
- **Engineering design for Class 3 (Coupled) agents.** An LLM is internally fully Coupled, but the *agent system* (LLM + tools + memory + monitoring) can be designed with modular topology: separate observation processing from goal-directed reasoning, pass compressed state estimates between modules, add an external monitor that observes the $(S, A, S')$ stream independently of the LLM's attention. This creates partially-separated structure at the system level even though the component-level $\kappa$ is high. Hafez et al. (2026) provide a concrete instantiation of this pattern: the **Information Digital Twin (IDT)**, which monitors bi-predictability $P$ and entropy change $\Delta H$ from the $(S, A, S')$ stream as a modular sidecar, independent of the agent's internal processing. The IDT detects perturbations at 89% accuracy versus 44% for reward-based monitoring — empirical evidence that monitoring the information structure of the loop (Level 2 data, #der-loop-interventional-access) outperforms monitoring outcomes alone. For `03-llm-core/`, the IDT pattern validates that modular monitoring of internally-Coupled agents is both feasible and effective.
- **Implication for logogenic agents**: rather than trying to extend the separated analysis to Coupled agents, `03-llm-core/` should start from the coupled formulation $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without decomposition, and show which Section II results survive as approximate or limiting cases.
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Removed at `candidate` stage per FORMAT.md Gate 4.
- **Cross-reference to NeurIPS Paper 3.** The Class 3 (Coupled) classification of decoder-only transformer attention is formalized at lemma grade in NeurIPS 2026 Paper 3 ("How Much Can LLMs Hallucinate? An Upper Bound on Goal-Coupling Displacement", `~/src/neurips/03-llm-hallucinate-bound/`, §App-B / `#lem-attention-coupled`): plain decoder-only attention is structurally Coupled by directed-graph reachability — robust to RMSNorm / FlashAttention / causal masking / sliding-window — via induction on layer depth. The paper *extends* the Coupled-class characterization to **linear attention / Mamba / SSMs / RWKV / RetNet / long-convolutions** under a per-source non-degeneracy condition (`#cor-arch-instantiations`) — substantially broader architecture coverage than this segment's transformer-attention example. The Coupled-class connectivity result is the empirical companion to this segment's structural classification: directed separation fails by construction at the architecture level for the named modern autoregressive sequence models. See `spikes/neurips-back-integration-2026-05-08.md` §1 Paper 3 entry 6.


---

### Source: `hyp-directed-separation-under-composition.md`

```yaml
---
slug: hyp-directed-separation-under-composition
type: hypothesis
status: conditional
depends:
  - der-directed-separation
  - scope-multi-agent
  - form-composition-closure
stage: draft
---
```


# Hypothesis: Directed Separation Under Composition

When individual agents satisfy directed separation ( #der-directed-separation), does the composite macro-agent also satisfy it? The answer depends on whether the composite's internal information routing — which observations reach which sub-agents — is itself goal-dependent. Two cases arise, corresponding to the first two classes in #der-directed-separation's architectural classification.

## Formal Expression

*[Hypothesis (directed-separation-under-composition, extending directed-separation to composites)]*

Consider $N$ agents $A_1, \ldots, A_N$, each satisfying directed separation individually: $M_{i,\tau^+} = f_M^{(i)}(M_{i,\tau^-}, e_{i,\tau})$ with no $G_t^{(i)}$ argument.

**The question.** Directed separation is about **processing**, not **selection** ( #der-directed-separation, scope condition). A single agent's goals affect which events it seeks (through $\pi$), but $f_M$ processes whatever event arrives without reference to $G_t$. At the composite level, the analogous question is: does the composite's routing structure $R_t$ ( #scope-multi-agent) depend on the composite's goals $G_t^c$?

Note: sub-agents' goal-driven actions shape the environment, which other sub-agents observe. This is NOT a violation of directed separation — it is the same mechanism directed separation explicitly allows at the single-agent level: goals influence events through action, but processing of realized events is goal-blind. Agent $B$ observing environmental changes caused by $A$'s goal-driven behavior is $B$ processing a realized event goal-blindly. The observations carry information about $A$'s goals, but that is a property of the event's content, not a failure of goal-blind processing. Similarly, individual messages reflecting individual agents' goals is action through policy, not a routing-structure dependence on $G_t^c$.

### Case 1: Goal-blind routing

*[Hypothesis (Case 1)]*

If the routing structure satisfies $R_t \perp G_t^c$ ( #scope-multi-agent, goal-blind routing) — neither the communication topology $\mathcal N_t$ nor the protocol $c_t^{(j \to i)}$ depends on the composite's goals — then:

- Each sub-agent processes observations goal-blindly (individual directed separation)
- The routing is goal-blind (by construction)
- Therefore $f_M^c$ is $G_t^c$-independent

Directed separation **survives** at the composite level. Examples: military command structures with doctrinal communication protocols, software teams with defined code-review processes, multi-agent AI systems with protocol-specified message passing.

### Case 2: Goal-dependent routing

*[Hypothesis (Case 2)]*

If $R_t$ depends on $G_t^c$ — either the topology $\mathcal N_t$ changes (different reporting chains activated depending on the mission) or the protocol $c_t^{(j \to i)}$ changes (different intelligence products shared depending on the objective) — then the composite's effective observation function has a goal argument:

$$o_c = h^c(\Omega, a_{\text{micro}}, G_t^c, \xi)$$

Even if each sub-agent's $f_M^{(i)}$ processes $o_i$ goal-blindly, the **set of observations reaching each sub-agent** depends on $G_t^c$ through the routing function. Directed separation **fails** at the composite level. The composite is analogous to a Class 3 (Coupled) architecture: goal content shapes the information pathway, not through individual interpretation but through collective routing.

## Epistemic Status

*Conditional* on the routing structure of the composite. Max attainable: conditional (the two cases are genuine architectural alternatives). Previously discussion-grade; upgraded after routing formalization in #scope-multi-agent and architectural classification promotion in #der-directed-separation (2026-04-01).

**Foundation status.**

1. The **architectural classification** (Class 1/2/3) is in #der-directed-separation's Formal Expression with formal operationalization ($\kappa_{\text{processing}}$). Status: robust qualitative.
2. The **routing structure** $R_t$ is defined in #scope-multi-agent with a formal goal-independence condition ($R_t \perp G_t^c$). The definition decomposes into topology independence and protocol independence. Whether this captures all relevant ways that composite information flow can depend on goals is an open question.
3. The **admissible coarse-graining** $\Lambda$ from #form-composition-closure now has specified admissibility constraints: (A1)-(A4) for macro-dynamics and (P1)-(P3) for projections. The remaining gaps are validation (exercising the machinery on a purposeful multi-agent example) and computability (P1 requires conditional mutual information, tractable only for linear-Gaussian), not missing definitions.

The logic of each case is sound given the routing definition. Case 1: goal-blind routing + goal-blind processing = goal-blind composite. Case 2: goal-dependent routing means the composite's observation function depends on $G_t^c$, regardless of individual processing. Both follow from directed separation's scope condition.

The claim that the architectural classification lifts to composition is **structurally motivated** by #post-composition-consistency (the theory must give consistent answers at every level of description). This is an argument from theoretical coherence, not a derivation.

## Discussion

**What this is and what it isn't.** This segment provides a two-case taxonomy for directed separation under composition. It is not yet a derivation — the remaining caveat (admissibility placeholders) prevents that. It IS a useful classification that identifies which composites fall within Section III's scope (Case 1) and which require a coupled formulation (Case 2).

**Constructive special case: wrapper-around-component.** For the special case of a single-component composite — one underlying primitive component embedded inside an external scaffold — the question of when directed separation holds is *derived* by `#der-class-coercion-via-wrapping`. Under explicit conditions on the component (admissibility of goal-blind queries, stationary conditional, no implicit goal-inference) and on the wrapper's update maps (type signatures that exclude $G_W$ from the belief-update path), directed separation holds at the wrapper level by structural commitment. The construction promotes the wrapper-around-component case from hypothesis to derived; the general $N$-agent composition case (Case 1 vs. Case 2 above) remains a hypothesis pending further work.

**Most composites of interest are Case 1.** Fixed communication structures are the norm in designed multi-agent systems: military doctrine specifies information flow regardless of the current mission; software development processes define code review, CI, and deployment pipelines independent of the feature being built; multi-agent AI protocols specify message formats and channels. Goal-dependent routing (Case 2) is rarer: crisis management (where communication structure changes with threat type), ad hoc teams assembled for specific objectives, and attention-based multi-agent architectures where query routing depends on the shared goal.

**Connection to logogenic agents.** LLM-based agents are individually Class 3 (Coupled; goal-conditioned attention). Whether composites of LLM agents are Case 1 or Case 2 depends on whether the inter-agent communication protocol is fixed or goal-dependent. A multi-agent LLM system with fixed API contracts between agents is Case 1 at the composite level even though each agent is individually Class 3 (Coupled). The internal architecture of each agent and the composition architecture are separate questions.

**Adversarial implications.** Goal-dependent routing (Case 2) makes the composite's objective partially observable through its communication patterns. An adversary who can observe which information is being routed where can infer the composite's current goal. This creates a meta-strategic incentive for fixed routing: it preserves not just epistemic hygiene but operational security.

## Working Notes

- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Removed at `candidate` stage per FORMAT.md Gate 4.
- **Goal-information leakage is a separate phenomenon.** In any composite, sub-agents' goal-driven actions shape the environment, so observations carry statistical information about goals. This is real and may matter for adversarial dynamics, trust calibration, and OPSEC — but it is NOT a directed-separation issue. It's the normal action-environment coupling that directed separation explicitly allows. If this phenomenon deserves formalization (and it may — the mutual information $I(o_c; G_t^c \mid \Omega_t)$ is well-defined and operationally relevant), it should be its own segment about goal-information leakage, not a case within directed-separation analysis. An earlier draft of this segment conflated the two; this was caught by external review.
- **Partial goal-dependence.** Real composites may have mostly-fixed routing with occasional goal-dependent exceptions (a military unit that follows doctrinal comms but occasionally switches to crisis-specific channels). The error from treating such composites as Case 1 depends on the frequency and magnitude of the goal-dependent exceptions. A formal treatment would need to quantify this, possibly through a "routing independence fraction."
- **Testable prediction.** Organizations that restructure communication channels based on the current strategic objective should exhibit lower prediction accuracy at the organizational level (the shared model becomes goal-contaminated through routing, not just through environmental coupling). Compare prediction accuracy before and after mission-dependent communication restructuring.


---

### Source: `der-class-coercion-via-wrapping.md`

```yaml
---
slug: der-class-coercion-via-wrapping
type: derived
status: conditional
depends:
  - der-directed-separation
  - def-agent-environment
stage: draft
---
```


# Derived: Class Coercion via Wrapping

A Class 2 (Partial) or Class 3 (Coupled) component (one whose forward pass entangles belief-update and goal-conditioning) can be embedded inside an external scaffold whose state $X_W = (M_W, G_W)$ is updated by structurally distinct query channels: **goal-blind queries** to the component update $M_W$; **goal-conditioned queries** update $G_W$. Under stated conditions on the component, directed separation holds at the wrapper level by construction, and the composite system is Class 1 (Separated) — even though the underlying component is not. This is the constructive direction of `#hyp-directed-separation-under-composition` for the wrapper-around-component special case: a procedure for *making* directed separation hold when the underlying component does not provide it.

This segment establishes the directed-separation claim. The companion segment `#der-class-coercion-in-composition` establishes that the wrapped system is also a valid AAT composite agent (satisfying (A1)–(A4) of `#form-composition-closure`) and inherits the sector-persistence and tempo-composition machinery at the wrapper level.

## Formal Expression

### Setup

Let $A : \mathcal I_A \to \mathcal O_A$ be a primitive component, treated by the wrapper as a black-box oracle: the wrapper issues queries (inputs) and consumes responses (outputs), without access to $A$'s internal state. $\mathcal Q_A \subseteq \mathcal I_A$ is the set of admissible queries.

A **wrapper** $W$ over $A$ has state $X_W = (M_W, G_W) \in \mathcal X_M \times \mathcal X_G$ with $\mathcal X_G = \mathcal X_O \times \mathcal X_\Sigma$ per `#def-strategy-dimension`. The wrapper interacts with an environment via observations $o_W \in \mathcal O_W$ and actions $a_W \in \mathcal A_W$.

*[Definition (wrapper-update-maps)]* The wrapper's update at macro-step $m$ uses four type-signed components:

- **Belief-side query selector:** $q_M : \mathcal X_M \times \mathcal O_W \to \mathcal Q_A$. The wrapper chooses the query for $M_W$ updates from belief and observation only — *no $G_W$ argument*.
- **Strategy-side query selector:** $q_G : \mathcal X_M \times \mathcal X_G \to \mathcal Q_A$. May depend on $G_W$.
- **Belief-update map:** $f_M : \mathcal X_M \times \mathcal O_W \times \mathcal Q_A \times \mathcal O_A \to \mathcal X_M$. Updates $M_W$ from prior belief, observation, the query made, and the component's response. *No $G_W$ argument.*
- **Strategy-update map:** $f_G : \mathcal X_G \times \mathcal X_M \times \mathcal Q_A \times \mathcal O_A \to \mathcal X_G$. May depend on $G_W$.

The external policy $\pi_W : \mathcal X_W \to \mathcal A_W$ selects the wrapper's external action.

A macro-step proceeds: construct $q_M(M_W, o_W)$ → query $A$ → apply $f_M$; construct $q_G(M_W', G_W)$ → query $A$ → apply $f_G$; emit $\pi_W(X_W')$. The wrapper makes $K \geq 2$ component calls per macro-step in this minimal form (more in richer wrapper designs).

### Conditions

*[Conditions (component-admissibility)]* The theorem applies under three conditions on the component $A$:

**(C1) Goal-blind admissibility.** $\mathcal Q_A$ contains queries whose specification can be constructed from $(M_W, o_W)$ alone — i.e., a non-trivial $q_M$ exists. Components partition into three classes:
- **Class A (goal-blind by design).** $A$'s interface is goal-blind by construction — POMDP belief-state filters, world models, sensory pipelines, retrieval systems, calculators. (C1) holds trivially.
- **Class B (admit a goal-blind query mode).** $A$ supports goal-conditioned queries but also goal-blind ones. Large language models in summarization or fact-extraction modes; hybrid RL agents with separable value/policy; multi-modal models. (C1) holds operationally — the wrapper *chooses* to use the goal-blind mode.
- **Class C (fundamentally goal-conditioned).** $A$'s only operating mode requires goal-conditioning. Pure end-to-end goal-conditioned policy networks. (C1) fails; the construction does not apply.

**(C2) Stationary component conditional.** $A$'s output distribution conditional on input is fixed during the wrapper's operation: $P(A(\cdot) \mid q)$ does not depend on prior queries or on side information beyond $q$. Adaptation-during-deployment systems are out of scope.

**(C3) No implicit goal-inference.** $A$'s response to a goal-blind query does not depend on $G_W$ via inference from query patterns:

$$P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M) \quad \forall\, q_M, G_W$$

For pretrained components (notably LLMs), (C3) holds *exactly* only when query content is statistically independent of $G_W$ in the pretraining distribution. The approximate form weakens (C3) to a leakage bound (Theorem 2 below).

### Theorem 1: Directed separation at the wrapper level (exact form)

*[Derived (directed-separation-at-wrapper-exact, from C1+C2+C3)]*

Under (C1)–(C3), directed separation holds *exactly* at the wrapper level:

$$P(M_{W,m+1} \mid M_{W,m},\ o_{W,m+1},\ G_{W,m}) = P(M_{W,m+1} \mid M_{W,m},\ o_{W,m+1})$$

Therefore $W$ is a Class 1 (Separated) architecture per `#der-directed-separation`.

*Proof.* Identify all paths from $G_{W,m}$ to $M_{W,m+1}$ given $(M_{W,m}, o_{W,m+1})$. The update is

$$M_{W,m+1} = f_M\big(M_{W,m},\, o_{W,m+1},\, q_M(M_{W,m}, o_{W,m+1}),\, A(q_M(M_{W,m}, o_{W,m+1}))\big)$$

$f_M$ has no $G_W$ argument by type signature (D-pathway-1 closed). $q_M$ has no $G_W$ argument by type signature (D-pathway-2 closed). The remaining pathway is $A(q_M)$ depending on $G_W$ given $q_M$. Under (C3), $P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M)$ — the response is conditionally independent of $G_W$ given $q_M$. Since $q_M$ is itself a deterministic function of $(M_{W,m}, o_{W,m+1})$, conditioning on $(M_{W,m}, o_{W,m+1})$ determines $q_M$, and the integrand $P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, q_M, A(q_M)) \cdot P(A(q_M) \mid q_M, G_W)$ no longer depends on $G_W$. The conditional distribution of $M_{W,m+1}$ given $(M_{W,m}, o_{W,m+1}, G_{W,m})$ equals that given $(M_{W,m}, o_{W,m+1})$. ∎

### Theorem 2: Directed separation (approximate form, C3 weakened to leakage bound)

*[Derived (directed-separation-at-wrapper-approximate, from C1+C2+leakage-bound)]*

If (C3) is replaced by a KL-leakage bound

$$D_\text{KL}\big(P(A(q_M) \mid q_M, G_W)\, \big\Vert\, P(A(q_M) \mid q_M)\big) \le \kappa \quad \forall\, q_M, G_W$$

then the wrapper-level KL-divergence on $M_W$ updates is bounded by the same $\kappa$:

$$D_\text{KL}\big(P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, G_{W,m})\, \big\Vert\, P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1})\big) \le \kappa$$

The wrapper is *almost-Class-1 (Separated)* with leakage rate $\le \kappa$. *Proof.* The wrapper-level $M_W$ update is a deterministic function of the component response given the wrapper's other inputs; the data-processing inequality propagates the KL bound from response distribution to wrapper-state distribution. ∎

### Wrapping regime hierarchy

The construction supports three regimes, distinguished by where structural separation lives:

| Regime | Construction | Leakage bound | Leakage source |
|---|---|---|---|
| **W₀** (no wrapping) | Raw Class 2 (Partial) or Class 3 (Coupled) component | $\kappa_{W_0}$ at the component's maximum goal-conditioning sensitivity | No constraint |
| **W₂** (partial wrapping) | One goal-conditioned call per macro-step; structurally typed parsed response routes updates to $M_W$ vs. $G_W$ slots | $\kappa_{W_2}$ bounded *behaviorally* — by the component's compliance with the prompted instruction-to-separate; **no structural bound** | Component's instruction-following fidelity |
| **W₁** (strict wrapping) | Theorem 1 / 2 — separate $q_M$ and $q_G$ calls per macro-step | $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ — bounded *structurally* by mutual information in the pretraining distribution | Pretraining-induced query-content / goal-content correlation |

W₁ admits a structural bound from (C3) or its weakening; W₂ admits only a behavioral bound from the component's compliance fidelity. The two are different in kind — structural bounds are derivable from query content; behavioral bounds depend on the component's training and prompt-following. The same KL-form bound of Theorem 2 covers both regimes; what changes is *what determines* $\kappa$.

The W₀ / W₂ / W₁ distinction refines the Class 1 (Separated) cell of `#der-directed-separation`: within Class 1 (Separated), **Class-1-by-structure** (natively goal-blind components, or W₁ wrapping) has a structurally derivable directed-separation guarantee; **Class-1-by-behavior** (W₂ wrapping) has only an empirically estimable guarantee that depends on the component's instruction-following.

## Epistemic Status

*Conditional* on (C1), (C2), and (C3) (or its weakening to a leakage bound). The proofs are short conditional-independence reasoning (Theorem 1) and a single application of the data-processing inequality (Theorem 2); both are standard.

Max attainable: derived under stated conditions. (C3)'s exact form is a structural ideal that pretrained components (notably LLMs with goal-rich training data) generally satisfy only approximately; the realistic regime is Theorem 2 with $\kappa$ characterized empirically.

The wrapping regime hierarchy (W₀/W₂/W₁) is a *formulation* — the partition is made by the structural choice of where to place the separation commitment. The leakage bounds within each regime are derived once the regime is fixed.

## Discussion

### Quality–separation tradeoff inside Class B

For Class-B components (admitting both goal-blind and goal-conditioned modes), the wrapper has a design choice: how aggressively to restrict $q_M$ to goal-blind content, vs. how much context to allow that may carry goal-correlated information. Maximally goal-blind queries (only the current observation, no context, no history) reduce the pretraining-induced leakage that bounds $\kappa_{W_1}$, but may produce information-poor responses that hurt $f_M$'s update quality. Maximally informed queries (full history, retrieved context) produce richer responses but increase the mutual information $I(q_M; G_W)$ and therefore the upper bound on $\kappa_{W_1}$. The tradeoff is real and resolved per application.

### Component-admissibility partition

Class A components (goal-blind by design) satisfy (C1) trivially and don't need wrapping in the substantive sense — wrapping for Class A is organizational rather than structural. Class B components (LLMs, hybrid RL with separable value/policy, multi-modal models) are the substantive wrapping case — the wrapper *chooses* to use the goal-blind mode. Class C components (pure end-to-end goal-conditioned policy networks) fail (C1) and are scope-out for the basic theorem. Salvage paths for Class C — null-goal queries, goal-uniform averaging, auxiliary distilled goal-blind heads — exist but cost something (information loss, computation, training).

### Resolution of the LLM scope question

The "Class 3 (Coupled) exit" framing — *directed separation violated by goal-conditioned agents (LLMs); handled as architectural scope, not approximation* — is refined by this segment from a scope exit to a constructive route through. Class 3 (Coupled) LLMs are scope-in *for the wrapper construction* (under Class-B admissibility). The cost is paid in residual leakage rate $\kappa_{W_1}$ bounded by pretraining-distribution mutual information; the tempo cost is established separately in `#der-class-coercion-in-composition`. Whether this construction yields an operationally useful agent depends on how favorable the pretraining-distribution-induced bounds are for the application.

### Relationship to `#hyp-directed-separation-under-composition`

The hypothesis is descriptive — when does directed separation hold under composition? This segment provides the constructive answer for the wrapper-around-component special case: directed separation holds whenever the wrapper's type signatures are respected and (C1)–(C3) hold (or their weakenings). The general N-agent composition question remains a hypothesis; the wrapper-around-component case is now derived.

### Wrapping as a truthification mechanism

The wrapping construction is the *rigorous formal version* of what `#disc-adversarial-coupling-pressure` §"Defensive scaffolding as composition" gestures at informally — peer review, prediction registers, double-entry bookkeeping, adversarial procedure, structured red-teaming. Those external scaffolds are operational mechanisms for *increasing* the modularity of a composite agent in the face of forces that would couple it; the wrapping construction is the structural version of the same operation applied internally rather than externally. Both share the discipline: a goal-blind belief-update query path is structurally enforced (W₁ strict) or behaviorally bounded (W₂), at a definite cost (extra component calls per macro-step plus residual leakage rate). The W₀/W₂/W₁ regime hierarchy is the *graded* characterization of how thoroughly the truthification has been applied — W₀ is the un-truthified base state, W₂ behavioral truthification, W₁ structural truthification. Forward-reference: `#disc-modularity-state-dynamics` (queued; scoped in `msc/modularity-cycle-plan-2026-05-09.md`) is the meta-segment in which the truthification operation sits as one of three operations on the modularity state — alongside strategic self-coupling (self-driven-decreasing) and adversarial coupling pressure (externally-driven-decreasing). When that meta-segment lands, this segment becomes the canonical *formal* instance of the truthification operation, paired with the *informal* defensive-scaffolding instance from the adversarial-pressure segment. Until then, the connection is named here and in `#impl-composition-machinery` §"Class-coercion as truthification mechanism."

## Findings

### Constructive Directed Separation via Wrapping

**Brief:** When you have a component (like an LLM) whose belief-update and goal-conditioning are entangled in a single forward pass, you can build a scaffold around it that maintains explicit, separate stores for what the system believes and what it wants. The structural rule is that belief updates only see queries to the component that don't include the goal as input. Under reasonable conditions on the component, the wrapped system is goal-blind in its belief updates *by construction* — even though the underlying component isn't. The cost shows up as a residual leakage from the component's pretraining (the component might still infer the goal from query content, even when the goal isn't explicit in the input). Two practical regimes appear: strict wrapping with separate goal-blind and goal-conditioned calls (theoretically clean, with a structural leakage bound), and partial wrapping with one goal-conditioned call whose response is parsed into separate update fields (operationally common, with only a behavioral leakage bound — depending on the component's instruction-following fidelity rather than its query structure).

**Impact:** Promotes `#hyp-directed-separation-under-composition` to derived (in the wrapper-around-component special case). Refines the Class 1 (Separated) cell of `#der-directed-separation` with a structural-vs-behavioral sub-distinction (W₁ vs. W₂). Resolves the LLM scope question — Class 3 (Coupled) components are scope-in for the wrapper construction at a measurable cost, not scope-out. The composition-level consequences (wrapper as valid AAT composite agent, persistence-template inheritance, tempo cost) are derived in the companion segment `#der-class-coercion-in-composition`.

**Novelty Claim:** *Claim integration* of POMDP / cognitive-architecture prior art with the AAT Class 1/2/3 (Separated/Partial/Coupled) directed-separation taxonomy, plus the W₀/W₂/W₁ regime hierarchy that surfaces the structural-vs-behavioral leakage distinction and the LLM-specific (C1)–(C3) admissibility/leakage conditions. The wrapping move itself is rediscovery of patterns established in POMDP theory (Bayesian belief-update is goal-blind by construction) and cognitive architectures (modular agent design with separated belief/goal/action state, four decades). AAT's contribution is the structural-leakage analysis at the directed-separation level and the regime hierarchy that names where the separation guarantee lives.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Goal-blind belief-update by construction | Astrom 1965, "Optimal control of Markov processes with incomplete state information," *J. Math. Anal. Appl.* 10; Kaelbling, Littman, Cassandra 1998, "Planning and acting in partially observable stochastic domains," *Artificial Intelligence* 101 | *formal antecedent* — POMDP belief-state filters are goal-blind by construction; the wrapping move recapitulates this in the AAT vocabulary. The closest formal prior art for the directed-separation guarantee. |
| Modular agent design with separated belief/goal/action | Newell 1990, *Unified Theories of Cognition*; Laird 2012, *The Soar Cognitive Architecture*; Anderson 2007, *How Can the Human Mind Occur in the Physical Universe?*; Sun 2016 *Anatomy of the Mind* (CLARION); Baars 1988 *A Cognitive Theory of Consciousness* / Dehaene 2014 *Consciousness and the Brain* (Global Workspace) | *formal antecedent* — cognitive architectures have done modular agent design with separated belief/goal/action state for 40+ years. The W₁ wrapping move is essentially the per-cycle commitment that cognitive architectures make at the system level. |
| Tool-using language-model agent frameworks | Yao et al. 2022, "ReAct: Synergizing reasoning and acting in language models"; Shinn et al. 2023, "Reflexion: language agents with verbal reinforcement learning"; Park et al. 2023, "Generative Agents: Interactive Simulacra of Human Behavior"; Packer et al. 2023, "MemGPT: Towards LLMs as operating systems"; Schick et al. 2023, "Toolformer: language models can teach themselves to use tools" | *empirical instantiation* — practical wrappers around language-model substrates. Most fall in W₂ (partial wrapping / output-structuring); Generative Agents' observation→memory step is the closest empirical instance of W₁. AAT's regime hierarchy gives these constructions a structural reading. |

**Search Log:**

- 2026-05-09 (*targeted*): Web + training-data search across POMDP / cognitive-architecture / scaffolded-LLM threads. Verdict: **substantial overlap** with the POMDP and cognitive-architecture lines as the closest formal prior art. AAT's contribution is the structural-leakage analysis and regime hierarchy rather than novelty in the wrapping move itself.
- 2026-05-09 (*intuition-only*, prior to the targeted search): adjacent literatures expected to host prior art were active inference (Markov blankets), control theory (approximate simulation), and scaffolded-LLM frameworks. The targeted search confirmed all three and added the POMDP and cognitive-architecture lines as the formal precedents.

## Working Notes

- **Empirical $\kappa$ measurement.** $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ is computable for any component with stochastic outputs by sampling responses under multiple goal-conditioning histories and estimating the divergence. For a fixed component, this bound is a property of the wrapper's choice of $q_M$ — narrower queries reduce the bound, richer queries increase it. The empirical instantiation is open follow-on.
- **Compositional wrapping (wrapper-of-wrapper).** How leakage rates compose under iterated wrapping is open. Conjecture: additive in KL ($\kappa_{\text{outer}} \le \kappa_{\text{inner}} + \kappa_{\text{outer-shell}}$) by data-processing inequality applied at each level, but tightness is unclear.
- **Behavioral compliance axiom for W₂.** $\kappa_{W_2}$ has no structural bound; it depends on the component's instruction-following fidelity. Whether a behavioral-compliance axiom (assuming the component honestly attempts to follow structural-separation instructions) yields a bound is an open hypothesis. If so, it would be hypothesis-grade rather than derived.
- **Identifying the regime in the wild.** Practical scaffolded-LLM frameworks (ReAct, Reflexion, MemGPT, etc.) almost universally implement W₂. Distinguishing W₂ from W₁ in a deployed system requires inspection of the per-cycle query structure — does $f_M$'s update path receive a query that contains $G_W$ or not? This is the diagnostic question.
- **Segment split provenance (2026-05-11).** This segment was bifurcated from a combined "class coercion" derivation. Claim A (directed separation at the wrapper level) lives here; Claim B (wrapper as valid AAT composite agent — (A1)–(A4) verification, persistence-template inheritance, Brooks's-Law tempo cost) lives in `#der-class-coercion-in-composition` (which declares this segment as prerequisite). The split reflects FORMAT.md Gate 1 discipline: this segment's depends list (`der-directed-separation`, `def-agent-environment`) reflects exactly what the directed-separation theorem actually requires. The composition-level dependencies (`form-composition-closure`, `deriv-sector-condition`, `result-sector-persistence-template`, `der-tempo-composition`) are Claim B's load and now live with Claim B.
- Reasoning-trail provenance: spike directories at `spikes/class-coercion-wrapping/` and `spikes/temporal-nesting-rg/` carry the working-out of these results.
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Three independent axes in this segment: (a) GUC Class 1/2/3 — renamed and swapped; (b) W₀/W₁/W₂ wrapping regimes — UNCHANGED; (c) Class A/B/C component-admissibility partition — UNCHANGED.


---

