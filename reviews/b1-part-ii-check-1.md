---
kind: review
author:
  name: Claude Opus 5.5 (B.1 checker, bare brief)
  role: independent adversarial checker
sources:
  - msc/inside-out-2026-10/b1-claim-records/01-check-1.md
written: 2026-10-30
---

# B.1, Part II: an independent check of the sixteen Claim Records

KR **B.1** (`msc/inside-out-2026-10/INTENT.md`; top intent B: every load-bearing claim says what kind of claim it is, about which agents, and what would refute it). The checks below re-derive from the text as written at `f9d11a4a`. The sixteen segments, `deriv-convention-monotonicity`, `impl-causal-access` and `doc/sop/format.sop.md` are byte-identical between `f9d11a4a` and `2ec6ec58`. One `## Cn (check)` per segment, with per-record detail in the free text. For every defect, the text says whether **the record misreads a sound body**, **the record faithfully carries a defective body**, or **both are defective**, so whoever integrates knows what to edit. The derivations and the format-level feedback are in the source file above.

What I did not do: I read none of the primaries behind the `[^recall-2026-10-30]` footnotes, so no footnote comes off on my account. For Hafez et al. I read the arXiv abstract page only. Where I cite literature from memory (Allais; Choi et al. 2007; Bar-Hillel's direction; Daw et al.), the source file marks it as recall.

## C1 (check)
- target: segment:form-objective-functional
- at: f9d11a4a
- act: rederive
- line: derivation
- criterion: Is the record's population, (A1)–(A3) (and (A4) for the expectation form), the boundary of the class the interface admits and excludes, as the body's "exactly the agents this interface excludes" says? Is Instantiated "not by this project … not as a test of its target class" true?
- committed: after
- outcome: narrowed
- recheck: source §1; check that the target-region row $\mathbb 1[s_T \in R]$ is real-valued and that its contour sets are closed only when $R$ is clopen

Both are defective. (i) The body's own table carries a row outside the population: the target-region objective $V = \mathbb 1[s_T \in R]$ has a real-valued representation, yet its lower contour set at a value-0 trajectory is $\{s_T \notin R\}$, which is closed only if $R$ is open. So (A3) fails for any $R$ that is closed and not open, while the interface admits the row. (A1)–(A3) are sufficient for a continuous representation, not necessary for a real-valued one, and "the agents on which the axioms fail are exactly the agents this interface excludes" is false. (ii) (E1) "admit no real-valued representation at all" holds on rich domains such as $\mathbb R^2$; on a countable trajectory space every complete preorder is representable, lexicographic ones included. (iii) The expectation form needs the vNM axioms on *lotteries* (completeness, transitivity and mixture continuity on lotteries, plus independence; on an infinite outcome space, a further continuity or dominance condition). The body states (A1)–(A3) on trajectories and adds only (A4). (iv) Instantiated: humans are individual agents, and the body names "individual agents" as the target class without excluding them. Allais-type violations of independence (A4) are systematic in human choice data. GARP consistency (A1–A2) largely holds (Choi, Fisman, Gale & Kariv 2007, from recall). So the honest field is "yes, on humans: (A1)–(A2) roughly hold, (A4) fails", unless the body excludes humans. The record's falsifier tests only GARP, that is (A1)–(A2), and leaves (A3)–(A4) untested.

## C2 (check)
- target: segment:form-complete-agent-state
- at: f9d11a4a
- act: read-check
- line: derivation
- criterion: Does the record's register, population and false-of (the frozen-coordinate counterexample) match the body and #deriv-decomposition-uniqueness as summarized there?
- committed: after
- outcome: confirmed
- recheck: compare the record's four fields with the Epistemic Status paragraph

Faithful. Kalman + LQR as an instance of a *representation* is fine here; the learning-agent-scope problem in C6 does not arise, because this segment precedes the narrowing.

## C3 (check)
- target: segment:def-strategy-dimension
- at: f9d11a4a
- act: read-check
- line: derivation
- criterion: Are both records faithful, and does the descriptive timescale record name a falsifier that would refute the body's sentence?
- committed: after
- outcome: confirmed
- recheck: Discussion, "different update dynamics"

Faithful. The record honestly states that the population is unbounded ("many agent populations"). One coverage note: `der-orient-cascade` Discussion carries a five-level version of the ordering ($\nu_{\text{epistemic}} \gg \cdots \gg \nu_{O\text{-revision}}$), and no record covers it.

## C4 (check)
- target: segment:def-agent-spectrum
- at: f9d11a4a
- act: read-check
- line: derivation
- criterion: Does the Richens et al. record state the theorem's hypotheses as its population, and is "Instantiated: by an external theorem" an instantiation in the format's sense? Is "False of: none" true of the taxonomy given that record?
- committed: after
- outcome: narrowed
- recheck: arXiv 2506.01622v5, Assumption 1 and Definition 5; Theorems 1–2

The record misreads the external source, and the record set is internally in tension. (i) Assumption 1 of Richens, Abel, Bellot & Everitt (arXiv 2506.01622v5, ICML 2025) is a *finite, communicating, stationary* controlled Markov process with at least two actions and a *fully observed* environment. A bounded agent is defined by a failure rate $\delta$ relative to the optimal success probability on goals of depth $\le n$. The record's "finite MDPs with a regret bound" drops full observability and stationarity, the two hypotheses AAT's agents most often violate. (ii) The format defines Instantiated as a quantity measured or run on an agent the theory did not construct. A theorem is not that; the field should read "no". (iii) The record calls the theorem "descriptive", which is the register question the source file raises at format level. (iv) "False of: none; a continuum excludes nothing" sits beside the body's claim of "two independent dimensions". By the second record, the blind-seeker region (structured objective, no model) is empty of agents competent at depth $n \ge 2$ in Richens's population. So the independence of the axes is a falsifiable claim, and the second record bears on it.

## C5 (check)
- target: segment:der-directed-separation
- at: f9d11a4a
- act: rederive
- line: derivation
- criterion: R1: the Bayes-filter recursion carries no goal argument, and the factorization holds by signature. R2: the falsifier can refute the structural classification. R4: the proper-scoring argument and the falsifier.
- committed: after
- outcome: narrowed
- recheck: source §2

R1 confirmed for deterministic $f_M$. For a stochastic $f_M$ (a particle filter, a sampled LLM update), $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, e_\tau)$ also needs the update's internal randomness to be independent of $G_t$. A shared PRNG makes the noise correlated with earlier goal-dependent draws, so "the signature excludes it" is too quick. The record should name this proviso. R2: the body defines the classes structurally ("distribution-independent") and also by bands of $\kappa$ ($\approx 1$: Class 3; $0 \lt \kappa \lt 1$: Class 2), and the two definitions conflict: a Class 3 wiring at $\kappa = 0.3$ is Class 2 by band. The record's falsifier inherits the conflict, because a low $\hat\kappa$ from an LLM on one event cannot refute a structural placement that the body says is distribution-dependent in magnitude. That is a body defect the record carries faithfully. R4 confirmed: the conditional law is the unique minimizer of expected score under a strictly proper rule. The proviso should read "the goal carries no information about the world beyond $(M_{\tau^-}, e_\tau)$" (or the action must be in the conditioning set), not "beyond $M_{\tau^-}$". R4's falsifier is unspecified on which goal-blind encoder is meant. If it is the one optimal for the goal-neutral score at equal capacity, no goal-allocated encoder can beat it and the falsifier cannot fire. This bears on open question `degradation-norm-encoding-vs-updating`; I do not answer it. R3's True-of exemplar (the $G_t$-independence of $Q_O$) is defective; see C6. Instantiated "no" is confirmed: nothing in `empirica/`, and NeurIPS Paper 3 lists the first $\hat\kappa$ instantiation as future work. The LLM sycophancy literature (goal- or preference-conditioned shifts in stated belief) is an uncited lead to examine, not an instantiation. The Findings and Working Notes state the Hafez figures as "89% perturbation detection … accuracy". The paper's own wording, at abstract level, is 89.3% *of coupling degradations detected*; see C7.

