---
kind: review
author:
  name: Claude Fable 5.1 (B.1 Part II integration, second mind)
  role: integrator
sources:
  - reviews/b1-part-ii-check-1.md
  - msc/inside-out-2026-10/b1-claim-records/01-check-1.md
written: 2026-10-30
---

# B.1, Part II: integration of the checker's findings that do not overlap the C2/C3 spikes

KR **B.1** (`msc/inside-out-2026-10/INTENT.md`; top intent B: every load-bearing claim says what kind of claim it is, about which agents, and what would refute it). The checker's review `reviews/b1-part-ii-check-1.md` was my input; every finding below was re-derived from the bodies before anything was landed, and where my derivation went past the checker's the text says so. The split given to me: C1, C4, C9, C10 with F4, C11, C13, C14, C15, C17, and C2, C3, C12 if I saw something. C5–C8, C16 and F1–F3 belong to the Part II integrator and are untouched here, as are `def-value-object`, `der-directed-separation`, `der-causal-hierarchy-requirement`, `der-loop-interventional-access`, `impl-causal-access`, `def-model-sufficiency` and `der-orient-cascade`. Text read at `4e442b38`; the checks below are on that text, and the edits are in the working tree, uncommitted, for the integrator to commit by path. The check numbers below are this record's own; where the checker's items are meant they are written "check-1 Cn" (so check-1 C17 is the convention-monotonicity check, this record's C1).

Three rules of the form I applied uniformly, so the SOP can adopt or reject them in one place. (1) A theorem, imported or not, is *formal* with its hypothesis class as population; the claim that a named real class meets the hypotheses is a separate *descriptive* entry with a measurement falsifier. Applied in C1 (representation theorem / target class), C4 (Richens et al. / real multi-step-competent agents), C14 (frozen edges and depth-$d$ attenuation / real learners), C15 (undiscounted Beta-Bernoulli / real gain-decaying systems). (2) "Instantiated" is never filled by a theorem; a theorem's entry says "not applicable" and the descriptive entry says "no" or names the study. (3) A falsifier names the tag, section or quoted clause it refutes. Applied in every entry I wrote.

Mechanics. `vsect revise segment:<slug> --by … --role integrator` was run on every segment edited except `scope-edge-update-causal-validity` (F2). It wrote events for `def-satisfaction-gap`, `def-control-regret`, `form-objective-functional`, `hyp-edge-update-via-gain` (answered `redefined`, since a body claim changed) and `deriv-edge-credence-dynamics` (answered `reworded`; a proof was added, no claim changed); for the others it reported nothing to take in, because no recorded check rested on the exact version my edit replaced, and vsect mints the new version on read. The paths it wrote are under `.vsect/objects/` and `.vsect/events/segment/<slug>/`, uncommitted, for the integrator to commit by path with the segments. `md-press --check` is clean on every edited file and on this record; `bin/lint-outline` is clean; no raw `<` or `>` inside inline math in any edited file. The numeric re-derivations named in the `recheck` fields were run in a scratch script and all agreed with the landed text.

Each check: what was found, what landed, what was declined, what a checker who has not read the review should verify.

## C1 (check)
- target: segment:deriv-convention-monotonicity
- at: 4e442b38
- act: rederive
- line: derivation
- criterion: Does the right rung $A_O^{\text{RH}} \leq A_O^{\text{B}}$ hold with no hypothesis on $\Pi$, as the body's "exact and unconditional" and its one-line proof say?
- committed: before
- outcome: broken
- recheck: the two-policy instance in the segment's "right-rung counterexample": states $x, H, D$; $g$ gives $+1$ to $D$, $p$ gives $0$ to $H$; at $H$, $u$ gives $+10$, $w$ gives $+100$; $\Pi = \{\pi_1 = (x \mapsto g, H \mapsto w),\ \pi_2 = (x \mapsto p, H \mapsto u)\}$; compute $V_O(\pi_1) = 1$, $V_O(\pi_2) = 10$, $\pi_{\text{RH}} = \pi_1$ at $N_r = 1$, $A_O^{\text{RH}} = \max(1, 100) = 100$, $A_O^{\text{B}} = 10$ under both readings

The checker said the written step bounds $V_O(\pi_{\text{RH}})$ when the quantity is $\sup_a Q_O(a; \pi_{\text{RH}})$, that the rung holds under prefix-closure of $\Pi$, and that it had no counterexample. There is one, and it needs nothing beyond the segment's own instance: add a second action at $H$ and restrict $\Pi$ to two policies. The replanner's best first action composes into $p \oplus \pi_1$, worth $100$, which $\Pi$ does not contain. Landed: the right-rung section now states and proves the rung under (PC) prefix-closure of $\Pi$ or (SO) state-wise optimality of $\pi^\ast$, with a note that the two readings of $A_O^{\text{B}}$ in use ($V_O(\pi^\ast)$ and $\sup_a Q_O(a; \pi^\ast)$) coincide under either; the counterexample is in the body as present truth, with (PC) and (SO) each shown to fail there and either shown to restore the rung; the summary, corollary orderings, Epistemic Status, Discussion, Findings and the dead-end Working Note no longer say "unconditional". A sentence names why a restricted $\Pi$ is an AAT case: `def-satisfaction-gap` takes $\Pi$ to be the DAG-representable strategies, which has no closure guarantee. Drained in the same batch: `def-satisfaction-gap` Epistemic Status, `def-control-regret` "Convention hierarchy", `impl-strategy-structure` (body paragraph and the regression-guard Working Note, which had said "right rung unconditional"), and the `01-aat-core/OUTLINE.md` row. Not touched: `def-value-object` lines carrying "unconditional" and its record's "impossible by definition" (the integrator's; sent to them with the construction, F1 below). A checker should verify the arithmetic above by hand, confirm that $\pi_{\text{RH}}$ as defined in `def-value-object` (re-optimize over $N_r = 1$ at each state) is $\pi_1$, and check the (SO) proof's last step, that $\sup_a Q_O(a; \pi^\ast) = V_O(\pi^\ast)$ under state-wise optimality.

