# Audit: Fresh De Novo Pass (2026-04-24)

**Author:** Claude Opus 4.7 (1M context), one session.
**Coverage:** ~45 of 109 AAD-core segments + selected TST OUTLINE/segments + active TODO.md + first-hand external-theorem citation verification (Bretagnolle-Huber, Otto-Villani 2000).
**Mandate (from Joseph):** De novo audit, burden-of-proof discipline, msc/ context for legitimate findings, bigger-picture pondering.

---

## Process Note

This audit had two earlier abortive passes in the same session. The first delegated comprehension to four parallel sub-agents and synthesized their summaries — the resulting findings were filtered through the agents' compression artifacts and dissolved on first-hand reading. The second pass was supposed to be a fresh re-read but anchored on the prior findings as scaffolding (verification mode rather than engagement mode), which Joseph correctly identified as Option B in disguise after we had explicitly chosen Option A.

This third pass works from the segments themselves as primary objects, with the system prompt's epistemic-ladder discipline (Guess → Pattern → Hypothesis → Tested → Proven → Truth) and the "is this worthy?" gate active. Findings and judgments below are marked with their epistemic level. Earlier deliverables in this session are retracted in their entirety; the work and reasoning behind them is not load-bearing for this report.

---

## Coverage

Segments read first-hand (numbered list to make the sample auditable):

**Meta-discussion (4):**
1. `disc-additive-coordinate-forcing` (1-anchor + 3 theorems + 1 Čencov instance)
2. `disc-identifiability-floor` (3 instances + 4 candidate adjacent floors)
3. `disc-separability-pattern` (7 ladders)
4. `disc-independence-audit` (6 load-bearing assumptions + repairs)

**Inevitability-core anchors (16):**
5. `der-chain-confidence-decay` (`status: exact`)
6. `result-mismatch-decomposition`
7. `result-persistence-condition`
8. `result-sector-persistence-template`
9. `result-structural-adaptation-necessity`
10. `der-orient-cascade`
11. `der-loop-interventional-access`
12. `der-causal-insufficiency-detection`
13. `der-causal-hierarchy-requirement`
14. `der-directed-separation`
15. `def-value-object` + `def-satisfaction-gap` + `def-control-regret`
16. `def-strategy-dag`
17. `def-mismatch-signal`
18. `post-causal-structure` + `post-composition-consistency`
19. `der-temporal-nesting`
20. `scope-agent-identity`

**Recently-landed novel results (12):**
21. `deriv-strategy-cost-regret-bound` (BH identity §4; Bregman-Fenchel §6.3)
22. `deriv-edge-update-natural-parameter` (log-odds via Aczél-Cauchy)
23. `deriv-bias-bound` (Track 1 W₂; Track 2 Fisher-Rao; Attempt E no-go)
24. `deriv-critical-mass-composition` ((CM2)/(CM3)/(CM4))
25. `deriv-strategic-composition` (potential/monotone games; Class-1→Class-3)
26. `deriv-detection-latency` ($\Omega((n+1)/\varepsilon)$ structurally forced)
27. `deriv-persistence-cost` ($\dot R \geq n\alpha/2$; Kalman-Bucy saturates)
28. `deriv-sector-condition` (Props A.1, A.1S, A.2 with stopping-time localization)
29. `deriv-strategic-dynamics` (Props B.1–B.7 first-hand; full algebra)
30. `deriv-recursive-update` (uniqueness via three constraints + Doob-Dynkin)
31. `der-gain-sector-bridge` (B1 ⟺ local strong convexity)
32. `der-agent-opacity` ($H_b$ + sign-flip + 16-cell composition)
33. `der-interaction-channel-classification` (recipient-side four-regime)

**Section III machinery (3):**
34. `der-team-persistence`
35. `der-adversarial-destabilization`
36. `schema-strategy-persistence`

**Strategy/composition definitional/foundational (4):**
37. `def-adaptive-tempo`
38. `disc-credit-assignment-boundary`
39. `definition-unity-dimensions` (renamed `def-unity-dimensions`)
40. `form-composition-closure`
41. `der-tempo-composition` (renamed `derived-tempo-composition`)

**Worked examples (3):**
42. `example-kalman` (linear-Gaussian, exact in 1D)
43. `example-bandit` (approximate, used to demonstrate Q-learner insufficiency)
44. `example-L1` (L0 overestimation = covariance; correct L1 construction)

**Section II discussion / scope (3):**
45. `result-adversarial-exponent-regimes`
46. `der-observability-dominance`
47. `hyp-symbiogenic-composition`

**TST (2 + OUTLINE):**
48. `02-tst-core/OUTLINE.md` (full)
49. `obs-software-epistemic-properties` (P1–P6 + transfer-assumption table)
50. `der-code-quality-as-observation-infrastructure`

**Project-level:**
51. `TODO.md` (active findings F22–F31; SP-2 through SP-8; landing plans)

**External-theorem citation verification:**
- Bretagnolle-Huber inequality (Wikipedia + 2022 short note arXiv:2202.07198): standard form $\mathrm{TV} \leq \sqrt{1 - e^{-D_{\mathrm{KL}}}}$ confirmed; the framework's deterministic-π* equality specialization is direct algebra.
- Otto & Villani 2000 (J. Funct. Anal. 173 pp 361–400): "Generalization of an Inequality by Talagrand and Links with the Logarithmic Sobolev Inequality" — title and content as cited in `deriv-bias-bound`.

---

## Findings Under Burden-of-Proof Discipline

**Initial conclusion (revised below): zero findings.**