## C6 (check)
- target: segment:def-value-object
- at: f9d11a4a
- act: rederive
- line: derivation
- criterion: Record 1: is the $G_t$-independence of $Q_O$ a consequence of $\kappa_{\text{processing}} = 0$ alone, can its falsifier fire, and is Kalman + LQR inside the stated population and outside the stated false-of? Is the (C1)–(C3) triple the same triple as in #der-loop-interventional-access?
- committed: after
- outcome: broken
- recheck: source §3; the principal-set-goal counterexample

Both are defective. (i) Read as written, "at fixed $(M_t, O_t, \pi_{\text{cont}}, N_h)$, $Q_O$ does not vary with $G_t$" is true *by definition* for every agent, Class 3 included, because $Q_O$ is an expectation under the model $M_t$ and has no $\Sigma_t$ argument. The record's falsifier therefore cannot fire, and $\kappa = 0$ is not used. The non-trivial reading is $\mathbb E[V \mid M_t, G_t, do(a)] = \mathbb E[V \mid M_t, do(a)]$. It needs more than $\kappa = 0$: the bounded-signaling assumption ($G_t$ reaches the world only through action, which #der-directed-separation says fails for humans, LLMs and robots), and a goal that carries no world information beyond $M_t$. Counterexample at $\kappa = 0$: a causally-disciplined agent whose goal ("reach the shelter") was set by a principal who knows a storm is coming and the agent's $M_t$ does not. Then $G_t$ is informative about outcomes given $M_t$. The body's argument "there is no path from $G_t$ to outcomes bypassing both the action channel and $M_t$" asserts the needed premise and does not derive it from $\kappa = 0$. (ii) Kalman + LQR (True of) is excluded by the record's own population, because #der-causal-hierarchy-requirement places LQR outside learning-agent scope. It also falls under the record's own False-of, because LQR's policy is deterministic in its state, which the record says fails (C1). (iii) The identification gate is miscomposed. When (C3) holds *by construction* (the model encodes $P(o \mid do(a))$), positivity and ignorability are not needed; they are conditions for identifying the mechanism *from data*. So the conjunction "(C1) and (C2) and (C3)" is wrong as a gate. (iv) The record says the triple is the same as the loop segment's, but the two (C3)s differ: here "$M_t$ encodes the action-transition mechanism"; there "the map from decision to executed action is known". Record 2 (convention hierarchy) is confirmed apart from the right-rung proof gap in C17.