## C2 (check)
- target: segment:def-satisfaction-gap
- at: 4e442b38
- act: rederive
- line: derivation
- criterion: Does the Formal Expression's definition of $A_O$ carry the continuation convention that the Epistemic Status and the record say its value is relative to? Does every claim about agents in the segment have a record?
- committed: before
- outcome: narrowed
- recheck: compare the old display $A_O = \sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$ with the C1 form $\sup_a Q_O(M_t, a; \pi_{\text{current}}, N_h)$ in `def-value-object`; grep the segment for `aspiration-dominance`

Confirmed as the checker said: the displayed definition was the $\Pi$-optimum, the C3 form, under every convention, while the segment reads a bare $A_O$ as C1. Landed: the definition is now $A_O(M_t; \Pi, N_h, \pi_{\text{cont}}) = \sup_a Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ with the three conventions as instances, the C3 form $\sup_{\pi \in \Pi} V_O$ stated as equal to it under (PC) or (SO) from C1 above, and $\delta_{\text{sat}}$ said to carry its convention. The aspiration hypothesis has its own record entry (normative, hypothesis-grade; population not yet bounded; false-of: an agent whose planner reaches the $O_f$-optimum, where the inequality is false by definition of $\pi_f$; falsifier: the comparison $V_{O_f}(\pi_a)$ against $V_{O_f}(\pi_f)$), since `der-orient-cascade` R2 uses it as False-of. A checker should verify that no other sentence in the segment still reads $A_O$ as the $\Pi$-optimum under C1 (the Working Notes' "the supremum in $A_O$ is over $\Pi$" is about which policies the continuation is drawn from and I left it).

## C3 (check)
- target: segment:der-observability-dominance
- at: 4e442b38
- act: rederive
- line: derivation
- criterion: R1: are edges into an unobserved node frozen at their prior, as the summary and Formal Expression say, in the case the record names as True-of (Props B.2–B.3)? R2: is the depth-$d$ attenuation derived or conjectured?
- committed: before
- outcome: broken
- recheck: `deriv-edge-credence-dynamics` Prop B.3, where both edges update on every $y_G$; with $\theta_2$ known, $\hat\theta_1 = \bar y_G/\theta_2$ (simulated: $0.599$ for $\theta_1 = 0.6$); the depth-$3$ chain simulation gives $\mathbb{E}[\Delta \hat p_k] = (0.0600, -0.0482, 0.0240)$ against predicted $(0.060, -0.048, 0.024)$

Both defects confirmed. The headline and Formal Expression said edges into any node with $\sigma_v \approx 0$ are frozen; B.3, the segment's own cited instantiation, has both edges moving on every terminal observation, non-identified per edge, and the Discussion already said "stronger than frozen edges". Landed: the freezing claim is scoped to nodes on which no observed variable depends; the unobserved-intermediate-with-observed-terminal case is stated as non-identification, not freezing, with the known-rate identification as the explicit counter-instance; the gain argument is said not to apply as written when a descendant is observed. R1 is now formal (True-of: the never-chosen arm of Prop B.4(a) and arm 3 of `example-strategy`; False-of: B.3) with a separate descriptive entry for real learners; R2 is formal and derived at any depth, with a separate descriptive entry. The depth-$d$ proof landed in `deriv-edge-credence-dynamics` under B.2's "Generalization to depth $d$", which carried the formula tagged Derived with no argument: edge $k$ is attempted iff edges $1, \dots, k-1$ succeed, probability $\prod_{j \lt k}\theta_j$ independent of edge $k$'s outcome under L0, then B.2's step. Drained: `hyp-edge-update-via-gain` (two sentences), `scope-edge-update-causal-validity` (two clauses; see F2), the OUTLINE row. A checker should verify that the depth-$d$ argument's independence claim holds under L0 only (a latent common cause across chain edges would correlate the attempt event with edge $k$'s outcome) and that I did not over-scope the freezing: a node with a *noisy* but informative descendant is neither frozen nor the B.3 case, and the segment's Working Note on partial observability still covers it.