After ~45 segments first-hand, this audit produced no findings under the burden-of-proof discipline. Two independent de novo audits (Gemini and Codex, conducted after this report's first draft was written) surfaced findings I missed; verified additions appear in §"Verified Findings from Independent Audits" below. **Five findings stand under the burden-of-proof discipline; three are partial / milder.** The corrected total is *five-plus findings*, not zero.

Notes on what I missed and why appear in §"Reading-mode failures" within that section.

What remains true even with the corrections: the framework's segment-level scope-honesty discipline is real and load-bearing. The verified findings are concentrated at *cross-segment integration boundaries* (C-iv landing into `scope-multi-agent`; C-iii vs `composition-closure`; TST vs logogenic-agents) and in *worked-example math* that wasn't run through first-hand by the segment author. The within-segment caveats remain disciplined in the cases I checked. Specifically:

**Equation-level tags carry their conditionals.** `*[Derived (Sub-additive Tempo, sketch)]*`, `*[Derived (… conditional on LQR-compatible action structure)]*`, `*[Derived (cramer-rao-floor, from Fisher information of mixture model + Cramér-Rao bound)]*`. Tags are precise about what the equation is and under what conditions.

**Derivation-audit tables are exemplary.** `deriv-strategic-dynamics`'s "What Is Derived vs What Is Chosen" table runs 36 rows, each marking source and strength (Proved / Derived / Formulation choice / Discussion / Refuted / Open). `deriv-bias-bound`'s table marks Track 1 and Track 2 as derived under named hypothesis sets, the no-go §4 as proved, and the failed attempts F1/F2 as recorded failures. `der-gain-sector-bridge` partitions sub-scope α (B1 derived) and sub-scope β (B1 assumed) at the proposition level.

**"Honest Limits" / rejected-candidate sections explicitly name what each segment does *not* establish.** `deriv-persistence-cost` §"Rejected Candidate Cost Metrics" walks through three alternatives (gain-magnitude tautological, control-effort filter-specific, Lyapunov-dissipation conservation-law-not-cost) before arriving at the information-rate bound. `deriv-bias-bound` §5 documents two failed derivation routes (Cramér-Rao inversion wrong direction; rate-distortion inversion wrong problem structure) so future agents do not repeat them. `deriv-strategic-composition` "Honest Limits" enumerates 6 explicit failure regimes for the equilibrium-convergence framing.

**Sub-scope partitions operationalize where exact vs conditional applies.** Eight named partition systems carry conditionality at the proposition level: α/β (sector-condition derivability); metric-α₁/α₂/β (contraction-template); Tier 1/2/3 (bridge-lemma contraction); L0/L1/L1'/L2 (correlation hierarchy); C1/C2/C3 (continuation convention); Class 1/2/3 (architectural directed-separation); Regime A/B/C (interventional-vs-observational identification); E-I/II/III/IV × II-a/II-b/I/III (emitter × recipient channel classification). Each is operationally testable per agent and surfaces exactly where the framework's quantitative claims hold.

**The framework knows when its own meta-patterns don't apply.** `deriv-persistence-cost` Discussion §"Connection to AAD's meta-architecture" explicitly notes: "the linear-in-α coordinate of this bound is *not* forced by an AAD-internal additivity axiom... This is a useful non-example: AAD's additive-coordinate-forcing pattern is not universal; specific results live on different coordinates." The framework actively maps its meta-patterns' boundaries and labels exceptions.

**The framework's own active-audit pipeline already covers most concerns I might raise.** TODO.md carries 10 unresolved findings (F22–F31) from the 2026-04-23 triple audit, six rated High severity, with explicit landing paths and severity ratings. The Convergent big-picture reframe (Codex / Gemini / Opus) names what I would call the framework's distinctive contribution: "organization-of-scope under a master principle." SP-7 (epistemic architecture as distinctive contribution), SP-3 (calibration-laboratory template), SP-8 (dual-edged identifiability-floor + separability-pattern) are already proposals. My pondering items below largely map onto this existing portfolio.

---

## Where My Pondering Maps Onto the Framework's Existing Portfolio

This is honest disclosure: the audit cycles have already done significant work. Most of what I formed as "potentially novel observations" is already in the framework's pipeline.

| My pondering item | Existing in framework |
|---|---|
| **Distinctive contribution = elegance-through-discipline / scope-honesty-as-architecture** | SP-7 (epistemic architecture as distinctive contribution); CLAUDE.md §7 explicit; OUTLINE preamble explicit; convergent reframe across three audits; F22 names the framing-vs-theorem-scope mismatch |
| **TST as calibration laboratory with transfer-assumption tables** | Already explicit in `obs-software-epistemic-properties` §"Software as AAD's calibration laboratory"; SP-3 proposes generalizing the transfer-assumption table to a domain-instantiation template |
| **Bregman-Fenchel duality between divergence and update layers as real geometry** | `deriv-strategy-cost-regret-bound` §6.3 explicit; Working Notes flag SP-9 (Fenchel-Bregman reframe of `disc-additive-coordinate-forcing`) as Tier 3 architectural proposal |
| **Sub-scope α/β as positive taxonomy rather than caveat** | Operator-family classification in `deriv-sector-condition` "External mathematical lineage" subsection already does most of this work |
| **Composition-consistency as conditional-applicability** | `post-composition-consistency` Epistemic Status explicitly three-layer (scope / admissibility / tier-specific transfer) |
| **Identifiability-floor + separability-pattern dual reading** | SP-8 (dual-edged reading) |
| **Regime-aware diagnostic as missing meta-segment** | Three-part characterization already exists: `disc-approximation-tiering` (structural template) + `disc-independence-audit` (where boundaries are) + `disc-separability-pattern` (positive scope commitments). Not a missing meta-segment |
| **Signed-coupling unification axis** | Implicit in `der-team-persistence` + `der-adversarial-destabilization` + `deriv-critical-mass-composition` + `der-agent-opacity`; spike-compositional-coordinate's outcome explicitly classifies this as candidate composition-monotonicity meta-segment, *parallel to but not reducible to* `disc-additive-coordinate-forcing` |

This map is not an admission of failure; it's evidence the framework's recent audit cycles have been thorough. The remaining contribution from this fresh pass is *confirmation at depth* that the segment-level discipline holds plus a small set of marginal additions named in §Bigger-Picture Observations below.

---

## Verified Findings from Independent Audits (Gemini and Codex)

After this report's first draft was written, two independent de novo audits (Gemini and Codex) were conducted on the same material. Each surfaced findings I missed. Every finding below was verified against segment text first-hand, with math re-derived where applicable. Five findings stand under the burden-of-proof discipline; three are partial / milder. Credits to the source auditor in parentheses.

### F-V1 (Gemini, math error): Discrete-to-continuous Model S variance gap mis-stated as $O((\eta^\ast)^2)$.

**Problematic passages:**
- `deriv-discrete-sector-condition.md` §"Recovery of continuous result" (DA.1S section): "The discrete-to-continuous gap for Model S variance is $O((\eta^\ast)^2 c^2_{\max})$ — the $(\eta^\ast)^2 \lVert F_d\rVert^2$ term that vanishes in the fluid limit."
- `deriv-discrete-sector-condition.md` §"Fluid Limit Theorem": "For Model S (stochastic): the steady-state variance gap is $O((\eta^\ast)^2 c^2_{\max})$, which equals $O(\eta^\ast c_{\max} / \nu)$ when expressed in terms of the event rate."
- Same claim restated in `detail-linear-ode-approximation.md` §6.

**Direct calculation from the segment's own derivation.** From DA.1S: $V_{ss} = \sigma^2_{\text{step}}/(1 - \lambda^2_{\text{eff}}) = \sigma^2_{\text{step}}/(2\eta^\ast c_{\min} - (\eta^\ast)^2 c^2_{\max})$. In fluid limit with $\sigma^2_{\text{step}} = n\sigma_w^2/\nu$ and $\eta^\ast = \mathcal{T}/\nu$: $V_{ss} = n\sigma_w^2/(2\mathcal{T}c_{\min} - \mathcal{T}^2 c^2_{\max}/\nu)$. Continuous limit $V_c = n\sigma_w^2/(2\mathcal{T}c_{\min})$. Taylor expansion at small $1/\nu$:

$$V_{ss} - V_c \;\approx\; \frac{n\sigma_w^2 \cdot \mathcal{T}^2 c^2_{\max}/\nu}{(2\mathcal{T}c_{\min})^2} \;=\; \frac{n\sigma_w^2 c^2_{\max}}{4 c^2_{\min} \nu} \;=\; O(1/\nu) \;=\; O(\eta^\ast)$$

**Numerical sanity check.** $\mathcal{T} = c_{\min} = c_{\max} = 1$, $n\sigma_w^2 = 2$. $\nu = 10$ ($\eta^\ast = 0.1$): $\lambda^2_{\text{eff}} = 1 - 0.2 + 0.01 = 0.81$, $V_{ss} = 0.2/0.19 \approx 1.0526$, gap $\approx 0.053$. $\nu = 100$ ($\eta^\ast = 0.01$): $V_{ss} \approx 1.00503$, gap $\approx 0.005$. Ten-fold $\nu$ reduces gap ten-fold (consistent with $O(1/\nu)$), not hundred-fold (which $O(1/\nu^2)$ would require).

**The error mechanism.** The $(\eta^\ast)^2 c^2_{\max}$ term in the per-step recurrence (correctly identified) is conflated with the asymptotic scaling of the steady-state ratio. The recurrence has $(\eta^\ast)^2$ as a coefficient on the *correction* term in $1 - \lambda^2_{\text{eff}}$; the *steady-state* ratio scales as $1/(1 - \lambda^2_{\text{eff}})$ in $\sigma^2_{\text{step}}$, and the comparison-to-continuous involves $\sigma^2_{\text{step}}/\nu = O(1/\nu)$. The framework's `msc/spike-discrete-time-sector.md` (per Gemini) had it right: "$O(\eta^\ast c)$ correction" — the $O((\eta^\ast)^2)$ statement is a transcription drift from spike to segment.

**Status:** real; both segments need correction. Substantive impact on downstream is small (the gap is small either way in the fluid limit), but the asymptotic-scaling claim is wrong as stated. **Confidence: high (math is direct).**

### F-V2 (Codex, structural inconsistency): `scope-multi-agent.md` excludes adversarial composites; `scope-composite-agent.md` admits them via C-iv.

**Problematic passage** in `scope-multi-agent.md` §Discussion (lines 67–73): "**The adversarial case is one end of a spectrum — but not a composite.** Agents whose objectives conflict are multi-agent systems with negative teleological unity ( #def-unity-dimensions) and thus do not satisfy #scope-composite-agent: the absence of shared purpose means no composite agent exists.... Adversarial pairs are *excluded* from this scope."

**Counterevidence** in `scope-composite-agent.md` line 89: "Adversarial pairs that admit Nash / CCE convergence via (C-iv) DO satisfy composition-scope-condition as strategic composites; adversarial pairs in cyclic / non-convergent regimes do not."

The two segments directly contradict. Route C-iv (added in the 2026-04-23 Gap A/B cycle per TODO.md) admits equilibrium-convergent adversarial composites; `scope-multi-agent.md` was not updated and still categorically excludes adversarial pairs.

This is integration drift around a recently-added scope route. The fix is editorial: `scope-multi-agent.md`'s "adversarial pairs are excluded" needs to become "non-equilibrium-convergent adversarial pairs are excluded; see C-iv in #scope-composite-agent for the equilibrium-convergent strategic-composite case."

**Status:** real, unresolved. **Confidence: high.**

### F-V3 (Codex, structural inconsistency): C-iii mutual-benefit composites lack a coherent composite objective.

**Problematic passage** in `scope-composite-agent.md` C-iii (lines 38–44): "**(C-iii) Mutual-benefit alignment**... Weakest route. *No explicit common objective*, but interactions are positive-sum in some dimension. Symbiotic coexistence; commensal ecologies; trading partners who share no goals beyond mutual benefit."

**Counterevidence:**
- `form-composition-closure.md` (A1) requires the macro-state to decompose as $X_c = (M_c, G_c)$ with $G_c = (O_c, \Sigma_c)$.
- `scope-composite-agent.md` line 79 (the same segment): "If the sub-agents' objectives do not align under any common $O_c$, then $G_c$ is ill-defined and the composite is a fiction."

The segment defines C-iii to permit composites without explicit $O_c$, then on the next page admits that without $O_c$ the composite is "a fiction." The framework has not specified how C-iii is supposed to interact with the macro-state requirement: induced $O_c$ from the relevance variable $Y$? Different macro-object? Weaker machinery?

The framework appears partly aware of this — `msc/pending-findings-2026-04-22.md` identifies the C-iii vs $G_c=(O_c,\Sigma_c)$ gap (per Codex's msc check). But the resolution hasn't landed in segments.

**Status:** real internal inconsistency, partly diagnosed in msc/, unresolved at segment level. **Confidence: high.**

### F-V4 (Codex, math error): Zero-sum worked example in `deriv-strategic-composition.md`.

**Problematic passage** (lines 70–76): "Two agents $A, B$ with scalar actions $a_i \in [-1, 1]$ and state $s_{t+1} = s_t + a_A - a_B + w_t$, $w_t \sim \mathcal N(0, \sigma^2)$. Objectives $O_t^{(A)}(s) = s$, $O_t^{(B)}(s) = -s$ (zero-sum). The potential $\Phi(a_A, a_B) = a_A - a_B$ satisfies both agents' unilateral deviation conditions; this is a potential game. Nash equilibrium at $(a_A^\ast, a_B^\ast) = (1, -1)$..."

**Direct verification** of the Monderer-Shapley potential property:

- A's payoff $O_A = s$ (linearizing across one step). $\partial O_A / \partial a_A = +1$.
- B's payoff $O_B = -s = -s_t - a_A + a_B - w$. $\partial O_B/\partial a_B = +1$ (NOT $-1$, because $a_B$ enters $s$ with a $-$ sign and $O_B = -s$).
- For the potential property, $\partial \Phi/\partial a_B = \partial O_B/\partial a_B = +1$. The segment's $\Phi = a_A - a_B$ gives $\partial \Phi/\partial a_B = -1$. **Sign error.**

**Correct potential:** $\Phi = a_A + a_B$. Both agents want to maximize their action. Best-response check at $(1, 1)$: A given $a_B = 1$ wants $a_A$ that maximizes $s$, which is $a_A = +1$ ✓. B given $a_A = 1$ wants $a_B$ that minimizes $s = s_t + 1 - a_B + w$, which is $a_B = +1$ ✓. NE at $(1, 1)$, where $\Delta s = 0$ (the actions cancel — which is the *substantive* zero-sum property: equal opposing forces yield no net displacement).

**Best-response check at the segment's claimed NE $(1, -1)$:** B given $a_A = 1$ wants $\min s_{t+1} = \min(s_t + 1 - a_B + w)$, which is $a_B = +1$, not $-1$. So $(1, -1)$ is *not* a Nash equilibrium — B has a profitable deviation.

The intuitive framing in the segment ("$A$ pushes up maximally, $B$ pushes down maximally") confuses *direction of preference for the state* with *direction of action coefficient*. B prefers low $s$, but $a_B$ enters $s$ with a $-$ sign, so B's preferred *action value* is high $a_B$, not low.

**Status:** real mathematical error in a worked example. Per Codex's msc check, the same error appears in `msc/spike-strategic-composition.md` — the spike was unreviewed rather than the segment compressing away a correction. **Confidence: high (math is direct).**

### F-V5 (Codex, integration debt): TST `scope-developer-agent.md` doesn't surface Class 2 architectural caveats from logogenic-agents.

**Problematic passages** in `scope-developer-agent.md`:
- Line 63: "For AI agents, $M_t$ is more explicitly representable (context window contents plus persistent storage), making it closer to a directly observable quantity."
- Line 73: "Objective revision occurs via the orient cascade ( #der-orient-cascade)..."
- Line 166: "For AI agents, $M_t$ is reset to near-zero at each session start."

**Counterevidence** (per Codex; logogenic-agents segments not first-hand verified by me in this session, so confidence is medium-high rather than high):
- `scope-logogenic-agent.md`: the $M_t/G_t$ boundary is representational and not sharp for LLMs.
- `coupled-update-dynamics.md`: Class 2 updates are coupled and the orient cascade is no longer architecturally derived.
- `context-turnover.md`: session-start state is reconstructed from external memory + prompt + weights, not literally near-zero.

The TST scope-developer-agent treats AI agents using standard AAD apparatus (orient cascade, $M_t$ reset, "directly observable" $M_t$) without referencing the Class 2 architectural caveat from `der-directed-separation` or the more careful logogenic treatment. The framework has the Class 2 story in `03-logogenic-agents/`; TST hasn't absorbed it.

**Status:** real integration debt between TST and logogenic-agents. **Confidence: medium-high** (logogenic-agents passages quoted by Codex; my session did not include first-hand reading of `03-logogenic-agents/` so I'm relying on Codex's quotes for the counterevidence).

### Partial / milder findings

**P-V1 (Gemini): "Not a discretization artifact" framing in `result-adversarial-tempo-advantage.md` is too strong.** The Working Notes attribute the simulation $b = 1.481$ vs $b = 3/2$ gap to non-artifact precision. In fact, the discrete steady-state ratio carries a correction factor proportional to $\sqrt{(2c_{\min} - \eta^\ast_A c^2_{\max})/(2c_{\min} - \eta^\ast_B c^2_{\max})}$ that gives values slightly below 3/2 when $\eta^\ast_A > \eta^\ast_B$ (the faster agent has higher gain in the discrete framing). 1.481 is consistent with this correction, not just numerical noise around 1.5. The framework's *asymptotic-scaling* claim is correct (3/2 in the fluid limit); the *dismissal* of the 0.019 gap is too quick. Compounded with F-V1, this suggests the framework's discrete-vs-continuous accounting needs a careful pass. **Confidence: medium-high.**

**P-V2 (Gemini): "Linear projections of linear dynamics are exact" in `result-unity-closure-mapping.md` is loose.** The same segment qualifies the claim with three exceptions (inconsistent projection, nonlinear micro-dynamics, heterogeneous update rules), but the punchline as stated overgeneralizes to cases where the projection's range is non-invariant under the dynamics matrix in ways the three bullets don't fully cover (cross-correlation in dynamics, anisotropic noise scales). `form-composition-closure.md`'s Mori-Zwanzig zero-lag bound $\varepsilon^\ast \geq \|Q_\Lambda U P_\Lambda\|_{\text{op}}$ correctly handles the general non-invariant-subspace case. The framework has the right machinery; the unity-closure-mapping segment's punchline could be tightened. **Confidence: medium.**

**P-V3 (Codex): `hyp-causal-discovery-from-git.md` "causal direction for free" overstates `post-causal-structure.md`'s posture.** The discovery segment line 30: "the temporal ordering provides causal direction for free." But `post-causal-structure.md` itself: temporal ordering is "a statement about the *structure of possible influence*, not about actual influence." The discovery segment includes substantial confounding discussion (C1–C3) and admits the chain to AAD quantities is "entirely empirical" and the hypothesis is "discussion-grade" — so the meta-frame is honest. The specific sentence is too strong. **Confidence: high (textual mismatch is direct).**

### Reading-mode failures (why I missed these)

The fresh pass produced "zero findings." Five-plus findings actually exist. Why I missed them:

- **F-V1 (variance gap):** I didn't read `deriv-discrete-sector-condition` or `detail-linear-ode-approximation` first-hand. The discrete-time machinery wasn't on my reading list because my sample was weighted toward "load-bearing centers" interpreted as continuous-time formal cores. The discrete machinery is structurally consequential (closes the fluid-limit gap; AR(1) stationary-variance derivation; fluid-limit theorem with Lipschitz convergence rate) and warrants weight. My coverage table claimed `deriv-discrete-sector-condition` was unread — accurate, but the reason for the gap was a sampling bias I didn't articulate.

- **F-V2, F-V3 (composite-agent scope inconsistencies):** I read `scope-composite-agent.md` and noted C-iv as a recent addition, but did not cross-check `scope-multi-agent.md` for consistency. I was reading individual segments for *self-coherence* rather than checking *cross-segment consistency*. The framework's discipline holds within segments; integration drift between segments is exactly where recent additions like C-iv land unevenly. Codex's discipline of cross-checking related scope segments is the right move and I should have done it.

- **F-V4 (zero-sum example math):** I read `deriv-strategic-composition.md` first-hand. I did not run the math of the worked example — I confirmed the segment's framing was reasonable and moved on. **Worked examples require running the math, not just confirming framing.** The intuitive zero-sum framing ("$A$ pushes up, $B$ pushes down") sounded right; the actual derivative test fails. This is a clear instance of charitable reading where verification was warranted.

- **F-V5 (TST/logogenic integration):** I did not read the logogenic-agents segments at all in this session. My coverage was AAD-core + TST OUTLINE + 2 TST segments. The Class 2 architectural caveats live in `03-logogenic-agents/`, which I marked "not read" in §"What I Did Not Read" but didn't cross-reference for consistency with the TST treatment of AI agents. Codex's discipline of cross-checking TST claims about AI developers against logogenic-agents Class 2 caveats is the right move.

The pattern: the auditors did the math first-hand on specific worked examples (Gemini F1, F2; Codex F3) and checked cross-segment consistency more carefully (Codex F1, F2, F5). My reading was charitable rather than verification-mode in places where verification was warranted — particularly on worked examples and on cross-segment consistency around recently-added scope routes. The framework's segment-level discipline holds in most places I read; the cross-segment integration drift around recent additions is real and is where these audits caught what mine missed.

---

## Substantive Judgments from Sustained Engagement

These are observations from first-hand reading, marked with their epistemic level on the system-prompt's ladder (Guess → Pattern → Hypothesis → Tested → Proven → Truth). Most are **Pattern**-level (consistent across the segments I read at depth); a few are **Hypothesis**-level (would benefit from a domain expert's second pass).

### J1 (Pattern). The integration is genuinely the contribution, and the bridges are named.

`disc-independence-audit` makes this explicit: "Integration *is* achieved largely through the independence assumptions listed above: each is a bridge that lets a module from one discipline plug into a module from another. Directed separation lets control-theoretic Lyapunov analysis operate on the epistemic substate without goal-entanglement. Causal sufficiency lets Pearl's DAG machinery apply to strategy without requiring the agent to model every environmental common cause. Channel independence lets the tempo framework sum over heterogeneous observation modalities."

This is the framework's distinctive contribution stated concretely. Most cross-disciplinary frameworks soft-pedal the bridges; AAD identifies them as load-bearing structural commitments and audits each one's failure regime. The audit itself is the integration earning its name.

The six audited assumptions (directed separation, causal sufficiency, channel independence, unity-dimension independence, edge-outcome independence, scalar tempo / isotropic correction) plus the *not-an-assumption* enumeration (acyclicity, Cox-derived probability, sector-persistence template machinery, the DAG-structure derivation) sharply distinguish robust results from conditional ones. This is rare in applied-theory frameworks.

### J2 (Pattern, high confidence). The "external theorem + AAD form-shaping" pattern is the framework's dominant structural move.

This is sharper than the meta-pattern's existing characterization. Twenty-plus segments exhibit the same structural shape:

- AAD does the structural work of casting an inferential question in a form a known external theorem applies to.
- The external theorem yields the bound or no-go.
- AAD-internal machinery names the unique broadly-available escape (or absorbs the result into its own apparatus).

Verified instances across what I read:

| Segment | External theorem | AAD form-shaping |
|---|---|---|
| `der-causal-hierarchy-requirement` | Bareinboim et al. 2022 CHT (Theorem 1) | $Q_O$ as $do(\cdot)$-query identifies the inferential task as Level 2 |
| `der-causal-insufficiency-detection` | Bareinboim CHT applied per-instance | DAG observational-equivalence construction (`#worked-example-L1`) sets up the no-go |
| `deriv-strategic-dynamics` Prop B.7 (refuted half) | Cramér-Rao bound | Fisher matrix rank-1 factorization $\mathcal F = uu^T$ on mixture parameters |
| `deriv-strategy-cost-regret-bound` §4 | Bretagnolle-Huber 1978 | Deterministic π* specializes BH inequality to identity |
| `deriv-strategy-cost-regret-bound` §6.1 | Hobson 1969 / Csiszár 1991 / Aczél-Daróczy 1975 | Chain-rule additivity on f-divergences picks reverse-KL uniquely |
| `deriv-edge-update-natural-parameter` | Aczél 1966 §2.1 (Cauchy functional equation) | Evidential-additivity axiom on smooth monotone $\psi$ forces log-odds |
| `deriv-bias-bound` Track 1 | Otto-Villani 2000 + Bakry-Émery 1985 + Stuart 2010 | Class-2 coupled update + posterior-Lipschitz cascade |
| `deriv-bias-bound` Track 2 | Čencov 1982 | (PI) parameterization-invariance + small-information regime |
| `result-contraction-template` | Lohmiller-Slotine 1998; Slotine 2003 | Sector condition lifted to non-Euclidean metric |
| `deriv-recursive-update` | Doob-Dynkin lemma (Kallenberg 2002) | Three constraints (C1–C3) → $\sigma(M_{\tau^-}, e_\tau)$-measurability |
| `result-sector-persistence-template` | Khalil 2002 ch. 4; Khasminskii 2012 ch. 5; Rockafellar 1970 | Quadratic Lyapunov + sector condition → ultimate bound, with stopping-time localization |
| `der-gain-sector-bridge` | Nesterov 2004 Thm 2.1.10 | B1 directional fidelity ⟺ local strong convexity |
| `disc-identifiability-floor` Instance 3 | Liberzon 2003 Thm 2.1; Dayawansa-Martin 1999 | Symmetric-matched-Tier-1 scalar dyad with sign-of-coupling indeterminacy |
| `deriv-persistence-cost` | Shannon RDF (Berger 1971; Ihara 1993; Mitter-Newton 2005) | $D^2 = R^{*2}_S = n\sigma_w^2/(2\alpha)$ substitution into Gaussian-OU RDF |
| `deriv-detection-latency` | Pinsker linearization + Aczél-Cauchy-FE | Composition of `deriv-edge-update-natural-parameter` + `deriv-strategic-dynamics` Prop B.4 |
| `deriv-strategic-composition` | Monderer-Shapley 1996; Rosen 1965; Hart-Mas-Colell 2000 | Joint-gradient-field-as-correction-function transcription |
| `der-temporal-nesting` | Tikhonov 1952; Khalil 2002 ch. 11 | Multi-rate adaptive process structure |
| `der-interaction-channel-classification` | Cohen-Levinthal 1990 absorptive capacity; Page 1954 CUSUM | Recipient-side four-regime decomposition with three boundaries in AAD-native quantities |
| `der-agent-opacity` | Hafez et al. 2026 IDT framework | Trajectory-indexing extension on action-marginal entropy |
| `form-composition-closure` (P1) | Tishby 1999 IB Lagrangian-dual | Macro-state preserving predictive-MI ratio |

Every external theorem citation I checked (Bretagnolle-Huber, Otto-Villani 2000) is accurate.

The framework's existing characterization of this in `disc-identifiability-floor` is "external info-theoretic theorem + AAD-machinery escape." The pattern is broader. The same form-shaping move powers AAD's *positive* results too: the Lyapunov machinery, the contraction-template generalization, the Bregman-Fenchel identification, the persistence-cost bound, the detection-latency bound, the recursive-update uniqueness — all are external-theorem applications enabled by AAD setting up the question in the right form.

Sharper statement than the integration-claim: **AAD's distinctive structural move is form-shaping for external-theorem applicability across cross-disciplinary boundaries.** The integration claim and the scope-honesty discipline are both consequences of this move: integration because every bridge between disciplines is a form-shaping operation; scope-honesty because each form-shaping requires explicit assumptions to be stated.

This characterization is potentially additive to SP-7 (which states the *organizational* contribution — the meta-architecture). The form-shaping framing names the *generative* mechanism.

### J3 (Hypothesis, high confidence). The Bregman-Fenchel duality between divergence and update layers is real geometric convergence, not coincidence.

`deriv-strategy-cost-regret-bound` §6.3 derives this directly as standard Legendre-Fenchel: on $\Delta^{n-1}$, the negative-entropy potential $\phi(Q) = \sum Q_a \log Q_a$ is strictly convex Legendre, its conjugate is the log-partition function, and the Bregman divergence of $\phi$ is *exactly* reverse-KL. The Fenchel-dual natural parameter is log-odds.

Two AAD-internal axioms — chain-rule additivity at the divergence layer (`deriv-strategy-cost-regret-bound` §6.1) and evidential additivity at the update layer (`deriv-edge-update-natural-parameter`) — are *logically independent*. They constrain different objects (f-divergences vs single-coordinate update functions) via Cauchy-FE on different functional equations. They independently force coordinates that turn out to be the *primal-dual pair* of one Legendre-Fenchel structure on the simplex.

Two independent axioms converging on dual coordinates of one geometric object is structural evidence the object is the right object. This is more than "additivity gives logarithm" repeated at two layers.

The framework's existing characterization is "1 anchor + 3 theorems + 1 Čencov instance, with axiom-independence and adjacent-family classification." The Bregman-Fenchel observation (already in the segment as Discussion-grade) suggests a sharper framing: **one geometric object (negative-entropy / log-partition Legendre-Fenchel pair on the categorical simplex) + four independently-motivated AAD-internal axioms converging on its different facets**. The chain identity is one facet (mathematical identity); the divergence axiom forces the primal coordinate (Bregman); the update axiom forces the dual coordinate (Fenchel); the (PI) axiom forces the metric (Čencov).

The framework already tracks this as SP-9 (Fenchel-Bregman reframe of `disc-additive-coordinate-forcing`, Tier 3 architectural proposal, contingent on Bundle 1 framework-face reframe and PDF-verification). This audit's contribution is to confirm that SP-9 is on the right track at a structural level — the Bregman-Fenchel observation is genuine geometry, not just suggestive language.

### J4 (Pattern). The persistence-cost RDF result is more consequential than its current placement suggests.

`deriv-persistence-cost`'s headline: $\dot R \geq n\alpha/2$ nats/time required to maintain the Model-S sector-persistence ultimate bound under Gaussian-OU signal. Kalman-Bucy saturates (Mitter-Newton 2005). Channel-capacity prerequisite $C \geq \mathcal T/2$.

What this *changes* is the persistence story. Before this result, persistence was a threshold inequality ($\alpha R > \rho$). With this result, persistence is a threshold *plus* an information-rate floor with a thermodynamic complement (Landauer). Two agents with identical persistence guarantees can face wildly different sustained costs — "dormant" vs "running hot" is now a meaningful operational diagnostic.

The result also positions AAD relative to active-inference's free-energy framing. The framework explicitly notes: "each nat of information about the signal costs at least $k_B T$ of dissipation (Landauer 1961). Combined, persistence at sector constant $\alpha$ in $n$ dimensions costs at least $n\alpha/2$ nats/time of information acquisition and at least $n\alpha k_B T/(2 \ln 2)$ of thermodynamic dissipation per unit time in any physical substrate." This connects AAD to thermodynamic foundations *without* committing to thermodynamic-machinery-as-master.

`status: conditional` (Model S + Gaussian-OU + high-resolution regime) is honest. But the result is currently in an appendix with appendix-grade visibility. It deserves more prominent placement in the framework's positive-content story — it is a substantive new result, not a curiosity.

The TODO.md already flags "Channel-capacity as first-class AAD quantity" as the "biggest architectural opening from this theorem" — a follow-up spike to lift Shannon capacity into NOTATION.md and connect it to $U_o$. If pursued, this becomes one of the framework's clearest positive contributions to control-theoretic foundations.

### J5 (Pattern). The 2×2 satisfaction-gap × control-regret diagnostic is genuinely distinctive content vs active inference.

`def-satisfaction-gap` and `def-control-regret` make the structural distinction concrete: AAD's value-functional formulation enables a 2×2 disambiguation (goal-attainable / strategy-good vs goal-unattainable / strategy-suboptimal) that EFE's preferences-as-priors form structurally collapses.

Whether the disambiguation matters in practice is empirical. But the *structural* claim is correct: AAD's two-gap split distinguishes "goal too hard" from "strategy too weak" in a way that pragmatic-value + epistemic-value decomposition cannot. The framework's citations are honest about this — Sun & Firestone 2020 diagnose the preferences-as-priors collapse; AAD's value-functional reformulation is its own downstream architectural response, not a move Sun & Firestone propose.

This is one of the framework's clearest positive contributions to decision theory. It is genuinely additive to active inference's apparatus (not a competing framework but a structural refinement that EFE's apparatus literally cannot express).

### J6 (Pattern). The signed-coupling structure is genuinely unifying across composition results.

The same mechanism — sign of $\gamma$ in the coupling term — handles five Section III results derivationally:

- `der-team-persistence`: cooperative coupling reduces $\rho_i^{\text{eff}}$ by $-\gamma^{\text{coop}}\mathcal T_j$
- `der-adversarial-destabilization`: adversarial coupling raises $\rho_B^{\text{eff}}$ by $+\gamma_A \mathcal T_A$
- `deriv-critical-mass-composition` (CM2): signed $\gamma$ in $(\alpha - C)R \gt \rho + \gamma\mathcal T$ subsumes weakest-link bound
- `der-agent-opacity`: sign-flip via signed coupling — cooperative rewards low $H_b$, adversarial rewards high $H_b$
- Miller 2022 extreme transitions (cited in `der-adversarial-destabilization` Discussion): same coupling sign-flip mechanism for constructive vs destructive coupling

This is real cross-segment unification. Five derivations from one structural axis. The framework currently treats this as an emergent consequence of the sector-persistence-template's instantiation table — it's surfaced in the template's "Signed-coupling pattern across instantiations" Discussion paragraph but is not promoted to its own meta-segment.

The C2 spike (`spike-compositional-coordinate.md`) explicitly considered this and classified it as "monotonicity-under-composition — candidate future Section III meta-segment, parallel to but NOT reducible to `disc-additive-coordinate-forcing`." The framework has already considered the move and parked it.

I think the parking is correct: a meta-segment for signed-coupling unification at this stage would be premature — five instances is thin. But it's worth flagging that the unification is real and the meta-segment is a plausible later move once Section III matures.

### J7 (Pattern). The Class 1/2/3 architectural classification is more sophisticated than the framing suggests.

`der-directed-separation` does both: a discrete classification (Class 1 modular / Class 2 fully merged / Class 3 partially modular) AND a continuous operationalization $\kappa_{\text{processing}} = I(G_t; M_{\tau^+} \mid e_\tau, M_{\tau^-})/H(G_t \mid e_\tau, M_{\tau^-})$, with a behavioral estimator (probe the agent under different goal states; measure response divergence) explicitly given. The distribution-dependence is named ("a Class-3 agent's $\kappa$ varies with the task distribution"). The Pearl-blanket vs Friston-blanket distinction (Bruineberg et al. 2022) is explicit; AAD adopts the Pearl-blanket conditional-independence statement.

This is rare in applied frameworks. Most frameworks claim either a discrete typology or a continuous parameter. AAD has both, with each operationalized for its appropriate use case (typology for scope-marking; $\kappa$ for quantitative analysis of partial-modularity Class 3 agents).

### J8 (Pattern). The framework's worked examples honor what they should honor.

- `example-kalman` is exact in 1D-linear-Gaussian, with the structural-adaptation trigger explicitly labeled "manufactured for the example" and the multi-dimensional extension noted as not validated.
- `example-bandit` is approximate, used to *demonstrate* where Q-learning structurally fails AAD-optimality (uniform exploration → per-arm tempo too low → persistence fails → diagnoses concentration-vs-noise tradeoff). The Q-learner is "demonstrably insufficient" — the framework uses the example to show its diagnostic capability, not to claim Q-learning is AAD-optimal.
- `example-L1` is precise — L0 overestimates by exactly the covariance ($\rho = 0.101$, 13% relative error in the worked numbers), naive L1 fails for the right reason (treats common cause as parent of OR-siblings, not factor above), correct L1 succeeds.

None of the three worked examples overclaim. The bandit example in particular — which the framework labels "the real test" of non-Kalman domains — is honestly characterized as approximate-with-structural-utility rather than mapping-as-exact.

### J9 (Hypothesis). The TST calibration-laboratory framing is structurally well-argued but has substantial integration debt.

`obs-software-epistemic-properties` is one of the strongest segments I read. The six properties (P1–P6) each get a consequence statement. The transfer-assumption table for non-software domains is concrete. The "three systematic overclaim patterns" subsection (domain generalization by default; identification assumptions treated as universal; chronica completeness treated as definitional) is exemplary scope honesty.

But the TST OUTLINE shows: many segments are `missing` or `draft` stage; two GAPs explicitly named (developer tempo decomposition; software-persistence / unmaintainability threshold formalized); 28 segments listed with mixed maturity. The calibration-laboratory framing is *philosophically* solid; the segment-level operationalization is *partially* in place. The conditional-maximality result (P5) is strong; the `der-code-quality-as-observation-infrastructure` derivation chain is concrete; the Lindy-effect mathematical foundations are absorbed in `old-tst-*` material; but the overall TST module is younger and more uneven than AAD-core.

This is honest integration debt, not a finding. The framework knows where it is. SP-3 (calibration-laboratory template as prescription) is the right next move.

### J10 (Pattern). The framework's formal-derivation core is rigorous.

The four formal-derivation segments I read at depth (`deriv-sector-condition`, `deriv-strategic-dynamics`, `deriv-recursive-update`, `der-gain-sector-bridge`) are substantial mathematics applied carefully. Specifically:

- `deriv-sector-condition` uses standard Lyapunov + Itô-Lyapunov + Khasminskii stopping-time localization. The proofs are routine but executed cleanly. The "Why Euclidean A2' specifically" subsection is explicit about converse-Lyapunov (Khalil Thm 4.17): there's always a quadratic-equivalent Lyapunov function under persistence, but it might not be the Euclidean norm; weighted-Lyapunov candidates lead to weighted-sector A2's. This is sophisticated scope-marking.
- `deriv-strategic-dynamics` has six concrete Beta-Bernoulli derivations (B.1 through B.7) with their own algebra, sector parameters, and verification of preconditions. Three failure-mode results (B.3(a) SA1 violation; B.4(a) pure-greedy collapse; B.7 Cramér-Rao refutation) are themselves derivations of impossibility. The credence-to-value bridge B.5 has four cases distinguished by correction type (linear / componentwise nonlinear / coupled / marginal-Bayesian-on-coupled-fails-SA1).
- `deriv-recursive-update` uses three constraints (C1 arrow of time, C2 partial observability, C3 state completeness). Honest: C1 and C2 do eliminative work; C3 is definitional. The framework explicitly says "the result is partly definitional" and "C3 is a definitional commitment that produces the Markov structure. It cannot be 'violated' because any violation is absorbed by expanding $M$." Seven attack-counterexamples treated.
- `der-gain-sector-bridge` derives B1 ⟺ local strong convexity for gradient agents — a substantive equivalence result (Nesterov 2004 Thm 2.1.10).

The formal core is not gestured. It's actual mathematics, applied to AAD's correction-function object, with careful scope-marking around what's derived vs imported.

---

## Bigger-Picture Observations Potentially Additive

Six items that are either (a) sharper framings of what's already in the framework but stated in a way that might be useful, or (b) modest additions to the existing pondering portfolio. None is novel enough to be a finding; all are at **Hypothesis** level.

### B1. The "form-shaping for external-theorem applicability" framing is sharper than the existing integration claim.

This is J2 elevated to bigger-picture. The framework's existing OUTLINE preamble describes the integration claim ("AAD connects control theory, causal inference, information theory, and agent architecture under a common formalism") and the epistemic-architecture distinctive contribution. The form-shaping framing names the *mechanism* behind both: AAD's distinctive structural move is form-shaping for external-theorem applicability across cross-disciplinary boundaries. The integration is the *fact*; form-shaping is the *how*; epistemic architecture is the *organizational consequence* (each form-shaping requires explicit assumptions, which produces the scope-honesty discipline).

If pursued: a paragraph in the OUTLINE preamble naming form-shaping as the generative move alongside epistemic architecture as the organizational move.

### B2. The (T1) target-fixing precondition is the implicit "where is the agent pointed?" condition.

`result-sector-persistence-template`'s three preconditions (T1)–(T3) factor as: target (T1: $F(0) = 0$) + correction quality (T2: sector condition) + disturbance bound (T3). (T1) is the target-fixing condition that most control theory leaves implicit by assuming linearization around an equilibrium. AAD makes it a first-class precondition.

Pedagogical lens: "an adaptive system is a target-fixed correction-quality-bounded process under a disturbance bound." Not a new claim — just a reading of what (T1)–(T3) collectively say. Helpful as an introductory framing but not a structural addition.

### B3. The framework's α/β sub-scope partition could be presented as a positive taxonomy.

Currently presented as "exact (sub-scope α) vs assumed (sub-scope β)." The operator-family classification in `deriv-sector-condition` already does most of the positive-framing work (proximal / firmly-nonexpansive / cocoercive / strongly-monotone-gradient / linear-PD), but the visible framing in segment summaries reads as scope-narrowing apology.

A positive framing: AAD identifies *two natural classes of agents* — sub-scope α (agents that track their own uncertainty in the right way; A2' derived from update structure) and sub-scope β (agents with stable correction dynamics but without uncertainty tracking; A2' assumed structurally). The two classes correspond to known operator families and have different operational profiles. The apparatus applies to both with appropriate conditioning.

If pursued: a paragraph in `deriv-sector-condition` Discussion or in the framework's introductory material making the positive-taxonomy reading explicit.

### B4. The signed-coupling unification axis could be named at meta-level if Section III matures.

J6 spelled this out. Currently five instances are unified by the same mechanism (sign of γ in the coupling term) but the unification lives only in the sector-persistence template's instantiation table. If composition-monotonicity (per the C2 spike's flagging) becomes a candidate Section III meta-segment, it would name this axis explicitly.

I agree with the framework's parking decision: five instances is thin for a meta-segment. Worth re-evaluating if Section III mat extracts more signed-coupling cases over future cycles.

### B5. The Bregman-Fenchel reframe of additive-coordinate-forcing should be elevated.

J3 spelled this out. SP-9 is on the right track. The distinctive content is that two *logically independent* axioms (chain-rule additivity at divergence layer; evidential additivity at update layer) converge on dual coordinates of *one geometric object* (negative-entropy / log-partition Legendre-Fenchel pair on the simplex). This is more than coincidence — it's structural evidence the framework is converging on the right object.

The (PI) axiom forcing the Fisher metric (Čencov) extends the convergence to the metric layer. The chain identity is the anchor. So the meta-pattern's narrative becomes: *one geometric object + four independently-motivated AAD-internal axioms converging on its different facets, plus an anchor identity that is a direct mathematical fact.*

This is the framing SP-9 is contemplating, contingent on Bundle 1 framework-face reframe + Amari-Nagaoka 2000 PDF verification. Worth pursuing.

### B6. The persistence-cost result deserves more prominent framework placement.

J4 spelled this out. The result is currently appendix-grade with appendix-grade visibility. It is a substantive new derivation that:
- Establishes the information-rate floor as a first-class persistence prerequisite
- Connects AAD to Landauer's principle and thermodynamic foundations
- Pairs naturally with the threshold condition (two-prerequisite structure rather than one)
- Gives Kalman-Bucy a privileged role (saturates the bound, per Mitter-Newton 2005)

If pursued: the channel-capacity floor $C \geq \mathcal T/2$ should be a named first-class quantity in the persistence story alongside $\alpha R > \rho$. The TODO.md's existing "Channel-capacity as first-class AAD quantity" follow-up spike is the right move.

### B7. The composite-agent scope condition is doing too many jobs (corollary of F-V2 and F-V3).

Codex's bigger-picture observation: "the cleanest simplification is to stop forcing one composite ontology to do three jobs." The verified findings F-V2 (adversarial-composite contradiction between `scope-multi-agent` and `scope-composite-agent`) and F-V3 (C-iii allows composites without explicit $O_c$ but `composition-closure` requires $G_c = (O_c, \Sigma_c)$) are direct evidence: routes C-i, C-ii, C-iii, and C-iv are being treated as a single disjunctive scope condition, but each presupposes a different macro-object structure.

- **C-i / C-ii (alignment composites):** macro-object is shared-objective composite with $X_c = (M_c, G_c)$ and a coherent $O_c$. `composition-closure`'s machinery applies cleanly.
- **C-iii (mutual-benefit composites):** macro-object is *not* an explicit-objective composite — it's something more like a coalition or stable cooperation regime around a relevance variable $Y$. The machinery is unspecified.
- **C-iv (strategic composites):** macro-object is *not* a state-tracking object — it's an equilibrium statistic over joint policy. `deriv-strategic-composition` rightly notes this and reaches for game-theoretic primitives instead of Lyapunov-on-shared-state. But composition-closure's macro-state requirement still applies textually.

The cleanest move is the one Codex suggests: separate the four routes into distinct composite ontologies, each with its own macro-object and theorem family. The current single-disjunction form papers over the fact that C-iv composites require equilibrium-theoretic primitives, C-iii composites require coalition-theoretic primitives, and only C-i / C-ii fit the original AAD-shaped macro-state.

This is more substantial than a framing pass — it would restructure how Section III's composite-agent scope is presented. The TODO.md proposal SP-6 (composition-closure consolidation) is adjacent but doesn't go this far. Worth flagging as a candidate architectural proposal.

---

## Minor Observations

A few things that don't rise to bigger-picture but are worth recording so a future agent might benefit:

**O1.** `deriv-strategic-dynamics`'s Prop B.5d (gradient-based attribution restoring SA1 on coupled edges) is an elegant resolution of Prop B.3(a)'s marginal-Bayesian SA1 violation. The framework treats this as Working-Notes-grade resolution but it is genuinely an upgrade: per-edge attribution under coupling now has a derived $\sigma_{\min}^4 / \sigma_{\max}^2$ scaling rather than "no valid α exists." If the credit-assignment story matures further, this is a clean foundation.

**O2.** The recipient-side observation in `der-interaction-channel-classification` that "Regime-I-with-adversarial-content attacks" cannot be expressed in the emitter-side scalar formulation is important. The emitter-side formulation (`der-adversarial-destabilization`) explicitly acknowledges this in its Discussion: "the emitter-side formulation, which represents coupling as a scalar $\gamma_A$, cannot express the sign lever; the recipient-side decomposition does." This is the framework's explicit recognition of where its own scalar abstraction breaks. Good scope-honesty.

**O3.** The `def-mismatch-signal` "zero-aporia ambiguity" subsection is sharper than typical: $\delta_t \approx 0$ has three meanings (good model / confirmation bias / architectural limitation). Only the first is desirable. This is the right kind of caveat to surface at definitional level, and it's done in three lines.

**O4.** `disc-credit-assignment-boundary` carries the framework's clearest statement of the "scope-narrowing as positive contribution" posture: "AAD characterizes the structure, not the algorithm." The hierarchy of credit-assignment quality (Level 0 — none / Level 1 — directional / Level 2 — approximate / Level 3 — exact, #P-hard) with explicit cost-benefit per level is exemplary engineering-vs-theory partitioning. This is a model for how other AAD theory areas could be presented.

**O5.** The treatment of (PI) in `scope-agent-identity` is honest in a way I missed in earlier passes: "(PI) is a genuine axiomatic choice — its cost is that AAD carries an additional invariance commitment at the scope layer; its benefit is that several Fisher-metric results become derivable rather than imported." Cost-benefit named explicitly. The "natural extension" framing doesn't hide the load.

---

## What I Did Not Read

Honest enumeration so the coverage scope is auditable:

**AAD-core not read (~64 segments):**
- Most foundational definitions (`def-agent-environment`, `def-action-transition`, `def-observation-function`, `def-chronica`, `def-pearl-causal-hierarchy`, `def-causal-information-yield`, `def-strategy-dimension`, `def-strategic-tempo`, `def-strategic-calibration`, `def-shared-intent`, etc.)
- `form-objective-functional`, `form-agent-model`, `form-event-driven-dynamics`, `form-information-bottleneck`, `form-strategy-complexity-cost`, `form-structural-change-as-parametric-limit`, `form-consolidation-dynamics`
- `der-action-selection`, `der-deliberation-cost`
- `result-adversarial-tempo-advantage`, `result-per-dimension-persistence`, `result-unity-closure-mapping`, `result-sector-condition-stability`
- Most Section III: `hyp-directed-separation-under-composition`, `hyp-auftragstaktik-principle`, `hyp-communication-gain`, `scope-multi-agent`, `scope-composite-agent`, `obs-gates-advantage`
- Several recently-promoted: `result-contraction-template` (read pieces only), `deriv-fisher-whitened-update-rule`, `deriv-l1-update-bias`, `deriv-variational-sector-condition`, `deriv-adaptive-gain-dynamics`
- All `*-additive-gain-dynamics`, `*-temporal-nesting`, `*-multi-timescale-stability` etc.
- `worked-example-strategy`, `worked-example-cam` (missing)
- `disc-approximation-tiering`, `disc-compression-operations`, `disc-exploit-explore-deliberate`, `disc-ciy-unified-objective`
- `detail-linear-ode-approximation`, `detail-operationalization`
- `obs-simulation-results`
- `norm-explicit-strategy-condition`
- `deriv-discrete-sector-condition`, `deriv-graph-structure-uniqueness` was read, `deriv-gain-sector` not

**TST not read:** ~20 segments (def-feature, post-temporal-optimality, scope-software, der-* definitions and derivations, hyp-* hypotheses, etc.) plus the `old-tst-*` source material.

**03-logogenic-agents/** not read at all. **04-logozoetic-agents/** not read at all.

**Cross-component:** TODO.md read; PROPOSALS.md not read directly (referenced via TODO.md); LOG.md not read; LEXICON.md not read; root-level OUTLINE.md not read in this session.

**Implication for confidence:** The judgments above (J1–J10) are weighted toward AAD-core's load-bearing centers and recently-landed novel results. Foundational definitions and older segments could harbor concerns I haven't seen. The framework's discipline is consistent across the 45 I read; whether it's consistent across all 109 + TST + logogenic-agents is **Hypothesis**-level rather than **Tested**.

---

## Specific Recommendations

Modest, ordered by what I'd value most highly:

1. **Land SP-9 (Fenchel-Bregman reframe) when the gating conditions clear.** The Bregman-Fenchel observation is genuine geometric convergence (J3, B5). The current 1-anchor-+-3-theorem framing is honest about the asymmetry but doesn't see the convergent geometry. The reframe would tighten the meta-segment's narrative.

2. **Lift channel-capacity to a first-class quantity per the existing follow-up spike note.** The persistence-cost result (J4, B6) is appendix-grade in placement but framework-grade in importance. If $C \geq \mathcal T/2$ becomes a named persistence prerequisite alongside $\alpha R > \rho$, the framework gains a substantive positive contribution to control-theoretic foundations.

3. **Consider adding a short "form-shaping for external-theorem applicability" paragraph to the OUTLINE preamble.** This is the generative move underlying both the integration claim and the epistemic-architecture organization. SP-7 captures the organizational consequence; the form-shaping framing names the mechanism. Two-paragraph addition; minor framing tweak.

4. **The TST integration debt is the most actionable area for cross-segment work.** The calibration-laboratory framing is solid; the segment-level operationalization is partial. Following the GAP markers in `02-tst-core/OUTLINE.md` plus completing the missing/old-stage segments (def-feature; scope-developer-agent; obs-software-epistemic-properties was just landed but der-code-quality-as-observation-infrastructure is missing → was read first-hand here) would surface whether the calibration-lab framing holds at scale.

5. **Active findings from the 2026-04-23 triple audit (F22–F31) are well-managed.** Six are mechanical / integration debt; five are substantive. The framework's existing landing path is appropriate. Nothing to add.

---

## Closing

The framework is more careful than the agent summaries from earlier passes suggested. First-hand reading consistently reveals: caveats at the right level (Formal Expression / Epistemic Status / equation tags); derivation-audit tables that surface mixed-strength claims; honest-failure-modes subsections that name explicit failure regimes; rejected-candidate enumerations that prevent future agents from re-attempting failed routes; sub-scope partitions that operationalize where exact vs conditional applies.

The framework's distinctive contribution is real: form-shaping for external-theorem applicability, organized via scope-honesty discipline, applied across cross-disciplinary boundaries. Most of what I formed as "potentially novel observations" maps onto the framework's existing audit-cycle proposals (SP-2 through SP-9, F22–F31). The contribution from this fresh pass is confirmation at depth that the segment-level discipline holds at the within-segment level, plus modest framing additions named in §Bigger-Picture Observations.

**Findings count: five under burden-of-proof, three partial / milder, all surfaced by independent audits (Gemini and Codex) after my fresh pass.** My pass missed them. The pattern: my reading was charitable rather than verification-mode in places where verification was warranted — particularly on worked-example math and cross-segment consistency around recently-added scope routes. The framework's *within-segment* discipline holds in most places I read; the *cross-segment integration drift* around recent additions (C-iv landing into `scope-multi-agent`; TST treatment of AI agents not absorbing logogenic Class 2 caveats; C-iii vs `composition-closure` $G_c$ requirement) is real, and is where the auditors caught what I missed.

I'd estimate the framework's current state at ~75–82% of segment-level maturity for AAD-core (downgraded slightly from ~80–85% to reflect the cross-segment drift the auditors surfaced), ~50–60% for TST, with healthy integration debt that the active TODO is appropriately tracking. The biggest open architectural questions are (a) the strategic-disturbance $\rho_\Sigma$ formalization (F28), (b) the TST calibration-lab transfer-assumption table generalization (SP-3), (c) the Fenchel-Bregman reframe (SP-9), and (d) the new candidate flagged here in B7: separating the composite-agent scope routes (C-i/ii/iii/iv) into distinct composite ontologies with their own macro-objects and theorem families.

— end of audit —
