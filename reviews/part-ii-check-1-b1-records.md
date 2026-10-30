---
kind: review
author:
  name: Claude Opus 5.5 (independent checker of 8f7dd870, Part II B.1 record corrections)
  role: independent checker
sources:
  - reviews/b1-part-ii-integration-1.md
  - reviews/b1-part-ii-check-1.md
written: 2026-10-30
---

# Independent check of 8f7dd870: Part II claim-record corrections outside the C2/C3 cluster

KR **B.1** (`msc/inside-out-2026-10/INTENT.md`; top intent B: every load-bearing claim says what kind of claim it is, about which agents, and what would refute it; "someone other than the author checks each record"), touching **C.1** (every verified defect replaced, then independently verified). Text read at HEAD `242ebc33`; no commit after `8f7dd870` touches any of the fifteen segments it changed, so what is read here is what landed. The second mind's account (`reviews/b1-part-ii-integration-1.md`) was read whole. The checker's review it worked from (`reviews/b1-part-ii-check-1.md`) was not read, so this check rests on the bodies, not on either earlier check. The numeric items (C1, C2, C3, C12) were run in throwaway `python3 -I` scripts. The rest are hand derivations or reads, and each item's `act` and text say which. Every `recheck` field restates its instance in full, so the field alone is enough to redo it. This record's content is its findings list, not its silences: what I did not check is listed at the end.

The headline: the right-rung strengthening in `#deriv-convention-monotonicity` is the right move, and its counterexample is correct. But the (SO) branch has a false step, and both branches rest on an unstated premise. (SO) does not make the two readings of $A_O^{\text{B}}$ coincide (C1 below). Both (PC) and (SO) silently use $\pi_{\text{RH}} \in \Pi$, which canon's C2 construction does not deliver (C2 below: a four-policy class has (PC) and (SO) both holding and the rung failing, $51$ against $10$). The integrator's own account asked a checker to verify exactly the (SO) step. The repairs are local and leave a true statement with all its hypotheses named. One of them, the first-action reading, also makes C3's infeasibility verdict sound for every policy class. They are written out under each item. Outside the convention-monotonicity cluster, two more records are broken as written: the aspiration hypothesis's population lies inside its own False-of (C5), and `#form-objective-functional`'s rewritten exclusion sentence equates two different boundaries (C10). Everything else checked was confirmed or narrowed.

## C1 (check)
- target: segment:deriv-convention-monotonicity
- at: 242ebc33
- act: rederive
- line: derivation
- criterion: Under (SO) alone, is $\sup_a Q_O(M_t, a; \pi^\ast, N_h) = V_O(M_t, \pi^\ast; N_h)$, as the (SO) paragraph's last step and the sentence "Under either hypothesis the two readings of $A_O^{\text{B}}$ in use … coincide" say? Does the right rung hold under (SO) on each reading?
- committed: after
- outcome: broken
- recheck: deterministic, decision point $x$, one continuation step. At $x$: $p$ pays $+2$ to $H$, $g$ pays $+1$ to $D$. At $H$: only $u$, $+10$. At $D$: $d_1$ pays $0$, $d_2$ pays $+50$. $\Pi = \{\pi_A = (x \mapsto p, H \mapsto u, D \mapsto d_2),\ \pi_B = (x \mapsto g, H \mapsto u, D \mapsto d_1)\}$. $V_O(\pi_A) = 12$, $V_O(\pi_B) = 1$, so $\pi^\ast = \pi_A$. (SO) holds: at $H$ the class supremum $10$ and at $D$ the class supremum $50$ are both attained by $\pi_A$. (PC) fails: $g \oplus \pi_A \notin \Pi$. The $N_r = 1$ replanner takes $p$ at $x$ ($2 \gt 1$), $u$ at $H$, $d_2$ at $D$, so $\pi_{\text{RH}} = \pi_A \in \Pi$. $\sup_a Q_O(a; \pi^\ast) = \max(2 + 10,\ 1 + 50) = 51$ against $V_O(\pi^\ast) = 12$; $A_O^{\text{RH}} = 51$. Ran: rung holds on the $Q$-reading ($51 \leq 51$), fails on the $V$-reading ($51 \gt 12$), readings differ.

The first half of the (SO) argument is sound: with $\pi_{\text{RH}} \in \Pi$, $Q_O(a; \pi_{\text{RH}}) \leq Q_O(a; \pi^\ast)$ for every first action, so $A_O^{\text{RH}} \leq \sup_a Q_O(a; \pi^\ast)$. The last step is not. (SO) constrains $\pi^\ast$ at the successor states only and says nothing about whether $\pi^\ast$'s own first action is the best first action *given $\pi^\ast$ as continuation*. $\sup_a Q_O(a; \pi^\ast)$ is the one-step backup of the class-optimal value at $x$, and it can strictly exceed $V_O(\pi^\ast) = \sup_{\pi \in \Pi} V_O(\pi)$ whenever the better composite $a \oplus \pi^\ast$ lies outside $\Pi$. That is the very situation (PC) excludes and (SO) does not.