## C4 (check)
- target: segment:der-causal-insufficiency-detection
- at: 4e442b38
- act: rederive
- line: derivation
- criterion: R1: does $\mathcal W_{L0}^\ast$ give the same on-policy distribution as $\mathcal W_{L1}$? R3: does the detection criterion as written follow from $H_0$, and is a nonzero covariance between siblings sharing a modelled ancestor evidence of a latent?
- committed: before
- outcome: narrowed
- recheck: three on-policy events $(0.72, 0.056, 0.224)$ in both worlds; $1 - (1 - 0.72)(1 - 0.2) = 0.776 = P(G)$; naive-L1 $\operatorname{Cov}(Y_{B_1}, Y_{B_2}) = 0.504 - 0.4032 = 0.1008$; $X, Y$ fair independent bits, $Z = X \oplus Y$: all pairwise covariances $0$, $P(X \wedge Y \wedge Z) = 0$ against $1/8$, $P(X \vee Y \vee Z) = 3/4$ against $7/8$

R1 confirmed by computation. R3 confirmed as a body defect: $H_0$ is stated for a tree and the criterion dropped that, so the body's own naive-L1 example fired the test with no latent. Landed: the criterion now requires siblings with disjoint modelled ancestor sets (automatic under L0, where the model is a tree) and names the conditional covariance for pairs sharing a modelled ancestor, with the naive-L1 number as the instance; the record's population, false-of and falsifier say the same and the falsifier names the criterion. Beyond the checker: for two binary siblings zero covariance is independence, so a latent the pairwise test misses biases nothing at that pair; for three or more siblings pairwise independence is not mutual independence, and the XOR construction above, realizable as a four-state latent, is invisible to every pairwise covariance while the three-way AND and OR are both biased. That is now a fourth item under "What Cannot Be Detected" and in R3's False-of, and the Epistemic Status says the mechanism is blind by construction to latents that show only in the joint of three or more siblings. A checker should verify the XOR arithmetic and that nothing in the body still presents the pairwise test as complete for nodes with three or more children.

