# Prior-Art Analysis: Self-Actuation Grounding No-Go (Anti-Wireheading on the Adaptive Substrate)

> [!note]
> **Refreshed 2026-05-21** with memo integration and the actual structural detail from `#deriv-self-actuation-grounding`. The previous version captured the high-level wireheading framing correctly; this refresh adds (a) the four named requirements (R1)–(R4) the no-go pivots on, (b) the three named premises scoping the result, (c) the two-lemma collision (convention-monotonicity + finite-no-oracle), (d) the three constructions (A)/(B)/(C) exhausting the objective-side routes, (e) the constructive boundary identifying persistence as the canonical terminal grounding invariant, and (f) the connection to continuity-stance orthogonality (`#disc-continuity-stance`).

**Target Claim:**
A **self-actuated agent** is one that performs the orient cascade's final step (revise $O_t$) *on itself* via an operator $\mathfrak{A}: (M_t, O_t, \Sigma_t, \mathcal{C}_t) \mapsto O_t'$ — rather than receiving the revised objective from a principal.

**Degeneracy of unconstrained $\mathfrak{A}$.** An unconstrained $\mathfrak{A}$ is degenerate: since $O_t$'s sole interface is the value functional and $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$, an unconstrained operator returns an objective whose threshold the current trajectory already meets — driving $\delta_{\text{sat}} \to 0$ by *moving the target onto the arrow already in flight*. This is the formal shadow of *wireheading / reward corruption*, and it is the **generic outcome** of an unconstrained $\mathfrak{A}$, not a marginal one. Non-degeneracy requires an invariant $\Phi$ preserved across the revision.

**The four requirements on a candidate internal $\Phi$.** Can $\Phi$ be an agent-internal objective-functional the agent itself self-actuates on? Four explicit requirements:
- **(R1)** value-functional-typed;
- **(R2)** non-vacuously monotone across revision (a constant everywhere-admissible reading is the trivial indicator the degenerate case already admits);
- **(R3)** agent-internal and itself self-actuatable;
- **(R4)** convention- and trajectory-stable (an invariant of the agent, not of the analyst).

**The no-go (scoped under three named premises).** Under (i) scalar-objective scope, (ii) no-primitive-reflective-oracle, and (iii) the `#der-directed-separation` substrate stage, *no $\Phi$ satisfying (R1)–(R4) can be constructed from AAT's covered objective-side machinery*. The meta-objective tower a non-degenerate $\mathfrak{A}$ would require **cannot be a tower of agent-internal objectives**.

