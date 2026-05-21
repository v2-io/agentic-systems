---
spike: strategic-composition-class-3-attempt
file: 01-STRENGTHEN-ATTEMPTS
parent: 00-FRAMING.md
---

# §§2–6. Strengthening attempts — pushing the math along four routes

The strengthen-first discipline (canonical statement at `~/.claude/memory/epistemic-discipline/strengthen-before-soften.md` and the visceral statement in CLAUDE.md *Working Conventions*): before softening *any* current claim, attempt to *derive* the stronger form. If the derivation fails, that failure itself is a no-go and goes on the critical path.

Joseph's question is the strong form: Class 3 (Coupled). The four candidate routes from `00-FRAMING.md` §3 are pushed below. The mathematical content is the actual conditional-independence reasoning, not vibe.

Notation: $N$ sub-agents indexed $i \in \{1, \ldots, N\}$. Sub-agent $i$ has belief state $M_t^{(i)}$, purposeful state $G_t^{(i)} = (O_t^{(i)}, \Sigma_t^{(i)})$, observation $e_\tau^{(i)}$ at micro-step $\tau$, belief-update map $f_M^{(i)}$, purposeful-update map $f_G^{(i)}$, and policy $\pi^{(i)}: \mathcal X^{(i)} \to \mathcal A^{(i)}$. Each sub-agent is individually Class 1: $M_{\tau^+}^{(i)} = f_M^{(i)}(M_{\tau^-}^{(i)},\, e_\tau^{(i)})$ with no $G^{(i)}$ argument. Composite state $X^c_t = (M_t^c, G_t^c)$ aggregates the sub-states by some specified coarse-graining $\Lambda$ (`#form-composition-closure`). Composite event $e_\tau^c$ is the per-sub-agent event tuple. Composite update $f_M^c$ is the tuple of sub-agent updates plus whatever the routing structure $R_t$ (`#scope-multi-agent`) imposes.

## §2. Route (R1) — Cross-agent direct cross-talk (goal-dependent routing)

**Setup.** Suppose strategic interaction requires direct goal-state transmission between agents — agent $j$ communicates content that depends on $G_t^{(j)}$ to agent $i$ through a channel that does *not* pass through environment-acting action $a^{(j)}_t$. Examples: cheap-talk pre-play communication (Crawford-Sobel 1982), explicit type announcement in revelation-mechanism games (Myerson 1979), pre-commitment via verifiable signaling (Spence 1973), pre-action negotiation in cooperative-game theory.

**Push.** With cross-talk channel $c_{j \to i}: \mathcal G^{(j)} \to \mathcal M_{\text{message}}^{(i)}$, the message agent $i$ receives is $m_{j \to i} = c_{j \to i}(G_t^{(j)})$. Append the message to agent $i$'s event stream: $e_\tau^{(i)} = (e_\tau^{(i),\text{env}},\, \{m_{j \to i}\}_{j \neq i})$. The composite event $e_\tau^c$ then carries $G_t^c$-content directly, *not mediated by past actions*.

The composite update $f_M^c$ applied to $e_\tau^c$ propagates $G_t^c$ into $M_{\tau^+}^c$ structurally:

$$M_{\tau^+}^c \;=\; f_M^c(M_{\tau^-}^c,\, e_\tau^c) \;=\; f_M^c\!\left(M_{\tau^-}^c,\; (e_\tau^{c,\text{env}},\, \{c_{j \to i}(G_t^{(j)})\}_{i \neq j})\right).$$

Conditioning on $(M_{\tau^-}^c, e_\tau^{c,\text{env}})$ (the *environment-mediated* part of the event stream — the part that would be available without cross-talk):

$$I\!\left(G_t^c;\; M_{\tau^+}^c\,\mid\, M_{\tau^-}^c,\, e_\tau^{c,\text{env}}\right) \;\geq\; I\!\left(G_t^c;\; \{c_{j \to i}(G_t^{(j)})\}\,\mid\, M_{\tau^-}^c,\, e_\tau^{c,\text{env}}\right) \;\gt\; 0$$