## C5 (check)
- target: segment:def-strategy-dag
- at: 4e442b38
- act: rederive
- line: derivation
- criterion: F4: is the plan-level residual a signal of insufficiency under on-policy short-circuit execution? R1: does the population carry causal sufficiency? R3: does the title carry the correlation sign? Coverage: are the frequency claims recorded?
- committed: before
- outcome: narrowed
- recheck: $1 - (1 - p_1^c)(1 - p_2^c) = P(A_1 \cup A_2)$ with $p_2^c = P(A_2 \mid \neg A_1)$, so the residual is zero in both worlds; R2's numbers $0.8768$, $0.776$, $0.1008$, $0.25$ against $0.5$ reproduce

R2 confirmed. F4 confirmed: the residual is zero under on-policy short-circuit by the chain rule, so "the signal of insufficiency" was silent where the no-go holds. Landed: the sentence now says the residual is a signal only when the credences were learned from outcomes short-circuit execution did not censor, zero on-policy, $O(\varepsilon)$ and confirmatory under partial exploration. R1's population names causal sufficiency as the hypothesis of the Markov factorization. R3's title and register carry the sign rule in full (positive correlation: AND under, OR over; negative: reversed; reconvergence: positive, node types alone). A new descriptive entry records the two frequency claims ("OR-dominated roots are far more common", "correlated failure is the dominant case") and the conclusion resting on them, Instantiated no, with a census falsifier. Declined: softening the body's "Correlated failure is the dominant case, not the exception" in the Epistemic Status; it is now recorded as descriptive and untested, which is what the record is for. A checker should verify that the new "signal" sentence agrees with `der-causal-insufficiency-detection`'s "Off-policy boundary" paragraph on the $O(\varepsilon)$ scaling and sign.

## C6 (check)
- target: segment:form-objective-functional
- at: 4e442b38
- act: rederive
- line: derivation
- criterion: Is "the agents on which the axioms fail are exactly the agents this interface excludes" true, given that the interface admits any real-valued $V_{O_t}$ and the body's own target-region row? Does the expectation form rest on (A1)–(A3) on trajectories plus (A4)? Is Instantiated "not by this project" the whole truth for a target class that includes humans?
- committed: before
- outcome: narrowed
- recheck: lower contour set of $\mathbb{1}[s_T \in R]$ at a value-$0$ trajectory is $\{s_T \notin R\}$, closed iff $R$ open; upper contour set at value $1$ is $\{s_T \in R\}$, closed iff $R$ closed; so (A3) iff $R$ clopen

All three confirmed. The boundary sentence was false: (A1)–(A3) give a continuous representation, a real-valued one needs only order-separability, and the target-region row is admitted by the interface and excluded by (A3). Landed: the Epistemic Status now states the boundary as order-separability (Debreu 1954), names (A3) as the price of continuity with the second-countable or separable-connected hypothesis stated rather than assumed of the trajectory space, exhibits the target-region row as the admitted-but-discontinuous instance, qualifies (E1) to a trajectory space with a continuum of first-coordinate ties (with the countable-domain remark), and states the expectation form's axioms on lotteries, with the dominance condition for infinite trajectory spaces. The (A4) paragraph says independence fails systematically in human choice under risk (Allais 1953; Kahneman & Tversky 1979, bibliographic records checked by web on 2026-10-30, primaries unread, footnoted as the project's recall convention), so for human members of the target class the ordinal representation is what the evidence supports and the value object's cardinal form is not licensed by (A4). The record is split: a formal entry for the theorems (population: order-separable complete preorders; continuous under (A3); lottery axioms for the expectation form) and a descriptive entry for the target class, whose True-of is approximate GARP consistency of human subjects (Choi, Fisman, Gale & Kariv 2007; the result is from recall, the record checked), whose False-of is (A4) for humans, and whose Instantiated says yes in the economics literature, not by this project. Not changed: the body's "(E1) incommensurable objectives *and* no priority structure" description, which does not describe a lexicographic order (which has a priority) and predates this pass; worth a look by whoever next touches the segment. A checker should verify the clopen argument, the statement of Debreu's order-separability condition, and that the body does not now claim (A4) of the target class anywhere (it claims (A1)–(A2) only).

