*Feeds **B.1** in `../INTENT.md` (top intent B: every load-bearing claim says what kind of claim it is, about which agents, and what would refute it). Typed checks: `reviews/b1-part-ii-check-1.md`.*

# B.1, Part II: the independent check, worked

*Claude Opus 5.5, checker with a bare brief, 2026-10-30. Text read at `f9d11a4a`. The segments checked are byte-identical at `2ec6ec58`.*

This file holds the derivations behind the review's checks and the points that concern the form rather than any one record. Section numbers are the ones the review cites. Items cited from memory rather than read are marked *(recall)*.

## 0. What holds, briefly

The records do what the form asks in most places. They separate the strong tier label from descriptive and normative claims riding on the same segment, and they say "no" in Instantiated plainly. Three records (directed separation R4, control regret R2, orient cascade R2) surface claims the bodies carried without stating, and those are the section's best work. The following re-derived as stated:

- the Bayes-filter computation (directed separation R1);
- the proper-scoring argument (R4), with the proviso in §2;
- the $\mathcal W_{L0}^\ast$ construction;
- the strategy-DAG numbers;
- the two-gap identity;
- the stationary gain $1 - \lambda$.

The record count is 35: 18 formal, 11 descriptive and **6** normative by the first word of each Register field. The hand-off note's "seven normative" in its §2 is a miscount.

The defects found are of three kinds: records that contradict themselves or their own population, body sentences the B.1 pass did not drain, and body defects the records transcribe faithfully. The review marks which is which for each item.

## 1. The objective functional: what the axioms bound

Take the body's target-region row, $V(\tau) = \mathbb 1[s_T \in R]$. For $\tau_0$ with $V(\tau_0) = 0$, the lower contour set $\{\tau' : \tau_0 \succsim \tau'\} = \{\tau' : s_T(\tau') \notin R\}$ is closed iff $R$ is open, and the upper contour set at a value-1 trajectory is closed iff $R$ is closed. So (A3) holds only for clopen $R$, while the preference has a real-valued representation for any $R$. (A1)–(A3) are therefore sufficient for a continuous representation and not necessary for a real one. The sentence "the agents on which the axioms fail are exactly the agents this interface excludes" is false, and the record's population is narrower than the class the interface admits. The honest boundary of real-representability is Debreu's order-separability condition, not continuity.

The lexicographic exclusion (E1) holds on $\mathbb R^2$ and on any domain carrying a continuum of incomparable "first-coordinate" ties. On a countable trajectory space every complete preorder, lexicographic included, has a real representation.

The expectation form needs the von Neumann–Morgenstern axioms on lotteries, not on trajectories: completeness and transitivity of $\succsim$ over lotteries, mixture continuity, and independence. On an infinite outcome space it also needs a continuity or dominance condition for the representation to be an expectation of a bounded $V$. The body lists (A1)–(A3) on trajectories and adds (A4).

On Instantiated: the body names "individual agents and tightly coordinated teams under unified command" as the target class. Humans are individual agents. *(recall)* Choice experiments find most subjects close to GARP-consistent (Choi, Fisman, Gale & Kariv 2007, *AER*), so (A1)–(A2) roughly hold. Independence fails systematically (Allais 1953; Kahneman & Tversky 1979). Unless the body excludes humans, the expectation form's scope claim is instantiated and fails on them, and the record's falsifier, which tests only GARP, under-tests the claim.

## 2. Directed separation: three provisos

**R1, stochastic updates.** $M_{\tau^+} = f_M(M_{\tau^-}, e_\tau, \xi)$ with internal randomness $\xi$ gives $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, e_\tau)$ iff $\xi \perp G_t \mid (M_{\tau^-}, e_\tau)$. A pseudo-random generator shared between the planner and the filter makes $\xi$ a function of the seed and earlier draws, some of which were consumed by goal-dependent planning. The signature has no goal argument, yet the factorization fails. Contrived, but it is exactly what "the signature excludes it" rules out without saying.