whenever the cross-talk channel transmits non-trivial information about $G_t^c$ (the channel is not constant-on-goals). The diagnostic $\kappa^c$ measured against the *environment-mediated* event stream is therefore bounded away from zero — Class 3 by the formal criterion.

**Breakdown.** This **does derive Class 3**, but it derives Class 3 from goal-dependent routing, *not* from strategic composition per se. It is exactly the mechanism `#hyp-directed-separation-under-composition` Case 2 already names. Strategic interaction *can* require this (cheap-talk equilibria, mechanism design with reporting); strategic interaction *can also* run without it (Cournot equilibria reached via private price-observation; auctions with private types where the only "signal" is the equilibrium bid). The first welfare theorem of microeconomics is a paradigm case of strategic interaction reaching equilibrium with *no* direct cross-talk — only environment-mediated price information.

**Conditional Class 3 derivation:** Strategic composition + goal-dependent direct cross-talk channel → Class 3 (Coupled) composite.

**Why this is a derived no-go on the *unconditional* claim:** The unconditional "strategic composition → Class 3" claim *cannot* be supported by (R1) because (R1)'s antecedent is not implied by strategic composition. Cournot is a counter-example: partially-opposing objectives, equilibrium reached, no direct cross-talk required, routing remains goal-blind under standard demand-curve observation. By the formal criterion, the Cournot composite is Class 1 (Separated) at the composite level — the same class as its individual agents — even though it satisfies (C-iv) by potential-game equilibrium convergence.

**Cournot witness for the no-go.** Two agents with quadratic profit $O^{(i)}(q_A, q_B) = q_i(a_0 - b(q_A + q_B) - \kappa)$, partially-opposing through the shared price. Each agent observes $(q_A, q_B)$ at the end of each period (standard Cournot information structure). $f_M^{(i)}$ is the Bayes update on the implied demand parameters from observed quantities and prices; no $G^{(i)}$ argument. $f_M^{(i)}$'s output is the agent's posterior on demand parameters and on the other agent's strategy — the *content* of $M_t^{(i)}$ includes a model of $G_t^{(j)}$ (the other's profit-maximization objective), but the *update function* $f_M^{(i)}$ is structurally goal-blind. Routing is goal-blind (both agents see the same end-of-period quantities). Composite $f_M^c = (f_M^{(A)}, f_M^{(B)})$ is goal-blind in $G^c$ at the composite level. **Cournot composite: Class 1 (Separated) by the formal criterion.** This is the counter-example that refutes "strategic composition → Class 3 unconditionally."

## §3. Route (R2) — Rational-expectations equilibrium structural coupling

**Setup.** At a rational-expectations Nash equilibrium, each agent's belief about others' strategies is *correct*. Agent $i$'s belief about $\pi_\ast^{(j)}$ matches the actual $\pi_\ast^{(j)}$, which is the best-response of $j$ under $O^{(j)}$ to its belief about $\pi_\ast^{(-j)}$, etc. At equilibrium, this forms a coupled fixed point: $\pi_\ast^{(i)} = \mathrm{BR}_i(\pi_\ast^{(-i)},\, O^{(i)})$ for all $i$.

At equilibrium, $M_t^c$ encodes the *true* $\pi_\ast^{(-i)}$ for each $i$ (in the relevant slot of $M_t^{(i)}$), which is a function of $\{O^{(j)}\}_{j \neq i}$ via the best-response. Inverting: $\{O^{(j)}\}$ is recoverable from $M_t^c$ via the structure of the equilibrium.

So at equilibrium, *as a structural fact about the equilibrium state*, the composite belief state $M_t^c$ and the composite goal state $G_t^c$ (in its $\Sigma^c$-component, since equilibrium *strategies* are the relevant fixed-point object) are mutually determined. There is a deterministic map $G_t^c \leftrightarrow M_t^c$ at equilibrium.

**Push.** Does this force Class 3 by the formal criterion? The criterion measures the residual information flow $I(G_t^c;\, M_{\tau^+}^c \mid e_\tau^c,\, M_{\tau^-}^c)$, conditioned on $(M_{\tau^-}^c, e_\tau^c)$. The conditioning is the load-bearing piece.