## C7 (check)
- target: segment:der-causal-hierarchy-requirement
- at: f9d11a4a
- act: read-check
- line: derivation
- criterion: R1: faithful application of the Causal Hierarchy Theorem. R2: can the Hafez figures and arXiv id be confirmed, and can the population be named?
- committed: after
- outcome: narrowed
- recheck: arXiv abstract page 2603.01283 (Hafez, Reid & Nazeri, "The Informational Cost of Agency: A Bounded Measure of Interaction Efficiency for Deployed Reinforcement Learning")

R1 confirmed. R2: the abstract of arXiv 2603.01283 reports the Information Digital Twin detecting "89.3% of coupling degradations against 44.0% for reward based monitoring", with 4.4 times lower latency, across 21 trained continuous-control agents. The hand-off note's statement that the figures are not in that paper's visible text is not borne out at abstract level. The verification flag can come off at abstract granularity, and the population can be named: 21 trained continuous-control RL agents. The experimental setup is still unread. The body's "detects environmental perturbations at 89% accuracy" does not match the paper's wording (a detection rate for coupling degradations). That is a body defect the record carries.

## C8 (check)
- target: segment:der-loop-interventional-access
- at: f9d11a4a
- act: rederive
- line: derivation
- criterion: Is (C2) as written satisfiable by an agent in agency scope? Is R2's register right, and is its True-of instance stated correctly? Do the Working Notes agree with the corrected body?
- committed: after
- outcome: narrowed
- recheck: do-calculus rule 2, which uses the graph with $a_t$'s outgoing edges removed

Body defects, carried faithfully. (i) (C2) "in mutilated-graph form, $a_t$ is $d$-separated from $o_{t+1}$ given history". In the usual sense of mutilation (edges *into* $a_t$ removed), $a_t \to o_{t+1}$ survives, so the condition is never met by an action with an effect, which is every agency-scope agent. The intended condition is $d$-separation in $G_{\underline{a_t}}$ (the edges *out of* $a_t$ removed): the back-door criterion. The gloss "the policy is unconfounded with the outcome mechanism" is right. The same wording appears in #def-value-object and #impl-causal-access (F1–F3). (ii) Tabular Q-learning converges to $Q^\ast(s,a) = \mathbb E[r + \gamma \max_{a'} Q^\ast(s', a') \mid s, do(a)]$, not to $\mathbb E[R \mid s, do(a)]$. (iii) R2 states an identification result conditional on hypotheses, which is formal; "descriptive" is the register question raised at format level. (iv) The Working Note "Goal-conditioned LLM policies violate (C2) by construction" contradicts the corrected body sentence: an agent whose decision state is a function of its recorded history satisfies (C2) given that history. The C.2/C2 spike holds this area; I note the drain without resolving it.