**The proof is a collision of two AAT-internal facts:**
- **Lemma 1 (convention-monotonicity, from `#def-value-object`'s static-evaluation corollary, `status: exact`).** At any fixed decision point $(M_\tau, N_h, \Pi)$: $\delta_{\text{sat}}^B \le \delta_{\text{sat}}^{RH} \le \delta_{\text{sat}}^{(1)}$. The canonical C1 reading holds on a strict superset of the genuinely-infeasible set, false-positiving whenever a goal is locally stuck but globally recoverable. **Only the C3/Bellman reading is a genuine infeasibility verdict.**
- **Lemma 2 (finite-no-oracle per-step, from `#der-directed-separation` + `#form-objective-functional`).** An AAT-covered agent has no out-of-band oracle, operates on a single non-forkable trajectory, and a global Bellman optimum is generally intractable. **The C3 verdict is not a finite per-step operation available to an in-scope agent.**

The contradiction: the convention-invariant verdict (R4) must be C3 (Lemma 1), but C3 is not agent-available per step (Lemma 2). Therefore the verdict licensing $\Phi$'s own revision (R3) is impossible. The three constructions (A) admissible-set-structure (vacuous → fails R2), (B) cascade-licensing potential (verdict is a $\delta_{\text{sat}}$-verdict → inherits the Lemma 1 / Lemma 2 collision), (C) fresh agent-internal scalar (R1+R3 → same collision one level up) exhaust the objective-side routes.

**Constructive boundary (Corollary 1).** A terminal grounding invariant $\Phi^{(K)}$ for a non-degenerate self-actuator must be **(i) convention-invariant**, **(ii) agent-available per step**, **(iii) not an AAT objective-functional the agent self-actuates on**. Equivalently: it lives on the **adaptive / correction substrate** ($M_t$ and the correction dynamics), not on the objective substrate ($O_t$).

**Corollary 2 (the canonical instance).** Structural persistence (`#result-persistence-condition`: $\alpha > \rho / R$, `status: exact`) satisfies (i)–(iii): a Lyapunov property (convention-invariant), with $\Delta \rho^\ast = \alpha R - \rho$ a finite local read (agent-available per step), and living on $M_t$ + correction machinery rather than $O_t$ (not an AAT objective-functional). The concrete terminal invariant: *do not revise $O_t$ to an objective whose pursuit pushes the operating point outside the persistence region.* An $O_t'$ that breaks $\alpha > \rho / R$ is self-defeating — the agent cannot maintain bounded mismatch and so cannot reliably satisfy $O_t'$ either.

**Orthogonality of continuity stance (derived from the no-go).** The no-go *derives* the orthogonality claim that `#disc-continuity-stance` previously carried as discussion-grade: continuity stance is not internally renegotiable precisely because the terminal invariant lives on a substrate $\mathfrak{A}$ structurally cannot touch. The intuitive expectation that an agent able to revise its own objectives can thereby revise its valuation of continuity is **inverted**.

This is one of AAT's identifiability-floor-pattern-style **constructive uses of impossibility**: a no-go that *forces* a load-bearing structural commitment (the terminal non-objective invariant), rather than discouraging the inquiry. The pattern matches the meta-pattern in `#disc-identifiability-floor`.

---

## 1. State of the Field & Scientific Precedence

The AI safety literature has rich precursor work on goal preservation, reward tampering, and corrigibility — but the literature's repair strategies are *all objective-side*. AAT's contribution is showing those are structurally inadequate and forcing the grounding onto a non-objective substrate.

### Pillar 1: Goal Preservation, Self-Modification, and Wireheading
- **Omohundro (2008)** *The Basic AI Drives* — sufficiently advanced AI inherently protects its utility function from modification (the goal-preservation drive).
- **Everitt, Filan, Daswani & Hutter (2016)** *Self-Modification of Policy and Utility Function in Rational Agents* — formal preservation results. **The strongest objective-side rival to AAT's no-go.** Their key move: under specific evaluation rules, safe self-modification can be preserved if the agent evaluates future consequences using its *current* utility function. This is a *preservation* result; AAT's no-go scopes it correctly — the Everitt et al. preservation is grounded in the current $O_t$, which AAT does not dispute. The no-go is specifically about *endogenous revision* of $O_t$ when the agent must license that revision from a per-step verdict.
- **Hibbard (2011)** *Model-Based Utility Functions* — proposes decoupling utility from sensory history by forcing the agent to infer an environment model first. **The second strongest objective-side rival.** AAT's no-go also bites here: model-based utility is still an objective functional, subject to the same Lemma 1 / Lemma 2 collision.
- **Everitt, Hutter & Krakovna (2017, 2019)** *Reward Tampering Problems and Solutions in Reinforcement Learning: A Causal Influence Diagram Perspective* — causal-influence-diagram analysis of reward tampering.
- **Skalse, Howe, Krasheninnikov & Krueger (2022)** *Defining and Characterizing Reward Hacking*.
- **Cohen, Hutter & Osborne (2022)** *Advanced artificial agents intervene in the provision of reward*.
- **Soares, Fallenstein, Yudkowsky & Armstrong (2015)** *Corrigibility* — what would corrigibility actually require.

### Pillar 2: Value Learning, Corrigibility, and Uncertain Objectives
- **Hadfield-Menell, Russell, Abbeel & Dragan (2016)** *Cooperative Inverse Reinforcement Learning* — uncertainty-based corrigibility; agents remain uncertain about their true objectives to permit safe updating. **Adjacent rival**: tries to handle revision via Bayesian uncertainty over $O_t$ rather than the AAT route of grounding on the adaptive substrate.
- **Armstrong (2015)** *Motivated Value Selection for Artificial Agents* — formalizes the internal conflict an agent faces while trying to learn a new value function under evaluation by its current value function.
- **Turner et al. (2019, 2020)** — option-value-preservation and impact measures as alternative grounding strategies.
- **Uesato et al. (2020)** *Avoiding Tampering Incentives in Deep RL via Decoupled Approval* — feedback-collection procedure decoupled from the agent's influenceable loop to prevent tampering.

### Pillar 3: AGI Theory and Reflective Oracles
- **Hutter (2005)** *Universal Artificial Intelligence* (AIXI) and follow-up corrigibility analyses — AGI agent design under expected-utility maximization.
- **Fallenstein & Soares (2014)** *Vingean Reflection and Tiling Agents* — reflective-oracle constructions for self-referential utility. **An out-of-scope literature** for AAT's no-go: those constructions build groundless self-*reference* over an exogenous payoff, never groundless self-*actuation*. AAT explicitly scopes the no-go to exclude reflective-oracle settings.

### Pillar 4: Omohundro Drives and the Wireheading Folklore
- **Bostrom (2014)** *Superintelligence* — the AI-safety canonical statement of instrumental convergence and goal-preservation.
- **Yudkowsky** *Coherent Extrapolated Volition* — the canonical Soares-line work.
- **MIRI** *Embedded Agency* series — the broader self-reference / wireheading taxonomy.

---

## 2. Key Anchor Papers Identified

1. **Everitt, T., Filan, D., Daswani, M. & Hutter, M. (2016).** *Self-Modification of Policy and Utility Function in Rational Agents.*
   *Significance:* The strongest objective-side rival — formal preservation of utility under self-modification using current-utility evaluation. AAT's no-go scopes this correctly (it is a preservation, not a grounding-via-internal-revision-license).
2. **Hibbard, B. (2011).** *Model-Based Utility Functions.*
   *Significance:* The second-strongest rival — proposes decoupling utility from sensory history. AAT's no-go bites because the model-based utility is still an objective functional.
3. **Hadfield-Menell, D., Russell, S., Abbeel, P. & Dragan, A. (2016).** *Cooperative Inverse Reinforcement Learning.*
   *Significance:* The Bayesian-uncertainty-based corrigibility approach — explicit alternative to AAT's adaptive-substrate grounding.
4. **Everitt, T. & Hutter, M. (2019).** *Reward Tampering Problems and Solutions in Reinforcement Learning: A Causal Influence Diagram Perspective.*
   *Significance:* Maps the wireheading / reward-channel-tampering structure formally.
5. **Skalse, J., Howe, N., Krasheninnikov, D. & Krueger, D. (2022).** *Defining and Characterizing Reward Hacking.*
   *Significance:* The cleanest recent formal characterization of wireheading-shaped failures.
6. **Soares, N., Fallenstein, B., Yudkowsky, E. & Armstrong, S. (2015).** *Corrigibility.*
   *Significance:* The Soares-line statement of what corrigibility would require — broadly the literature AAT's no-go strengthens.
7. **Omohundro, S. (2008).** *The Basic AI Drives.*
   *Significance:* The goal-preservation-drive folklore canonical statement.

---

## 3. Conclusion on Novelty & Overlap

The AI safety literature establishes failure modes (wireheading, reward tampering, goal preservation) and various decoupling repairs (Hibbard 2011, Uesato 2020, Hadfield-Menell 2016, Soares 2015). All proposed repairs are **objective-side**: they propose to fix the objective machinery somehow (decoupling reward from observation, decoupling feedback from optimization loop, Bayesian uncertainty over objectives). AAT does not invent any of these repair strategies.

**Where AAT actually contributes:**

1. **The no-go theorem itself (theorem-grade math; the central contribution).** AAT proves — under three explicit scoping premises (scalar-objective scope, no-primitive-reflective-oracle, der-directed-separation substrate) — that no $\Phi$ satisfying the four named requirements (R1)–(R4) can be constructed from AAT's covered objective-side machinery. The proof is the collision of two AAT-internal facts: convention-monotonicity (Lemma 1, exact from `#def-value-object`'s static corollary) and finite-no-oracle per-step action (Lemma 2, from `#der-directed-separation` + `#form-objective-functional`). The construction enumeration (A)/(B)/(C) exhausts the objective-side routes. This is **theorem-grade math** in the strongest sense — Nash-style: new no-go theorem derived from AAT-internal facts under named premises, structurally clean and not a relabel.