At rational-expectations equilibrium, $M_{\tau^-}^c$ already pins down $G_t^c$ (by the structural map). Conditioning on $M_{\tau^-}^c$ removes most of the entropy in $G_t^c$ to begin with. Both numerator and denominator of $\kappa^c$ become small:

$$H\!\left(G_t^c\,\mid\, M_{\tau^-}^c,\, e_\tau^c\right) \to 0 \qquad I\!\left(G_t^c;\, M_{\tau^+}^c\,\mid\, M_{\tau^-}^c,\, e_\tau^c\right) \to 0$$

The ratio $\kappa^c$ then has a $0/0$ form at equilibrium; the structural coupling between $G^c$ and $M^c$ is *invisible* to the residual-information criterion because it is *already in* $M_{\tau^-}^c$.

This is actually clarifying. The architectural-class criterion measures *additional* coupling beyond what is already encoded in the prior belief state. Coupling that is *constitutive* of the equilibrium state — present in $M_{\tau^-}^c$ before the update — is not coupling the criterion measures. It is structure, not pathway.

**Off-equilibrium push.** Off equilibrium, the coupling becomes pathway-shaped: agents *update* their beliefs about others' strategies based on observed actions. The update $f_M^{(i)}$ takes observed $a_{t-1}^{(j)}$ as input and Bayes-updates the belief about $\pi_\ast^{(j)}$. Each updating step still has no $G^{(i)}$ argument (the Bayes likelihood model $P(a^{(j)} \mid \pi^{(j)})$ is goal-blind, parameterized by $\pi^{(j)}$ which encodes $G^{(j)}$ structurally but is not literally $G^{(i)}$ entering $f_M^{(i)}$). The $G$-content reaching $M_{\tau^+}^c$ flows through the action channel from $G_{t-1}^{(j)} \to a_{t-1}^{(j)} \to e_\tau^{(i)} \to f_M^{(i)}$, which is exactly the action-channel mechanism `#hyp-directed-separation-under-composition` explicitly licenses as *not* a directed-separation violation.

**Breakdown.** (R2) yields no Class 3 derivation. At equilibrium the coupling is constitutive (invisible to the criterion); off equilibrium it is action-channel-mediated (licensed by the criterion). Neither produces a pathway from $G_t^c$ to $M_{\tau^+}^c$ that bypasses $e_\tau^c$ in the way Class 3 requires.

**A subtler finding from (R2).** The equilibrium structural coupling — even though it does not register as Class 3 in $\kappa^c$ — is real and load-bearing. It is what `#scope-composite-agent` (C-iv) calls the *equilibrium structure $\mathcal E$* serving as the composite's macro-state. Strategic composition's actual macro-state $G_t^c$ is **not a state variable in the same shape as a single-agent $G_t$**. It is a fixed-point object — the equilibrium structure $\mathcal E$. The architectural-class criterion was designed to operate on state-variable $G_t$. When $G_t^c = \mathcal E$ is structurally type-different, the criterion is type-mismatched.

This is the entry point to §7 (`02-REFRAME-INSIGHT.md`). For (R2)'s purposes here: the route does *not* yield Class 3, *and* it yields a derived observation about the type-mismatch — which is genuine progress on the right axis, just not on the axis Joseph's question pointed at.

## §4. Route (R3) — Mutual-modeling recursion

**Setup.** In strategic interaction, each agent maintains a model of other agents' models of *its own* policy, of *its own* model of *their* policies, etc. The hierarchy of beliefs (Mertens-Zamir 1985, Brandenburger-Dekel 1993). At level $k$, agent $i$ holds beliefs about $(N-1)^k$ chains of cross-agent models.

The question: does the *iterated* inference compound goal-content into $M_{\tau^+}^c$ in a way the single-step criterion misses?

**Push.** Let $M_t^{(i),k}$ denote agent $i$'s level-$k$ belief — at level 0, agent $i$'s belief about the world; at level 1, agent $i$'s belief about each $j$'s level-0 belief; at level $k$, agent $i$'s belief about agent $j_1$'s belief about agent $j_2$'s ... belief at level 0.