## C9 (check)
- target: segment:norm-explicit-strategy-condition
- at: f9d11a4a
- act: read-check
- line: derivation
- criterion: Does the record agree with the body, and can its falsifier separate the norm from its precondition?
- committed: after
- outcome: narrowed
- recheck: Epistemic Status bullet "Model bias"; the record's False-of

(i) The record corrects a body sentence that the body still carries: Epistemic Status "loop-based learning does not [inherit model bias]". The record attributes its correction to "(Working Notes)", but it is in the audit-gold follow-up items. Under integration-is-replacement, the body sentence is what should change. (ii) Under the precondition the record keeps (equivalent outcomes, every cost in one unit), "choose the cheaper" is optimal by definition. A comparison run where the precondition holds can therefore go against the rule only through *ex-ante* misestimation of the four costs. The falsifier tests cost estimation, not the norm, and should say so. (iii) From recall: Daw, Niv & Dayan 2005 is a computational account fitted mainly to rodent devaluation data, so "the arbitration the human literature reports" needs a human citation (e.g. Daw et al. 2011).

## C10 (check)
- target: segment:def-strategy-dag
- at: f9d11a4a
- act: rederive
- line: derivation
- criterion: R2 (tree iff exact): the minimal case and the #example-L1 numbers. R1's population against its hypotheses. Coverage: does every distinct claim the segment makes have a record?
- committed: after
- outcome: narrowed
- recheck: $1-(1-0.72)(1-0.56) = 0.8768$; $0.8 \cdot (1 - 0.1 \cdot 0.3) = 0.776$; $\operatorname{Cov} = 0.504 - 0.4032 = 0.1008$; three-node AND case $0.25$ against $0.5$

R2 confirmed: the numbers reproduce. Sufficiency: in a tree, distinct parents have disjoint ancestor sets, hence independent statuses. Necessity: the minimal reconvergent cases. I did not re-derive the general degree argument for every non-tree. R1's population ("every explicit causal plan over a finite horizon") drops causal sufficiency, a hypothesis its own register names and the body calls "systematically violated". R3's title omits the correlation sign: for a latent cause the sign is set by node type *and* the sign of the correlation, which the body states. Coverage gap: the body's frequency claims, "OR-dominated roots are far more common than AND-dominated roots in practice" and "correlated failure is the dominant case", carry the conclusion "net bias is overestimation", and no record covers them. The "signal" sentence in "Detecting latent common causes" is a body defect (F4).

## C11 (check)
- target: segment:def-satisfaction-gap
- at: f9d11a4a
- act: rederive
- line: derivation
- criterion: Does the Formal Expression carry the convention-relativity the record and Epistemic Status claim? Is every claim about agents recorded?
- committed: after
- outcome: narrowed
- recheck: compare $A_O = \sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$ with $A_O^{(1)} = \sup_a Q_O(M_t, a; \pi_{\text{current}}, N_h)$

Body defect, carried faithfully. The defining formula has no continuation parameter. $\sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$ is the $\Pi$-optimum, $A_O^{\text{B}}$, under every convention. The C1 and C2 attainabilities are sups over the first action of $Q_O$ with a fixed continuation, and no formula in the segment states them. So "its value is relative to the continuation convention" is not carried by the definition the record is a record of. The aspiration hypothesis (tag `aspiration-dominance`) is a claim about agents with no record anywhere, yet `der-orient-cascade` R2 uses it as its False-of.

## C12 (check)
- target: segment:def-control-regret
- at: f9d11a4a
- act: rederive
- line: derivation
- criterion: R1 identity $\delta_{\text{sat}} + \delta_{\text{regret}} = V_{O_t}^{\min} - V_O(M_t, \pi_{\text{current}}; N_h)$; R2 falsifier names a comparison
- committed: after
- outcome: confirmed
- recheck: add the two definitions under one convention

The identity holds when both terms are computed under one convention. R2 is honestly recorded as untested.

