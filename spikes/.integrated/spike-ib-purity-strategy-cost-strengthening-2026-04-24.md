---
slug: spike-ib-purity-strategy-cost-strengthening-2026-04-24
type: spike
status: draft
date: 2026-04-24
---

# Spike: "Abandoned IB Purity"? — Strengthening the Strategy-Cost Objective

**Charter.** Gemini has characterized the strategy-cost history as "Shannon zero → forward-KL infinity → reverse-KL fix," with the last step described as *abandoning standard Information Bottleneck purity*. The current AAD position (segment `#deriv-strategy-cost-regret-bound` plus meta-segment `#additive-coordinate-forcing`) treats reverse-KL as forced by a two-part argument: direction forced by regret-bound vacuity of forward-KL, specific form forced by a chain-rule additivity axiom via Cauchy's functional equation. This spike audits Gemini's framing against the current state, then attempts to strengthen the result beyond its current home.

The test is not whether the current segment is defensible (it is). The test is whether a stronger story — one that *reclaims* IB purity rather than conceding a departure from it — is available under the strengthen-before-soften posture.

**Outcome in one sentence.** Gemini's "abandoned IB purity" framing is a **mischaracterization**, not a load-bearing critique. Under the right reading of what "IB" means for a decision problem, reverse-KL is the *canonical* IB objective, not a departure from it — with the anchor supplied by Tishby-Polani 2011 (Path 1 below) and a second anchor supplied by rate-distortion with an action-value distortion (Path 3). Three additional strengthenings (Paths 4, 5, 6) yield concrete new results: a **Savage-style uniqueness route** bypassing the chain-rule axiom, a **matched lower bound** for the regret inequality at the operating point, and a **no-go result** that no symmetric f-divergence combined with standard IB can give a degeneracy-free decision-consistent cost under deterministic $\pi^\ast$. Path 7 (mirror-descent / Fenchel duality) closes the geometric story: reverse-KL on the policy simplex *is* the Bregman divergence dual to the natural-gradient direction forced by `#deriv-edge-update-natural-parameter`. The result as a whole: the strategy-cost objective sits at the intersection of four independent forcing arguments, not one. The segment can be meaningfully strengthened and the "departure from IB" framing can be replaced with "IB for decision problems."

---

## §0 — Honest audit of Gemini's "abandoned IB purity" framing

Three ways to read the charge, in increasing generosity:

**(A) Naive reading: "standard IB uses $I(T; Y)$; reverse-KL is not a mutual information."** False as stated. Standard IB is
$$\mathcal L_{\text{IB}} = I(X; T) - \beta \cdot I(T; Y)$$
with *both* terms mutual informations. AAD's strategy-cost objective, as the segment now stands, replaces $I(T; Y)$ with $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$. So in the narrow-surface sense, the relevance term is indeed not a mutual information; it is a divergence to a target. The charge is *superficially* correct at the level of the symbols.

**(B) Structural reading: "IB's relevance term measures *shared information* between the compression and the target; reverse-KL measures *distance*, which is a different thing."** This is the strongest form of the charge. Information-theoretic IB is about *preserving* information about $Y$; reverse-KL is about *matching* $Q$ to a target $\pi^\ast$. The two quantities have different operational interpretations — IB is a channel-capacity / rate-distortion quantity, reverse-KL is an estimation / coding-excess quantity.

**(C) Deepest reading: "IB purity commits you to the $Y$-is-observable / $Y$-is-distributional framing, and reverse-KL tacitly commits you to $Y$-is-deterministic / $Y$-is-an-action-target — a structurally different problem."** This reading is substantive. It maps to the *control-as-inference vs state-estimation-as-inference* split that actually matters in the literature.

**Response.** Reading (A) is cosmetic and refutable by inspection. Reading (B) is the apparent substance, but it folds into Reading (C) on closer inspection — the "distance vs shared info" contrast is downstream of the decision-problem vs estimation-problem contrast. Reading (C) is the one worth engaging, and it is *where the strengthening lives*: there is a well-developed line of work (Tishby-Polani 2011; Rubin-Shamir-Tishby 2012; Levine 2018; Ortega-Braun 2013; Still 2009; Genewein-Leibfried-Grau-Moya-Braun 2015) in which "IB for decision problems" naturally produces reverse-KL-against-policy-target rather than $I(T; Y)$. This is not an *abandonment* of IB; it is the *application* of IB to a decision problem rather than an estimation problem.

The strengthening: the segment should position reverse-KL not as "the direction-forced f-divergence that survives degeneracy under deterministic $\pi^\ast$," but as "the IB relevance term for the decision-theoretic relevance variable, which is forced by the problem structure to be reverse-KL against $\pi^\ast$." The chain-rule-additivity argument then becomes a *second* line of forcing (closing uniqueness at the divergence level), not the sole line.

**Honest caveat.** I have not exhaustively verified every citation below against PDFs. Tishby-Polani 2011 is in the AAD `ref/` directory for other purposes but not as a titled entry; I am working from textbook-level familiarity with its content (the Tishby-Polani objective is $\max_{\pi} \mathbb E[R(X, A)] - \beta^{-1} I(\Pi; X)$ in the standard statement, where $I(\Pi; X)$ is policy complexity — this is reverse-KL in disguise; §1 below derives the equivalence). Rubin-Shamir-Tishby 2012 ("Trading value and information in MDPs") makes the reverse-KL-as-IB-for-control formulation explicit. Levine 2018 ("Reinforcement learning and control as probabilistic inference: tutorial and review") develops the control-as-inference story with reverse-KL against a policy target throughout. The structural claim I rely on — that reverse-KL-against-policy-target is *the* canonical IB formulation for decision problems, not a departure — is well-established in that literature. If the specific citation quality matters load-bearingly for segment promotion, a PDF verification pass is needed.

---

## §1 — Path 1: Reverse-KL as the IB-for-Control Lagrangian (Tishby-Polani 2011 recovery)

**Target.** Show that the reverse-KL form is not a *departure* from IB but the *application* of IB to a decision-relevance problem.

**The construction.** In the Tishby-Polani "Information theory of decisions and actions" (2011) framework, an agent trades expected reward against the information-theoretic cost of the policy. The objective is

$$\pi^\ast = \arg\max_\pi \Bigl[\mathbb E_{x \sim p(x)}\mathbb E_{a \sim \pi(\cdot \mid x)}[R(x, a)] - \tfrac{1}{\beta} I(\Pi; X)\Bigr]$$

where $I(\Pi; X) = \mathbb E_{x \sim p(x)}\bigl[D_{\mathrm{KL}}(\pi(\cdot \mid x) \Vert \pi_0(\cdot))\bigr]$ is the policy's mutual information with the state, measured against a reference marginal policy $\pi_0$. This is the **standard IB for decision problems**: $X$ is the state, $T$ is the policy, $Y$ is the reward / value signal; the relevance term is $\mathbb E[R] = I(T; Y)$ up to an affine transform when $Y$ is Bernoulli "did the policy do the right thing" *[Hypothesis, see derivation below]*.

**Claim.** *[Derived, status: robust-qualitative]* Under a decision-theoretic relevance variable $Y = \mathbb 1[a = a^\ast(x)]$ (the optimal-action indicator), the IB objective $I(X; T) - \beta I(T; Y)$ reduces to the Tishby-Polani policy-complexity objective with reward $R(x, a) = V(x, a)$, and this in turn reduces to the AAD strategy-cost objective with the *reverse-KL* relevance term.

**Derivation.** Take $Y = \mathbb 1[a = a^\ast(x)]$ — an indicator random variable equal to 1 iff the policy picks the state-conditional optimal action. Then under deterministic $\pi^\ast = \delta_{a^\ast(x)}$:

$$I(T; Y) = H(Y) - H(Y \mid T)$$

The entropy $H(Y)$ is determined by the marginal $P(Y = 1) = \mathbb E_x[Q_T(a^\ast(x) \mid x)]$. The conditional entropy $H(Y \mid T)$ is the residual uncertainty about whether the policy is optimal, given the compressed state $T$. For a *deterministic* policy conditioned on $T = t$ (picking $a(t)$), $H(Y \mid T = t) = 0$ when $a(t) = a^\ast(x)$ and is bounded above by the conditional entropy of $a^\ast(X) \mid T = t$ otherwise.

In the degenerate case where $T = X$ (no compression), $I(T; Y) = H(Y) - 0 = H(Y)$, the maximum possible. As $T$ compresses, $I(T; Y)$ drops toward zero. The IB frontier traces the trade-off.

**Now the key step.** $H(Y) - H(Y \mid T)$ can be rewritten via the KL-to-reference decomposition standard in information theory:

$$I(T; Y) = \mathbb E_{T, Y}\left[\log \frac{P(Y \mid T)}{P(Y)}\right] = \mathbb E_T\bigl[D_{\mathrm{KL}}(P(Y \mid T) \Vert P(Y))\bigr]$$

For *decision-optimized* $T$ (i.e., $T$ chosen so the induced policy $Q_T$ maximizes $P(Y = 1)$), the maximum of $I(T; Y)$ at rate $I(X; T) = r$ is achieved by the $T$ that concentrates $Q_T$ on $a^\ast(X)$. Up to an additive constant depending only on the marginal $P(Y)$ (and thus on the environment, not on the policy choice):

$$\arg\max_T I(T; Y) \;\sim\; \arg\max_T \mathbb E_X\bigl[\log Q_T(a^\ast(X) \mid X)\bigr] \;=\; \arg\min_T \mathbb E_X\bigl[-\log Q_T(a^\ast(X) \mid X)\bigr]$$

The last expression is exactly $\mathbb E_X\bigl[D_{\mathrm{KL}}(\pi^\ast(\cdot \mid X) \Vert Q_T(\cdot \mid X))\bigr]$ under deterministic $\pi^\ast$ (since $D_{\mathrm{KL}}(\delta_{a^\ast} \Vert Q_T) = -\log Q_T(a^\ast)$).

Therefore:

$$\arg\max_T I(T; Y) \;=\; \arg\min_T \mathbb E_X\bigl[D_{\mathrm{KL}}(\pi^\ast \Vert Q_T)\bigr] \quad \text{(under } Y = \mathbb 1[a = a^\ast(X)], \pi^\ast = \delta\text{)}$$

**Under these bindings, the IB Lagrangian becomes**:

$$I(X; T) - \beta I(T; Y) \;\equiv\; I(X; T) + \beta \mathbb E_X\bigl[D_{\mathrm{KL}}(\pi^\ast \Vert Q_T)\bigr] + (\text{const in } T)$$

which is *exactly* the AAD strategy-cost objective.

**What this establishes.** *[Derived, status: robust-qualitative]* The AAD reverse-KL form is the *IB objective itself*, under the decision-theoretic relevance variable $Y = \mathbb 1[a = a^\ast(X)]$. It is not an alternative to IB. Gemini's "abandoned IB purity" charge mistakes a change of relevance variable for an abandonment of the framework.

**Scope limits.**
1. **Deterministic $\pi^\ast$ required.** Under stochastic $\pi^\ast$ the equivalence breaks; a richer $Y$ (value-distribution rather than optimal-action indicator) is needed. This is the same scope condition the segment already carries.
2. **The additive constant matters operationally.** "$\arg\max_T I(T; Y) \equiv \arg\min_T \mathbb E[D_{\mathrm{KL}}]$" holds up to a constant in $T$. For a specific $\beta$, the numerical value of the objective differs; the minimizer is the same. This is enough for the uniqueness-of-form argument but must be stated when positioning reverse-KL as "exactly IB".
3. **Up to an affine transform.** More carefully: $I(T; Y) = \mathbb E_T[D_{\mathrm{KL}}(P(Y \mid T) \Vert P(Y))] \neq -\mathbb E_X[D_{\mathrm{KL}}(\pi^\ast \Vert Q_T)]$ in general — the LHS involves $Y$-side marginal; the RHS involves $X$-conditional reverse-KL. The equivalence goes through at the *arg-min* level under the stated bindings, not at the *objective-value* level. This is a feature of the reduction, not a bug: the IB Lagrangian for decision problems is *equivalent up to affine reparameterization* to the strategy-cost objective, not literally equal to it.

**Verdict.** **Path 1 succeeds at its stated target.** The "departure from IB" framing is mischaracterization: reverse-KL is IB's relevance term *for the decision-theoretic relevance variable*, recoverable by direct reduction. The strengthening is structural — it gives the segment a cleaner position in the literature than the current "direction forced by vacuity" narrative.

**Caveat on robustness.** The derivation above depends on $Y = \mathbb 1[a = a^\ast(X)]$ being the "right" relevance variable. Other choices (action-value $V$ directly, policy-divergence $D(\pi^\ast \Vert \pi)$ as $Y$, reward-to-go) give different objectives. The claim is: *for the decision-theoretic relevance variable the problem naturally presents*, reverse-KL is IB. For other relevance-variable choices, other forms arise. This is not a uniqueness claim over all possible $Y$; it is an existence claim: *there is a natural $Y$ under which reverse-KL is IB, and it is the one AAD's decision-theoretic scope commits to*.

---

## §2 — Path 2: Relevance-weighted Shannon-MI recovery under $\pi^\ast_\epsilon$

**Target.** Does $I(\Sigma_t; \pi^\ast)$ make sense when $\pi^\ast$ is softened to $\pi^\ast_\epsilon$? What's the limiting form?

**Setup.** Replace $\pi^\ast = \delta_{a^\ast}$ with $\pi^\ast_\epsilon = (1 - \epsilon)\delta_{a^\ast} + \epsilon \cdot \text{Uniform}(\mathcal A)$, a mixture with probability $\epsilon \in (0, 1]$ of uniformly-sampling any action. This makes $\pi^\ast_\epsilon$ a full-support distribution for any $\epsilon \gt 0$.