The composite belief state is $M_t^c = \{M_t^{(i),k}\}_{i, k}$ (in principle infinite-dimensional; in practice truncated at some $k_{\max}$).

The composite update $f_M^c$ then is a tuple of per-level updates. Each per-level update is structurally:

$$M_{\tau^+}^{(i),k} \;=\; f_M^{(i),k}\!\left(M_{\tau^-}^{(i),k},\; e_\tau^{(i),k},\; \{M_{\tau^-}^{(i),k-1}\}\right)$$

where $e_\tau^{(i),k}$ at level $k$ is what agent $i$ *infers* about agent $j$'s level-$(k-1)$ belief from observed action $a_\tau^{(j)}$. The level-$(k-1)$ belief argument feeds the recursive estimation.

Crucially, $f_M^{(i),k}$ — the level-$k$ belief update — *still has no $G_t^{(i)}$ argument*. Goal-blindness is per-level. The level-$k$ Bayes update processes incoming evidence (action observations interpreted at level $k$) goal-blindly. The fact that the *evidence* at level $k$ encodes goal-content recursively from levels $k-1, k-2, \ldots, 0$ is *belief-content* property, not a processing-pathway property.

**Where the push runs out.** Iterating goal-blind updates does not produce a goal-dependent update. The composition of goal-blind functions remains goal-blind. The recursion adds *structure* to $M^c$ — the iterated belief hierarchy makes $M_t^c$ exquisitely informative about $G_t^c$ at equilibrium — but it does not add a $G_t^c \to f_M^c$ pathway.

**A genuine subtlety here.** The Mertens-Zamir universal type space construction *implicitly* makes the equilibrium agents' *processing* depend on common knowledge of rationality, which is sometimes presented as a kind of goal-content baked into the model. But this baking is *parameter*-level (it shapes the *equilibrium* the dynamics converge to), not *runtime* — the actual per-step belief update at each level remains goal-blind.

**Breakdown.** (R3) does not derive Class 3. The recursion compounds belief-content but does not introduce processing-pathway coupling.

**Side observation.** (R3) does suggest that for *truncated*-level models (agent computes only level-0 and level-1 beliefs), the composite is *less* informative about $G^c$ than for full-level rational-expectations agents. The dynamic-regime axis — what type of equilibrium the dynamics admit — depends on the truncation depth. This is another angle on the §7 reframing: strategic composition's structure varies along a *dynamic* axis (truncation depth, convergence type, equilibrium concept) that the architectural-class axis does not capture.

## §5. Route (R4) — Shared computational substrate

**Setup.** Some multi-agent compositions share *internal* infrastructure — attention budget, working memory, world-model parameters, or in the LLM case the literal forward-pass tensor that all agents compute on. A canonical example: multi-agent LLM systems where each "agent" is a persona within the same base model (chain-of-thought multi-role prompting). Another: tightly-coupled embedded multi-robot systems with shared sensor processing.

**Push.** Under shared substrate, the composite goal $G_t^c$ shapes resource allocation directly. The shared attention mechanism, for example, allocates compute across sub-agents based on the joint task — which encodes $G_t^c$. The level of attention each sub-agent's $f_M^{(i)}$ receives then varies with $G_t^c$, even though *each* $f_M^{(i)}$ at fixed allocation is locally goal-blind.

Formally: let $\alpha_t = \alpha(G_t^c)$ denote the resource-allocation vector with components $\alpha_t^{(i)}$ for each sub-agent. Then the *effective* $f_M^{(i)}$ used at time $t$ is $f_M^{(i)}[\alpha_t^{(i)}]$ — a goal-blind function indexed by an allocation parameter that itself depends on $G_t^c$. This gives:

$$M_{\tau^+}^c \;=\; \{f_M^{(i)}[\alpha^{(i)}(G_t^c)](M_{\tau^-}^{(i)}, e_\tau^{(i)})\}_i \;=\; \tilde f_M^c(M_{\tau^-}^c,\, e_\tau^c,\, G_t^c)$$