## C13 (check)
- target: segment:der-causal-insufficiency-detection
- at: f9d11a4a
- act: rederive
- line: derivation
- criterion: R1: the $\mathcal W_{L0}^\ast$ construction gives equal on-policy distributions. R3: does "nonzero sibling covariance implies causal insufficiency" hold for the agent's graph as stated?
- committed: after
- outcome: narrowed
- recheck: $(1 - \theta_C\theta_{1\mid C}) \cdot \theta_2^\ast = \theta_C(1-\theta_{1\mid C})\theta_{2\mid C}$; then compute sibling covariance on the naive-L1 graph of #example-L1

R1 confirmed by direct computation on the three observable events. R3 is a body defect the record carries faithfully. $H_0$ is stated for a causally sufficient *tree*, but the detection criterion drops the tree condition ("$\hat\rho_{ij} \neq 0 \Rightarrow$ DAG is causally insufficient"). On a causally sufficient reconvergent graph, such as the naive-L1 graph of #example-L1 where $C$ is modelled as parent of both siblings, the siblings' covariance is $0.1008$ with no latent cause missing. The test fires, and R3's own falsifier ("covariance … with no latent present") is realized by the body's own example. The criterion needs "siblings with disjoint modelled ancestor sets", or covariance conditional on modelled shared ancestors. A smaller point: for a latent with more than two states, both siblings can depend on it with zero covariance. Binary siblings are then independent, so nothing is biased at that node.

## C14 (check)
- target: segment:der-observability-dominance
- at: f9d11a4a
- act: rederive
- line: derivation
- criterion: R1: are edges touching an unobserved node frozen at their prior, and is the True-of instance one where they are? R2: is the depth-$d$ product derived or conjectured?
- committed: after
- outcome: broken
- recheck: #deriv-edge-credence-dynamics Prop B.3, where edges update from $y_G$ alone

Both are defective. R1's True-of (Props B.2–B.3, unobservable intermediate) is the case R1's False-of calls "not frozen but biased". In B.3 both edges update on every terminal observation; they are not identified per edge, but they are not frozen. The body's headline "unobservable strategy edges cannot be updated … frozen at their prior" holds only when *no observed variable depends on the node*. The gain argument $\eta = U_{\text{edge}}/(U_{\text{edge}} + U_{\text{obs}}) \to 0$ concerns observation of the node itself and ignores downstream evidence. R1's falsifier is realizable: with $\theta_2$ known, edge 1's rate is identified from $y_G$ as $P(y_G = 1)/\theta_2$. R2 under-claims. The depth-$d$ attenuation $\alpha_k = \prod_{j \lt k}\theta_j / (n_k+1)$ follows by the same per-trial argument as B.2 (derivation in the source file). It is derived at B.2's tier, not conjectured.

## C15 (check)
- target: segment:schema-strategy-persistence
- at: f9d11a4a
- act: rederive
- line: derivation
- criterion: R2: the stationary gain under exponential forgetting. R1: does the falsifier refute the claim as stated?
- committed: after
- outcome: narrowed
- recheck: $\hat p' - \hat p = (y - \hat p)/(\lambda n + 1)$; $n_{\text{eff}} = 1/(1-\lambda)$

R2's gain is confirmed: $1 - \lambda$ per observation at the stationary count. R2's population ("the four verified topologies") over-reaches B.1F, which is single-edge. For an intermittently observed edge discounted per time step, the per-observation gain at stationarity is not $1 - \lambda$. #deriv-evidence-allocation-ceiling handles this, but the record's title does not. R1's falsifier fires on benign drift: a frozen estimate at the centre of an oscillating band stays within $R_\Sigma$ indefinitely. The claim is about failing a worst-case threshold, so it needs worst-case (adversarial) drift with $R_\Sigma$ below the range of $\theta$. R1 and R2 also take different registers for statements about update rules of the same kind (format-level point).

## C16 (check)
- target: segment:der-orient-cascade
- at: f9d11a4a
- act: read-check
- line: derivation
- criterion: Does the body now consistently say which steps are forced and which are recommended, as R1 and R2 require? Can 4c's trigger fire in the regime where #der-causal-insufficiency-detection's no-go holds?
- committed: after
- outcome: broken
- recheck: grep the segment for "forced by information dependency", "ORDERING is exact", "derived from the satisfaction-gap"; residual-degeneracy section of #der-causal-insufficiency-detection

