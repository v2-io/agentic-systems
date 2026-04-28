# Audits — 2026-04-22 evening (post-strengthening cycle)

**Purpose.** Three independent de novo audits run *after* the strengthening cycle's commits had landed (`14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`). Each was given the same prompt: audit the current repository state with burden-of-proof on the auditor, prefer in-segment counterevidence to the auditor's first impression, and surface bigger-picture suggestions distinct from the local findings.

The audits' outputs feed into:

- `audits/pending-findings-2026-04-22.md` "Post-strengthening evening batch" section (Findings 16–21)
- `msc/architectural-proposals-2026-04-22.md` "Post-strengthening evening additions" section (O-BP8 through O-BP16)
- `TODO.md` highest-priority cleanups + updated architectural-proposals ordering
- `CLAUDE.md` Theory Character §7 (honesty as architectural principle, surfaced from Opus's closing observation)

The transcripts below are preserved verbatim for transparency about the rescinded-findings tables (each auditor lists candidate findings they checked and rescinded on in-segment counterevidence — the burden-of-proof signal that makes the surviving findings trustworthy).

---

## Codex

I audited `src` first and only then used `msc/` to look for additional material tied to live issues. Four issues clear the burden-of-proof threshold in the current repository state.

**Findings**

1. Section II's headline scope is still broader than its actual theorem scope. Problematic passage: `01-aad-core/src/scope-agency.md:14` says adding causal action "unlocks the interventional and purposeful results of Sections II and III," and `01-aad-core/src/def-agent-spectrum.md:30` calls actuated agents "the full scope of AAD." Strongest counterevidence in `src`: `01-aad-core/src/der-causal-hierarchy-requirement.md:30` explicitly narrows to "learning purposeful agents," and `01-aad-core/src/der-directed-separation.md:84` says exact Section II results apply to Class 1 while Class 2 requires the coupled formulation. Status: still real. The caveats exist, but they are scattered; the repo still lacks one stable Section II entry statement naming the true intersection of agency scope, learning-agent scope, and architectural scope. Confidence: high.

2. Section III still leans too hard on the timescale heuristic relative to what the composition machinery presently proves. Problematic passage: `01-aad-core/src/post-composition-consistency.md:38` calls timescale separation "a reliable practical test" and says the gap to Tier 1 is "small in common settings." Strongest counterevidence in `src`: `01-aad-core/src/form-composition-closure.md:151` says the bridge lemma needs the stronger incremental sector bound, not just A4, and `01-aad-core/src/der-tempo-composition.md:30` says the closure-defect-to-overhead link is still a sketch and may miss additional coordination costs. Status: still real. The local caveats are honest, but `composition-consistency` still speaks as if the practical/theorem gap is minor in ordinary cases without matching derivational support. Confidence: high.

3. The mutual-benefit route `(C-iii)` still does not clearly supply the composite objective/state object that downstream composition assumes. Problematic passage: `01-aad-core/src/scope-composite-agent.md:38` defines `(C-iii)` via a relevance variable `Y` and says there is "No explicit common objective," yet `01-aad-core/src/scope-composite-agent.md:50` lets any of `(C-i)/(C-ii)/(C-iii)` establish composite status. Strongest counterevidence in `src`: `01-aad-core/src/form-composition-closure.md:99` narrows downstream requirements by allowing "simpler goal representations" rather than always a full strategy DAG, and `01-aad-core/src/scope-composite-agent.md:70` correctly states that composition applies only where `O_c` is well-defined. Status: still real. Even with the weaker downstream requirement, current `src` does not show how a merely positive-sum `Y` induces the thin `O_c` needed for `G_c`; the issue is under-specification, not just phrasing. Confidence: high.

4. The coupled/logogenic diagnostic story still overstates operational computability. Problematic passage: `03-logogenic-agents/src/result-coupled-diagnostic-framework.md:18` says the diagnostic quantities "can be computed after each coupled update," and `03-logogenic-agents/src/result-coupled-diagnostic-framework.md:40` gives a direct recipe "From `X^(post)`, compute …". Strongest counterevidence in `src`: `03-logogenic-agents/src/result-section-ii-survival.md:127` says statement-level survival is not "operational extractability" and requires separate instrumentation, and `03-logogenic-agents/src/def-coupled-update-dynamics.md:66` says the `M/G` decomposition is post-hoc, analytical, and not generally computable. Status: still real. The framework has the right caveat elsewhere, but this segment still reads like a runtime recipe for quantities that the repo itself treats as analytically reconstructed and instrumentation-dependent. Confidence: high.

**Unintegrated `msc/` support**

- For the scope seam, `audits/analysis-2026-04-06.md:265` already proposes naming "learning-agent scope," and `audits/2026-03-14-fresh-eyes-assessment.md:57` gives the cleaner sentence: Section II for modular agents, coupled/logogenic analysis for Class 2.
- For the bridge-lemma gap, `spikes/spike-bridge-lemma-contraction.md:5` cleanly states why A4 constrains only the correction component, not the full update map, and `msc/working-composition-admissibility.md:247` treats timescale separation as only a sufficient route, not a near-equivalent theorem.
- For `(C-iii)`, `spikes/spike-composition-correlated-kalman.md:589` already distinguishes objective-composition Cases A/B/C and says only Case A is straightforward, while `spikes/spike-projection-admissibility.md:459` adds the honest "no macro-strategy" option.
- For logogenic diagnostics, `ref/agentic-tft/agentic-tft-evaluation-framework.md:71`, `ref/agentic-tft/agentic-tft-cognitive-loop-spec.md:110`, and `ref/agentic-tft/agentic-tft-narrative-as-implementation.md:106` already push toward the better framing: these quantities are estimated in language with explicit tracking/instrumentation, not directly read out from an internal state object.

**Bigger Picture**

- The repo wants one explicit scope lattice: `adaptive -> agency -> learning-purposeful -> exact Section II modular scope -> coupled/logogenic scope`. A lot of present friction is just this lattice being distributed across segments instead of stated once and reused.
- The repo also wants one explicit three-layer contract for every major claim: `object exists`, `exact theorem transfers`, `quantity is operationally extractable`. Several current seams are really layer-collapses, not mathematical contradictions.
- Composition looks cleaner if treated as typed admissibility rather than one blanket notion of "composite agent": model-only composites, goal-bearing composites, strategy-bearing composites, each crossed with Tier 1/2/3 contraction status. That would make `(C-iii)` usable without forcing every positive-sum system into full `G_c=(O_c,\Sigma_c)`.
- The most promising unification is not "everything reduces to one scalar," but "the same projection/compression shape recurs": `M_t`, `Σ_t`, shared intent, and macro-projection all preserve predictive relevance under bounded loss. That feels like the deepest available simplification without overclaiming.

---

## Gemini

Based on a rigorous, de novo audit of the agentic systems framework in the current repository state (primarily focusing on the `src/` directories of `01-aad-core`, `02-tst-core`, `03-logogenic-agents`, and `04-logozoetic-agents`), along with an integration analysis against the `msc/` directory, here are the findings.

### FIRST PASS: Core Framework Audit

Here are the structural findings evaluated strictly against the current repository state (`src/`):

#### Finding 1: The L1 Repair Mechanism Lacks Formal Persistence Guarantees
- **Problematic Passage:** The framework handles causal insufficiency (correlated failures) by augmenting the DAG with common-cause nodes (L1 repair). However, `01-aad-core/src/example-L1.md` states: *"Sector-condition verification for L1' has not been derived... the full transfer through B.5b is an open item."*
- **Strongest Counterevidence:** `01-aad-core/src/deriv-graph-structure-uniqueness.md` argues: *"The Correlation Hierarchy... provides the practical framework... L0 formal results transfer to correctly constructed L1 DAGs."* Furthermore, `orient-cascade.md` formally relies on L1 augmentation as the structural repair mechanism in step 5b.
- **Status: Still Real.** The framework leans heavily on L1/L1' as the "practical default" to save the DAG's Markov property from causal insufficiency. Claiming that L0 results transfer to L1 while explicitly noting in a worked example that the transfer is "an open item" and "not derived" means a load-bearing pillar of the strategy layer lacks the Lyapunov stability guarantees of the base theory.
- **Confidence:** High.

#### Finding 2: Additive Communication Gain is Naive to Adversarial Game Theory
- **Problematic Passage:** `01-aad-core/src/hyp-communication-gain.md` defines an additive model for trust and communication noise, but admits: *"The additive model captures the defender's response to detected misalignment; it does not model the attacker's optimization over the defender's trust dynamics."*
- **Strongest Counterevidence:** `01-aad-core/src/der-team-persistence.md` explicitly calls out the limitations of channel independence and notes that adversarial dynamics are a recognized sub-domain of Section III.
- **Status: Still Real.** While the text recognizes the limitation, Section III explicitly claims to cover "adversarial dynamics." Providing a formulation for communication gain that structurally ignores an optimizing adversary leaves a massive theoretical hole in any multi-agent adversarial application.
- **Confidence:** High.

#### Finding 3: Logogenic Goal-Conditioning Bias Bound is Unproven
- **Problematic Passage:** In `03-logogenic-agents/src/result-section-ii-survival.md`, the text attempts to bound the bias introduced by LLMs processing goals and observations simultaneously (violating directed separation): *"The bound $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa \cdot H(G_t \mid e_\tau, M_{\tau^-})$ deserves formal derivation... Without this, the bound is order-of-magnitude guidance, not a theorem."*
- **Strongest Counterevidence:** `03-logogenic-agents/src/result-coupled-diagnostic-framework.md` provides a normative workaround: compute diagnostics post-hoc and apply the 2x2 diagnostic table with "awareness that the diagnostics may be biased."
- **Status: Still Real.** For Class 2 agents (like modern LLMs), directed separation fails by definition. If the bias bound is merely an unproven heuristical guess, the entire application of AAD's exact Section II machinery to LLMs rests on a foundation that cannot formally guarantee its own accuracy.
- **Confidence:** High.

#### Finding 4: Causal Sufficiency Necessity is Unproven
- **Problematic Passage:** `01-aad-core/src/deriv-graph-structure-uniqueness.md` notes: *"The necessity direction — no non-DAG structure... can satisfy P1–P4 plus causal sufficiency — is not established here."*
- **Strongest Counterevidence:** The same file immediately mitigates this: *"For practical purposes this gap is unimportant because the proved sufficiency gives a rigorous grounding for the DAG structure... must-if-sufficient-via-this-route."*
- **Status: Already Caveated.** The text correctly lowers its epistemic claim to sufficiency rather than necessity.
- **Confidence:** High.

#### Finding 5: Composition Closure Contraction Assumption
- **Problematic Passage:** `01-aad-core/src/form-composition-closure.md` states: *"the bridge from sector-bounded correction to full-update-map contraction requires an assumption beyond (A4)..."*
- **Strongest Counterevidence:** The same file resolves this via a late-breaking update: *"CHARACTERIZED 2026-04-06... The precise additional condition is the incremental sector bound (DA2'a-inc)... Three agent tiers emerge..."*
- **Status: Already Caveated/Resolved.** The framework explicitly categorizes agents into Tier 1, 2, and 3 based on this exact mathematical gap.
- **Confidence:** High.

### SECOND PASS: Integration Issues from `msc/`

A search of the `msc/` directory reveals that the legitimate issues identified above have been actively investigated but fail to be properly integrated into the canonical `src/` segments:

1. **L1 Sector Condition Transfer (Finding 1):**
   - `spikes/spike-L1-worked-example.md` explores the qualitative tradeoff, noting that *"L1 has lower $\alpha_\Sigma$ (harder to persist) but honest calibration."* However, the formal mathematical transfer of the sector condition to the L1 graph remains absent. The spike confirms the behavioral intuition but fails to close the mathematical gap flagged in `worked-example-L1.md`.

2. **Attacker Optimization vs Communication Gain (Finding 2):**
   - `msc/old-tf-appendix-f-multi-agent.md` lists a specific falsification condition: *"Falsified if: ... a well-tuned fixed trust weight consistently matches or outperforms the adaptive communication gain... This would indicate that the additional uncertainty terms... don't carry usable information."* The theory in `msc/` acknowledges that game-theoretic dynamics might render the additive hypothesis worse than a static heuristic, but this critical vulnerability is not surfaced in the canonical `communication-gain.md`.

3. **Logogenic Bias Bound (Finding 3):**
   - `audits/pending-findings-2026-04-21.md` shows active refinement of this exact issue. It refines the bound to a much tighter information-theoretic form: $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa \cdot I(G;\Omega\mid e,M)$, describing it as a *"strict refinement of the coarser bound in `#result-section-ii-survival`."* The integration issue is that `section-ii-survival.md` is still serving the stale, "order-of-magnitude guidance" bound instead of the tightened formal refinement discovered in the spikes.

### BIG PICTURE SYNTHESIS

Based on this rigorous audit, here is an intuition-driven synthesis on how the framework could be made more beautiful, concise, and fundamental moving forward:

1. **Continuous Parameterization over Discrete Tiering:** The framework currently relies heavily on discrete approximation tierings (L0/L1/L2 for correlation, C1/C2/C3 for value conventions, Tier 1/2/3 for contraction). As hinted at in `msc/architectural-proposals-2026-04-22.md`, these could be unified into a continuous information-geometric space. By treating correlation depth, replanning horizons, and contraction tightness as continuous variables ($\lambda, N_r, \mu \in [0,1]$), the "tier switches" simply become gradient descent over a rate-distortion tradeoff, eliminating the need for rigid boundaries and complex "switch detection" diagnostics.

2. **Unifying $M_t$ and $\Sigma_t$ as Projections:** The strict separation between the epistemic model ($M_t$) and the strategy DAG ($\Sigma_t$) forces immense complexity (like the L1 common-cause node repair). If an agent is viewed purely as a collection of compression maps over its causal history, $M_t$ and $\Sigma_t$ are not distinct objects, but merely two projections of the same causal source tuned to different relevance variables (prediction vs. guidance). This perspective elegantly dissolves the "Class 2 Agent" problem: an LLM's forward pass is simply one holistic compression producing both projections simultaneously, making logogenic agents native to the theory rather than a scope-violating exception.

3. **Population-Level Lyapunov Dynamics:** The sector condition successfully proves persistence for individual agents, but it acts as a behavioral black box. As shown in `spikes/spike-neutral-drift-lyapunov.md`, the sector condition is blind to structural "neutral drift" (agents that behave identically now but will fail differently later). To make the theory truly complete for multi-agent and composition dynamics (Section III), the Lyapunov machinery must be elevated from the agent level to the population level, tracking the *distribution* of correction architectures and endogenous coupling coefficients ($\gamma$) rather than just static bounds.

4. **Natural Parameters for Strategic Dynamics:** The mathematical machinery currently groans under the weight of probabilities bounded at $[0,1]$ (leading to the $O(1/n)$ bias observed in the spikes). By shifting the strategy DAG update rules entirely into log-odds (natural parameter space) and defining mismatch $\delta$ via KL-divergence, the sector condition, update gain, and tempo would collapse into a single, elegant concept: natural gradient descent on a Riemannian manifold. This would make the mathematical core vastly more concise and inherently robust to the edge cases currently requiring extensive patching.

---

## Opus

### Honest summary first

I read the core Section I backbone (scope-condition, persistence-condition, sector-persistence-template, information-bottleneck), the Section II load-bearing segments (directed-separation, strategy-dag, graph-structure-uniqueness, causal-insufficiency-detection, strategic-dynamics-derivation including Props B.1–B.7 and B.5 bridge, identifiability-floor, loop-interventional-access, complete-agent-state, satisfaction-gap, orient-cascade, strategy-complexity-cost, worked-example-L1), the main Section III assembly segment (composition-closure), and the TST spine (software-epistemic-properties, temporal-optimality, developer-as-act-agent, specification-bound, change-expectation-baseline, exponential-cognitive-load, dual-optimization, causal-discovery-from-git). I also ran an Explore agent over the remaining Section III composition segments.

What the audit actually finds, honestly: The framework is unusually well-caveated. Nearly every potential issue I noticed is either (a) already flagged in TODO.md, (b) tagged with an honest epistemic label within the segment, or (c) explicitly discussed in Working Notes. The 2026-04-21 / 2026-04-22 strengthening cycles appear to have done exactly what they claimed. Several "findings" I formed during reading collapsed under in-segment inspection.

Three legitimate findings survive the burden-of-proof test. One is subtle and I don't think is tracked anywhere; two are minor honesty-of-label issues, one of which is already tracked.

### Finding 1 — KL-form "non-degeneracy" claim in #form-strategy-complexity-cost is misleading

**Confidence: medium-high. Still real. Not tracked in TODO.**

Problematic passage at `01-aad-core/src/form-strategy-complexity-cost.md:42`:

$$\Sigma_t^\ast = \arg\min_{\Sigma_t} \left[\, I(\mathcal C_t;\, \Sigma_t) \;+\; \beta_\Sigma \cdot D_{\mathrm{KL}}\bigl(Q_{\Sigma_t}(\pi \mid M_t) \,\big\Vert\, \pi^\ast(\cdot \mid M_t)\bigr)\right]$$

And line 55: "The two forms agree in the limit where the DAG encoding is rate-distortion optimal and the policy posterior is sample-recoverable; the operational form is the one an agent actually runs. The theoretical form places the objective on the same variational frontier as $M_t$, shared intent, and composition projection, with the KL-form relevance term resolving the Shannon-zero degeneracy that arises under deterministic $\pi^\ast$."

And Epistemic Status line 123: "The variational form replaces an earlier Shannon-MI form … which had a Shannon-zero degeneracy: when $\pi^\ast$ is a deterministic function of $M_t$ (the standard scope), Shannon mutual information to a constant vanishes identically, collapsing the objective to $\arg\min \operatorname{DL}(\Sigma_t)$. The KL form does not have this degeneracy."

**The technical issue.** Per line 42, $Q_{\Sigma_t}(\pi \mid M_t)$ is "the action distribution induced by the strategy DAG given the current model state" and $\pi^\ast(\cdot \mid M_t)$ is "the optimal-policy reference." The segment explicitly allows $\pi^\ast$ deterministic given $M_t$.

When $\pi^\ast(\cdot \mid M_t) = \delta_{a^\ast(M_t)}$ is a point mass:

$$D_{\mathrm{KL}}(Q \Vert \delta_{a^\ast}) = \begin{cases} 0 & \text{if } Q = \delta_{a^\ast} \\ +\infty & \text{otherwise} \end{cases}$$

because $D_{\mathrm{KL}}(Q \Vert P)$ requires the support of $Q$ to be contained in the support of $P$. So the KL form does have a degeneracy under deterministic $\pi^\ast$ — a different one from the Shannon-zero degeneracy, but arguably worse for the intended purpose: instead of collapsing to $\arg\min\mathrm{DL}$, the objective becomes a hard constraint ($Q$ must match $\pi^\ast$ exactly) with no graded measure of "how close" a sub-optimal $\Sigma_t$ is to the optimum.

For a genuinely graded divergence from a deterministic optimum, the correct direction is reversed:

$$D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log Q_{\Sigma_t}(a^\ast \mid M_t)$$

which is finite and grades continuously in the probability mass $Q_{\Sigma_t}$ places on the optimal action.

**Suggested repair.** Either (a) reverse the KL direction to $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$, (b) explicitly treat $\pi^\ast$ as a Boltzmann-softmax-over-$V_{O_t}$ distribution (which avoids deterministic support and makes either direction finite and graded), or (c) acknowledge the deterministic case requires additional smoothing and present the KL as one of several admissible variational shapes.

### Finding 2 — #scope-developer-agent frontmatter status: exact conflicts with internal labels

**Confidence: high. Still real. Already tracked (TODO Finding 14).**

Problematic passage at `02-tst-core/src/scope-developer-agent.md:4`: `status: exact`.

Internal Epistemic Status at lines 160–162: "This is a definition — it names the correspondence between software development entities and AAD formal objects. The mapping is exact in the sense that each AAD quantity has a concrete, identifiable software counterpart. The definition itself is not a truth-claim; the substantive claims come from applying AAD's derived results… The observation channel tables and action classification are discussion-grade taxonomies — useful organizing structures, not exhaustive or formally derived."

The frontmatter appears to use "exact" in the sense "the mapping is well-defined," but this is a category error — frontmatter status is for claim strength across the segment, not for definitional cleanness of a correspondence.

(Already tracked. Surfaced because the frontmatter is the single most-scannable epistemic signal in the repo, so the mismatch has outsized blast radius for fresh readers.)

### Finding 3 — #disc-identifiability-floor meta-pattern status is self-contradictory between frontmatter and internal text

**Confidence: medium. Ambiguous. Not tracked.**

Problematic passage at `01-aad-core/src/disc-identifiability-floor.md:4`: `status: robust-qualitative`.

Internal Epistemic Status at line 95: "*Robust qualitative.* The meta-pattern itself is a *discussion-grade* observation: two derived instances exist… each is a legitimate no-go via external theorem. Whether the pattern is a *generative principle* — whether future AAD work will systematically encounter and derive more instances — is a *hypothesis* that the adjacent open floors test."

Then line 99: "Max attainable: *robust qualitative* for the meta-pattern (it is a presentational organizing principle, not a derivation)."

Within a single Epistemic Status paragraph, the segment labels the meta-pattern three different ways: (i) robust-qualitative (opening word), (ii) discussion-grade ("the meta-pattern itself is a discussion-grade observation"), and (iii) hypothesis ("whether the pattern is a generative principle … is a hypothesis"). The frontmatter chooses (i).

### Findings that DID NOT survive the burden-of-proof test (reported for transparency)

| Initial concern | Why rescinded |
|---|---|
| #der-loop-interventional-access status exact but heavily caveated | The Epistemic Status at line 32–34 carefully scopes "exact" to data availability, not identification strength. Honest narrow-scope exact claim. |
| #def-strategy-dag "L0 results transfer exactly to L1/L1'" overclaims | The Correlation Hierarchy table (lines 99–101) makes explicit that L0/L1/L1' have different $\alpha$ values (three-way, three-way, five-way gating). A careful reader disambiguates. |
| #der-causal-insufficiency-detection no-go generality | Explicitly tiered: exact for shallow strict-prerequisite, robust qualitative for general. Working Notes acknowledge the general construction hasn't been carried out. |
| #def-satisfaction-gap convention-relativity | Already tracked in TODO.md lower-priority list and in-segment Epistemic Status. |
| #obs-software-epistemic-properties P5 "conditional maximality" as empirical claim about current tooling | Explicitly scoped to "current standard team protocols"; held at Empirical Claim tier; Working Notes flag the property-table-walk vs. uniqueness-theorem gap. |
| Software as "richest AAD testbed" | Already caveated (line 84) and tracked (TODO Finding 15). |
| Section III Explore-agent's six findings | Five of six have in-segment acknowledgment (bridge-lemma Tier scoping, disjunctive scope flagged in Working Notes, two-axis closure flagged in unity-dimensions Working Notes, etc.). The remaining one (tempo-composition not explicitly referencing composition-scope-condition) is implicit via the #form-composition-closure dependency — borderline finding, low-priority editorial. |

### The bigger picture — where this framework wants to go

**A. The sector-persistence template is the real center of gravity.** The 2026-04-21 factoring of #result-sector-persistence-template was the single most consequential architectural move in the recent cycles. Six persistence-flavored results collapse into one Lyapunov argument with six different effective-disturbance decompositions.

Natural generalization: the template's state variable $\xi$ is always a projection defect — model mismatch is $\Omega$-projected-to-$M$, strategic mismatch is truth-projected-to-edge-credences, closure defect is micro-projected-to-macro, adversarial destabilization is target-projected-to-observable. The disturbance is always the rate at which the projection target shifts faster than the projection can track. This would make the framework readable as: **"An adaptive system is a projection whose contraction rate exceeds its target's drift rate."** This single sentence might be a stronger organizing principle than the current "adaptation and actuation dynamics" framing. Every named defect in AAD — $\delta$, $\delta_\Sigma$, $\delta_s$, $\delta_c$, $\varepsilon^\ast$, $e_m$, $U_o$, $U_M$, IB compression cost — is a projection-fidelity measurement.

**B. The four stratified ladders want to be named as one.** L0/L1/L1'/L2 (correlation), C1/C2/C3 (convention), Class 1/2/3 (architecture), Tier 1/2/3 (contraction), A/B/C (identification regime), adaptive/agency/composite (scope) — all have the same shape: separable-core → structured-repair → general-open. The #disc-identifiability-floor segment has named half of this pattern (the no-go half). The positive half is implicit everywhere and named nowhere. TODO's C-BP2 proposes this as "master separability pattern."

**C. Observability is a master variable waiting to be surfaced.** Once I'd read Prop B.7's refutation under unobservable $C$, the identifiability-floor framing of "observability-as-information-augmentation," P4 in #deriv-graph-structure-uniqueness (observable intermediates), P6 in #obs-software-epistemic-properties (agent-controlled $U_o$), B.2 vs B.3 (observable vs unobservable intermediate), and #der-observability-dominance — a unified picture emerges:

Every structural AAD move is ultimately about what's observable to whom, at what cost. Identifiability is observability-of-parameters. Directed separation is observability of $G_t$ to $f_M$ (forbidden). Loop interventional access is observability of causal structure via action-contrast. Shared intent is observability of composite $O_c$ to sub-agents. Code quality is observability of intent to future developers.

A single segment (or a reorganization around) "Observability: what can be seen, at what cost, with what identification strength" might re-center the whole theory. It would subsume #scope-edge-update-causal-validity (regime A/B/C), #der-observability-dominance, parts of #scope-agency, #der-directed-separation's $\kappa_{\text{processing}}$, and the identifiability floor instances — all of which are currently presented as distinct machinery.

**D. The theory currently lacks a master "resource budget" variable.** Bounded rationality appears piecewise: cognitive cost of $\Sigma_t$ (IB/MDL); deliberation cost; update gain's implicit dependence on agent capacity; context window constraints for LLMs; description length limits for strategies. But there's no single $B_t$ (budget) variable that the agent allocates across $(M_t, \Sigma_t, O_t)$ maintenance. Introducing one would let you derive, rather than separately postulate, quantities like $d^\ast$, $\eta^\ast$'s dependence on capacity, $\beta_\Sigma$'s calibration, and the compression ratios across the four IB instances.

Pragmatic suggestion: a #resource-budget segment with $B_t$ as the master variable, from which $\mathrm{DL}(\Sigma_t) + \mathrm{DL}(M_t) + \mathrm{DL}(O_t) \leq B_t$ is a constraint, and the three compressions are a joint allocation problem. This is adjacent to O-BP7 (known structural absences) in TODO.

**E. The Cox-parallel for graph-structure is explicitly incomplete — and possibly reachable.** #deriv-graph-structure-uniqueness is sufficiency-only. Cox's theorem is necessary-and-sufficient. The necessity direction for AAD would be: any non-DAG structure satisfying P1–P4 plus causal sufficiency is isomorphic to a DAG. Alternative graphical models (factor graphs, junction trees, chain graphs) encode different independence relations; the question is whether the specific independence relation forced by P1–P4 + causal sufficiency requires DAG semantics. I suspect this is provable via Lauritzen's characterization of Markov properties on different graph classes. It would elevate graph-structure-uniqueness from "as strong as current form permits" to a full Cox-style result.

**F. The framework is Section-I-strong, Section-II-backbone-strong, Section-III-sketch.** The asymmetry is honestly acknowledged in the 01-aad-core/OUTLINE.md preamble. But there's a natural move that could pull Section III up: composition closure is the sector-persistence template applied to a projection defect, which is itself a compression operation, which has the same IB shape as $M_t$, $\Sigma_t$, and shared intent ( #disc-compression-operations gets close to this). If the four compressions are unified under one variational problem, and the six persistence results are unified under one Lyapunov template, then composition emerges as a third application of the same machinery rather than new theory. This is O-BP1 + O-BP2's natural extension.

**G. Two presentational moves that would be disproportionately valuable.**

1. Per-segment "what's derived vs. chosen vs. assumed" table at the top. #deriv-graph-structure-uniqueness has one (line 154–165) and it's the clearest epistemic signal in the whole repo. A compact version in every derivation-type segment would save future agents (and readers) hours.
2. A "minimal proof of viability" worked example that hits every Section I/II result. #example-L1 is the closest thing but is scoped to the correlation hierarchy. A single worked example — say, a literal two-service deployment with specified $\rho$, $\mathcal{T}$, $\Sigma_t$ — that instantiates every major AAD quantity concretely would crystallize the claim "this is a theory of real agents, not a formal game."

### One closing observation

The most striking thing this audit surfaced is not a finding but a characteristic: **the framework's honesty is load-bearing.** Segments that would be overclaimed elsewhere are scoped, tiered, and Working-Noted here. The 2026-04-22 #disc-identifiability-floor move is a beautiful example: it takes what would be embarrassing negative results (we can't do X, we can't do Y) and reframes them as structural features that strengthen the machinery that can escape the floor. This is the epistemic stance the framework is actually organized around, and it deserves a first-class place in the top-level outline rather than only in the late-cycle meta-segment. **The theory's conservatism is not a limitation — it is the theory's architectural principle.**