where the third argument $G_t^c$ enters $\tilde f_M^c$ structurally through the allocation map. This is a $G_t^c \to f_M^c$ pathway bypassing $e_\tau^c$. **Class 3 by the formal criterion.**

**Breakdown — but a different kind of breakdown.** (R4) genuinely *does* derive Class 3, but the derivation rests on the shared-substrate condition — *not* on strategic composition. Strategic composition does not entail shared substrate; shared substrate does not entail strategic composition. The two are independent axes that can intersect.

Strategic composition over agents on *distinct* substrates (two firms in Cournot competition; two countries in a security dilemma; two LLM agents each running their own inference) does **not** enter Class 3 by (R4) because there is no shared resource for $G_t^c$ to act through. The Cournot witness from §2 applies again.

Aligned composition over agents on *shared* substrate (a multi-headed neural network optimizing a shared objective) **does** enter Class 3 by (R4) — the shared attention allocates compute based on the shared goal — even though the objectives are aligned. So (R4)'s mechanism cuts orthogonally to the alignment/strategic axis.

**Conditional Class 3 derivation:** Shared computational substrate + composite goal shaping resource allocation → Class 3 (Coupled) composite. Strategic composition is *neither* sufficient *nor* necessary for this condition.

**For multi-LLM systems specifically:** (R4) is the genuine Class 3 mechanism, and it applies whenever the multi-agent system shares the underlying model. Strategic vs aligned objectives is independent. The framework's machinery for Class 3 logogenic agents (`#der-class-coercion-via-wrapping`) is the right tool here — but framed as "shared-substrate Class 3 composite," not as "strategic-composition Class 3 composite."

## §6. Revisiting the current Class 2 claim — is *it* derivable?

Strengthen-first now turns its attention backwards. The four attempts above failed to derive Class 3 from strategic composition alone. What about Class 2 (Partial)? Does the *current* claim survive its own audit?

**The current claim** (`#deriv-strategic-composition` Discussion, `#der-directed-separation` Composite-level inheritance):

> Each sub-agent individually is Separated (its own $f_M^{(i)}$ remains goal-blind with respect to its own $G_t^{(i)}$), but the composite's $(M_c, G_c)$ acquires intrinsic coupling because each sub-agent's $M_t^{(i)}$ includes a model of other sub-agents' policies — which are themselves goal-dependent.

**The conflation.** This passage runs two distinct things together:

(a) The *processing function* $f_M^{(i)}$ takes $G_t^{(i)}$ as an argument. (No, by Class 1 assumption.)

(b) The *content of* $M_t^{(i)}$ encodes goal-information — about other agents' goals $G_t^{(j)}$. (Yes; $M_t^{(i)}$ is the agent's belief about the world, which includes other agents and their policies, and policies encode goals.)

The Class 1/2/3 partition is **structurally about (a), not (b)**. A POMDP belief-state filter that models other agents' goals is still Class 1 in the AAT sense — the processing is goal-blind, the belief content can be anything the agent legitimately learns from observation. Class 2 (Partial) per `#der-directed-separation` means "*some* shared infrastructure, *some* separate pathways" — biological cortex, hybrid AI with separated preprocessing — referring to *processing topology*, not belief content.

**Testing against the formal criterion.** For a composite of Class 1 sub-agents with goal-blind routing, the composite-level $\kappa^c$:

- Each $f_M^{(i)}$ has no $G_t^{(i)}$ argument (by Class 1 individually).
- Routing $R_t$ is goal-blind ($R_t \perp G_t^c$, by assumption).
- Composite $f_M^c$ is therefore goal-blind in $G_t^c$ at fixed $e_\tau^c$.
- $I(G_t^c;\, M_{\tau^+}^c \mid M_{\tau^-}^c,\, e_\tau^c) = 0$.
- $\kappa^c = 0$.

By the formal criterion, **the strategic composite under goal-blind routing is Class 1 (Separated) at the composite level** — same class as its individual agents. The current "Class 2" claim is not licensed by the criterion.