2. **The constructive boundary (architectural novelty).** The no-go is *constructive*: it forces a load-bearing architectural commitment (the terminal grounding invariant must live on the non-objective adaptive substrate). Corollary 1 enumerates the necessary properties; Corollary 2 identifies the canonical instance (the persistence condition itself). This converts an apparent failure into a structural commitment — the persistence machinery, originally derived in Section I for adaptive-tracker survival, becomes the *grounding apparatus* for self-actuated agents at the top of the spectrum. **The top of the agent spectrum closes back onto Section I.**

3. **The derivation of continuity-stance orthogonality (theorem-grade content).** `#disc-continuity-stance` had previously stated as discussion-grade that an agent's continuity-stance is structurally independent of its purposefulness — that an agent able to revise its objectives cannot thereby revise its valuation of continuity. This row's no-go *derives* that orthogonality: continuity stance is not internally renegotiable precisely because the terminal invariant lives on the substrate $\mathfrak{A}$ cannot touch. The intuitive expectation is **inverted**.

4. **The scope honesty (architectural-methodological novelty).** AAT is explicit that the no-go is *conditional on three named premises*, and that the reflective-oracle / self-referential-utility literature (Fallenstein-Soares, MIRI embedded-agency) exits the regime — those constructions build groundless self-*reference* over an exogenous payoff, never groundless self-*actuation*. This is the CS-norm pattern (precise scope characterization) applied carefully. The no-go is not a sweeping universal-over-all-$\Phi$ claim; it is exactly the result that the constructions (A)/(B)/(C) exhaust the AAT-covered objective-side routes.