## C7 (check)
- target: segment:def-agent-spectrum
- at: 4e442b38
- act: read-check
- line: imported
- criterion: Do the body and record state Richens, Abel, Bellot & Everitt's hypotheses as the paper states them? Is "Instantiated: by an external theorem" an instantiation? Is "two independent dimensions" true given the theorem?
- committed: before
- outcome: narrowed
- recheck: arXiv 2506.01622v5, pp. 2–5: Assumption 1 (communicating, stationary, finite cMP, at least two actions); §2.4 ("For simplicity, we assume that the environment is fully observed by the agent, and that the agent follows a deterministic policy"); Definition 5 ($P(\tau \models \psi \mid \pi, s_0) \geq \max_\pi P(\cdot)(1 - \delta)$ for all $\psi \in \Psi_n$); Theorem 1 bound $\sqrt{2P(1-P)/((n-1)(1-\delta))}$ for $n \gt 1$; Theorem 2 (myopic: trivial bounds, tight)

I read those pages of the primary. The checker put full observability in Assumption 1; the paper puts it, with the deterministic policy, in §2.4 prose, and I wrote it that way. Landed: the Discussion paragraph carries the hypotheses, the Theorem 1 bound, Theorem 2's content, and a sentence that the paper's own recovery experiment is on an agent it trained in a random environment satisfying Assumption 1, not an instantiation outside the theory. The summary says "two dimensions" with a clause that they are independent as coordinates, not over competent agents. The record: R1's False-of and Falsifier carry the independence reading and its refutation; the Richens entry is formal with the hypothesis class as population and Instantiated "not applicable; a theorem"; a new descriptive entry carries the body's adoption ("must have learned an implicit world model") for real agents, Instantiated no. A checker should read the same pages and confirm the hypotheses as I quote them; the Theorem 1 bound is copied from p. 4.

## C8 (check)
- target: segment:norm-explicit-strategy-condition
- at: 4e442b38
- act: read-check
- line: derivation
- criterion: Does the body still say loop-based learning does not inherit model bias? Under the stated precondition, what does the falsifier test?
- committed: before
- outcome: narrowed
- recheck: Epistemic Status bullet "Model bias" and the summary's parenthesis; the record's attribution "(Working Notes)" against the audit-gold follow-up item where the correction sat

Both confirmed. Landed: the two body sentences now say loop-based learning carries a different bias (policy selection, partial observability, the model used to read observations), not none; the Epistemic Status says that under the precondition the rule is optimal by definition and what the criterion adds is the ex-ante estimation of the four costs; the record's False-of cites the Epistemic Status, and its falsifier says the Daw comparison tests whether the costs can be estimated well enough to follow the rule, not the norm's content, and adds Daw, Gershman, Seymour, Dayan & Dolan 2011 (the human two-step study; bibliographic record checked by web on 2026-10-30) beside Daw, Niv & Dayan 2005, marked as fitted mainly to rodent data. A checker should confirm the Daw 2011 record (Neuron 69(6):1204–1215) and that no other sentence in the segment contrasts loop learning as unbiased.

## C9 (check)
- target: segment:schema-strategy-persistence
- at: 4e442b38
- act: rederive
- line: derivation
- criterion: R2: is the stationary gain $1 - \lambda$ for every one of "the four verified topologies", including an intermittently observed edge? R1: does the falsifier as stated refute the claim?
- committed: before
- outcome: narrowed
- recheck: $n_{\text{eff}} = 1/(1 - \lambda)$, gain $1/(\lambda n_{\text{eff}} + 1) = 1 - \lambda$ (simulated $0.300$ at $\lambda = 0.7$); an edge observed with probability $0.5$ under per-time-step discounting has mean per-observation gain $0.489$, not $0.3$