**This is exactly what `#hyp-directed-separation-under-composition` Case 1 already says** — and `#hyp-directed-separation-under-composition` does *not* mention Class 2 anywhere. The Case 1 / Case 2 dichotomy is binary: Class 1 (goal-blind routing) or Class 3 (goal-dependent routing). The "Class 2" stepping-stone the current `#deriv-strategic-composition` and `#der-directed-separation` invoke does not appear in the hypothesis segment that they reference for the framework.

**A second strand of conflation.** Class 2 (Partial) per `#der-directed-separation` is the *within-agent* mixed-pathway case (biological cortex). The "Class 2 composite" claim in `#deriv-strategic-composition` is using "Class 2" in a *different* sense — composite-level partial coupling through cross-agent belief content. Two senses of "Class 2" travel under the same label. The separability-pattern table in `#disc-separability-pattern` row 3 also uses "Class 2 (Partial) — directed separation holds for identified submodules" — a third sense, distinct from both above. **Three distinct senses of "Class 2" circulate currently**, with the framework treating them as if they were one. The cleanest cut after this spike: keep "Class 2 (Partial)" for the within-agent mixed-pathway case (the architectural sense `#der-directed-separation` actually defines), and don't extend it to the composite-level case without a separate definition.

**What is true about the strategic composite that the current Class 2 claim was *trying* to capture.** Strategic composites really *are* different from aligned composites in important ways:

- They admit equilibrium dynamics rather than contraction dynamics.
- Their macro-state is an equilibrium structure $\mathcal E$, not a state-space point.
- Their belief content includes cross-agent goal-imputations that aligned composites do not need.
- They exhibit failure modes (saddle-point equilibria, last-iterate non-convergence, multi-equilibrium selection ambiguity) that aligned composites do not.

These are real differences. They are not, by the formal architectural-class criterion, "Class 2" differences. They are *dynamic regime* differences. §7 (in `02-REFRAME-INSIGHT.md`) is where this lands.

## §7. Interim verdict from §§2–6

Pushed across four routes:

| Route | Yields Class 3? | If conditional, on what? | Strategic-composition-entailed? |
|---|---|---|---|
| (R1) Cross-agent direct cross-talk | Yes | Goal-dependent routing structure | **No** — Cournot is a strategic counter-example |
| (R2) Rational-expectations equilibrium | No (at equilibrium $0/0$; off-equilibrium action-channel) | — | — |
| (R3) Mutual-modeling recursion | No (per-level updates remain goal-blind) | — | — |
| (R4) Shared computational substrate | Yes | Shared substrate + composite goal shaping allocation | **No** — independent axis (cuts across alignment/strategic axis) |

Two conditional Class 3 derivations exist — (R1) and (R4) — both with antecedents *not* implied by strategic composition. The unconditional "strategic composition → Class 3" claim is **refuted by the Cournot witness** (§2 closing paragraphs).

The current "strategic composition → Class 2" claim survives only as conflation between (a) belief-content goal-information and (b) processing-pathway coupling. By the formal architectural-class criterion of `#der-directed-separation`, the goal-blind-routed strategic composite is Class 1 (Separated) at the composite level, same as its individual sub-agents. The "Class 2" label as used in the strategic-composition derivation is **not the same "Class 2"** as the within-agent partial case `#der-directed-separation` formally defines.

What §§2–6 collectively show:

- **A no-go on the architectural axis** for strategic composition: by the existing criterion, strategic composition is class-preserving (Class 1 sub-agents + goal-blind routing → Class 1 composite). Class 3 follows from independent additional conditions (routing dependence or shared substrate), not from strategic composition itself.
- **The current Class 2 claim conflates senses of "Class 2"** that are formally distinct.
- **The inter-segment contradiction** (00-FRAMING §1) is real and is a GUC-rename-residue defect, not a derivation difference.

§7 (`02-REFRAME-INSIGHT.md`) now turns to *what* strategic composition genuinely shifts — the missing axis the framework has been awkwardly trying to fit into the architectural classification.
