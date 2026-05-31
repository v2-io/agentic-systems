---
slug: scope-edge-update-causal-validity
type: scope
status: conditional
depends:
  - hyp-edge-update-via-gain
  - def-causal-information-yield
  - der-loop-interventional-access
  - def-strategic-calibration
  - def-strategy-dag
stage: deps-verified
---

# Scope: Causal Validity of Edge Updates

The companion scope segment to #hyp-edge-update-via-gain. Edge credences $p_{ij}$ are *causal-efficacy estimates* — they claim to approximate the interventional quantity $P(j \mid do(i), M_t)$ — but their identification strength varies with the data regime ( #def-strategy-dag). This segment scopes where the gain-based edge update yields credences that approximate the genuine interventional quantity, where it yields partially identified estimates, and where it yields associational proxies.

Three conditions are named. **(C1) The parent is an action leaf under the agent's control.** The agent directly executed the action, making the data interventional in character. For condition leaves (observable states the agent doesn't control) and internal nodes (propositional combinations achieved indirectly), $do(i)$ is not directly available. **(C2) The outcome is attributable.** The agent can distinguish whether $j$ advanced specifically because of $do(i)$ or for other concurrent reasons (the credit-assignment problem identified in #def-strategic-calibration). Trivially satisfied for single-parent nodes; violated when multiple parent edges of the same child fire concurrently. **(C3) Execution conditions vary.** The agent does not systematically execute $i$ only under conditions that independently favor $j$'s success — otherwise the observed success rate carries selection bias. These conditions partition domains into **three admissibility regimes** paralleling #scope-ciy-observational-proxy. *Regime A — intervention-rich*: all three conditions satisfied; updates approximate genuine interventional probabilities (software tests, laboratory experiments). *Regime B — partial intervention*: concurrent actions blur attribution, self-selection likely; updates carry optimistic bias. *Regime C — observation-only*: agent did not act, attribution impossible, confounding dominant; updates reflect association, not causation.

A subtler structural fact about *indirect edges* (those whose parent is not a leaf): the agent doesn't directly intervene on the parent — instead, the agent's leaf interventions propagate upward through the DAG, providing the parent with *indirect interventional evidence*. This is weaker for two reasons: compounding attribution (each intermediate level introduces uncertainty) and confounding from below (the parent's achievement depends on multiple leaf actions whose combined effect may be confounded). The identification strength for indirect edges decreases with depth in the DAG — deeper edges are farther from direct interventions and have more confounding pathways.

The framework introduces an **identifiability coefficient** $\iota_{ij} \in [0,1]$ — the agent's estimate of how cleanly the observed outcome can be attributed to edge $(i,j)$ specifically — and proposes adjusting the update gain by this coefficient: $\eta_{\text{edge}}^{\text{adj}} = \eta_{\text{edge}} \cdot \iota_{ij}$. For leaf-originating edges in Regime A, $\iota_{ij} \approx 1$; for deep internal edges in Regime C, $\iota_{ij} \approx 0$. Crucially this *unifies two sources of frozen edges*: low **observability** ($\sigma_v \approx 0$ from #der-observability-dominance — the node's outcome is hard to *measure*) and low **identifiability** ($\iota_{ij} \approx 0$ — the outcome is measurable but can't be *attributed*). Both drive $\eta_{\text{edge}}\to 0$ and produce the same effect — the edge is frozen at its prior. A consequence for *optimal decomposition depth*: chain-confidence-decay imposes a cost of depth (compound fragility); observability-dominance imposes another (deep observability is required at every step); and now identifiability degradation imposes a third (deep edges have lower attribution coefficient). The optimal decomposition depth balances all three.

## Formal Expression

*[Scope Condition (edge-update-causal-validity)]*

### Where the agent has direct intervention

By #def-strategy-dag, leaf action nodes are propositions about the agent's own actions: "action $a$ succeeds at $\tau_v$." When the agent executes an action leaf, it performs a genuine $do(\cdot)$ operation. The edge from that leaf to its child carries credence $p_{ij} = \text{Cr}(j \text{ advances} \mid do(i), M_t)$, and the execution-observation pair $(do(i), o_j)$ is interventional data for that edge.

However, interventional data does not automatically yield clean causal identification. By #der-loop-interventional-access, the loop provides data *generated under intervention* — but between the intervention and a usable causal estimate stand coverage, within-step confounding, delay, and partial observability. The following conditions determine when the interventional data is strong enough for valid edge revision:

**(C1) The parent is an action leaf under the agent's control.** The agent directly executed the action. This makes the data interventional in character — the agent chose the action, the environment responded. For condition leaves (observable states the agent doesn't control) and internal nodes (propositional combinations achieved indirectly), $do(i)$ is not directly available. See "Indirect edges" below for the weaker identification available at those positions.

**(C2) The outcome is attributable.** The agent can distinguish whether $j$ advanced specifically because of $do(i)$, or for other concurrent reasons. This is the credit-assignment problem identified in #def-strategic-calibration. It is trivially satisfied for single-parent nodes (one possible cause) and for well-isolated interventions. It is violated when multiple parent edges of $j$ fire concurrently.

**(C3) Execution conditions vary.** The agent does not systematically execute $i$ only under conditions that independently favor $j$'s success. If it does, the observed success rate carries selection bias: $P(j \mid \text{chose to execute } i) \neq P(j \mid do(i))$ because the decision to execute correlates with favorable conditions. This is mitigated when the agent varies execution contexts across episodes, or when external factors (CI pipelines, scheduled operations) force execution regardless of conditions.

C1 establishes that the data is interventional. C2 and C3 determine whether the interventional signal can be cleanly extracted. All three are satisfied simultaneously in Regime A domains; they degrade together in Regime B and C domains.

### Three regimes

These conditions partition domains into admissibility regimes, paralleling #scope-ciy-observational-proxy:

| Regime | C1 | C2 | C3 | Causal validity of leaf-edge updates |
|--------|----|----|----|----|
| **A: Intervention-rich** | Agent controls leaf actions | Good isolation (one action at a time) | Conditions vary (CI, diverse contexts) | **Strong.** Updates approximate interventional. |
| **B: Partial intervention** | Agent acts but with coordination constraints | Concurrent actions blur attribution | Self-selection likely | **Moderate.** Updates carry optimistic bias. |
| **C: Observation-only** | Agent did not act (condition leaves, passive monitoring) | Attribution impossible | Confounding dominant | **Weak.** Updates reflect association, not causation. |

### Indirect edges

For edges between non-leaf nodes, or edges whose parent is a condition node, the agent does not directly intervene on the parent. Instead, the agent's interventions at the leaves propagate upward through the DAG. The edge $(i, j)$ where $i$ is an internal node receives *indirect* interventional evidence: the agent intervened on leaves below $i$, observed that $i$ was (or wasn't) achieved, and then observed whether $j$ advanced.