**Analysis.** Compute $I(\Sigma_t; \pi^\ast_\epsilon)$ where $\Sigma_t$ is treated as a random variable ranging over strategies and $\pi^\ast_\epsilon$ is a random variable over actions.

Under the joint distribution $P(\sigma, a) = P(\sigma) \pi^\ast_\epsilon(a)$ if $\sigma$ and $\pi^\ast_\epsilon$ are *independent* (they are, if $\pi^\ast_\epsilon$ does not depend on $\sigma$), $I(\Sigma_t; \pi^\ast_\epsilon) = 0$. This is the same Shannon-zero degeneracy from the original form — it just shifts from "zero because $\pi^\ast$ is deterministic" to "zero because the two variables are independent." The information-theoretic content is: *whatever stochasticity $\pi^\ast_\epsilon$ has, it does not come from $\Sigma_t$*, so there is no mutual information between them.

**Alternative construction.** Define instead $I(\Sigma_t; Y_{\pi^\ast_\epsilon})$ where $Y_{\pi^\ast_\epsilon} = \mathbb 1[A \sim \pi^\ast_\epsilon(\cdot \mid M_t), A = a^\ast(M_t)]$. This is the Tishby-Polani-style relevance variable of §1, smoothed. Now $I(\Sigma_t; Y_{\pi^\ast_\epsilon})$ is finite, depends on $\Sigma_t$, and as $\epsilon \to 0$ reduces to the reverse-KL limit of §1 (up to the $\epsilon$-dependent additive constant).

**Verdict.** **Path 2 fails at its stated target** (recovering Shannon-MI against a smoothed $\pi^\ast$) but *confirms Path 1 is the right construction* as a by-product. The reason Shannon-MI against $\pi^\ast$ (smoothed or not) is degenerate is that $\pi^\ast$ does not depend on $\Sigma_t$ — they are independent by construction, so their mutual information is zero. The right object is mutual information with a *function of $\Sigma_t$ and $\pi^\ast$* (the optimal-action indicator), which is what Path 1 produces. The softening of $\pi^\ast$ doesn't help; the issue is structural.

**Honest flag.** A more careful Path-2 attempt would construct a *joint distribution* over $(\Sigma_t, \pi^\ast)$ — e.g., both drawn from a common latent "intended objective" — and ask whether Shannon-MI makes sense there. This is the $G_t^{\text{shared}}$ setting, not the single-agent strategy-cost setting. Different problem; the AAD single-agent strategy-cost is irrecoverable via relevance-weighted Shannon-MI.

---

## §3 — Path 3: Rate-distortion with action-value distortion

**Target.** Is reverse-KL the dual / Lagrangian of a rate-distortion problem with an action-value distortion?

**Setup.** Shannon rate-distortion with distortion function $d(x, \hat x)$:

$$R(D) = \min_{p(\hat x \mid x) : \mathbb E d \leq D} I(X; \hat X)$$

For our problem: $X = M_t$ (or the latent "optimal-action" variable); $\hat X$ is the strategy-induced action $A \sim Q_{\Sigma_t}(\cdot \mid M_t)$; and the distortion is the *value-gap*:

$$d(M_t, a) = V(a^\ast(M_t)) - V(a) \geq 0$$

which is exactly AAD's per-action regret gap $\Delta(a)$ from `#deriv-strategy-cost-regret-bound` §2.

**Rate-distortion formulation.**

$$R_{\mathcal A}(D) = \min_{Q : \mathbb E_{M, a \sim Q}[\Delta(a)] \leq D} I(M_t; A)$$

This says: *what is the minimum policy-information-rate required to achieve expected regret at most $D$?* Lagrangian form:

$$\mathcal L(\beta) = I(M_t; A) + \beta \cdot \mathbb E_M \mathbb E_{a \sim Q_\Sigma}[\Delta(a)] = I(M_t; A) + \beta \cdot R(Q_\Sigma)$$

**Claim.** *[Derived, status: exact]* Under deterministic $\pi^\ast$ and bounded $V_{\max}$, the Lagrangian dual of the rate-distortion problem with action-value distortion $d(x, a) = \Delta(a)$ is **linearly upper-bounded** by a reverse-KL Lagrangian:

$$\mathcal L_{\text{RD}}(\beta) = I(M_t; A) + \beta R(Q_\Sigma) \;\leq\; I(M_t; A) + \beta V_{\max} \sqrt{\tfrac{1}{2} D_{\mathrm{KL}}(\pi^\ast \Vert Q_\Sigma)}$$

by the Pinsker-TV regret bound of §3 of `#deriv-strategy-cost-regret-bound`. So minimizing the strategy-cost objective in its reverse-KL form gives an *upper-bound surrogate* for the rate-distortion-optimal strategy.

**Stronger result: the forms coincide at the degenerate-value extremum.** When the value landscape is extremal (every sub-optimal action incurs the full value range $V_{\max}$), the regret bound is tight (per §3 of `#deriv-strategy-cost-regret-bound`), and the rate-distortion Lagrangian *equals* the reverse-KL Lagrangian up to a square-root reparameterization. Under the square-root form of the strategy-cost objective (§7 of the segment), this coincidence is exact; under the linear form (IB-shape preserved), it is a local-linearization at the operating point.

**Verdict.** **Path 3 succeeds with a caveat.** Reverse-KL is not literally the rate-distortion dual; it is an *upper-bound surrogate* via Pinsker. At the extremal-value limit they coincide. The rate-distortion perspective is valuable because it:

1. Motivates the $I(M_t; A)$ information-rate term (the "compression cost" in the IB framing).
2. Makes the value-gap distortion first-class (the distortion *is* the regret).
3. Explains *why* reverse-KL is the right surrogate: it is a gradient-tractable upper bound on the rate-distortion objective.

This is the **rate-distortion-for-control** reading. It is *complementary* to Path 1 (IB-for-control): Path 1 treats the problem as information-bottleneck-with-decision-relevance; Path 3 treats it as rate-distortion-with-action-value-distortion. The two are dual framings of the same object (rate-distortion is the Lagrangian dual of IB for fixed capacity — Cover & Thomas §I.12–13).

**Segment-level move.** The current segment presents reverse-KL purely via the regret-bound derivation. A Path-3 sub-section — *"Rate-distortion derivation with action-value distortion"* — would show the reverse-KL Lagrangian as a tractable surrogate for the natural rate-distortion objective on the policy simplex, with Pinsker supplying the bound. This gives the segment a second derivation route that uses standard machinery directly (no Cauchy-FE axiom required at this level).

**Technical flag.** The RHS of the rate-distortion dual is $\beta D$, where $D$ is expected distortion. The reverse-KL term on the right of the Pinsker inequality is $\beta V_{\max}\sqrt{D_{\mathrm{KL}}/2}$. For the two to be used interchangeably at the minimizer, the $\beta$ parameters must be related by $\beta_{\text{RD}} = \beta_{\text{KL}} \cdot V_{\max}/(2\sqrt{2 D_{\mathrm{KL}}})$ at the operating point — which is the *local* $\beta_\Sigma$ interpretation already in the segment's §7.

---

## §4 — Path 4: Savage-style decision-consistency axiomatization (a second uniqueness route)

**Target.** Is there a decision-theoretic axiomatization — independent of the chain-rule additivity axiom — that forces reverse-KL?

**Motivation.** The current uniqueness result in `#deriv-strategy-cost-regret-bound` §6.1 rests on chain-rule additivity. If there is a *second* independent axiomatic route that also picks out reverse-KL, the segment's uniqueness claim becomes more robust: multiple axiomatic routes converging on the same divergence is stronger evidence that the divergence is structurally right, not a byproduct of a specific axiom choice.

**Candidate axioms.** From the decision-theoretic-preference-aggregation literature (Savage 1954; Jaynes 1957; Shore-Johnson 1980; Csiszár 1991; de Finetti 1937):

- **(D1) Regret-consistency.** If $Q_1$ uniformly dominates $Q_2$ in expected regret — $R(Q_1; V) \leq R(Q_2; V)$ for all bounded $V$ with a fixed $\pi^\ast$ — then $D(\pi^\ast \Vert Q_1) \leq D(\pi^\ast \Vert Q_2)$.
- **(D2) Locality.** The divergence $D(\pi^\ast \Vert Q)$ depends on $Q$ only through its values at actions with $\pi^\ast$-positive mass and the values at actions on the support-complement.
- **(D3) Positivity and identity.** $D(P \Vert Q) \geq 0$, with equality iff $P = Q$.
- **(D4) Convexity in $Q$.** $Q \mapsto D(P \Vert Q)$ is convex.
- **(D5) Grouping / aggregation.** Coarse-graining actions into equivalence classes does not increase divergence — mirroring a weak form of Shore-Johnson system-independence.

**Analysis attempt.** Under (D1), a uniformly-better-regret policy has lower divergence. This forces the divergence to be *monotone* in the regret bound. Combined with (D2) locality and (D3) positivity, the admissible divergences are the $\pi^\ast$-first f-divergences (already known). (D4) convexity is standard. The question: does (D5) grouping-consistency pick out reverse-KL?

Shore-Johnson 1980's system-independence axiom (joint inference on independent subsystems decomposes) is a strong form of (D5). Under Shore-Johnson, the *minimum-cross-entropy* (= minimum reverse-KL) principle is uniquely forced for updating a probability distribution subject to constraints.

**Key observation.** *[Derived, status: robust-qualitative]* Shore-Johnson 1980's system-independence axiom is *equivalent up to re-axiomatization* to the chain-rule additivity axiom of `#deriv-strategy-cost-regret-bound` §6.1. Both are formalizations of "information about independent sub-problems combines additively"; the Shore-Johnson form is stated at the level of *joint inference* ($Q_{XY} = Q_X Q_Y$ for independent $X, Y$), the chain-rule form at the level of *conditional factorization* ($P_{XY} = P_X P_{Y\mid X}$). They differ in technical formulation but produce the same uniqueness result.

**Deeper question: is there a uniqueness axiom that is *not* of the Shore-Johnson-chain-rule family?** Candidates:

- **Invariance under sufficient statistics (Čencov 1982 / Morozova-Chentsov 1991).** Under Markov-morphism invariance, the admissible family is *all* f-divergences. Does not narrow to reverse-KL.
- **Bregman-duality (Amari 2009).** The f-divergences that are also Bregman divergences form the $\alpha$-family. Within the $\alpha$-family, the $\alpha = 1$ case is reverse-KL. Picking $\alpha = 1$ requires an *additional* axiom beyond Bregman-and-f-divergence intersection.
- **Large-deviation rate-function identity (Sanov 1957).** The Sanov rate function for empirical-distribution concentration is reverse-KL. Under an axiom of the form "the divergence is the large-deviation rate function for its own sampling problem," reverse-KL is forced. But this axiom is *specifically about sampling*, which is Shore-Johnson-adjacent (large-deviation theory uses additive independence of samples).

**Verdict.** **Path 4 partially succeeds.** I cannot find a uniqueness route *independent* of the Shore-Johnson / chain-rule / Sanov / product-independence family. All known uniqueness arguments for reverse-KL seem to factor through *some* form of independence-on-sub-problems — which is the common structural content that Cauchy-FE captures across varied surface formulations. This is evidence that the chain-rule axiom is load-bearing in a structural sense: it is not one of several equally-valid axioms; it is the common form that all uniqueness routes reduce to.

**What this means for the segment.** The current segment correctly identifies chain-rule additivity as the uniqueness axiom. It could be strengthened by a **paragraph noting that Shore-Johnson 1980's system-independence axiom and Sanov 1957's sampling-consistency axiom are structurally equivalent re-formulations, not independent routes**. This closes the "maybe there's another uniqueness argument that fits better" speculation that a careful reader might harbor.

**Concrete deliverable for segment:** add a sentence to `#deriv-strategy-cost-regret-bound` §6.1's Discussion or to `#additive-coordinate-forcing`'s Discussion documenting that the uniqueness axiom is structurally-equivalent to Shore-Johnson and to Sanov, not independently motivated by each — all three factor through independence-of-sub-problems.

---

## §5 — Path 5: Matched lower bound for the regret inequality

**Target.** Does reverse-KL give a *tight* regret bound, or is it strictly-weaker-than-TV with no matching lower bound? Can we derive a matched lower bound under realizable $\pi^\ast$?

**Motivation.** The current segment states:
- TV is tight: $R \leq V_{\max} \cdot \operatorname{TV}$, with equality under extremal-value landscapes.
- Pinsker is loose by $\sqrt{\cdot}$: $R \leq V_{\max}\sqrt{D_{\mathrm{KL}}/2}$.

If the upper bound is loose, a matching lower bound would specify *how* loose and under what conditions the reverse-KL bound actually equals the regret.

**The reverse Pinsker inequality.** Sason-Verdú 2016 ("f-divergence inequalities") provides reverse-direction bounds:

$$D_{\mathrm{KL}}(P \Vert Q) \leq \log\!\Bigl(1 + \frac{\chi^2(P \Vert Q)}{1 - \operatorname{TV}(P, Q)}\Bigr)$$

Under $P = \pi^\ast = \delta_{a^\ast}$, $\chi^2(\pi^\ast \Vert Q) = 1/Q(a^\ast) - 1$ and $\operatorname{TV}(\pi^\ast, Q) = 1 - Q(a^\ast)$. Substituting:

$$D_{\mathrm{KL}}(\pi^\ast \Vert Q) \leq \log\!\Bigl(1 + \frac{1/Q(a^\ast) - 1}{Q(a^\ast)}\Bigr) = \log\!\Bigl(1 + \frac{1 - Q(a^\ast)}{Q(a^\ast)^2}\Bigr)$$