Why it matters: canon now holds two definitions of $A_O^{\text{B}}$, bridged only by this step. `#def-satisfaction-gap` (changed in this commit) defines every attainability as a first-action supremum, $A_O^{\text{B}} = \sup_a Q_O(a; \pi^\ast)$, and asserts $= \sup_{\pi \in \Pi} V_O$ "provided … closed under prefixing … or $\pi^\ast$ is optimal over $\Pi$ from every state a first action can reach". `#def-value-object` :81 says $A_O^{\text{B}} = V_O(M_t, \pi^\ast; N_h)$ with no qualifier. `#deriv-convention-monotonicity` opens its proof with "Write $A_O^{\text{B}} = \sup_{\pi \in \Pi} V_O = V_O(\pi^\ast)$ ( #def-value-object)". On that $V$-reading the (SO) branch of the right rung is false (instance above).

Repair I would make, two options; I would take (a).

(a) Make the $Q$-reading canonical everywhere, since it is the one the attainability definition uses and the one the (SO) argument proves. In `#def-value-object` :81, write $A_O^{\text{B}} = \sup_a Q_O(M_t, a; \pi^\ast; N_h)$, which is at least $V_O(M_t, \pi^\ast; N_h) = \sup_{\pi \in \Pi} V_O$ for every $\Pi$ (take $a = \pi^\ast$'s own first action), with equality under (PC) or under (G) below. In `#deriv-convention-monotonicity`, replace "Under either hypothesis the two readings … coincide" with: "Under (PC) the two readings coincide; under (SO) the rung holds on the first-action reading, and the readings coincide when also (G)." In `#def-satisfaction-gap`'s proviso on the display $A_O^{\text{B}} = \sup_{\pi \in \Pi} V_O$, replace "or $\pi^\ast$ is optimal over $\Pi$ from every state a first action can reach" with "or $\pi^\ast$'s own first action is a best first action under $\pi^\ast$ as continuation (G)".

(b) Strengthen (SO) to (SO)+(G), with (G) defined as: $\pi^\ast(x) \in \arg\sup_a Q_O(M_t, a; \pi^\ast, N_h)$, meaning no first-action deviation followed by $\pi^\ast$ beats $\pi^\ast$. Ran: (G) fails on the instance above, where $g$ then $\pi^\ast$ is worth $51$ against $12$. Then $A_O^{\text{RH}} \leq \sup_a Q_O(a; \pi^\ast) = Q_O(\pi^\ast(x); \pi^\ast) = V_O(\pi^\ast)$ on both readings.

A strengthening falls out of (a) and is worth landing with it. On the $Q$-reading, $A_O^{\text{B}} \geq \sup_{\pi \in \Pi} V_O$ for every $\Pi$. So $\delta_{\text{sat}}^{\text{B}} \gt 0$ implies that no member of $\Pi$ reaches the threshold, for every policy class, with no closure hypothesis. "C3 gives no false 'unattainable' diagnoses" (`#def-satisfaction-gap` Epistemic Status, `#impl-strategy-structure`) is therefore unconditional in $\Pi$. The hypothesis-bearing direction is the converse: $\delta_{\text{sat}}^{\text{B}} \leq 0$ certifies a member of $\Pi$ only under (PC) or (G). Under (SO) alone it certifies only "some first action then $\pi^\ast$", which the agent can execute but which $\Pi$ may not contain. Whether that counts as "attainable" is a modelling choice the segment should name.

## C2 (check)
- target: segment:deriv-convention-monotonicity
- at: 242ebc33
- act: rederive
- line: derivation
- criterion: Both branches use $\pi_{\text{RH}} \in \Pi$ ("That $\pi_{\text{RH}}$ is drawn from $\Pi$ …"; "since $\pi_{\text{RH}} \in \Pi$"; the counterexample's "a member of $\Pi$ as the derivation requires"). Is that membership a consequence of C2's definition, or an unstated third hypothesis the rung fails without?
- committed: after
- outcome: broken
- recheck: deterministic, $N_h = 3$, $N_r = 1$. $x$ has the single action $a$ (pays $0$, to $s$). At $s$: $\alpha$ pays $+1$ to $t_1$, $\beta$ pays $0$ to $t_2$. At $t_1$: $c_1$ pays $0$, $c_2$ pays $+50$. At $t_2$: $d$ pays $+10$. $\Pi = \{m_1 = (s \mapsto \alpha, t_1 \mapsto c_1, t_2 \mapsto d),\ m_2 = (s \mapsto \beta, t_1 \mapsto c_2, t_2 \mapsto d)\}$, both $x \mapsto a$. $V_O(m_1) = 1$, $V_O(m_2) = 10$, $\pi^\ast = m_2$. (PC) holds: the only first action is $a$ and $a \oplus m_i = m_i$. (SO) holds: at $s$ the class supremum $10$ is attained by $m_2$. The replanner, with each one-step window's argmax taken over $\Pi$ (equivalently over all actions, since the members cover every action), takes $\alpha$ at $s$ ($1 \gt 0$) and $c_2$ at $t_1$ ($50 \gt 0$). Stitched $\pi_{\text{RH}} = (s \mapsto \alpha, t_1 \mapsto c_2) \notin \Pi$. Ran: $A_O^{\text{RH}} = 0 + 1 + 50 = 51 \gt 10 = A_O^{\text{B}}$ on both readings. Non-vacuous variant, also run: add a second first action $b$ at $x$ (pays $0$, to $s$) and take $\Pi$ to be the four policies $\{a, b\} \times \{m_1\text{'s tail}, m_2\text{'s tail}\}$. (PC) then holds non-trivially, (SO) holds, the stitched replanner is still outside $\Pi$, and the result is the same: $51$ against $10$ on both readings.

The rung fails with (PC) and (SO) both true. This fires the falsifier `#def-value-object`'s record states for the right rung: "a policy class satisfying the closure hypothesis in which $\sup_a Q_O(a; \pi_{\text{RH}}) \gt \sup_a Q_O(a; \pi^\ast)$". The cause is that receding-horizon replanning stitches together, state by state, the first actions of different window-optimal members. For a restricted class the stitched policy need not be a member, even when every window's argmax is taken over $\Pi$. `#def-value-object` :77 defines $\pi_{\text{RH}}(M_\tau) = \arg\max_\pi V_O(M_\tau, \pi; N_r)$ "applied at each $\tau$", with no $\Pi$ and no statement about the stitched policy. `#def-satisfaction-gap` asserts the continuation is "drawn from the available policy class $\Pi$" under every convention, which is a stipulation C2's construction does not honour. The landed segment says (correctly) that restricted, DAG-representable $\Pi$ is the AAT case. That is also exactly the case where membership fails.

Repair I would make: name the third hypothesis and state the rung as $(M) \wedge ((PC) \vee (SO))$ on the $Q$-reading (with C1's (G) or (PC) for the $V$-reading). (M) reads: the receding-horizon policy, stitched from the window optima, is a member of $\Pi$. A cleaner single hypothesis covers all of (M), (PC), (SO) and (G) at once, and I would offer it as the headline sufficient condition. Call it **rectangularity**: $\Pi$ is the set of all (history-dependent, or time-indexed Markov) policies with $\pi(s) \in A_\Pi(s)$ for given state-wise admissible sets, and the first-action supremum ranges over $A_\Pi(x)$. Then the window argmax picks from $A_\Pi(s)$, so the stitched policy is a member (M); $a \oplus \pi$ is a member for $a \in A_\Pi(x)$ (PC); and Bellman's equation on the restricted decision process makes $\pi^\ast$ optimal from every state (SO) and greedy at $x$ (G). That argument is my own and was not run beyond the two instances above, which are both non-rectangular. The full policy class is the rectangular case with $A_\Pi(s)$ the whole action set. A DAG-representable class is generally not rectangular, so for the AAT case the rung stays a hypothesis-bearing statement, and the segment's sentence saying so remains true.

The counterexample in the body (C3 below) is unaffected: there $\pi_{\text{RH}} = \pi_1 \in \Pi$, both (PC) and (SO) fail, and the rung fails.

## C3 (check)
- target: segment:deriv-convention-monotonicity
- at: 242ebc33
- act: rederive
- line: derivation
- criterion: Is the landed right-rung counterexample correct as stated, including its claims that (PC) and (SO) each fail there and that restoring the full class restores the rung? Is the (PC) branch's proof correct?
- committed: after
- outcome: confirmed
- recheck: $x$: $g$ pays $+1$ to $D$, $p$ pays $0$ to $H$; $H$: $u$ $+10$, $w$ $+100$; $D$: $0$. $\Pi = \{\pi_1 = (x \mapsto g, H \mapsto w), \pi_2 = (x \mapsto p, H \mapsto u)\}$. Ran: $V_O(\pi_1) = 1$, $V_O(\pi_2) = 10$, $\pi^\ast = \pi_2$, $\pi_{\text{RH}} = \pi_1$, $A_O^{\text{RH}} = \max(1, 100) = 100$, $A_O^{\text{B}} = 10$ on both readings; over all policies $\pi^\ast$ takes $w$ at $H$ and $A_O^{\text{B}} = 100$.

Confirmed by hand and by script. The (PC) branch is correct as a derivation once $\pi_{\text{RH}} \in \Pi$ is granted (C2), and it gives both readings. The frame sentence (decision point $x$, one continuation step, not the left-rung frame) is accurate and needed. Two small consistency points. (i) The summary paragraph calls this "the same two-state instance", while `#def-value-object` calls it "the three-state two-policy instance". Both count $x, H, D$ differently, and a reader comparing the segments will stumble; "the same instance ($x$, $H$, $D$)" in both would do. (ii) The closing line, "with $\pi_{\text{current}} = \pi_1$ … $A_O^{(1)} = 100 \gt A_O^{\text{B}}$", is true and useful, and it is the observation that leads to F2 below.

## C4 (check)
- target: segment:deriv-self-actuation-grounding
- at: 242ebc33
- act: rederive
- line: derivation
- criterion: Is Lemma 1 as now scoped true, does the no-go's assembly use only "the C1 and C3 verdicts are not the same predicate", and does anything downstream use the superset direction?
- committed: after
- outcome: narrowed
- recheck: C1 versus C3 directly, $Q$-reading. If $\pi_{\text{current}} \in \Pi$ and (PC), then $\sup_a Q_O(a; \pi_{\text{current}}) = \sup_a V_O(a \oplus \pi_{\text{current}}) \leq \sup_\Pi V_O \leq A_O^{\text{B}}$. If $\pi_{\text{current}} \in \Pi$ and (SO), then $Q_O(a; \pi_{\text{current}}) = r(a) + V_O(s', \pi_{\text{current}}) \leq r(a) + V_O(s', \pi^\ast) = Q_O(a; \pi^\ast)$ for each $a$. Read: Lemma 1, the Assembly paragraph (:55), the table row :80 and "Class robustness" (:98) of `#deriv-self-actuation-grounding`. Grep for "superset" across `0*-*/src/*.md` finds only Lemma 1 itself. Grep of `#disc-value-functional-grounding-floor` for "convention-invariant" (lines 24, 40, 74).

Lemma 1's use survives. The Assembly uses it as "the only convention-invariant infeasibility verdict is the C3 reading", not the superset direction. On the first-action reading (C1 above), $\delta_{\text{sat}}^{\text{B}} \gt 0$ certifies that no member of $\Pi$ reaches the threshold for every $\Pi$, so that use holds without any closure hypothesis. The grounding-floor segment describes the engine as "not convention-invariant", which is the same thing. No other segment in the four components uses the superset direction. Residual carrier: the table row :80 still cites "#def-value-object Corollary (static-evaluation form, exact)" with no hypothesis (in F1's drain).

The scoping is more restrictive than it needs to be, so this is a strengthening rather than a correction. Lemma 1 now conditions the superset on *both* rungs' hypotheses, including order-consistency (RH-1/2/3) for the left rung. But the C1-versus-C3 comparison does not pass through C2. As the recheck shows, $A_O^{(1)} \leq A_O^{\text{B}}$ holds directly under $\pi_{\text{current}} \in \Pi$ and either (PC) (both readings) or (SO) (first-action reading only, per C1; on the C1 instance with $\pi_{\text{current}} = \pi_A$, $A_O^{(1)} = 51 \gt 12 = V_O(\pi^\ast)$), with no order-consistency at all. So the superset direction needs only the right-rung kind of hypothesis plus membership of the current policy. The sentence "Without them the two verdicts can disagree in either direction" is true (the body counterexample with $\pi_{\text{current}} = \pi_1$ gives $A_O^{(1)} = 100 \gt 10$). Repair I would make: in Lemma 1, cite "$A_O^{(1)} \leq A_O^{\text{B}}$ directly, under $\pi_{\text{current}} \in \Pi$ and (PC) or (SO) ( #deriv-convention-monotonicity)" in place of the two-rung chain. The same direct comparison could be one line in `#deriv-convention-monotonicity`'s corollary section, since `#def-value-object`'s diagnostic reading ("rests on the C1/C3 endpoints and the right rung", Discussion of `#deriv-convention-monotonicity`) is a C1-versus-C3 statement.

## F1 (finding)
- target: segment:deriv-convention-monotonicity

Drain for C1 and C2. Every carrier that now says "(PC) or (SO)" or "closed under prefixing … or $\pi^\ast$ optimal from every state reachable in one step" inherits both defects. From reading the files at HEAD, they are: `#deriv-convention-monotonicity` (summary, the tag, the (SO) paragraph's last step, the "two readings coincide" paragraph, corollary orderings, Epistemic Status, Discussion, Findings Claim and Brief, the dead-end Working Note); `#def-value-object` (summary :21, the Monotonicity block :91 and :101, C3 paragraph :81, Epistemic Status :137, the record at :171–179, whose falsifier the C2 instance fires, and the corollary paragraph); `#def-satisfaction-gap` (the proviso under the $A_O^{\text{B}}$ display, and the Epistemic Status sentence on the B $\leq$ RH half); `#def-control-regret` ("Convention hierarchy"); `#impl-strategy-structure` (body and regression guard (1)); `#deriv-self-actuation-grounding` Lemma 1 and its status-table row :80 (C4); and the `01-aat-core/OUTLINE.md` row :340. FINDINGS.md regenerates from the segment. Suggested replacement phrase for the short carriers: "holds when the replanner's policy lies in $\Pi$ and $\Pi$ is closed under prefixing a first action, or its optimum is optimal from every successor state (the latter on the first-action reading of $A_O^{\text{B}}$); automatic for the class of all policies".

## F2 (finding)
- target: segment:def-value-object

The same mechanism reaches C1 against C3, and the diagnostic reading rests on that comparison ("locally stuck under C1, infeasible under C3"). `#deriv-convention-monotonicity` says so in one sentence at the end of the right-rung counterexample. `#def-value-object`'s record ("The three continuation conventions order attainability, and the convention fixes what a diagnosis means") states only the two rungs. With C4's direct comparison available, the record's True-of could carry "$A_O^{(1)} \leq A_O^{\text{B}}$ under $\pi_{\text{current}} \in \Pi$ and (PC) or (SO)" as the statement the diagnostic actually uses, and its False-of could carry the body instance with $\pi_{\text{current}} = \pi_1$.

## F3 (finding)
- target: segment:deriv-convention-monotonicity

Catalog. The segment's `## Findings` entry uses `**Claim.**` / `**Brief.**` / `**Impact.**` / `**Related work.**`, with a period and in sentence case. It is the only Part I or II segment that does (41 segments use `**Brief:**`), and FINDINGS.md therefore shows only the `**Search Log:**` this commit added, under "Missing field" warnings. The form predates the commit; the commit's Search Log is the one field that reaches the catalog. Converting the four fields to the `format.sop.md` names (Brief / Impact / Novelty Claim / Related Work / Search Log) would put the strengthened claim in the catalog. "Antecedents" has no schema slot and could fold into Related Work.

## C5 (check)
- target: segment:def-satisfaction-gap
- at: 242ebc33
- act: read-check
- line: derivation
- criterion: Does the new record for the aspiration hypothesis (`aspiration-dominance`) bound a population on which the hypothesis can be true?
- committed: after
- outcome: broken
- recheck: the record's Population ("whose policy under each is the optimum for that objective in $\Pi$") against its False-of ("an agent whose policy class contains the $O_f$-optimum and whose planner finds it … false by definition of $\pi_f$"); the body's Discussion defines $\pi_a$, $\pi_f$ as "the optimal policies under aspirational $O_a$ … and feasible $O_f$".

The population as written lies inside the False-of. If $\pi_f$ is the $V_{O_f}$-optimum over $\Pi$ and $\pi_a \in \Pi$, then $V_{O_f}(M_t, \pi_a) \leq V_{O_f}(M_t, \pi_f)$ by definition. So the hypothesis is false on every agent the record says it is about. The record's own last sentence ("has content only where the planner's reach is limited") names the fix but does not apply it. The defect starts in the body: the Discussion's statement of the hypothesis uses $\Pi$-optimal policies, which makes the displayed inequality impossible. The three mechanisms it lists (escaping local optima, implicit regularization, conditioning) are all statements about a bounded optimizer.

Repair I would make (strengthen, not soften): restate the hypothesis with the policies a given bounded planner $\mathcal P$ *reaches*, $\pi_a = \mathcal P(O_a)$ and $\pi_f = \mathcal P(O_f)$ from the same initialization and budget, so the inequality reads $V_{O_f}(M_t, \mathcal P(O_a)) \gt V_{O_f}(M_t, \mathcal P(O_f))$. Then set the record's Population to agents whose planner does not attain the $\Pi$-optimum of $O_f$ (local search, gradient methods, bounded deliberation). The False-of becomes the exact-optimizer case, the boundary the record already names. The falsifier stays as written.

## C6 (check)
- target: segment:der-observability-dominance
- at: 242ebc33
- act: rederive
- line: derivation
- criterion: Is the scoped freezing claim true, does the B.3 case now read as non-identification throughout, and do the four records do the job (register, population, true/false instances, falsifier naming its clause)?
- committed: after
- outcome: confirmed
- recheck: $A \to B \to G$, $B$ unobserved, $\mathbb E[y_G] = \theta_1\theta_2$, so with $\theta_2$ known $\bar y_G / \theta_2 \to \theta_1$; an edge into a node with no observed descendant has no likelihood term, so under independent edge priors its posterior is its prior.

The scoping is right and consistent across summary, Formal Expression, Epistemic Status, records, `#hyp-edge-update-via-gain` (two places) and the OUTLINE row :174. Read only: `#scope-edge-update-causal-validity` :81 carries the same scoping (that file landed in `af518dd5`, not this commit). Three residues, each small:

(i) The freezing argument also needs the edge's prior to be independent of the parameters of edges that *are* observed. Under L0 that holds. Under a hierarchical or correlated prior, an unobserved edge moves through its coupling. The formal record's Population could add "with edge priors independent across edges", which is a one-clause narrowing of the population, not of the claim.

(ii) The first Working Note still says departments with poor measurement hold untested beliefs that are "structural (frozen $\eta_{\text{edge}}$)". The new descriptive record puts any department whose steps feed a monitored terminal in the B.3 regime, which is non-identification, not freezing. The note should say which regime it means, or be scoped to steps no recorded outcome bears on.

(iii) The descriptive record's falsifier has two disjuncts. The first ("step-level beliefs about unmonitored steps track measured outcomes once measurement is introduced no better than chance would predict against the frozen prior") reads as a *confirmation* of the claim, since untested beliefs tracking the truth no better than the prior is what the claim predicts. The second disjunct (beliefs no record bears on that nonetheless track the truth) is the real falsifier. Repair: drop the first disjunct, or invert it to "track measured outcomes better than the frozen prior would".

## C7 (check)
- target: segment:deriv-edge-credence-dynamics
- at: 242ebc33
- act: rederive
- line: derivation
- criterion: Is the depth-$d$ argument added to Prop B.2 correct, and is its independence step L0-only?
- committed: after
- outcome: confirmed
- recheck: one trial of a depth-$d$ chain with independent Bernoulli($\theta_j$) edges, short-circuit execution, all intermediates observed. Edge $k$ is observed iff $y_1 = \dots = y_{k-1} = 1$, with probability $\pi_k = \prod_{j \lt k}\theta_j$, independent of $y_k$. Conditional update $(y_k - \hat p_k)/(n_k+1)$, so $\mathbb E[\Delta \hat p_k] = \pi_k(\theta_k - \hat p_k)/(n_k+1)$.

Re-derived by hand; not simulated, since it is a one-line expectation. Independence of the attempt event from edge $k$'s outcome is exactly L0. Under a latent common cause on the chain the attempt event and $y_k$ are correlated, and the per-trial expectation picks up the covariance, so the "Generalization" paragraph's "Under L0" is the right and needed qualifier. The table row :658 ("Iteration of B.2 pattern … Derived") now has the argument behind it.

## C8 (check)
- target: segment:der-causal-insufficiency-detection
- at: 242ebc33
- act: rederive
- line: derivation
- criterion: Is the disjoint-modelled-ancestor condition correct and needed? Is the XOR construction right, realizable by one latent, and invisible to every pairwise covariance while AND and OR are biased? Does the criterion's new conclusion say what the test shows?
- committed: after
- outcome: confirmed
- recheck: `#example-L1` numbers $\theta_C = 0.8$, $\theta_{1\mid C} = 0.9$, $\theta_{2\mid C} = 0.7$: $P(B_1 \wedge B_2) = 0.504$, $0.72 \cdot 0.56 = 0.4032$, covariance $0.1008$. XOR: $X, Y$ fair independent, $Z = X \oplus Y$; each pair has $P(\cdot = 1, \cdot = 1) = 1/4$; $P(X \wedge Y \wedge Z) = 0$ against $1/8$; $P(X \vee Y \vee Z) = 1 - P(X = Y = 0) = 3/4$ against $7/8$. Latent $C = (X, Y)$, four states, with each sibling a deterministic function of $C$.

All confirmed by hand. The disjointness condition is needed: the body's own naive-L1 graph fires the unconditional test with no latent. The two-sibling remark (zero covariance is independence for binary variables) is right and is what makes the triple case the first blind spot. One wording point: the conclusion changed from "DAG is causally insufficient between siblings $i, j$" to "a cause outside the graph acts on siblings $i, j$". A significant covariance between siblings with disjoint modelled ancestors can also come from a missing direct edge between the siblings (one action's success changing the other's odds), or from selection by the joint-observability route itself, if that route is conditioned on outcomes. "Dependence the graph does not model (a latent common cause, or a missing edge between the siblings)" would be exact. The falsifier ("with no cause outside the graph") should match.

Adjacent, not from this commit: the "Off-policy boundary" display writes $\operatorname{sign}(R) = \operatorname{sign}(\rho)$ unconditionally, while the sentence above it gives "$+$ for OR-heavy, $-$ for AND-heavy, when $\rho \gt 0$". The display should carry the node-type factor.

## C9 (check)
- target: segment:def-strategy-dag
- at: 242ebc33
- act: rederive
- line: derivation
- criterion: Is the plan-level residual zero on-policy, and does the new "signal" sentence agree with `#der-causal-insufficiency-detection` on scaling and sign? Is the R3 sign rule right?
- committed: after
- outcome: confirmed
- recheck: short-circuit OR: $p_1 \to P(A_1)$, $p_2 \to P(A_2 \mid \neg A_1)$; $1 - (1 - p_1)(1 - p_2) = P(A_1) + P(\neg A_1)P(A_2 \mid \neg A_1) = P(A_1 \cup A_2)$ for any joint law. AND: $P(A \wedge B) = p_A p_B + \operatorname{Cov}$; OR: $P(A \vee B) = p_A + p_B - P(A \wedge B)$.

Confirmed. The new sentence's $O(\varepsilon)$ scaling and sign (overestimation at OR roots for a shared enabling cause, underestimation for exclusive alternatives) agree with the Off-policy boundary paragraph's prose. R1's population now carrying causal sufficiency is right, and so is the parenthesis saying the violation bounds which plans are in the population, not the representation. The new descriptive entry for the frequency claims is the right shape. Its falsifier (a census) names what would remove the ground for "net overestimation", which is what B.1 asks. "$O(\varepsilon)$ and confirmatory" leaves "confirmatory" undefined. I read it as "useful to confirm a covariance-test detection, not to make one", and the sentence could say that.

## C10 (check)
- target: segment:form-objective-functional
- at: 242ebc33
- act: rederive
- line: derivation
- criterion: Clopen argument; statement of the order-separability and continuity conditions; the sentence "The framework's own stated exclusion — incommensurable objectives *and* no priority structure — is the (E1) order-separability boundary"; consistency with the body's list of admissible scalarizations.
- committed: after
- outcome: broken
- recheck: lower contour set of $\mathbb 1[s_T \in R]$ at a value-$0$ trajectory is $\{s_T \notin R\}$ (closed iff the preimage of $R$ is open, so iff $R$ is open, the projection being open and continuous); upper contour set at value $1$ is $\{s_T \in R\}$ (closed iff $R$ closed). The body's summary paragraph and Epistemic Status item 2 ("Approximation"): "scalarization (weighted sum, lexicographic ordering, constraint-satisfaction with scalar residual) that preserves the diagnostic structure; the restriction excludes only agents with genuinely incommensurable objectives *and* no priority structure".

The clopen argument is correct. The order-separability characterization and the continuity hypothesis on the space (second-countable, or separable and connected) are stated as I know Debreu's results. I did not open Debreu (1954). The split of the record into a formal entry and a descriptive one is good. The lottery-axiom paragraph is correct, and so is the remark that (A1)–(A2) on trajectories are the degenerate-lottery restriction.

The identity sentence is false, and the commit rewrote it. (E1) as the segment defines it is lexicographic preference, "with a strict priority but no tradeoff rate". That *is* a priority structure. "Incommensurable objectives *and* no priority structure" describes something else: objectives the agent can neither trade off nor rank, which is an *incomplete* preorder, a failure of (A1). The segment treats that case separately, as the Pareto / vector-valued extension. So the body's stated exclusion and (E1) are different boundaries. The interface excludes three things: incompleteness (Pareto), (E1) lexicographic priority on a continuum domain, and (E2) cycles. The second contradiction is pre-existing, but this commit's sentence sits directly on it. The summary and the "Approximation" item still offer "lexicographic ordering" as a scalarization that "preserves the diagnostic structure", while (E1) says a lexicographic preference on a continuum trajectory space has no real-valued representation at all. Then $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$, both scalar differences, are undefined.

Repair I would make: (i) replace the identity sentence with "The interface excludes incompleteness (incommensurable objectives with no priority, the Pareto case below), (E1) and (E2); (A3) sits strictly inside the representable region as the price of continuity." (ii) Delete "lexicographic ordering" from the two scalarization lists, or qualify it as "on a countable trajectory space, or as the limit of weighted sums the agent actually uses". (iii) Change "excludes only agents with genuinely incommensurable objectives *and* no priority structure" in both places to name the three exclusions. The integrator's account flagged the "*and* no priority structure" wording as predating the pass and worth a look; this is that look.

## C11 (check)
- target: segment:def-agent-spectrum
- at: 242ebc33
- act: read-check
- line: imported
- criterion: Are Richens, Abel, Bellot & Everitt's hypotheses, bound and Theorem 2 quoted as the paper states them? Is the new independence clause true?
- committed: after
- outcome: narrowed
- recheck: local copy `ref/richens-2025-general-agents-world-models.pdf`, pp. 2–6 by `pdftotext`. Assumption 1 ("communicating, stationary, finite, controlled Markov process … with at least two actions"); §2.4 prose ("we assume that the environment is fully observed by the agent, and that the agent follows a deterministic policy"); Definition 5, inequality (2); Theorem 1 with $n \gt 1$ and $\lvert \hat P_{ss'}(a) - P_{ss'}(a) \rvert \leq \sqrt{2P_{ss'}(a)(1 - P_{ss'}(a))/((n-1)(1-\delta))}$; Theorem 2 ("trivial ($\epsilon = 1$) and tight"); Discussion ("In the proof (Section A.6) the agent is required to generalize only to a small subset of $\Psi_n$, comprising $O(n\lvert A\rvert\lvert S\rvert^2)$ simple composite goals"); Limitations ("proves the existence of a world model encoded in the agent's policy, not its specific use").

Hypotheses, bound and Theorem 2 are quoted correctly, and the placement (Assumption 1 versus §2.4 prose) is as the account says. The experiment sentence is accurate in substance. The paper says worst-case regret $\delta = 1$ on some goals with low *average* regret; "meets it on average" slightly overstates, and "has low average regret" is the paper's phrase. Two narrowings:

(i) The theorem's population is wider than the record says. The paper states Theorem 1 for regret bounds on all of $\Psi_n$ but says the proof needs only an $O(n\lvert A\rvert\lvert S\rvert^2)$ subset. The formal record's Population ("on every composite goal of depth up to $n$") is the paper's stated form, which is fine. But the descriptive entry's "with competence on fewer goals than all of $\Psi_n$" puts in the conjecture region agents the proof covers. Better: "on fewer goals than a sufficient subset (the paper's Algorithm 1 set)". The Discussion's "meet regret bounds on few goals" has the same issue. This is a deflation, not an overclaim.

(ii) The new independence clause depends on how the model axis is read. "The objective-rich, model-poor region holds no agent competent at depth beyond one" follows from Richens only if "model richness" means *a predictive model is determined by the policy*. The paper's Limitations say Theorem 1 shows the model is encoded in the policy, "not its specific use (e.g. for planning)". On the spectrum's own definitional reading ("agent maintains internal $M_t$ explicitly", which the Discussion keeps as "the original definitional posture"), a model-free policy meeting Definition 5 is objective-rich and explicitly model-poor, so the two axes are not shown dependent. Repair: in the summary and R1's False-of, say "on the extraction reading of model richness (a model is recoverable from the policy), the blind-seeker region holds no policy meeting Richens et al.'s Definition 5 at depth $n \geq 2$ in their setting". Also replace "competent" with "meeting Definition 5", since an agent can be competent on a narrow goal set without meeting it.

## C12 (check)
- target: segment:schema-strategy-persistence
- at: 242ebc33
- act: run
- line: derivation
- criterion: R2's stationary gain for an edge observed every step and for an intermittently observed edge under each discount convention; R1's falsifier; consistency with `#deriv-evidence-allocation-ceiling` "Discount convention".
- committed: after
- outcome: confirmed
- recheck: $\lambda = 0.7$; count update $n \leftarrow \lambda n + 1$ per observation, gain $1/(\lambda n + 1)$. Every-step: mean gain $0.3000$ (prediction $1 - \lambda$). Observed w.p. $0.5$, per-time-step discount ($n \leftarrow \lambda n$ on every step, $+1$ when observed): mean per-observation gain $0.4888$. Observed w.p. $0.5$, per-observation discount: $0.3000$. 400k steps, seed 1.

All three agree with the record. The record's attributions to EA.2 and "Discount convention" match that paragraph (per-observation gives exactly $\pi_i(1-\lambda)$; per-time-step has no closed form; the cap holds under both). R1's falsifier condition ($R_\Sigma$ below the range of $\theta$, worst-case drift) is right: an adversarial drift can hold $\theta$ near one end until the decaying-gain estimate settles there, then move $\theta$ to the other end faster than the estimate follows. The benign-drift remark is correct. The split into formal plus descriptive entries, with Behrens et al. as the neighbour outside the population, does what B.1 asks.

## C13 (check)
- target: segment:norm-explicit-strategy-condition
- at: 242ebc33
- act: read-check
- line: derivation
- criterion: Is the "loop learning unbiased" contrast gone everywhere in the segment, and is the falsifier's new reading (it tests cost estimation, not the norm) honest?
- committed: after
- outcome: confirmed
- recheck: grep the segment for "does not" near "bias"; read the Epistemic Status bullet "Model bias", the summary paragraph, and the record.

Confirmed. The falsifier's admission is honest and is the B.1-shaped answer: under the precondition the rule is optimal by definition, so what is testable is cost estimation. The Daw, Gershman, Seymour, Dayan & Dolan (2011) record (*Neuron* 69(6):1204–1215) matches my recall; I did not check it by web.

## C14 (check)
- target: segment:def-control-regret
- at: 242ebc33
- act: read-check
- line: derivation
- criterion: Does the drained "Convention hierarchy" paragraph agree with what is actually true of the right rung (C1, C2 above), and does the definition's non-negativity hold under every convention?
- committed: after
- outcome: narrowed
- recheck: the "Convention hierarchy" paragraph; the definition $\delta_{\text{regret}} = A_O - V_O(\pi_{\text{current}}) \geq 0$; the left-rung instance of `#deriv-convention-monotonicity` ($A_O^{\text{RH}} = 1$, $V_O(\pi_{\text{current}}) = 10$ in that frame).

The paragraph inherits C1 and C2 and is in F1's drain. Adjacent, not from this commit: "Always non-negative — given $\pi_{\text{current}} \in \Pi$" holds under C1 ($\sup_a Q_O(a; \pi_{\text{current}}) \geq Q_O(\pi_{\text{current}}(x); \pi_{\text{current}})$) and under C3 on the first-action reading. Under C2 it needs the left rung's order-consistency. With an unguarded $N_r \lt N_h$ replanner, $A_O^{\text{RH}}$ can fall below $V_O(\pi_{\text{current}})$ (the left-rung instance gives $1$ against $10$), so $\delta_{\text{regret}}^{\text{RH}} \lt 0$. The definition's non-negativity sentence should carry "under C1 and C3; under C2 given (RH-1/2/3)".

## F4 (finding)
- target: segment:def-value-object

The commit's edit to the struck-through Working Note ("the right rung was then thought exact unconditionally and is now conditional on closure of $\Pi$ (Monotonicity block, 2026-10-30)") adds history to a note that is already history: a resolved item, with its date and spike, kept in Working Notes. Under the effort's standing ("History goes in commit bodies and `CHANGELOG.md`, nowhere else") and `format.sop.md`'s "What earns a Working Note", the resolved item could be deleted outright. Its forward-pointing content (do not restore an unconditional rung) already lives as regression guard (1) in `#impl-strategy-structure` and in the dead-end note of `#deriv-convention-monotonicity`. Not urgent; the next integrator touching this segment for F1 can take it in the same edit.

## F5 (finding)
- target: segment:deriv-convention-monotonicity

On the three format rules the commit names for the SOP. I watched them play out across ten records here. My view:

(1) *A theorem is formal with its hypothesis class as population; adoption for a real class is a separate descriptive entry.* Adopt. In every case here it separated something that had been blurred: Richens (formal versus the "must have learned" adoption), the representation theorems versus the human target class, frozen edges versus organizations, undiscounted Beta-Bernoulli versus incumbents. Each time, the descriptive entry exposed a gap in which the population was unmeasured, and that is the information B.1 exists to surface. The cost is roughly doubled records for imported results. I think that is the right price, because the two entries have different falsifiers (counterexample versus measurement), and a single entry carrying both was where the overclaims hid. One refinement: where the body makes no adoption claim, no descriptive entry is owed. The rule should say "when the body adopts it", so it does not mint empty entries.

(2) *"Instantiated" is never filled by a theorem.* Adopt. "Not applicable" for the formal entry and "no / the study" for the descriptive one is unambiguous. The old "by an external theorem" read as instantiation and was not.

(3) *A falsifier names the clause it refutes.* Adopt. It is the rule that made two defects in this check visible quickly. In C6 the disjunct naming no clause turned out to be a confirmation, and in C2 the right rung's falsifier, once read against a named clause, was exactly the instance that fires it. It costs a phrase per record.

## What I did not check

Read but not re-derived: (RH-3)'s two inequalities and the claim that (RH-1)/(RH-2) are its special cases (pre-existing, not changed by this commit). Not opened: Debreu (1954), von Neumann–Morgenstern, Allais, Kahneman & Tversky, Choi et al. (2007), Behrens et al. (2007), the Daw papers. Statements about them are from my knowledge and are marked where they bear weight. Not read: `#scope-edge-update-causal-validity` beyond the one grep hit (it landed in `af518dd5`); `#impl-strategy-structure` beyond the changed paragraphs; `#deriv-self-actuation-grounding` beyond Lemma 1, the Assembly, the table and Class robustness; FINDINGS.md beyond the one entry; the README partials. I did not run `vsect` or check the `.vsect` events the account says it wrote. The rectangularity argument in C2 is my own and was checked only against the two non-rectangular instances.