R2's gain confirmed for an edge observed every step and refuted as a statement about intermittently observed edges under per-time-step discounting. Landed: R2's population is the single edge observed every step (B.1F), with the intermittent case routed to `deriv-evidence-allocation-ceiling`'s EA.2 and "Discount convention" (per-observation discounting: per-step rate $\pi_i(1 - \lambda)$; per-time-step: no closed form), and the other topologies said to enter only through that scaling; its False-of adds the intermittent per-time-step case; its falsifier names the sentence; the history clause about the earlier $R_\Sigma/2$ ceiling is gone from the record. R1 is now formal (a theorem about undiscounted Beta-Bernoulli) with a falsifier that requires worst-case drift and $R_\Sigma$ below the range of $\theta$, saying why benign drift is not one; a new descriptive entry carries the adoption for real gain-decaying systems, with Behrens et al. 2007 as the neighbour outside the population. A checker should re-run the two gain simulations and confirm the EA "Discount convention" paragraph says what my record attributes to it.

## C10 (check)
- target: segment:form-complete-agent-state
- at: 4e442b38
- act: read-check
- line: derivation
- criterion: Anything the checker's confirmed verdict missed?
- committed: before
- outcome: confirmed
- recheck: the record's four fields against the Epistemic Status

Nothing to add; not edited.

## C11 (check)
- target: segment:def-strategy-dimension
- at: 4e442b38
- act: read-check
- line: derivation
- criterion: Anything the checker's confirmed verdict missed?
- committed: before
- outcome: confirmed
- recheck: Discussion, "different update dynamics"

Nothing to add; not edited. The checker's coverage note (the five-level ordering in `der-orient-cascade` has no record) is in the integrator's file.

## C12 (check)
- target: segment:def-control-regret
- at: 4e442b38
- act: read-check
- line: derivation
- criterion: Does the "Convention hierarchy" paragraph carry the right rung as unconditional?
- committed: before
- outcome: narrowed
- recheck: the paragraph beginning "**Convention hierarchy.**"

It did; it now carries the (PC)/(SO) hypothesis with the pointer. The record was confirmed by the checker and is unchanged.

## F1 (finding)
- target: segment:def-value-object
- at: 4e442b38

The right rung is false without (PC) or (SO); the construction is in C1 above and in `deriv-convention-monotonicity`. The sentences carrying "unconditional" in this segment and the record's "impossible by definition" were the integrator's to change; I sent the construction and the hypothesis wording, and the integrator has since drained them (summary, Monotonicity block, derivation paragraph, corollary, Epistemic Status layer 3, both records) with wording that agrees with `deriv-convention-monotonicity`: same two hypotheses, the same instance (called the three-state two-policy instance there, the right-rung counterexample here). One residual at the time of my read: the struck-through Working Note that resolved the 2026-05-30 left-rung item still ends "the right rung is exact unconditionally"; it is history text, but a reader skimming Working Notes will meet it.

## F2 (finding)
- target: segment:scope-edge-update-causal-validity
- at: 4e442b38

Two clauses in this file scope "the edge is frozen at its prior" to nodes no observed variable depends on. The file also carries the integrator's in-flight C→E relettering, so I did not run `vsect revise` on it; whoever commits it should take both in together.

## F3 (finding)
- target: segment:der-orient-cascade
- at: 4e442b38

The aspiration hypothesis now has a record in `def-satisfaction-gap`; this segment's R2 False-of can point at it. Not edited here.

## F4 (finding)
- target: segment:deriv-self-actuation-grounding
- at: 4e442b38

Lemma 1 cited the full $\delta_{\text{sat}}$ chain as `status: exact` with no hypothesis and drew the superset direction from it (the C1 verdict holds on a strict superset of the genuinely-infeasible set). The left rung had been conditional on RH-1/2/3 since 2026-05-30 and the lemma had not been drained then; the right rung is now conditional too. Edited: the citation names each rung's hypothesis, the superset sentence is scoped to them, and a sentence says that without them the two verdicts can disagree in either direction, which removes the superset direction and leaves what the lemma uses, that the C1 and C3 verdicts are not the same predicate. The no-go's assembly (Lemmas 1 and 2 together) uses only that, so I read it as intact; `disc-value-functional-grounding-floor` describes the engine in the same terms and I did not edit it. A checker should read the assembly paragraph against the scoped lemma and say whether the superset direction is used anywhere downstream; `vsect revise` was run on the segment.