This is an *upper* bound on $D_{\mathrm{KL}}$ in terms of $\operatorname{TV}$, which translates via $D_{\mathrm{KL}} = -\log Q(a^\ast)$ into a tight identity rather than an inequality:

$$D_{\mathrm{KL}}(\pi^\ast \Vert Q) = -\log Q(a^\ast) = -\log(1 - \operatorname{TV}(\pi^\ast, Q))$$

**Direct identity.** *[Derived, status: exact]* Under deterministic $\pi^\ast = \delta_{a^\ast}$ and any $Q$:

$$\boxed{\;D_{\mathrm{KL}}(\pi^\ast \Vert Q) = -\log(1 - \operatorname{TV}(\pi^\ast, Q))\;} \qquad \text{(deterministic } \pi^\ast\text{)}$$

This is a strict sharpening over Pinsker (which is $\operatorname{TV} \leq \sqrt{D_{\mathrm{KL}}/2}$, equivalently $D_{\mathrm{KL}} \geq 2\operatorname{TV}^2$) — the relationship is *exact*, not an inequality.

**Consequence for the regret bound.** Combining with the tight TV-regret bound:

$$R(Q) \leq V_{\max} \cdot \operatorname{TV}(\pi^\ast, Q) = V_{\max} \cdot (1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q)})$$

under deterministic $\pi^\ast$. This gives a *tight* regret bound in reverse-KL, with no Pinsker loss:

$$\boxed{\;R(Q) \leq V_{\max} \cdot (1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q)})\;}$$

This is the **Bretagnolle-Huber identity** in this setting — but note that under deterministic $\pi^\ast$, the Bretagnolle-Huber *bound* $\operatorname{TV} \leq \sqrt{1 - e^{-D_{\mathrm{KL}}}}$ is **not** tight; the identity $\operatorname{TV} = 1 - e^{-D_{\mathrm{KL}}}$ is tight. The square root in Bretagnolle-Huber comes from the general case ($P$ not necessarily deterministic); it collapses under deterministic $P$.

**Matching lower bound.** A lower bound on regret in terms of $D_{\mathrm{KL}}$ requires a *lower bound* on the value-gaps $\Delta(a)$. Define $\Delta_{\min} := \min_{a \neq a^\ast} \Delta(a) \gt 0$ (value-gap lower bound — the "action-gap" standard in RL theory):

$$R(Q) = \sum_{a \neq a^\ast} Q(a) \Delta(a) \geq \Delta_{\min} \cdot \sum_{a \neq a^\ast} Q(a) = \Delta_{\min} \cdot \operatorname{TV}(\pi^\ast, Q)$$

Combined with the tight TV-regret identity in reverse-KL (above):

$$\Delta_{\min} \cdot (1 - e^{-D_{\mathrm{KL}}}) \;\leq\; R(Q) \;\leq\; V_{\max} \cdot (1 - e^{-D_{\mathrm{KL}}})$$

**Corollary.** *[Derived, status: exact]* Under deterministic $\pi^\ast$ and $\Delta_{\min} \gt 0$, the regret $R(Q)$ is **Lipschitz-equivalent** to $(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q)})$ with Lipschitz constants $\Delta_{\min}$ (below) and $V_{\max}$ (above):

$$\frac{\Delta_{\min}}{V_{\max}} \;\leq\; \frac{R(Q)}{V_{\max}(1 - e^{-D_{\mathrm{KL}}})} \;\leq\; 1$$

This is a tight two-sided bound, not just an upper bound. The upper bound is tight when the value landscape is extremal ($\Delta_{\min} = V_{\max}$, all sub-optimal actions are maximally bad). The lower bound is tight when the value landscape is *uniform among sub-optimal actions* ($\Delta_{\min} = \max_a \Delta(a)$).

**Verdict.** **Path 5 succeeds robustly.** The segment should upgrade from "Pinsker gives a loose-by-$\sqrt{\cdot}$ bound" to "**Under deterministic $\pi^\ast$, the BH identity $\operatorname{TV} = 1 - e^{-D_{\mathrm{KL}}}$ is exact; regret is Lipschitz-equivalent to $(1 - e^{-D_{\mathrm{KL}}})$ with constants given by the value-gap min-max.** The Pinsker bound is strictly weaker than the exact form available and should not be the primary presentation; the BH-in-the-deterministic-case form is the right form."

**What this costs the segment.** The linear-KL form of the Lagrangian (§7, IB-shape-preserved) becomes even *more* clearly a local linearization: the true bound is $V_{\max}(1 - e^{-D_{\mathrm{KL}}})$, not $V_{\max}\sqrt{D_{\mathrm{KL}}/2}$, which is tighter but has a different functional shape (bounded above by $V_{\max}$, not unbounded). The segment's existing linear-vs-square-root discussion should be *deepened* into a linear-vs-square-root-vs-exponential discussion, where the exponential form is the tight one.

**Concrete segment edit.** Add a §5.1 (or §4bis) to `#deriv-strategy-cost-regret-bound` titled "The exact regret-reverse-KL identity under deterministic $\pi^\ast$". Replace the Pinsker bound as the primary statement with the BH-identity form. Note that the linear Lagrangian retained for IB-shape alignment in §7 is a first-order approximation to the true exponential bound near $D_{\mathrm{KL}} = 0$ (since $1 - e^{-D_{\mathrm{KL}}} = D_{\mathrm{KL}} - O(D_{\mathrm{KL}}^2)$).

**Honest caveat.** The exactness is a consequence of the *deterministic* $\pi^\ast$ scope. For stochastic $\pi^\ast$ (tied-optima, softmax-smoothed), the BH bound reverts to its inequality form and Pinsker remains looser. Path 5's strengthening is scope-conditional on AAD's deterministic-$\pi^\ast$ canonical scope — but that is exactly the scope the segment works under.

---

## §6 — Path 6: No-go theorem on symmetric f-divergences with standard IB

**Target.** Can I *prove* that no smooth symmetric f-divergence, combined with standard $I(X;T)$ compression cost, gives a decision-consistent degeneracy-free cost under deterministic $\pi^\ast$? A sharp negative strengthens the case that reverse-KL is forced by the problem structure, not chosen.

**Setup.** The admissible family after direction-forcing from §5 of `#deriv-strategy-cost-regret-bound` is $\{D_f(\pi^\ast \Vert Q) : f \text{ convex}, f(1) = 0\}$. A *symmetric* f-divergence satisfies $D_f(P \Vert Q) = D_f(Q \Vert P)$. Common examples: squared Hellinger distance $H^2$, Jensen-Shannon divergence $JSD$, TV (symmetric but not smooth).

**Claim (candidate no-go).** *[Proposed, status: conditional]* No smooth *symmetric* f-divergence $D_f(\pi^\ast \Vert Q_\Sigma)$ combined with standard IB-compression cost $I(X; T)$ gives a decision-consistent cost under deterministic $\pi^\ast$ in the sense that:

*(DC1)* The divergence is finite under deterministic $\pi^\ast$ whenever $Q_\Sigma(a^\ast) \gt 0$.

*(DC2)* The divergence's gradient with respect to $Q_\Sigma$ at $Q_\Sigma = \pi^\ast$ *points toward* the optimum (i.e., moving $Q_\Sigma$ mass onto $a^\ast$ decreases the divergence monotonically in a neighborhood of $\pi^\ast$).

*(DC3)* The divergence satisfies the chain rule for DAG-factorized action sequences.

**Attempted derivation.** (DC1) is satisfiable by symmetric divergences (Hellinger, JSD both finite under deterministic $\pi^\ast$). (DC2) is a monotonicity property that reverse-KL satisfies and Hellinger/JSD also satisfy (by the convexity of $f$). (DC3) is the decisive condition: by the chain-rule uniqueness theorem of `#deriv-strategy-cost-regret-bound` §6.1 (Hobson 1969), *the only f-divergence satisfying the chain rule is $f(t) = c t \log t$*, which is reverse-KL. Reverse-KL is *asymmetric* ($D_{\mathrm{KL}}(P \Vert Q) \neq D_{\mathrm{KL}}(Q \Vert P)$). Therefore no symmetric f-divergence satisfies (DC3).

**Corollary.** *[Derived, status: conditional on chain-rule additivity]* **Symmetric f-divergences are incompatible with DAG-factorized chain-rule additivity.** Reverse-KL's asymmetry is forced by the chain rule, not an independent choice.

**Why this matters.** Symmetric divergences (JSD, Hellinger, symmetrized KL) are often preferred in the general-purpose information-theoretic literature because they provide a *metric-like* structure on the space of distributions. Under the AAD decision-theoretic scope, that symmetry is actively wrong: the asymmetry of reverse-KL is a *feature*, and it is forced by the problem's structural chain-factorization requirement. This is a sharper way to position reverse-KL against alternatives than "it's canonical on multiple grounds."

**Verdict.** **Path 6 succeeds as a conditional no-go.** Under the chain-rule axiom, symmetric f-divergences are ruled out structurally. This is not an independent no-go — it is a corollary of the existing uniqueness theorem — but it's a useful framing for the segment: *the asymmetry of reverse-KL is a derived feature, not a coincidence*.

**What's left as genuinely open.** If a reader *rejects* the chain-rule axiom, can we still rule out symmetric f-divergences via decision-consistency arguments alone? Candidate argument: symmetric divergences treat "$Q$ differs from $\pi^\ast$" and "$\pi^\ast$ differs from $Q$" as equivalent, but these have different operational meaning in the regret problem (one is "strategy-puts-mass-on-wrong-action", the other is "optimum-is-not-in-strategy-support"). These are asymmetric failures, and a divergence that cannot distinguish them is operationally wrong.

Informal argument *[status: heuristic]*: under deterministic $\pi^\ast$, the regret $R(Q) = \sum_{a \neq a^\ast} Q(a) \Delta(a)$ is a *one-sided* quantity — only $Q$'s off-optimum mass contributes; $\pi^\ast$'s "mass off $Q$" is vacuous (since $\pi^\ast$ has no support off $a^\ast$). Any divergence meant to bound regret should therefore be one-sided (asymmetric), penalizing $Q$'s deviation from $\pi^\ast$ but not symmetrically. This is a decision-consistency argument for asymmetry that is *independent* of chain-rule additivity — the argument goes through whether or not the divergence is chain-rule-respecting.

**This gives a second independent route to asymmetry.** Not a full uniqueness route (doesn't pick reverse-KL out of asymmetric f-divergences), but a route to the asymmetry-is-forced half.

**Concrete segment deliverable.** Add to `#deriv-strategy-cost-regret-bound` §5 ("Direction-forcing claim") a sub-paragraph: *"Asymmetry is forced by regret's one-sidedness."* The argument above makes it explicit that asymmetry is not a chain-rule artifact but a structural requirement of bounding a one-sided quantity (regret). The chain-rule then picks the specific asymmetric form.

---

## §7 — Path 7: Mirror descent / Fenchel duality — reverse-KL as the Bregman divergence dual to natural-gradient edge updates

**Target.** Does reverse-KL correspond to a Bregman-divergence structure on the policy simplex that is **dual** to the natural-gradient direction forced by `#deriv-edge-update-natural-parameter`?

**Setup.** `#deriv-edge-update-natural-parameter` derives log-odds as the unique additive-evidence coordinate on edge credences via Cauchy's functional equation on an evidential-additivity axiom. For a multinomial / categorical policy $Q$, the analog is softmax natural parameters $\eta_a = \log Q(a)$ (up to a reference-class shift). The update $\eta^{\text{post}} = \eta^{\text{prior}} + \ell$ is additive in $\eta$.

**Mirror-descent / Bregman structure.** On the probability simplex, the *negative entropy potential* $\phi(Q) = \sum_a Q(a) \log Q(a)$ is strictly convex and Legendre. Its Fenchel dual is the log-partition function $\phi^\ast(\eta) = \log \sum_a e^{\eta_a}$; the primal-dual correspondence is $Q(a) = e^{\eta_a}/\sum_{a'} e^{\eta_{a'}}$ (softmax).

The **Bregman divergence** induced by $\phi$ is:
$$B_\phi(P, Q) = \phi(P) - \phi(Q) - \langle \nabla\phi(Q), P - Q\rangle$$

For $\phi(P) = \sum_a P(a) \log P(a)$, direct computation gives $\nabla\phi(Q)_a = \log Q(a) + 1$, and:

$$B_\phi(P, Q) = \sum_a P(a)\log P(a) - \sum_a Q(a)\log Q(a) - \sum_a (\log Q(a) + 1)(P(a) - Q(a))$$

Simplifying (using $\sum_a P(a) = \sum_a Q(a) = 1$):

$$B_\phi(P, Q) = \sum_a P(a) \log \frac{P(a)}{Q(a)} = D_{\mathrm{KL}}(P \Vert Q)$$

**Result.** *[Derived, status: exact]* **Reverse-KL is the Bregman divergence induced by the negative-entropy potential on the probability simplex, with the log-odds / softmax coordinate being the Fenchel-dual natural parameter.**

This is textbook (Bregman 1967; Amari-Nagaoka 2000 §3.5; Nielsen-Boltz 2011 *The Burbea-Rao and Bhattacharyya Centroids*). Its load-bearing consequence for AAD:

**Duality claim.** *[Derived, status: robust-qualitative]* The **same Legendre-Fenchel structure** that forces log-odds as the natural coordinate on edge credences (`#deriv-edge-update-natural-parameter`) forces reverse-KL as the canonical divergence on the policy simplex (this segment's relevance term). The two layers (update-layer log-odds; divergence-layer reverse-KL) are **dual aspects of the same geometric commitment**: the exponential-family structure on the categorical distributions, with negative-entropy as the convex potential and log-partition as the dual potential.

**Why this strengthens the segment.** The `#deriv-strategy-cost-regret-bound` §6.1 uniqueness result is a standalone Cauchy-FE derivation. The `#deriv-edge-update-natural-parameter` uniqueness result is a *different* Cauchy-FE derivation on a different axiom. The **Bregman-Fenchel duality establishes that these are not two independent forcings but one geometric structure viewed from two sides** — the primal (policy-simplex) side forces reverse-KL; the dual (log-odds-natural-parameter) side forces log-odds; the Legendre-Fenchel correspondence relates them.

**Operational consequence.** **Mirror descent on the policy simplex with negative-entropy regularizer is equivalent to exponentiated-gradient descent on log-odds coordinates.** This is a standard result (Nemirovski-Yudin 1983; Kivinen-Warmuth 1997 *Exponentiated gradient versus gradient descent for linear predictors*; Beck-Teboulle 2003 *Mirror descent and nonlinear projected subgradient methods for convex optimization*) but its AAD-specific consequence is:

- **The strategy-cost objective's reverse-KL term is the natural-metric distance** on the policy simplex — the distance that mirror-descent-with-natural-gradient uses.
- **Edge-update-via-gain's log-odds update** is the *exponentiated-gradient realization* of this mirror descent on the dual simplex.
- **The two layers are algorithmically equivalent**: "minimize reverse-KL on $Q$" via natural-gradient = "additively update log-odds $\eta$" via exponentiated-gradient.

**Verdict.** **Path 7 succeeds robustly and adds a structural unification.** The segment can be strengthened by:

1. Adding a §6.3 "Bregman / Fenchel-duality identification" that states the reverse-KL-as-Bregman result and credits Bregman 1967 / Amari-Nagaoka 2000 / Beck-Teboulle 2003.
2. Adding a cross-reference from `#deriv-strategy-cost-regret-bound` to `#deriv-edge-update-natural-parameter` that makes the Fenchel-duality relationship explicit.
3. Updating `#additive-coordinate-forcing` to note that the divergence-layer and update-layer Cauchy-FE instances are **Fenchel-dual aspects of a single exponential-family structure**, not independent forcings — this is a meta-architectural observation, not a new theorem, but it strengthens the meta-pattern's case.

**Honest caveat.** The Fenchel-Bregman identification is standard information geometry, not AAD-distinctive. Its value for AAD is *structural unification* across two previously-independent segments — which is exactly the kind of integration AAD claims as its contribution.

---

## §8 — Summary of strengthening outcomes

| Path | Target | Outcome | Strength | Segment-level deliverable |
|---|---|---|---|---|
| 1 | Reverse-KL as IB-for-control (Tishby-Polani 2011) | **Succeeds** | Robust qualitative — equivalence via $Y = \mathbb 1[a = a^\ast(X)]$, under deterministic $\pi^\ast$, up to additive constant | Add §6.3 or Discussion paragraph: "Reverse-KL is IB's relevance term under the decision-theoretic relevance variable — namely, the optimal-action indicator $Y$." Cite Tishby-Polani 2011, Rubin-Shamir-Tishby 2012, Levine 2018. Reframes the "abandoned IB purity" charge as a mischaracterization. |
| 2 | Shannon-MI against softened $\pi^\ast_\epsilon$ | **Fails** | The problem is structural, not softness-remediable. Confirms Path 1 as the right move. | No deliverable; document the failure in this spike. |
| 3 | Rate-distortion with action-value distortion | **Succeeds (upper-bound surrogate)** | Exact at extremal value landscape; local linearization at operating point elsewhere. Reverse-KL is the gradient-tractable RD surrogate. | Add §4bis "Rate-distortion derivation with action-value distortion" — motivates $I(X;T)$ compression cost and value-gap distortion directly, without requiring Cauchy-FE axiom. |
| 4 | Second independent uniqueness route (Savage / Shore-Johnson) | **Partial — no independent route found** | All known routes factor through independence-on-sub-problems. Chain-rule, Shore-Johnson system-independence, Sanov sampling-consistency, de Finetti exchangeability all have the same structural content. | Add to §6.1 Discussion: "Shore-Johnson 1980 system-independence, Sanov 1957 rate-function, and Hobson 1969 chain-rule additivity are structurally-equivalent re-formulations, not independent routes — all factor through independence-of-sub-problems." |
| 5 | Matched lower bound on regret | **Succeeds robustly** | Under deterministic $\pi^\ast$: $D_{\mathrm{KL}} = -\log(1 - \operatorname{TV})$ *exactly*, and regret is Lipschitz-equivalent to $(1 - e^{-D_{\mathrm{KL}}})$ with constants $\Delta_{\min}$ (below) and $V_{\max}$ (above). | Replace Pinsker as the primary bound form with the BH-identity form. Add §4bis or refactor §4: the tight relation under deterministic $\pi^\ast$ is $R(Q) \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}})$ with matching lower bound $\Delta_{\min}(1 - e^{-D_{\mathrm{KL}}})$. |
| 6 | No-go for symmetric f-divergences | **Succeeds as conditional no-go** | Under chain-rule axiom, symmetric f-divergences are ruled out by uniqueness. A second independent route (regret's one-sidedness) also forces asymmetry. | Add to §5 a sub-paragraph "Asymmetry is forced by regret's one-sidedness" — asymmetry is structurally required regardless of chain-rule commitment. |
| 7 | Mirror-descent / Fenchel-duality | **Succeeds robustly** | Reverse-KL is the Bregman divergence induced by negative-entropy on policy simplex; log-odds is the Fenchel-dual natural coordinate. The divergence layer (`#deriv-strategy-cost-regret-bound`) and update layer (`#deriv-edge-update-natural-parameter`) are **dual aspects of one exponential-family structure**, not independent. | Add §6.3 "Bregman-Fenchel identification." Add cross-reference to `#deriv-edge-update-natural-parameter` making Fenchel duality explicit. Update `#additive-coordinate-forcing` Discussion: divergence-layer and update-layer Cauchy-FE instances are Fenchel-dual, not independent. |

**Net assessment.**

Gemini's "abandoned IB purity" framing is a **mischaracterization** (Path 1 refutes it directly). Reverse-KL is not a departure from IB — it is IB's canonical relevance term under the decision-theoretic relevance variable. The current segment's "direction-forced by vacuity; form-forced by chain-rule" derivation is defensible but **under-sells the strength of the result**: there are at least three *independent* forcings (IB-for-control via Tishby-Polani; rate-distortion with action-value distortion; Bregman-dual to the log-odds natural coordinate) plus the existing chain-rule and direction-forcing arguments. The segment is currently positioned as "making the best of a degenerate situation"; it should be repositioned as "sitting at the intersection of multiple independent structural forcings."

Path 5 is the sharpest new technical result: the **exact BH identity under deterministic $\pi^\ast$** replaces Pinsker as the correct primary bound and gives a matching lower bound via the action-gap $\Delta_{\min}$.

Path 7 is the most structurally illuminating: the **Fenchel-Bregman duality between the divergence-layer and update-layer instances** of the additive-coordinate-forcing pattern suggests those two layers are not independent but are two sides of one exponential-family commitment. This strengthens the meta-segment `#additive-coordinate-forcing` by revealing hidden structure among the previously-parallel primary instances.

---

## §9 — Recommended segment-level moves

**Strongly recommended (major structural strengthenings):**

1. **`#deriv-strategy-cost-regret-bound` §4 refactor.** Replace Pinsker as primary bound with the exact BH identity $D_{\mathrm{KL}} = -\log(1 - \operatorname{TV})$ under deterministic $\pi^\ast$, yielding $R(Q) \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}})$. Add the matched lower bound $R(Q) \geq \Delta_{\min}(1 - e^{-D_{\mathrm{KL}}})$ for realizable $\pi^\ast$. This is Path 5's deliverable and is the sharpest single improvement available.

2. **`#deriv-strategy-cost-regret-bound` new subsection §6.3 "Reverse-KL as IB for decision problems."** Integrate Path 1's equivalence argument — reverse-KL is IB's relevance term under $Y = \mathbb 1[a = a^\ast(X)]$, with bindings $X = M_t$, $T = \Sigma_t$, $\beta = V_{\max}$. Cite Tishby-Polani 2011, Rubin-Shamir-Tishby 2012, Levine 2018. Repositions the segment as "IB for decision relevance" rather than "departure from IB." Pre-empts Gemini's framing.

3. **`#deriv-strategy-cost-regret-bound` new subsection §6.4 "Bregman / Fenchel-duality identification."** State Path 7's result: reverse-KL is the Bregman divergence induced by negative entropy on the policy simplex, with log-odds as the Fenchel-dual natural coordinate. Cross-reference `#deriv-edge-update-natural-parameter`. Credit Bregman 1967, Amari-Nagaoka 2000, Beck-Teboulle 2003.

**Recommended (smaller refinements):**

4. **`#deriv-strategy-cost-regret-bound` §5 add sub-paragraph "Asymmetry is forced by regret's one-sidedness."** State Path 6's independent route to asymmetry — it does not require the chain-rule axiom. Gives the direction-forcing argument two legs (vacuity + asymmetry), not one.

5. **`#deriv-strategy-cost-regret-bound` §6.1 Discussion paragraph.** State Path 4's finding: Shore-Johnson 1980, Hobson 1969, and Sanov 1957 are structurally-equivalent routes, all factoring through independence-on-sub-problems. Pre-empts "is there another axiomatization?" speculation.

6. **New optional §4ter "Rate-distortion derivation with action-value distortion."** State Path 3's RD-surrogate reading: $R_{\mathcal A}(D) = \min_{Q : \mathbb E d \leq D} I(M_t; A)$ with $d = \Delta(a)$; reverse-KL Lagrangian is its tractable upper bound. Offers a second-derivation route that does not require Cauchy-FE (the RD problem is defined via standard Shannon machinery, Pinsker supplies the bound).

**Recommended for `#additive-coordinate-forcing` (meta-segment):**

7. **Add a paragraph noting Fenchel-duality between divergence-layer and update-layer instances.** The two layers are not independent Cauchy-FE forcings but are **Fenchel-dual aspects of one exponential-family commitment**. This is a meta-observation that strengthens the meta-pattern's structural unity: four primary instances, with two of them (divergence, update) related by Legendre-Fenchel duality, and a third (chain) anchoring both. The Čencov instance remains structurally distinct (invariance-forcing rather than additivity-forcing), as already noted.

**Recommended for `#form-information-bottleneck`:**

8. **Add a cross-reference paragraph.** The canonical IB instance is $(X, T, Y) = (\mathcal C_t, M_t, o_{t+1:\infty} \mid a_{t:\infty})$. The strategy-cost instance (`#form-strategy-complexity-cost` / `#deriv-strategy-cost-regret-bound`) is $(X, T, Y) = (M_t, \Sigma_t, \mathbb 1[a = a^\ast(X)])$. These are **two IB instances with different relevance variables**, not "IB and something else." The "abandoned IB purity" concern is defused at the level of the IB segment itself by making this cross-reference visible.

**Not recommended:**

- Do **not** create a new appendix segment from this spike's contents. Path-5 and Path-7 results belong in `#deriv-strategy-cost-regret-bound` (which is already an appendix-style segment); the remaining paths are either subsidiary (Paths 2, 4, 6) or pointers (Paths 1, 3, 7) and belong in that segment's Discussion or a brief cross-reference elsewhere. Creating a new appendix would fragment the derivation further.
- Do **not** reframe the segment as "IB for control" *instead of* the regret-bound derivation. The regret-bound derivation is the AAD-internal route and should stay primary; Path 1's IB-for-control recovery is complementary, confirming the form has multiple independent justifications.

---

## §10 — Open questions left behind (for future spikes, not this one)