The records are right and the body contradicts them. The B.1 split is stated at the top of Epistemic Status, but three sentences still say otherwise. In the same Epistemic Status paragraph: "The ordering of all steps is forced by information dependency" and "Step 5's escalation substeps (5a-5c) are derived from the satisfaction-gap disambiguation table". The convention paragraph has "The cascade's *ordering* is convention-independent (forced by information dependency)". The Working Note has "The cascade's ORDERING is exact — forced by information dependency". Outside the segment, `doc/sop/format.sop.md` line 558 lists "Resolution order forced by information dependency ($M_t$ before $\Sigma_t$ before $O_t$)", and $\Sigma_t$ before $O_t$ is the recommended part. The `01-aat-core/OUTLINE.md` row for #impl-orient-cascade and its heading say "forced by information dependency" without the split (the impl body itself is drained). The 4c trigger, "persistent $\delta_s \approx 0$ with $y_G \neq \hat P_\Sigma$ … usually $y_G \lt \hat P_\Sigma$", is the plan-level residual. #der-causal-insufficiency-detection proves that residual identically zero under on-policy short-circuit execution, because edge credences converge to the regime conditionals. So the trigger can fire only if credences were learned from uncensored outcomes, exactly when the covariance test is already available, and the body should say so. R2's False-of uses the unrecorded aspiration hypothesis (C11). The bearing on open question `cascade-objective-last-stopping-rule` is noted, not answered.

## C17 (check)
- target: segment:deriv-convention-monotonicity
- at: f9d11a4a
- act: rederive
- line: derivation
- criterion: Does the right-rung argument establish $A_O^{\text{RH}} \le A_O^{\text{B}}$ with no condition, as #def-value-object's record states ("impossible by definition")?
- committed: after
- outcome: narrowed
- recheck: source §5

The written step compares $V_O(\pi_{\text{RH}})$ with $V_O(\pi^\ast)$, values from $t$, and then says "taking the supremum over the first action preserves the inequality". The quantities compared are $\sup_a Q_O(a; \pi_{\text{RH}})$ and $\sup_a Q_O(a; \pi^\ast)$, and $Q_O(a; \pi) \neq V_O(\pi)$. The rung does hold when $\Pi$ is closed under prefixing a first action to $\pi_{\text{RH}}$, because then $Q_O(a; \pi_{\text{RH}}) \le \sup_\pi V_O = V_O(\pi^\ast) \le \sup_a Q_O(a; \pi^\ast)$. It also holds when $\pi^\ast$ is Bellman-optimal from every state. "Unconditional" therefore hides a closure hypothesis on $\Pi$. I have no counterexample.

## F1 (finding)
- target: segment:def-value-object
- at: f9d11a4a

(C2) "in mutilated-graph form, $a_t$ is $d$-separated from $o_{t+1}$ given history" is unsatisfiable for an action with an effect, if mutilation removes edges into $a_t$. The intended graph is $G_{\underline{a_t}}$. Separately, the identification gate should be stated as "(C3) by construction, or (C1)+(C2) to identify it from data", not as a conjunction of all three.

## F2 (finding)
- target: segment:der-loop-interventional-access
- at: f9d11a4a

The same (C2) wording as F1. The Working Note's "Goal-conditioned LLM policies violate (C2) by construction" contradicts the corrected Formal Expression sentence that an agent whose decision state is a function of its recorded history satisfies (C2) given that history.

## F3 (finding)
- target: segment:impl-causal-access
- at: f9d11a4a

Line 37 repeats the (C2) wording "$a_t$ d-separated from $o_{t+1}$ given history $H_t$ in mutilated-graph form"; see F1.

## F4 (finding)
- target: segment:def-strategy-dag
- at: f9d11a4a

"Persistent miscalibration of plan success after edge credences have converged is the *signal* of insufficiency" names the plan-level residual. Under on-policy short-circuit execution, #der-causal-insufficiency-detection proves that residual identically zero, so the signal is silent where the no-go holds. The sentence needs the precondition that the credences were learned from uncensored outcomes. The frequency claims "OR-dominated roots are far more common … in practice" and "correlated failure is the dominant case" are descriptive and unrecorded, and the net-overestimation conclusion rests on them.