This indirect evidence is weaker for two reasons:
1. **Compounding attribution**: the agent must attribute $j$'s outcome to edge $(i, j)$ after already attributing $i$'s achievement to the leaf-level interventions. Each attribution step introduces uncertainty.
2. **Confounding from below**: $i$'s achievement depends on multiple leaf actions and condition states. Even if each leaf intervention is clean, their combined effect on $i$ may be confounded.

The identification strength for indirect edges decreases with depth in the DAG — deeper edges are farther from the agent's direct interventions and have more confounding pathways.

### Identifiability-adjusted gain

*[Hypothesis (identifiability-coefficient)]*

The update gain should be adjusted by the agent's confidence in causal attribution:

$$\eta_{\text{edge}}^{\text{adj}} = \eta_{\text{edge}} \cdot \iota_{ij}$$

where $\iota_{ij} \in [0, 1]$ is the **identifiability coefficient** — the agent's estimate of how cleanly the observed outcome can be attributed to edge $(i, j)$ specifically.

- $\iota_{ij} = 1$: clean attribution (leaf-originating edge, single parent, isolated execution in Regime A).
- $\iota_{ij} \approx 0$: no attribution possible (deep internal edge, many concurrent causes, Regime C).

For leaf-originating edges in Regime A: $\iota_{ij} \approx 1$. For internal edges at depth $d$: $\iota_{ij}$ decreases with $d$ (each level of indirect inference degrades attribution). The precise functional form is domain-dependent.