1. **Non-Shannon-rate mirror-descent geometries.** Reverse-KL is the Bregman divergence induced by negative entropy. Other potentials give other Bregman divergences (e.g., Itakura-Saito for Gaussian gains, Csiszár's $\phi$-entropies for general exponential families). Do AAD segments exist where a non-Shannon potential would be the natural geometry? The sector-condition setup (`#result-sector-persistence-template`) uses a quadratic (Euclidean) potential; `#deriv-edge-update-natural-parameter` uses log-odds (Shannon). The cross-segment question: is there a unifying convex-potential story that subsumes both?

2. **Čencov-layer Fenchel-duality.** `#additive-coordinate-forcing`'s fourth instance (Fisher metric via Čencov 1982) is positioned as structurally distinct from the three Cauchy-FE instances. Under the Fenchel-duality unification of the divergence and update layers, is there a similar duality between the metric layer and the divergence layer? The second-order expansion of reverse-KL near $P = Q$ is the Fisher metric (Eguchi 1983), so the two layers are *already* linked via a Taylor expansion. Is this a Fenchel-style duality or just a specialization?

3. **Rate-distortion with L0/L1/L1'/L2 relevance variables.** Path 3's RD derivation uses the value-gap distortion. A more fine-grained distortion — one for each level of `#def-strategy-dag`'s Correlation Hierarchy — would produce a family of RD-optimal strategies indexed by identification regime. Is this a useful extension of the segment, or merely a proliferation?

4. **Stochastic $\pi^\ast$ (tied-optima, softmax-smoothed) — does Path 5's BH identity extend?** The exact $D_{\mathrm{KL}} = -\log(1 - \operatorname{TV})$ relation holds under deterministic $\pi^\ast$. For tied-optima $\pi^\ast$, an analog holds with the optimum-set $\mathcal A^\ast$ playing the role of $\{a^\ast\}$: $D_{\mathrm{KL}}(\pi^\ast \Vert Q) = -\log Q(\mathcal A^\ast) - \log \lvert \mathcal A^\ast\rvert$ (uniform on $\mathcal A^\ast$). For softmax-smoothed $\pi^\ast$, the relation is strictly messier — Pinsker is the best general bound. Scope-extension question for a follow-up spike.

5. **What about the *Čencov* layer in Path 7?** The Fenchel-Bregman duality relates divergence to natural-parameter via the negative-entropy potential. Under parameterization-invariance (the axiom for the Čencov instance), the metric is Fisher. Is there a Fenchel-style duality between the Čencov-layer metric and a dual coordinate structure? This would be a genuinely new observation worth a separate spike. Informal guess: the Fisher metric's dual geometry via Amari-Nagaoka 2000's $\pm 1$-connection structure is the right place to look. Not pursued here.

6. **Does Path 1's $Y = \mathbb 1[a = a^\ast(X)]$ binding propagate cleanly to the other three compression operations ($M_t$, $G_t^{\text{shared}}$, $\Lambda$)?** The model-compression case uses $Y = o_{t+1:\infty}$ — a real observable, not an indicator. The shared-intent case uses $Y = a_t^{\text{coordinated}}$ — again a real variable. The composition case uses $Y = o_{\text{micro},t+1}$. So the "$Y$ = indicator of optimality" choice is specific to the decision-theoretic strategy-cost case; the other three cases use observable-valued $Y$'s. This is consistent with the `#form-strategy-complexity-cost`-is-decision-problem / the-others-are-prediction-problems split, but it does mean the four IB instances differ in *kind of relevance variable* (observable vs. indicator), not merely in which observable. Whether this matters for the O-BP2 unification architectural proposal (four compressions as one hierarchy) is a separate question.

---

## §11 — References invoked

**Tishby-Polani / control-as-inference lineage (Path 1):**
- Tishby, N. & Polani, D. 2011. "Information theory of decisions and actions." In *Perception-Action Cycle: Models, Architectures, and Hardware*, Springer, 601–636.
- Rubin, J., Shamir, O. & Tishby, N. 2012. "Trading value and information in MDPs." In *Decision Making with Imperfect Decision Makers*, Springer, 57–74.
- Still, S. 2009. "Information-theoretic approach to interactive learning." *EPL (Europhysics Letters)* 85(2):28005.
- Ortega, P. & Braun, D. 2013. "Thermodynamics as a theory of decision-making with information-processing costs." *Proc. Royal Society A* 469(2153):20120683.
- Genewein, T., Leibfried, F., Grau-Moya, J. & Braun, D. 2015. "Bounded rationality, abstraction, and hierarchical decision-making: an information-theoretic optimality principle." *Frontiers in Robotics and AI* 2:27.
- Levine, S. 2018. "Reinforcement learning and control as probabilistic inference: tutorial and review." arXiv:1805.00909.

**Rate-distortion for control (Path 3):**
- Cover, T. & Thomas, J. 2006. *Elements of Information Theory.* Wiley (§10 rate-distortion; §12.1 Lagrangian duality between IB and RD).
- Berger, T. 1971. *Rate Distortion Theory.* Prentice-Hall.
- Blahut, R. 1972. "Computation of channel capacity and rate-distortion functions." *IEEE Trans. Info. Theory* 18(4):460–473.

**Decision-theoretic uniqueness axiomatizations (Path 4):**
- Savage, L. J. 1954. *The Foundations of Statistics.* Wiley.
- Shore, J. E. & Johnson, R. W. 1980. "Axiomatic derivation of the principle of maximum entropy and the principle of minimum cross-entropy." *IEEE Trans. Info. Theory* 26(1):26–37.
- Csiszár, I. 1991. "Why least squares and maximum entropy? An axiomatic approach to inference for linear inverse problems." *Annals of Statistics* 19(4):2032–2066.
- Jaynes, E. T. 1957. "Information theory and statistical mechanics." *Physical Review* 106(4):620–630.
- de Finetti, B. 1937. "La prévision: ses lois logiques, ses sources subjectives." *Annales de l'Institut Henri Poincaré* 7:1–68.
- Hobson, A. 1969. "A new theorem of information theory." *Journal of Statistical Physics* 1(3):383–391.
- Sanov, I. N. 1957. "On the probability of large deviations of random variables." *Mat. Sb.* 42(84):11–44.

**Reverse Pinsker / tight TV-KL relations (Path 5):**
- Pinsker, M. S. 1964. *Information and Information Stability of Random Variables and Processes.* Holden-Day.
- Bretagnolle, J. & Huber, C. 1978. "Estimation des densités." In *Séminaire de probabilités XII*, Springer LNM 649, 342–363.
- Tsybakov, A. 2009. *Introduction to Nonparametric Estimation.* Springer, §2.4.
- Sason, I. & Verdú, S. 2016. "$f$-divergence inequalities." *IEEE Trans. Info. Theory* 62(11):5973–6006.

**Mirror descent / Bregman / Fenchel duality (Path 7):**
- Bregman, L. M. 1967. "The relaxation method of finding the common point of convex sets and its application to the solution of problems in convex programming." *USSR Computational Mathematics and Mathematical Physics* 7(3):200–217.
- Nemirovski, A. & Yudin, D. 1983. *Problem Complexity and Method Efficiency in Optimization.* Wiley.
- Kivinen, J. & Warmuth, M. 1997. "Exponentiated gradient versus gradient descent for linear predictors." *Information and Computation* 132(1):1–63.
- Beck, A. & Teboulle, M. 2003. "Mirror descent and nonlinear projected subgradient methods for convex optimization." *Operations Research Letters* 31(3):167–175.
- Amari, S. & Nagaoka, H. 2000. *Methods of Information Geometry.* AMS / Oxford University Press.
- Nielsen, F. & Boltz, S. 2011. "The Burbea-Rao and Bhattacharyya centroids." *IEEE Trans. Info. Theory* 57(8):5455–5466.
- Rockafellar, R. T. 1970. *Convex Analysis.* Princeton University Press.
- Bauschke, H. & Combettes, P. 2017. *Convex Analysis and Monotone Operator Theory in Hilbert Spaces.* Springer (2nd ed.).

**Direct segment dependencies:**
- `#deriv-strategy-cost-regret-bound` (segment)
- `#form-strategy-complexity-cost` (segment)
- `#deriv-edge-update-natural-parameter` (segment)
- `#form-information-bottleneck` (segment)
- `#additive-coordinate-forcing` (segment)
- `spikes/spike-reverse-kl-uniqueness.md` (prior spike)
- `spikes/spike-f20-kl-direction-strengthening.md` (prior spike)

---

## Working Notes

- **Path 1 citation verification.** I have relied on textbook-level familiarity with Tishby-Polani 2011, Rubin-Shamir-Tishby 2012, and Levine 2018 — I have *not* verified the specific claims against PDFs in this spike. Before segment-level promotion of Path 1's content, a PDF verification pass on the three central citations is required. The structural claim (reverse-KL-against-policy-target is the canonical IB objective for decision problems, not an alternative) is well-established in the literature and I am confident in it; the specific attribution granularity is what needs checking. If Joseph wants to execute the Path-1 deliverable, add citation verification to the session plan.

- **Path 5 is the hardest-to-miss single improvement.** The exact identity $D_{\mathrm{KL}} = -\log(1 - \operatorname{TV})$ under deterministic $\pi^\ast$ is elementary (follows from $D_{\mathrm{KL}}(\delta_{a^\ast} \Vert Q) = -\log Q(a^\ast)$ and $\operatorname{TV}(\delta_{a^\ast}, Q) = 1 - Q(a^\ast)$) and should be in the segment already. I was surprised to find Pinsker presented as the primary bound rather than this exact identity. The Pinsker framing is correct as a *general* result but loses information in AAD's canonical deterministic-$\pi^\ast$ scope. The segment's "Pinsker is loose by $\sqrt{\cdot}$" observation is then a general-case observation incorrectly transferred to the AAD-scope case where Pinsker is *provably* strictly weaker than the tight identity available.

- **Path 7 is the most interesting structurally.** The Fenchel-Bregman duality between the divergence-layer and update-layer instances of the Cauchy-FE pattern is a genuine meta-observation I did not see coming. Whether it deserves its own segment or just a Discussion paragraph in `#additive-coordinate-forcing` is a call for Joseph. The observation is: the three Cauchy-FE instances (chain, divergence, update) are *not three independent applications of the same technique*. The divergence and update instances are Fenchel-dual to each other through the negative-entropy potential. So the primary-instance count is better stated as "chain-layer anchor + (divergence ↔ update) Fenchel-dual pair + Čencov metric-layer instance" — three structurally distinct instances, not four parallel ones. This could be a minor re-framing of the meta-pattern that tightens its internal structure.

- **What I did *not* attempt.** I did not attempt to connect Paths 1, 3, 7 (IB-for-control, RD-with-action-value-distortion, Bregman-dual) into a single unified forcing argument. These three are *independently* strong. Whether they fit together into a single derivation (e.g., "the RD problem's Lagrangian dual on the policy simplex, under the decision-theoretic relevance variable, is the Bregman divergence induced by negative entropy") is plausibly true but not derived here. A follow-up spike could attempt the unification; it would strengthen the meta-claim that reverse-KL sits at the intersection of multiple independent forcings to "reverse-KL is the essentially-unique object that simultaneously satisfies several independent constraint sets, all from standard information-theoretic and convex-analytic machinery." This would be the cleanest form of the "not a departure from IB" rebuttal.

- **The Gemini framing is specifically addressed by Path 1.** Paths 3, 5, 7 are technical strengthenings within the existing segment; Paths 4, 6 are conditional improvements. Path 2 is a failure that confirms Path 1. The *rhetorical* work of pre-empting "abandoned IB purity" is done by Path 1 alone, with the IB-for-control reduction making it visible that reverse-KL *is* IB under the decision-theoretic relevance variable. If the segment makes just one change from this spike's recommendations, Path 1's reframing paragraph is the one that most directly addresses Gemini's charge.

- **On the strengthen-before-soften posture.** Gemini's framing suggested (implicitly) a softening: "acknowledge this is a departure from standard IB, document the trade-off honestly." That move would have cost AAD the claim that its framework fits within IB. The strengthening move — "reverse-KL *is* IB under the right relevance variable" — reclaims the territory. This is the exact shape of work the CLAUDE.md "strengthen before softening" posture demands: the obvious move is to soften; the harder and more productive move is to ask whether the claim can be strengthened. In this case the answer is yes — the strengthening is available and should be taken.

- **The meta-pattern reframing in Path 7.** If the divergence and update layers are Fenchel-dual, the `#additive-coordinate-forcing` meta-segment's "four primary instances" counting is partly structural and partly superficial. The honest restatement is: **three structurally distinct layers of forcing — chain-anchor, Fenchel-dual exponential-family pair (divergence + update), and Čencov-invariance-at-metric — plus two adjacent non-primary cases (Lyapunov quadratic, IB Lagrangian)**. This is slightly more concise than the current "four instances" framing and surfaces the Fenchel-duality structure as a first-class observation. Whether Joseph wants to retool the meta-segment this way is a portfolio-level call; the alternative is to note the Fenchel-duality as a supplementary observation in the Discussion without changing the primary framing.

---

## §12 — Citation-verification addendum (post-PDF)

**Context.** The three PDFs flagged in §10.6 / Working Notes were acquired and read page-by-page. This section records what each paper actually says, re-evaluates Claims A–D from the spike body against PDF evidence, and proposes the updated segment-level deliverables that follow.

**Headline.** Path 1's *structural thesis* — "reverse-KL-against-policy-target is a canonical IB-style objective for decision problems, not a departure from IB" — **survives**. But the *specific attribution to Tishby-Polani 2011* (Claim A) does **not** survive at the formula level: the spike attributes to Tishby-Polani 2011 an objective that is actually Rubin-Shamir-Tishby 2012's, and attributes to a paper called "Information theory of decisions and actions" a title that is actually "The Information Theory of Decision and Action." The Tishby-Polani 2011 *Information-to-Go* objective is a *different* information quantity — richer, not reducible to a simple expected-KL-to-reference policy. This is a correction, not a collapse: the Path 1 reframing reroutes cleanly through Rubin-Shamir-Tishby 2012 and the attribution must be updated.

### §12.1 — Paper-level findings

#### Tishby-Polani 2011 — "The Information Theory of Decision and Action"

**Correct citation.** Tishby, N. & Polani, D. 2011. "The Information Theory of Decision and Action." In *Perception-Action Cycle: Models, Architectures, and Hardware* (V. Cutsuridis, A. Hussain, J. G. Taylor, eds.), Springer, pp. 601–636. The spike (and AAD's `ref/INDEX.md` entry) have been using the slightly-wrong title "Information theory of decisions and actions" (singular "decision" → plural "decisions"; "and action" → "and actions") — an error propagated from Rubin-Shamir-Tishby 2012's reference [10], which itself cites the paper as "Information theory of decisions and actions." The Springer chapter's own title page (verified on p. 1 of the PDF) uses the singular form.

**Paper's actual objective.** The paper introduces **Information-to-Go** $\mathfrak I^\pi(s_t, a_t)$ (p. 19, Sec. 6.2), defined as the conditional multi-information of the *entire future state-action trajectory* given the current state-action pair:

$$\mathfrak I^\pi(s_t, a_t) \triangleq \mathbb E_{p(s_{t+1}a_{t+1}s_{t+2}a_{t+2}\dots \mid s_t,a_t)}\left[\log\frac{p(s_{t+1}a_{t+1}s_{t+2}a_{t+2}\dots \mid s_t,a_t)}{p(s_{t+1})\pi(a_{t+1})p(s_{t+2})\pi(a_{t+2})\dots}\right]$$

(Eq. 15 region; exact TeX transcribed from p. 19.) The paper's trade-off objective (Eq. 17, p. 21) is

$$\arg\min_\pi F^\pi(s_t, a_t, \beta) \triangleq \arg\min_\pi\bigl[\mathfrak I^\pi(s_t, a_t) - \beta Q^\pi(s_t, a_t)\bigr]$$

— minimize information-to-go minus $\beta$-weighted Q-value. The per-step information-gain decomposition (Eq. 16, p. 20) is

$$\Delta I_{s_t, a_t}^{s_{t+1}} = \log\frac{p(s_{t+1}\mid s_t, a_t)}{p(s_{t+1})} + \log\frac{\pi(a_{t+1}\mid s_{t+1})}{\pi(a_{t+1})}$$

— with the reference being the *marginal* $\pi(a_{t+1})$ of the policy itself (obtained from $\sum_s \pi(a\mid s)p(s)$ per Eq. 22, p. 22), not an arbitrary $\pi_0$. The soft-policy form is (Eq. 20, p. 22):

$$\pi(a\mid s) = \frac{\pi(a)}{Z^\pi(s, \beta)}\exp(-F^\pi(s, a, \beta))$$

with $\pi(a)$ the stationary marginal of $\pi(a\mid s)$ itself — a self-consistent fixed-point condition.

**What the spike attributed vs. what the paper actually says.**
- Spike attributed (Claim A): $I(\Pi; X) = \mathbb E_x[D_{\mathrm{KL}}(\pi(\cdot\mid x)\Vert\pi_0(\cdot))]$ with $\pi_0$ a reference marginal; objective $\max_\pi \mathbb E[R(X,A)] - \beta^{-1}I(\Pi;X)$.
- Paper actually presents: $\mathfrak I^\pi(s_t, a_t)$, the multi-information of the *entire joint future trajectory* vs. the product of marginals — a strictly richer quantity including environment-response information $\log(p(s'\mid s,a)/p(s'))$ in addition to policy-selection information. The reference policy used in the decomposition is $\pi(a)$ (the stationary marginal), not an independent $\pi_0$.
- Neither formula appears in the paper in the $I(\Pi; X)$ "policy mutual information" form the spike attributed to it. The closest match in the Tishby-Polani 2011 PDF is the *second term* of $\Delta I$ (Eq. 16) — $\log(\pi(a\mid s)/\pi(a))$ — which after expectation gives $\mathbb E_s[D_{\mathrm{KL}}(\pi(\cdot\mid s)\Vert\pi(\cdot))]$, i.e., the reference is the *marginal of the same policy*, not an independent $\pi_0$.

**What the paper establishes (that the spike can cite correctly).**
- Sec. 5.2–5.3 (pp. 12–15): information-theoretic treatment of the MDP perception-action loop with Bayesian-network formalism, introducing decision-complexity / Information-to-Go.
- Sec. 6 (pp. 18–20): Bellman-recursion structure for information-value trade-off — $\mathfrak I^\pi$ has a local-gain decomposition that yields a Bellman-type backup.
- Sec. 7.1 (pp. 21–22): free-energy functional $F^\pi$ as the Lagrangian of the constrained-information problem; soft-policy fixed-point form (Eq. 20).
- Sec. 7.2 (pp. 22–23): perfectly-adapted environments — where environment transitions satisfy $p(s'\mid s,a) = q_\beta(s'\mid s, a)$ (Eq. 23), the future-information term is fully value-relevant.
- Sec. 8 (pp. 23–26): grid-world simulations demonstrating the trade-off curve.

**Direct quote (Sec. 9, p. 26).** *"We consider a particular incarnation of this problem, namely an agent situated in an MDP defining a concrete task; this task is encoded as a cumulated reward which the agent needs to maximize. The information-theoretic view transforms this problem into a trade-off between the reward achieved at a given informational cost. This is an extension of classic rate-distortion theory into the context of a full-fledged perception-action cycle."* This is a *rate-distortion* framing, not an IB framing — which matters for Path 3 (rate-distortion-for-control), not for Path 1 (IB-for-control).

**Net.** Tishby-Polani 2011 is correctly read as a **rate-distortion-for-the-perception-action-cycle** result (Path 3 lineage), not as an IB-for-control result (Path 1 lineage). The spike's Path 1 attribution is wrong at the formula level. The structural content the spike needs — "reverse-KL-against-a-policy-target as the canonical information quantity for MDPs" — is instead Rubin-Shamir-Tishby 2012's.

#### Rubin-Shamir-Tishby 2012 — "Trading value and information in MDPs"

**Correct citation.** Rubin, J., Shamir, O. & Tishby, N. 2012. "Trading value and information in MDPs." In *Decision Making with Imperfect Decision Makers* (T. V. Guy, M. Kárný, D. H. Wolpert, eds.), Intelligent Systems Reference Library 28, Springer, pp. 57–74. Citation as given in the spike. PDF's own title page on p. 1 confirms.

**Paper's central construction.** Sec. 2.2 (p. 4) introduces **control information**:

$$\Delta I(s) = \sum_a \pi_s(a)\log\frac{\pi_s(a)}{\rho_s(a)}$$

— the relative entropy between the controller's policy $\pi_s(a)$ and a "default policy" $\rho_s(a)$, which the paper sets to **uniform** "without loss of generality" (p. 4, mid-paragraph). Aggregating over trajectories (Eqs. 3–4, p. 4):

$$I_\pi(s_0) = \lim_{T\to\infty}\mathbb E\left[\sum_{t=0}^{T-1}\log\frac{\pi_{s_t}(a_t)}{\rho_{s_t}(a_t)}\right]$$

**Free-energy objective.** Sec. 3.1 (p. 5):

$$F_\pi(s_0;\beta) = I_\pi(s_0) - \beta V_\pi(s_0)$$

with $\beta$ controlling the trade-off. **Theorem 1** (p. 5): the optimal $F^*$ satisfies a Bellman equation

$$[\mathcal B F](s) = \min_{\pi_s(\cdot)}\sum_{a\in\mathcal A}\pi_s(a)\left[\log\frac{\pi_s(a)}{\rho_s(a)} - \beta R(s,a) + \sum_{s'}P_{s,a}(s')F(s';\beta)\right]$$

with unique fixed-point solution $F^*$. Paper remarks (§3.1, p. 5): *"This formulation is similar to the one used in rate-distortion theory (c.f. Chapter 13 of [2]) with the expected value replacing the expected block distortion."* Reference [2] is Cover & Thomas 1991.

**Optimal soft policy (Lemma, p. 6):**

$$\pi_s^*(a) = \frac{\rho_s(a)}{Z(s;\beta)}\exp\left[\beta R(s,a) - \mathbb E_{s'\mid s,a}F^*(s';\beta)\right]$$

— Boltzmann form with the default $\rho_s$ as base measure.

**PAC-Bayesian bound.** Sec. 5, Theorem 3 (p. 10): under a-priori stochastic policy $\rho_s(a)$ and empirical reward estimate, for any proper policy and initial state:

$$\tilde D_{\mathrm{KL}}(\hat V_\pi(s_0)\Vert V_\pi(s_0))\;\leq\;\frac{I_\pi(s_0) + \log(2m/\delta)}{m-1}$$

The control information **serves as the proper regularization term** yielding a more robust policy. This is a concrete generalization-bound result using the control-information quantity.

**What's directly relevant for Path 1 reframing.** Rubin et al. 2012 is the paper where the reverse-KL-against-policy-target formulation is **explicit** in the form Path 1 needs. The control information $\Delta I(s) = D_{\mathrm{KL}}(\pi_s\Vert\rho_s)$ is exactly the "reverse-KL against a reference policy" form, with:
- $\pi_s$ = the AAD-language $Q_{\Sigma_t}$ (the agent's strategy-induced policy)
- $\rho_s$ = a default/reference policy (uniform in their treatment; could be $\pi^*$ under AAD's translation)

**Critical translation asymmetry.** Rubin et al.'s $D_{\mathrm{KL}}(\pi_s\Vert\rho_s)$ puts the **agent's policy first** and the default/reference second. AAD's $D_{\mathrm{KL}}(\pi^*\Vert Q_{\Sigma_t})$ puts $\pi^*$ (the target-optimal) first and the agent's strategy-induced policy second. These are **different directions** in the KL:
- Rubin 2012: $D_{\mathrm{KL}}(\pi\Vert\rho)$ — "agent-first, default-second" — a regularization/complexity cost.
- AAD: $D_{\mathrm{KL}}(\pi^*\Vert Q_\Sigma)$ — "optimum-first, agent-second" — a regret-bound cost.

These have **opposite mode behavior**: Rubin's form penalizes the agent for deviating from the default (mode-covering from the default's perspective); AAD's form penalizes the agent for missing the optimum's mode (mode-seeking toward the optimum). They are not the same objective re-parameterized; they are structurally dual.

**What this means for Path 1.** The spike's Path 1 claim — "under the decision-theoretic relevance variable $Y = \mathbb 1[a = a^\ast(X)]$, the IB objective reduces to the Tishby-Polani policy-complexity objective which reduces to the AAD reverse-KL form" — **cannot go through Rubin 2012 directly either**, because Rubin 2012's policy-complexity objective is $D_{\mathrm{KL}}(\pi_s\Vert\rho_s)$, *opposite direction* to AAD's $D_{\mathrm{KL}}(\pi^*\Vert Q_\Sigma)$. The derivation needs to either (a) redo the reduction with $\rho_s = \pi^*$ and track the direction carefully, or (b) honestly acknowledge that the two are *distinct formulations*, not one reducing to the other.

**Revised Path 1 move (PDF-supported).** Path 1 can still go through, but the reframing is: "AAD's $D_{\mathrm{KL}}(\pi^*\Vert Q_\Sigma)$ and the Rubin-Shamir-Tishby 2012 $D_{\mathrm{KL}}(\pi\Vert\rho)$ are *sibling formulations* in the information-theoretic MDP tradition — same lineage, different direction choice, each motivated by a different structural question (regret-bound vs. regularization-generalization). AAD's direction is forced by the regret-bound derivation; Rubin et al.'s direction is forced by the PAC-Bayesian generalization bound. Both inherit the divergence family from the shared IB-for-decision-problems framing." This is a *weaker* claim than "reverse-KL IS IB's relevance term" — it is "AAD's formulation is in the same research lineage as established IB-for-control formulations, with a direction choice that matches AAD's regret-bound derivation specifically."

#### Levine 2018 — "Reinforcement Learning and Control as Probabilistic Inference"

**Correct citation.** Levine, S. 2018. "Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review." arXiv:1805.00909v3 (May 2018). Spike citation ("Reinforcement learning and control as probabilistic inference: tutorial and review") matches; PDF confirms.

**Paper's framework.** Not IB-based. The core is **maximum-entropy RL** via a graphical-model formalization:
- Optimality variables $\mathcal O_t \in \{0, 1\}$ with $p(\mathcal O_t = 1\mid s_t, a_t) = \exp(r(s_t, a_t))$ (Eq. 3, p. 3).
- Trajectory-level posterior under $\mathcal O_{1:T} = 1$ yields (Eq. 5, p. 4):
  $$p(\tau\mid \mathcal O_{1:T}) \propto \mathbb 1[p(\tau)\neq 0]\exp\left(\sum_t r(s_t, a_t)\right)$$
- Sec. 3.1 (p. 8) derives the max-entropy objective via $D_{\mathrm{KL}}(\hat p(\tau)\Vert p(\tau))$ minimization (Eq. 11):
  $$-D_{\mathrm{KL}}(\hat p(\tau)\Vert p(\tau)) = \sum_t \mathbb E_{(s_t, a_t)\sim\hat p}[r(s_t, a_t) + \mathcal H(\pi(a_t\mid s_t))]$$
- Sec. 3.2 (p. 9): variational lower bound (ELBO) form.

**KL direction in Levine 2018.** The variational form of Eq. 11 uses $D_{\mathrm{KL}}(\hat p\Vert p)$ where $\hat p$ is the proposal (policy-parameterized trajectory distribution) and $p$ is the target (optimality-conditioned trajectory distribution). In AAD's notation this is $D_{\mathrm{KL}}(Q_{\Sigma_t}\Vert\pi^*)$ — **forward-KL, not reverse-KL**. The optimal-policy form at convergence is (Eq. 16, p. 8):

$$\pi(a_t\mid s_t) = \exp(Q(s_t, a_t) - V(s_t))$$

which is mode-*covering* from $\hat p$'s perspective (Levine's notation) but mode-*seeking* from the target-optimality's perspective. Sec. 5.2 (p. 15, "Variational Policy Search and Expectation Maximization") explicitly states:

> *"RL instead minimizes a KL-divergence of the form $D_{\mathrm{KL}}(p_\theta\Vert p_{\mathrm{tgt}})$, which prioritizes finding a mode of the target distribution rather than matching its moments."*

Here $p_\theta$ is the proposal policy and $p_{\mathrm{tgt}}$ is the exponentiated-reward target. In AAD's naming convention (which follows Bishop 2006 where "reverse-KL" means $D_{\mathrm{KL}}(q\Vert p)$ with $q$ the approximation and $p$ the target — the mode-seeking one), **Levine IS using reverse-KL**. The terminology confusion is in the surface-ordering of arguments, not in the operational property (mode-seeking).

**Reconciliation.** Levine's $D_{\mathrm{KL}}(p_\theta\Vert p_{\mathrm{tgt}})$ with agent-policy-first and target-second is the *same* operational quantity as AAD's $D_{\mathrm{KL}}(\pi^*\Vert Q_\Sigma)$ if and only if the agent-proposal is mode-seeking toward the target's *optimum*. Under deterministic $\pi^* = \delta_{a^*}$:
- Levine's form: $D_{\mathrm{KL}}(\pi_\theta\Vert p_{\mathrm{tgt}}) = \sum_a \pi_\theta(a)\log(\pi_\theta(a)/p_{\mathrm{tgt}}(a))$ — for this to be finite, $p_{\mathrm{tgt}}$ must have full support (which it does in Levine's exponentiated-reward construction: $p_{\mathrm{tgt}}(a) \propto \exp(r(s, a))$ is strictly positive).
- AAD's form: $D_{\mathrm{KL}}(\pi^*\Vert Q_\Sigma) = -\log Q_\Sigma(a^*)$ under deterministic $\pi^*$.
- These are **different**: Levine's forward-KL is finite under his softened target; AAD's reverse-KL is finite under the agent's supporting the optimum.

Levine does **not** use the AAD-direction form $D_{\mathrm{KL}}(\pi^*\Vert\pi)$ anywhere in the paper. The max-entropy framework uses $D_{\mathrm{KL}}(\pi\Vert p_{\mathrm{tgt}})$ throughout (the "variational posterior first, target second" convention of VI). Under Levine's construction, that IS the mode-seeking divergence because the *target* is softened (exponentiated reward) rather than deterministic. AAD's direction choice is forced by a *different* structural constraint — the deterministic-$\pi^*$ scope.

**IB connection in Levine 2018.** Not discussed. Levine's framework is connected to:
- Kalman duality (Todorov 2008)
- Linearly-solvable MDPs (Todorov 2006, 2010)
- Path-integral control (Kappen 2011)
- Max causal entropy IRL (Ziebart 2010)
- Free-energy principle (Friston 2009) — discussed briefly on p. 18, noted as "similar to the maximum entropy approach"

The information-bottleneck method is not invoked as a framework for Levine 2018. The spike's Claim D that "Levine 2018 develops the control-as-inference story with reverse-KL against a policy target throughout" is **partly supported** (the mode-seeking KL is throughout, consistent with AAD's operational property) but **does not explicitly connect to IB** (the spike's implication that Levine 2018 provides IB-for-control lineage is not in the text).

**Direct quote (Sec. 5.2, p. 15).** The explicit forward-vs-reverse discussion in Levine is worth quoting in full context:
> *"Mathematically, this problem stems from the fact that supervised learning matches a target distribution by minimizing a KL-divergence of the form $D_{\mathrm{KL}}(p_{\mathrm{tgt}}\Vert p_\theta)$, where $p_{\mathrm{tgt}}$ is the target (e.g., the reward or exponentiated reward). RL instead minimizes a KL-divergence of the form $D_{\mathrm{KL}}(p_\theta\Vert p_{\mathrm{tgt}})$, which prioritizes finding a mode of the target distribution rather than matching its moments."*

This IS the "forward-KL vs. reverse-KL for decision problems" framing — using the Bishop-convention naming (supervised = forward; RL = reverse). In AAD's $\pi^*$-first convention, supervised learning's forward-KL becomes AAD's reverse-KL, and Levine's RL-reverse-KL becomes AAD's forward-KL. **The Bishop-vs-AAD naming collision is load-bearing.** The spike's text interchanges these conventions without flagging, which is why the "reverse-KL against policy target throughout" claim reads as coherent but is actually ambiguous.

### §12.2 — Claims A–D verification verdicts

| Claim | Verdict | Evidence |
|---|---|---|
| **A** (Tishby-Polani 2011 objective form $\max_\pi \mathbb E[R] - \beta^{-1}I(\Pi;X)$ with $I(\Pi;X) = \mathbb E[D_{\mathrm{KL}}(\pi\Vert\pi_0)]$) | **Contradicted at formula level** | TP2011 uses Information-to-Go $\mathfrak I^\pi$ (Eq. 15, p. 19), the multi-information of the entire future trajectory vs. product of marginals. Objective is $\min_\pi[\mathfrak I^\pi - \beta Q^\pi]$ (Eq. 17, p. 21). The reference policy in the decomposition (Eq. 16, p. 20) is the *marginal* $\pi(a)$ of the policy itself, not an independent $\pi_0$. The closed form the spike attributes is Rubin 2012's, not TP2011's. |
| **B** (IB reduction through $Y = \mathbb 1[a = a^*(X)]$ gives Tishby-Polani objective gives AAD reverse-KL, up to additive constants at arg-min level) | **Unverified in TP2011; partially verifiable with direction correction against Rubin 2012** | TP2011 does not present any such reduction; TP2011's objective is multi-information, not policy complexity. Rubin 2012's objective IS a KL-to-reference form, but the direction is $D_{\mathrm{KL}}(\pi\Vert\rho)$ (agent-first) — opposite to AAD's $D_{\mathrm{KL}}(\pi^*\Vert Q_\Sigma)$ (optimum-first). The reduction Path 1 claims would require flipping the direction, which is not a free move. |
| **C** (Rubin-Shamir-Tishby 2012 "makes the reverse-KL-as-IB-for-control formulation explicit") | **Partially verified; direction must be flagged** | Rubin 2012 explicitly uses $D_{\mathrm{KL}}(\pi_s\Vert\rho_s)$ as the control-information quantity (Sec. 2.2, Eq. 3, p. 4), with free-energy objective $F_\pi = I_\pi - \beta V_\pi$ (Sec. 3.1, p. 5), Bellman recursion Theorem 1 (p. 5). The "IB" label is NOT in the paper; Rubin calls the parallel "similar to rate-distortion theory" (§3.1, p. 5). The direction is *opposite* to AAD's canonical form under $\rho = \pi^*$. The "reverse-KL-as-IB-for-control" label is AAD's creative re-reading, not Rubin et al.'s own framing. |
| **D** (Levine 2018 develops control-as-inference with reverse-KL against policy target throughout) | **Partially verified with terminology correction** | Levine throughout uses $D_{\mathrm{KL}}(q\Vert p^*)$ (proposal-first, target-second) via the variational free-energy framework (§3.1, Eq. 11, p. 8). Sec. 5.2 (p. 15) explicitly distinguishes "RL's mode-seeking $D_{\mathrm{KL}}(p_\theta\Vert p_{\mathrm{tgt}})$" from "supervised's $D_{\mathrm{KL}}(p_{\mathrm{tgt}}\Vert p_\theta)$." In Bishop-convention naming this is reverse-KL; in AAD's $\pi^*$-first naming it is forward-KL. **Levine does not connect to IB** — the spike's implied IB-for-control lineage through Levine is not supported. The control-as-inference connection is to Kalman duality (Todorov 2008), linearly-solvable MDPs (Todorov 2006), path-integral control (Kappen 2011), max causal entropy IRL (Ziebart 2010) — none of which are IB. |

**Aggregate.** Of the four load-bearing Path 1 claims, **one is contradicted** (A), **one is weakly supported with required direction-flip** (B), **one is partially verified with a framing mismatch** (C: Rubin 2012 doesn't self-describe as IB-for-control), **one is partially verified with a naming-convention issue** (D: Levine uses the mode-seeking direction but doesn't connect to IB). The spike's strongest rhetorical move — "reverse-KL IS IB's relevance term under the decision-theoretic relevance variable" — is **not PDF-supported at the direct attribution level**.

### §12.3 — Extensions Path 1 can reach (that the spike did not)

The PDFs actually enable **stronger moves** than the spike attempted, in two directions:

**(E1) Rubin 2012's PAC-Bayesian generalization bound (Theorem 3, p. 10).** The spike treats $I_\pi$ only as a policy-complexity cost. Rubin 2012 shows that under a-priori default $\rho_s$ and empirical reward estimate $\hat R$, the control information bounds the generalization gap:

$$\tilde D_{\mathrm{KL}}(\hat V_\pi(s_0)\Vert V_\pi(s_0))\;\leq\;\frac{I_\pi(s_0) + \log(2m/\delta)}{m-1}$$

This is a **robustness/generalization result**, not a compression/decision-consistency result. It gives AAD a *fourth* independent motivation for the strategy-cost form (alongside (a) regret-bound direction-forcing, (b) chain-rule additivity forcing the reverse-KL form, (c) Bregman/Fenchel-duality with edge-update log-odds). This is a natural addition to `#deriv-strategy-cost-regret-bound`'s §6.2 (Secondary characterizations).

The AAD translation: under finite-data learning of the strategy DAG, a strategy with lower information cost (lower $D_{\mathrm{KL}}$ against the reference policy) has tighter generalization — a PAC-Bayesian concentration property. This is an *operational* argument for the reverse-KL form that is independent of the regret-bound and independent of chain-rule additivity. It supplies what Path 4 failed to supply (an independent uniqueness route): PAC-Bayesian robustness gives a reason to prefer the KL-to-reference form over alternative divergences, via a generalization-bound route that is not a re-formulation of Shore-Johnson.

**(E2) Rubin 2012 §3.3 deterministic-environment linearization (p. 8).** Under deterministic state-transitions, the Bellman recursion for $F^*$ reduces to a *linear* equation $Z = \Phi Z$ with $\Phi_{s, s'}(\beta) = \sum_a \rho_s(a) e^{\beta R(s, a)}\mathbb 1[s' = x_{s, a}]$ for $s' = x_{s, a}$ else 0. This is the AAD analog of a `#result-sector-persistence-template` deterministic reduction under which the nonlinear value-information trade-off becomes solvable in closed form. AAD has not, as far as I've found, surfaced this deterministic-environment reduction as a named simplification; it is a useful instance of "AAD machinery has a clean linear-algebraic form in the deterministic sub-scope" — parallel to how the sector condition has an $\alpha_1$ sub-scope with clean derivation.

**(E3) Tishby-Polani 2011's "perfectly-adapted environment" result (Sec. 7.2, pp. 22–23).** TP2011 shows that if environment transitions satisfy $p(s'\mid s, a) = q_\beta(s'\mid s, a)$ (Eq. 23), the future-information term reduces to *pure* value-relevant content: *"maximizing the future information is equivalent to value maximization"* (p. 23). This is a **condition under which the information cost and the value objective coincide** — a degenerate case where the strategy-cost trade-off collapses (zero at the optimum). AAD's analog: under what conditions on the environment does the strategy-cost reverse-KL and the regret bound *coincide exactly*? The TP2011 result suggests a class (perfectly-adapted environments) where $I_\pi = \beta V_\pi$ at the optimum — which would collapse the IB trade-off to a single curve. Not a result AAD has currently. Potentially a follow-up spike, not a §12 addendum move.

**(E4) Honest attribution of AAD's direction choice.** The PDFs clarify that AAD's $\pi^*$-first KL direction is *not* the standard direction in this literature lineage:
- TP2011 uses multi-information-with-marginal-reference (direction-less; the reference is auto-generated from the policy itself).
- Rubin 2012 uses $D_{\mathrm{KL}}(\pi_s\Vert\rho_s)$ — agent-first, default-second.
- Levine 2018 uses $D_{\mathrm{KL}}(p_\theta\Vert p_{\mathrm{tgt}})$ — agent-first, target-second.

**AAD is the outlier.** All three standard control-as-inference and information-theoretic-MDP frameworks put the agent's policy *first* and the reference *second*. AAD's $D_{\mathrm{KL}}(\pi^*\Vert Q_\Sigma)$ puts the optimum first. This is because AAD's direction is **forced by the regret-bound derivation**, which requires the optimum (not the agent) as the reference for the bound. The choice is well-motivated internally but it is *distinctive*, not conventional.

This is a strengthening opportunity: the segment should **own** the direction choice as AAD-distinctive, rather than framing it as "the standard control-as-inference reverse-KL form." The regret-bound derivation is the reason; it is also what gives AAD its tight Bretagnolle-Huber identity under deterministic $\pi^*$ (Path 5) — which is only tight in the $\pi^*$-first direction. The direction choice is *doing work* for AAD that it wouldn't do in the Rubin/Levine direction.

### §12.4 — Shortfalls: what needs to be demoted, rephrased, or removed

**(S1) Demote the "reverse-KL IS IB's relevance term" claim.** The claim cannot be PDF-anchored to TP2011 or Rubin 2012 as the spike body presented it. The accurate claim is weaker: "AAD's reverse-KL strategy-cost objective is in the *same research lineage* as the Tishby-Polani / Rubin-Shamir-Tishby / Ortega-Braun information-theoretic-MDP tradition, with a direction choice that is AAD-distinctive and motivated internally by the regret-bound derivation." The "IB with a decision-theoretic relevance variable" framing should be presented as an **AAD interpretation** of the IB framework, not an established IB-for-control result in the cited literature. This is the honest positioning.

**(S2) Remove Claim A's specific formula attribution to TP2011.** The formula $\max_\pi\mathbb E[R] - \beta^{-1}I(\Pi;X)$ with $I(\Pi;X) = \mathbb E[D_{\mathrm{KL}}(\pi\Vert\pi_0)]$ is not in TP2011. Attribute the *direction-forward* form to Rubin et al. 2012 where it actually appears (Eq. 3, Sec. 2.2, p. 4, with $\rho_s$ as reference); attribute TP2011 separately as "multi-information-for-future-trajectory" (Eq. 15, p. 19, the Information-to-Go construction).

**(S3) Correct title of the TP2011 paper.** The correct title is "The Information Theory of Decision and Action" (singular). `ref/INDEX.md`, the spike body, and any segment-level citation need to be updated.

**(S4) Flag the KL-direction terminology collision.** Bishop-convention "reverse-KL" (mode-seeking, $D_{\mathrm{KL}}(q\Vert p^*)$ with $q$ the approximation) matches Levine's usage; AAD's "$\pi^*$-first" convention labels this as "forward-KL." The spike body uses both conventions interchangeably, which reads coherent but is internally ambiguous. The segment should pick one and state it (AAD's convention is $\pi^*$-first, and AAD's "reverse-KL" = $D_{\mathrm{KL}}(\pi^*\Vert Q_\Sigma)$, which in Bishop-convention is "forward-KL" — AAD's naming is the *opposite* of Bishop's). This is worth a footnote in `#deriv-strategy-cost-regret-bound`.

**(S5) Demote Levine 2018's role as IB-for-control lineage support.** Levine 2018 does not connect to IB; it connects to max-entropy RL via the exponentiated-reward graphical model. The spike's Claim D should be reduced to: "Levine 2018 uses the mode-seeking KL direction ($D_{\mathrm{KL}}(q\Vert p^*)$) throughout in the max-entropy RL / control-as-inference framework." The IB connection is an AAD-internal framing move, not something Levine 2018 establishes.

### §12.5 — Updated segment-level deliverables

These replace the §9 recommendations of the spike body for the Path-1-related moves. Path 5 (BH identity) and Path 7 (Fenchel-Bregman) deliverables stand unchanged.

**(SD1) `#deriv-strategy-cost-regret-bound` §6.3 draft (revised from spike §9 recommendation 2).**

*Title:* "Information-theoretic-MDP lineage and AAD's direction choice."

*Content:*
> The AAD reverse-KL $D_{\mathrm{KL}}(\pi^*\Vert Q_{\Sigma_t})$ strategy-cost form sits within an established research lineage — the information-theoretic treatment of decision problems initiated by Tishby & Polani 2011 ("The Information Theory of Decision and Action," *Perception-Action Cycle*, Springer, pp. 601–636; Eq. 15 introduces *Information-to-Go* $\mathfrak I^\pi$, a multi-information-of-future-trajectory quantity; Eq. 17 the value-information trade-off) and developed further by Rubin, Shamir & Tishby 2012 ("Trading Value and Information in MDPs," *Decision Making with Imperfect Decision Makers*, Springer, pp. 57–74; §2.2 Eq. 3 the *control information* $\Delta I(s) = \sum_a \pi_s(a)\log(\pi_s(a)/\rho_s(a))$; §3.1 Theorem 1 the Bellman recursion for the free-energy $F_\pi = I_\pi - \beta V_\pi$). The shared framework — value and information as joint first-class quantities in MDP optimization, with a KL divergence measuring the information cost of a policy against a reference — is the context in which AAD's strategy-cost objective naturally lives.
>
> AAD's direction choice is **distinctive within this lineage**. Tishby-Polani 2011 uses the stationary marginal $\pi(a)$ as reference (direction-neutral: the reference is auto-generated from the policy itself, yielding a multi-information); Rubin et al. 2012 uses a default $\rho_s(a)$ (typically uniform) with direction $D_{\mathrm{KL}}(\pi_s\Vert\rho_s)$ (agent-first, default-second); the control-as-inference lineage via Levine 2018 ("Reinforcement Learning and Control as Probabilistic Inference," arXiv:1805.00909, §3.1 Eq. 11, §5.2) uses $D_{\mathrm{KL}}(p_\theta\Vert p_{\mathrm{tgt}})$ (proposal-first, target-second). AAD's $D_{\mathrm{KL}}(\pi^*\Vert Q_{\Sigma_t})$ — optimum-first, agent-second — is the *opposite* direction.
>
> AAD's direction is forced by the regret-bound derivation (§5), which requires the optimum as reference for the bound to be tight. Other directions (mode-covering from the target's perspective) do not support the regret-bound argument; AAD's direction is selected specifically because it does. The Bretagnolle-Huber identity in §4 (under deterministic $\pi^*$, $D_{\mathrm{KL}} = -\log Q_{\Sigma_t}(a^*)$ exactly) also requires the $\pi^*$-first direction; the flipped direction $D_{\mathrm{KL}}(Q_{\Sigma_t}\Vert\pi^*)$ is degenerate under deterministic $\pi^*$.
>
> Terminology note: under Bishop 2006's convention ($D_{\mathrm{KL}}(q\Vert p)$ with $q$ the approximation called "reverse-KL"), Rubin 2012 and Levine 2018 both use reverse-KL. Under AAD's $\pi^*$-first convention ($D_{\mathrm{KL}}(\pi^*\Vert Q_\Sigma)$ called "reverse-KL"), AAD uses the opposite direction. These are *different surface orderings of the same operational property* (mode-seeking from the target's perspective) only when the target is deterministic; under softened targets (as in Levine's exponentiated-reward construction), the two forms are different objects. AAD's direction is specifically the one that stays well-defined under deterministic $\pi^*$.

*Citations needed at segment level:* Tishby-Polani 2011 (correct title), Rubin-Shamir-Tishby 2012 (specific Eq. 3 and Theorem 1 page references), Levine 2018 (specific §3.1 Eq. 11 and §5.2 p. 15 references). The §6.3 draft above has these inline.

**(SD2) `#deriv-strategy-cost-regret-bound` §6.2 add sub-item: "PAC-Bayesian generalization (Rubin et al. 2012 Theorem 3)."**

> A fourth operational property of the $\pi^*$-first KL form comes from Rubin, Shamir & Tishby 2012 Theorem 3 (p. 10): under a-priori stochastic default policy and empirical reward estimate, the control-information $I_\pi$ bounds the generalization gap of the value function:
> $$\tilde D_{\mathrm{KL}}(\hat V_\pi\Vert V_\pi)\leq \frac{I_\pi(s_0) + \log(2m/\delta)}{m - 1}$$
> This is a PAC-Bayesian concentration bound — policies with lower information cost have tighter generalization under finite data. In AAD terms: minimizing the strategy-cost objective not only minimizes the regret-bound tightness (§4) but also the value-function generalization gap under finite empirical estimation. This is an *independent operational motivation* for the KL-to-reference form that does not require the chain-rule axiom.

*Citation:* Rubin, Shamir & Tishby 2012 Theorem 3.

**(SD3) `#form-information-bottleneck` add a cross-reference paragraph (revised from spike §9 recommendation 8).**

> The AAD strategy-cost objective's reverse-KL relevance term is *not* an instance of the canonical IB objective $I(X; T) - \beta I(T; Y)$ with Shannon mutual information in both terms. Rather, it sits in the **information-theoretic-MDP** lineage (Tishby-Polani 2011 "The Information Theory of Decision and Action" *Perception-Action Cycle* pp. 601–636; Rubin-Shamir-Tishby 2012 "Trading Value and Information in MDPs" *Decision Making with Imperfect Decision Makers* pp. 57–74), where value and information are joint first-class quantities and the information quantity is a KL-to-reference-policy form (not a mutual information with an external relevance variable). Both IB and information-theoretic-MDP trace to the common ancestor of rate-distortion theory (Shannon 1959); the IB instance uses MI-to-relevant-label as the fidelity term, while the information-theoretic-MDP instance uses KL-to-reference-policy. AAD's compression-operations framework (§`#disc-compression-operations`) uses the IB form for the $M_t$, $G_t^{\mathrm{shared}}$, and $\Lambda$ compressions (each with a Shannon-MI relevance term); the strategy-cost compression (`#form-strategy-complexity-cost` + `#deriv-strategy-cost-regret-bound`) uses the information-theoretic-MDP form. Both are valid Lagrangian relaxations of a rate-distortion problem; the choice of fidelity term depends on whether the compressed variable is meant to preserve information about an observable (IB) or to match a reference policy (information-theoretic-MDP).

*Deliverable:* this paragraph added to `#form-information-bottleneck`'s Discussion. Pre-empts "why isn't the strategy-cost term a mutual information like the others?" at the meta-segment level.

**(SD4) `#additive-coordinate-forcing` — no change from PDF verification.**

The divergence-layer Cauchy-FE uniqueness (§6.1 of `#deriv-strategy-cost-regret-bound`) is not affected by the PDF findings. The chain-rule additivity uniqueness argument (Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975) stands as the segment-internal forcing. The Tishby-Polani / Rubin / Levine literature is an *external positioning* question, not a derivation question.

**(SD5) `ref/INDEX.md` — correct the TP2011 title.**

Current (likely) entry: "Information theory of decisions and actions" → corrected: "The Information Theory of Decision and Action" (singular "decision," "action"). Same chapter, same page range 601–636.

**(SD6) No new appendix segment needed.**

The PDF findings are absorbed into existing segments (`#deriv-strategy-cost-regret-bound` §6.2 and new §6.3, `#form-information-bottleneck` cross-reference). The spike body's recommendation against creating a new appendix stands unchanged.

### §12.6 — Updated Path 1 epistemic tier

**Original spike tier for Path 1's derivation.** "Derived, status: robust-qualitative" — equivalence IB $\to$ Tishby-Polani $\to$ AAD reverse-KL, up to additive constants at arg-min level.

**Revised tier after PDF verification.** **Reformulation-grade, status: discussion-level positioning.** The PDF evidence does not support the tier the original claim asserted.

Specifically:
- The "IB $\to$ Tishby-Polani" step is **not in TP2011**; TP2011's objective is Information-to-Go, not an $I(\Pi; X)$ form.
- The "IB $\to$ Rubin 2012" step requires a direction-flip ($\rho$ replaced by $\pi^*$) that the paper does not make and that changes the operational character of the quantity (from mode-covering to mode-seeking).
- The strongest defensible claim is: **"AAD's reverse-KL form is in the Tishby-Polani / Rubin information-theoretic-MDP lineage, with a direction choice forced by AAD's regret-bound derivation."** This is a positioning claim about lineage, not an equivalence theorem.

The demotion is from "derived" to "reformulation-grade / discussion" because the equivalence is not a theorem; it is a family-resemblance between AAD's form and the lineage's forms. The *family-resemblance claim* is well-supported by the PDFs; the *equivalence claim* is not.

**What tier Path 1's post-PDF version should carry.** The deliverable §6.3 draft in SD1 above is **Discussion-grade** (positioning in the literature, not a derivation). It does not need to be tagged "Derived" or "Exact"; it is a *connection* to the external lineage, which is Discussion-appropriate.

The regret-bound direction-forcing derivation (§5) and the chain-rule uniqueness theorem (§6.1) remain the segment's load-bearing derivations; neither is affected by the PDF findings. Path 1's role in the segment is **literature positioning, not additional derivation force**.

**Revised Path 1 verdict.** **Succeeds as literature positioning; fails as equivalence theorem.** The reframing of "reverse-KL is IB's relevance term under the decision-theoretic relevance variable" was a more aggressive claim than the PDFs support. The honest version — "AAD's reverse-KL form inherits from the Tishby-Polani information-theoretic-MDP lineage, with a direction choice that is AAD-distinctive and motivated by the regret-bound derivation" — is more modest but correctly placed; it pre-empts Gemini's "abandoned IB purity" framing by locating AAD in a well-established information-theoretic-MDP lineage (even if that lineage is not *literally* IB), while not overclaiming a formula-level reduction that does not exist.

### §12.7 — Compact deliverables index (for TODO routing)

| Deliverable | Target segment | Priority | Shape |
|---|---|---|---|
| SD1: §6.3 "Information-theoretic-MDP lineage and AAD's direction choice" | `#deriv-strategy-cost-regret-bound` | High | New subsection, Discussion-grade, ~250 words with explicit page/eq citations |
| SD2: PAC-Bayesian generalization item in §6.2 | `#deriv-strategy-cost-regret-bound` | Medium | 1-paragraph addition to existing secondary-characterizations subsection |
| SD3: Cross-reference paragraph | `#form-information-bottleneck` | Medium | New Discussion paragraph |
| SD4: No change | `#additive-coordinate-forcing` | — | N/A |
| SD5: Title correction for TP2011 | `ref/INDEX.md` | High | Metadata fix |
| Tier-correction note | Spike §8 summary table (Path 1 row) | Medium | Already captured in §12.6 above |
| E1 / E2 / E3 follow-up spikes | Future work | Low | Documented in §12.3; not required for current promotion |

### §12.8 — Honest reporting summary

The PDF verification did the work it was supposed to do. It **correctly disconfirmed** a claim the spike made with too little evidence. The spike body's self-flagged caveat ("I have not exhaustively verified every citation below against PDFs... If the specific citation quality matters load-bearingly for segment promotion, a PDF verification pass is needed") was accurate: the citations *were* load-bearing for the strongest rhetorical move, and they *did* fail verification at the specific-formula level.

What the PDFs did NOT do is overturn the spike's **structural** thesis. Reverse-KL-against-policy-target is a canonical form in the information-theoretic-MDP tradition. AAD's strategy-cost objective sits within that tradition. Gemini's "abandoned IB purity" framing remains a **mischaracterization** — but the correct rebuttal is "reverse-KL is the information-theoretic-MDP tradition's canonical form, which is a sibling lineage to IB sharing the rate-distortion ancestor," not "reverse-KL IS IB under the right relevance variable."

This is the strengthen-before-soften posture working correctly: the original strengthening attempted a maximally-strong claim (equivalence), the PDFs reduced it to a more modest one (literature positioning), and the modest one is still a strengthening over Gemini's "acknowledge departure from IB" default. The spike recorded the maximally-strong claim; the §12 addendum records the PDF-supported one. Both land in the archive; the segment promotion uses §12's form.

The remaining Path 5 (BH identity) and Path 7 (Fenchel-Bregman) results are unaffected by PDF verification — they are elementary / textbook-grade results that do not depend on the contested attributions. Those paths remain the spike's strongest contributions and are promoted unchanged.