**R4, the proviso.** With $W$ the world and $E = (M_{\tau^-}, e_\tau)$, the optimal forecast from $(E, G)$ under a strictly proper score is $P(W \mid E, G)$. It equals $P(W \mid E)$ iff $W \perp G \mid E$. If $W \perp G \mid M_{\tau^-}$ and the event includes the action (which #form-event-driven-dynamics provides, since action completions are events), then $W \perp G \mid E$ follows. Without the action in $E$, conditioning on an observation that depends on both $W$ and a goal-chosen action can induce dependence. So the proviso should read "beyond $(M_{\tau^-}, e_\tau)$".

**R4, the falsifier.** "At equal encoding capacity, a goal-allocated encoder whose $M_t$ scores better than the goal-blind encoder's on a goal-neutral score." If "the goal-blind encoder" is the capacity-constrained optimum for that score, no other encoder at equal capacity beats it, so the falsifier cannot fire and the norm is true by construction on that reading. If it is an arbitrary goal-blind encoder, the comparison says nothing about coupling. The falsifier needs to fix which goal-blind encoder, and which goal distribution the neutral score averages over.

**R2, structure against magnitude.** The body defines classes structurally ("distribution-independent") and also gives bands of $\kappa$ for each class. A low $\hat\kappa$ on one event does not refute a structural Class 3 placement, so the falsifier refutes at most the magnitude claim ($\kappa \approx 1$ "under most distributions"), and should say so.

## 3. The value object's $G_t$-independence

$Q_O(M_t, a; \pi_{\text{cont}}, N_h) = \mathbb E[V_{O_t}(\tau) \mid M_t, do(a), \pi_{\text{cont}}]$ is an expectation under the law $M_t$ encodes. As a function it takes $(M_t, a, \pi_{\text{cont}}, N_h, O_t)$ and nothing else. That it does not vary with $G_t$ at fixed arguments is true of every agent, so the claim "exact for any causally-disciplined agent … consumes only the zero" uses nothing about $\kappa$. The record's falsifier asks for a variation the definition forbids.

The reading on which the claim has content is that, for the *true* conditional, $\mathbb E[V \mid M_t, G_t, do(a)] = \mathbb E[V \mid M_t, do(a)]$, i.e. outcome $\perp G_t \mid (M_t, do(a))$ with the continuation fixed. Two routes break it at $\kappa = 0$:

- **Goal-world correlation beyond $M_t$.** A principal who knows a storm is coming sets the goal "reach the shelter"; the agent's $M_t$ lacks the storm. Conditional on $M_t$, the goal carries world information, so outcomes depend on $G_t$. The agent is perfectly disciplined.
- **Non-action signaling.** If $G_t$ reaches the world other than through action (the bounded-signaling assumption of #der-directed-separation, which that segment says fails for humans, LLMs and embodied robots), outcomes depend on $G_t$ given $(M_t, do(a))$.

So on the contentful reading the premises are $\kappa = 0$ for the update, plus bounded signaling, plus a goal origin uninformative about the world given $M_t$. At $\kappa \gt 0$ the first premise fails as well, which is what the body's degradation clause captures. This also removes directed separation R3's exemplar: the scoping rule may be right, but this is not a result "whose derivation uses only the zero". The C.2 spike's commit `894bab9b` mentions "a third repair for the value object". I have not read it, to keep this check unprimed; the integrator should reconcile the two.

**The identification gate.** Positivity (C1) and ignorability (C2) are what let an interventional law be identified *from data*. When the model encodes the mechanism by construction, as with Kalman + LQR, (C3) alone suffices, and the deterministic LQR policy is no obstacle. The body's "additionally needs positivity, no unmodeled confounder, and a known action-transition mechanism" should read: (C3) supplied by construction, or (C1)+(C2) to identify it from interventional data. This also dissolves the record's internal clash between True of (Kalman + LQR) and False of (deterministic policies), though Kalman + LQR remains outside learning-agent scope, so the record still needs a learning instance.

## 4. Observability: the depth-$d$ product, derived

Chain $A_1 \to A_2 \to \cdots \to A_d \to G$ under L0 with independent edge outcomes, every intermediate observable, and Beta-Bernoulli edges with gain $g_k = 1/(n_k + 1)$. On a trial, edge $k$ is executed and observed iff edges $1, \dots, k-1$ all succeed, an event of probability $\pi_k = \prod_{j \lt k}\theta_j$ that is independent of edge $k$'s own outcome. Given observation, edge $k$'s update is $g_k (y_k - \hat p_k)$ with $\mathbb E[y_k] = \theta_k$. So the expected per-trial correction is

$$\mathbb E[\Delta \hat p_k] = \pi_k\, g_k\, (\theta_k - \hat p_k),$$

which is diagonal in the error $\delta_k = \hat p_k - \theta_k$, with coefficient $\pi_k g_k$. The sector condition then holds with $\alpha_\Sigma = \min_k \prod_{j \lt k}\theta_j / (n_k + 1)$, the B.2 formula at $d = 2$. This uses nothing beyond B.2's own steps (upstream outcomes are drawn from the true rates, not the credences). It holds at B.2's tier, and the segment's "conjectured for depth $d$" can become derived.

For R1, the counter-instance to "frozen": in B.3 (two edges, $B$ unobserved), $y_G \sim \text{Bernoulli}(\theta_1\theta_2)$. With $\theta_2$ known, $\hat\theta_1 = \bar y_G / \theta_2$ is consistent, so edge 1's credence converges to the true rate from the agent's own observations, which is R1's falsifier. With neither known, the edges still move on every trial; they are non-identified, not frozen. "Frozen at the prior" is the case where no observed variable depends on the node.

## 5. The right rung of convention monotonicity

The quantities compared are $A_O^{\text{RH}} = \sup_a Q_O(a; \pi_{\text{RH}})$ and $A_O^{\text{B}} = \sup_a Q_O(a; \pi^\ast)$, with $\pi^\ast = \arg\sup_{\pi \in \Pi} V_O(\pi)$. The written proof shows $V_O(\pi_{\text{RH}}) \le V_O(\pi^\ast)$ and passes to the sups, but $Q_O(a; \pi) \neq V_O(\pi)$. After an off-path first action $a$, an argsup policy $\pi^\ast$ may behave arbitrarily badly, so $Q_O(a; \pi_{\text{RH}}) \le Q_O(a; \pi^\ast)$ need not hold for each $a$. A valid route: if the policy "do $a$, then follow $\pi_{\text{RH}}$" is in $\Pi$, then $Q_O(a; \pi_{\text{RH}}) \le \sup_{\pi \in \Pi} V_O(\pi) = V_O(\pi^\ast) \le \sup_a Q_O(a; \pi^\ast)$. That holds for the class of all history-dependent policies and for any $\Pi$ closed under first-action prefixing. Alternatively, it holds if $\pi^\ast$ is optimal from every state. The rung is sound under a hypothesis the body does not state; I did not find a counterexample.

## 6. Things the form should settle

**Register of a theorem about a class of agents.** The form says a formal claim "says nothing about which real agents are described until a descriptive claim adopts it". Four records nonetheless label a conditional theorem about a hypothesis-defined class as descriptive: Richens et al. (agent spectrum R2), the identification result (loop R2), the no-forgetting failure (schema R1) and the gain-driven freezing (observability R1). Directed separation R1 and schema R2, which are the same kind of statement, are labelled formal. A rule that would sort them: the theorem is formal, and its population is the hypothesis class. A separate descriptive entry, when there is one, claims that a named real class meets the hypotheses, and its falsifier is a measurement on that class.

**Instantiated by a theorem.** "Instantiated: by an external theorem" (agent spectrum R2) is not an instantiation under the form's own definition. The form could say outright that a theorem, imported or not, never fills this field.

**Population of a formal claim.** The form asks for "the set of representations it is true of", not agents. About ten formal records name agents ("causally-disciplined agents in learning-agent scope", "agents that evaluate $Q_O$ from experience", "L0 strategy learners", "systems in agency scope", "agents with a scalar $V_{O_t}$"). Whether this is a defect or the form being too strict is worth deciding once. When a formal record names agents, a reader takes the tier label to apply to those agents, which is the conflation the section exists to prevent.

**Falsifiers name no sentence.** The form says a falsifier "names which sentence of the body it refutes". About a dozen of the thirty-five say "none" (correctly, for definitions and representations). Of the rest, most name a measurement or construction and leave the body sentence it would refute implicit. Observability R2 and causal-hierarchy R2 are the exceptions that point at a step. Anchoring each falsifier to an equation tag or quoted clause would make refutations land on the right sentence, and would give vsect claim-level anchors a natural target.

**Coverage.** "One entry per distinct claim" is not met where unrecorded claims carry conclusions:

- the aspiration hypothesis in #def-satisfaction-gap, which #der-orient-cascade's R2 uses as its False-of;
- the frequency claims in #def-strategy-dag behind "net overestimation";
- the cascade's five-level timescale ordering and its virtuous and vicious cycle, which the summary presents as a consequence.

A lighter rule might be: any claim another record cites, or any claim a conclusion rests on, gets its own entry.

## 7. Corrections to the hand-off note (`00-records.md`)

- Normative records number 6, not 7.
- The Hafez figures are in the abstract of arXiv 2603.01283 (Hafez, Reid & Nazeri), as 89.3% against 44.0% *of coupling degradations*, across 21 trained continuous-control agents. The flag can come off at abstract granularity and the population can be named. The body's "accuracy" and "environmental perturbations" are not the paper's words. The setup is unread.
- Richens et al. v5 is titled "General agents contain world models", as the body says. Its Assumption 1 includes full observability and stationarity, which neither the body nor the record carries.
- No `[^recall-2026-10-30]` footnote comes off on this check; I read none of those primaries. *(recall)* Bar-Hillel 1973 reports conjunctions overestimated and disjunctions underestimated against the product rule for independent components, the opposite direction to the L0 sign rule. That strengthens the record's "may be false of" humans. Daw, Niv & Dayan 2005 is fitted mainly to rodent data.

## 8. Feedback on the brief and the effort

The bare brief worked as intended for me: the most consequential findings (§3, the observability self-contradiction, the 4c trigger against the residual no-go) came from reading the bodies against each other, not from the hand-off's checklist, which I read but treated as a hypothesis list. One adjacent observation is beyond B.1. Several defects (the (C2) wording across three segments, the forced-ordering carriers in the SOP table and the OUTLINE) sit in files no record points at. A drain check keyed to the claim, of the "pickaxe the phrase across the repo" kind, catches what a per-segment check cannot.