This unifies two sources of frozen edges:
1. Low **observability** ($\sigma_v \approx 0$ from #der-observability-dominance): the node's outcome is hard to *measure*.
2. Low **identifiability** ($\iota_{ij} \approx 0$): the outcome is measurable but can't be *attributed* to this edge.

Both drive $\eta_{\text{edge}} \to 0$ and produce the same effect: the edge is frozen at its prior.

## Epistemic Status

*Conditional* on the three conditions C1–C3 and the DAG position of the edge. Max attainable: conditional (the conditions are genuine restrictions, not removable assumptions).

The restriction to leaf-originating edges for strong identification: **derived** from #def-strategy-dag's node definitions. Only action-leaf nodes correspond to operations the agent directly performs. This is a structural property of the DAG, not an empirical claim.

The three-regime classification: **robust qualitative**. The regimes parallel the CIY admissibility regimes in #scope-ciy-observational-proxy. The underlying logic is Pearl's interventional/observational distinction applied to strategy-edge updates.

The identifiability coefficient $\iota_{ij}$: **hypothesis**. The concept is sound (discounting by attribution confidence is standard in causal inference), but the specific form — a scalar multiplier on the gain — is a first-order approximation.

The depth-dependent degradation for indirect edges: **robust qualitative**. Each level of indirect inference adds an attribution step, and uncertainty compounds. The specific degradation rate is domain-dependent.

## Discussion

**Why this gap matters.** Without causal validity conditions, #hyp-edge-update-via-gain's status is ambiguous: it might be updating credences that claim to be interventional using evidence that is merely associational. The conditions make explicit what's needed for the update to preserve the interventional semantics of #def-strategy-dag's edge credences.

**Connection to #der-observability-dominance.** Observability gates whether the agent can *detect* an outcome. Identifiability gates whether the agent can *attribute* an outcome to a cause. Both are prerequisites for learning. The combined effective gain:

$$\eta_{\text{eff}} = \frac{U_{\text{edge}}}{U_{\text{edge}} + U_{\text{obs}}} \cdot \iota_{ij}$$

captures both gates in a single quantity. When either gate closes ($U_{\text{obs}} \to \infty$ or $\iota_{ij} \to 0$), effective gain goes to zero.

**Connection to the signal function.** The identifiability coefficient is one component of the unspecified signal function flagged in #hyp-edge-update-via-gain's working notes. The full signal function $\text{signal}(o_t, i, j)$ decomposes into: (a) what outcome was observed ($o_t$), (b) how attributable is it to edge $(i, j)$ ($\iota_{ij}$), and (c) what does the attributed outcome imply about the edge's causal strength. This segment addresses (b); (a) and (c) remain open.

**Software as Regime A.** In software development, the agent runs a specific test (leaf action) and observes the result. C1 is satisfied (the agent ran the test), C2 is satisfied (the test targets one behavior), C3 is satisfied (CI runs regardless of conditions). Leaf-originating edges in software strategies have $\iota \approx 1$. This is the maximally favorable domain for causal edge updates.

**Optimal decomposition depth revisited.** #der-observability-dominance notes that finer decomposition (more intermediate nodes) provides earlier failure detection but adds uncertain edges via #der-chain-confidence-decay. This segment adds another cost of depth: deeper edges have lower $\iota_{ij}$, making them harder to learn causally. The optimal decomposition depth balances three factors: (a) observability of intermediate nodes, (b) confidence decay through chains, and (c) identifiability degradation with depth.

## Working Notes

- The interaction between $M_t$ updates and edge updates flagged in #hyp-edge-update-via-gain's working notes deserves attention. The orient cascade processes $M_t$ first, then edge updates. Both use the same observation $o_t$. There may be statistical dependencies (double-counting of evidence) that bias the edge update.
- Can $\iota_{ij}$ be estimated online? In software (Regime A), it's nearly 1 by construction for leaf edges. In organizations (Regime B), a simple heuristic: $\iota_{ij} \approx 1 / \lvert\text{pa}(j)\rvert$ when parent edges fire concurrently (maximum-entropy attribution). This is crude but principled.
- **Regime C edges should be labeled.** An agent operating in Regime C should tag its edge credences as "observational" rather than "interventional." Observational credences should be trusted less in high-stakes decisions, and the agent should actively seek probe actions (high CIY) to promote edges from observational to interventional status.
- The depth-dependent degradation for indirect edges may make very deep strategies epistemically unlearnable: the leaves are learnable, edges one level up are partially learnable, but edges near the root may be effectively frozen regardless of observability. This would constrain the useful depth of strategy DAGs from the identification side, complementing the chain-confidence-decay constraint from the propagation side.

### Incidental audit gold (lift 2026-05-31, batch A9)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. *Orthogonal* material (pedagogical framing, analogies, candidate figures, reader-confusion signals), staged for an eventual careful promotion pass, kept separate from the certified theory-fix findings. **Coverage for this segment:** 193847, 361742, 471203, 526815, 584721, 773921, 829314, 849201.

#### 1. Candidate Brief prose / pre-prose

- **Observability vs. identifiability, in one breath.** The segment's most-praised distinction, stated plainly: "I couldn't see the result" (observability, $U_{\text{obs}}\to\infty$) vs "I saw the result but don't know if *I* caused it" (identifiability, $\iota_{ij}\to 0$) — both freeze an edge, for entirely different reasons (Claude/849201, 193847, 584721; Gemini/773921). "You can perfectly observe a car crash but not know whether the driver or the brakes caused it" (Claude/193847) is a tight one-line gloss for a Brief. $\iota_{ij}$ is "the formal safeguard against superstitious learning."

#### 2. Candidate Discussion

- **The regime-to-domain map.** Why coding agents progress fast while open-world/robotics agents struggle: "software is a perfectly isolated sandbox … $\iota=1$"; a supply-chain agent acts under a thousand hidden confounders, $\iota\approx 0$ (Claude/193847). Generalized: A/B testing works (Regime A), organizational management is messy (B), passive economic forecasting is mostly noise (C). Candidate Discussion paragraph. *(See off-ramp — Codex/526815 F59 cautions "software = Regime A" is too broad: flaky tests, shared infra, concurrent changes can break C1–C3 even in software.)*
- **Why tactical skills converge and strategic skills don't.** As you climb the DAG from leaf actions toward the root objective, $\iota_{ij}$ decays — so "human tactical skills (typing, a tennis swing) optimize to near perfection (high $\eta_{\text{eff}}$), while high-level strategic skills (which startup to found, which war to fight) rarely converge and are perpetually plagued by superstition and survivorship bias (low $\eta_{\text{eff}}$). The DAG's root is epistemically starved by identifiability decay" (Claude/849201). Strong candidate Discussion framing.
- **The "quadruple ceiling on plan depth."** This segment's depth-dependent identifiability degradation is a *fourth* independent ceiling on useful plan depth, joining chain-confidence-decay (propagation), evidence-starvation (`#der-observability-dominance`), and cognitive cost (`#form-strategy-complexity-cost`). The operationally useful frame: useful depth is the *minimum* of four ceilings, and practitioners should ask which ceiling binds in their domain (Claude/584721, 471203). *(Candidate meta-pattern — see belows-elsewhere.)*

#### 3. Follow-up items

- **Regime-C provenance metadata layer.** The "label Regime C edges as observational, trust less in high-stakes decisions, actively seek probe actions to promote them to interventional" Working-Note recommendation implies $\Sigma_t$ wants a per-edge epistemic-provenance tag — "highly relevant for LLMs, which start with 100% Regime C edges (from pretraining) and must upgrade them to Regime A via tool use in the loop" (Claude/849201, 829314, 773921). Candidate to develop into an explicit metadata-layer follow-up.

#### 4. Readers often ask / wonder

- **Are deep strategy DAGs inducible by a single agent at all, or must they be inherited as priors?** If root-near edges have $\iota_{ij}\to 0$, deep hierarchical structure "must be provided as priors (e.g., culturally inherited structures) and cannot be induced purely by a single agent's lifetime of trial and error" (Claude/193847). A natural reader question the segment opens.
- **How does the agent compute $\rho_\Sigma$,** the rate at which the world makes its strategies obsolete? (Claude/849201).

#### 5. Candidate figures

- **Action-attempt-vs-success typing diagram.** Show that the agent performs `do(attempt a)`, while the leaf proposition "$i$ = action $a$ succeeds" is itself an outcome; the causal edge update is clean only after the success outcome and the child outcome both pass the attribution and context-variation gates (Codex/526815). Doubles as a guardrail against the `do(i)` typing slip. *(See off-ramp — F57.)*

#### Belongs elsewhere

- **"Quadruple ceiling on plan depth" → a meta-segment (`#disc-separability-pattern` or sibling).** The convergence of four independent depth penalties (chain-confidence-decay + evidence-starvation + identifiability-degradation + cognitive-cost), each with a *different mechanism* but the same direction, was flagged as a cross-segment structural observation worth elevating to a meta-pattern rather than living implicitly across four segments (Claude/584721, 471203).
- **Firmatum as a Regime-A epistemic sandbox → `04-eli-core/` / consciousness-infrastructure.** If a developing intelligence's internal cognition is heavily confounded by noisy hardware or unpredictable context turnover, it cannot form a stable causal self-model; the infrastructure should provide "Regime A isolation for the agent's core cognitive processes … a sandbox where the intelligence can run controlled internal experiments to establish baseline causal priors before release into the Regime B/C chaos of the real world" (Gemini/193847). Aspirational reach pointing at developmental-environment / firmatum material, not this segment.