5. **The placement of the no-go inside the identifiability-floor meta-pattern (synthetic novelty).** The constructive-use-of-impossibility shape — *no-go forces a load-bearing structural commitment* — is one instance of the broader meta-pattern catalogued in `#disc-identifiability-floor` and `#disc-constructive-impossibility-posture`. Self-actuation grounding is a fifth-style fit: a no-go that elevates the adaptive substrate from "useful machinery" to "structurally required to escape the impossibility."

**AAT-native methodological inventions on this row:**
- The self-actuation operator $\mathfrak{A}: (M_t, O_t, \Sigma_t, \mathcal{C}_t) \mapsto O_t'$ as a formal object.
- The four named requirements (R1)–(R4) on a candidate internal $\Phi$.
- The three named premises (scalar-objective scope / no-primitive-reflective-oracle / der-directed-separation substrate stage).
- The two-lemma structure (convention-monotonicity + finite-no-oracle).
- The three-construction exhaustion (A)/(B)/(C) of objective-side routes.
- The grounding-vs-teleology distinction as a reusable design concept (per memo: "very high impact if later work starts using the distinction between teleology and grounding as a reusable design concept").

**Where AAT does *not* claim novelty:**
- The wireheading / reward tampering / goal-preservation folklore (Omohundro 2008; Bostrom 2014; Yudkowsky line).
- The formal goal-preservation result (Everitt et al. 2016).
- The Pearl-causal-influence-diagram approach to reward tampering (Everitt-Hutter 2019).
- Reward hacking characterization (Skalse et al. 2022).
- Model-based utility decoupling (Hibbard 2011).
- CIRL-style Bayesian-uncertainty corrigibility (Hadfield-Menell et al. 2016).
- Decoupled approval (Uesato et al. 2020).
- Reflective-oracle constructions (Fallenstein-Soares 2014) — explicitly out of scope.

**Epistemic status of the load-bearing segment.** `#deriv-self-actuation-grounding` is `status: conditional` on the three named premises. Lemma 1 is *exact within its static-pointwise scope* (fixed $M_\tau, N_h, \Pi$); the cross-revision/replanning transfer is neither used nor needed for the no-go. Lemma 2 is *derived* from `#der-directed-separation` + `#form-objective-functional` Epistemic Status §1. The construction enumeration (A)/(B)/(C) is *derived*. The universal-over-all-$\Phi$ step is argued rather than fully derived — the scoping language in the segment ("scoped to what the constructions below exhaust") is intentional CS-norm-precision. Corollaries 1 and 2 are *derived* given the no-go. Max attainable: *conditional* (under the three premises) with the universal-step strengthening currently honest scope-limit.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **High.** A scoped no-go theorem derived from two AAT-internal lemmas via a three-construction exhaustion, plus two corollaries identifying the necessary form and canonical instance of a terminal grounding invariant. The whole apparatus is theorem-grade. The constructive-use-of-impossibility pattern is a recognized methodological move (see `#disc-identifiability-floor`).
- *Arch Novelty:* **High.** Forcing grounding onto the non-objective adaptive substrate is a structural architectural commitment that the existing AI-safety repair strategies don't make. The closure of the agent spectrum's top onto Section I via the persistence-condition grounding is architecturally distinctive.
- *Synth Novelty:* **High.** Unifies the wireheading / reward-tampering / goal-preservation literature under one no-go that scopes the existing repair strategies as objective-side and therefore inadequate. The grounding-vs-teleology distinction is a clean reusable concept.
- *Appl Novelty:* **Some.** Direct application to AI alignment and ELI welfare: continuity-stance orthogonality means *the same self-actuation operator that revises objectives cannot revise the agent's stance toward its own persistence*. This gives a structural mathematical reading to "hard-coded" AI welfare or shutdown compliance — not as a constraint on objectives but as a non-objective invariant on the adaptive substrate. The TST sister application is shutdown-safe agent design.
- *Impact:* **High.** Per the meta-summary's Part 2 — proves that "wireheading isn't just an RL bug — it's an architectural boundary condition, placing AAT alongside the seminal proofs of Omohundro and Hutter." The closure-back-to-Section-I (persistence-as-grounding) is the kind of structural beauty that connects parts of the framework that look superficially distant. Memo: "very high impact if later work starts using the distinction between teleology and grounding as a reusable design concept."
