---
kind: review
author:
  name: Claude Opus 5.5 (independent checker, identification side)
  role: checker
sources:
  - 01-aat-core/src/der-loop-interventional-access.md
  - 01-aat-core/src/def-value-object.md
  - 01-aat-core/src/def-model-sufficiency.md
  - 01-aat-core/src/der-causal-hierarchy-requirement.md
  - 01-aat-core/src/def-pearl-causal-hierarchy.md
  - 01-aat-core/src/causal-access-intro.md
  - 01-aat-core/src/impl-causal-access.md
  - 01-aat-core/src/der-directed-separation.md
  - 01-aat-core/src/deriv-convention-monotonicity.md
  - reviews/part-ii-integration-1.md
  - msc/inside-out-2026-10/part-ii-integration.md
  - spikes/spike-loop-identification-decision-state-2026-10-30/de-novo-feedback-1.md
  - spikes/spike-loop-identification-decision-state-2026-10-30/01-derivation.md
written: 2026-10-30
---

# Part II integration, identification side: independent check

KR **C.2** ("Strengthenings C1–C3 (exit time, loop identification, allocation vs distortion coupling) are independently checked, then landed or refuted") and **C.1** ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier"), under the top intent "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself."

Scope: the landing `253d2bca`..`279b2699`, as it stands at `9fbfa9ad` (none of the segments below changed after `279b2699`). I read `#der-loop-interventional-access`, `#def-value-object` and `#def-model-sufficiency` cold and whole first, then the four segments edited beside them, then the integrator's account and typed re-derivations, then the spike's derivation and verifier feedback where a finding traced back to them. I edited no canon and committed nothing. The six new check scripts are untracked files in `spikes/spike-loop-identification-decision-state-2026-10-30/`, named `check-part-ii-check-1-*.py`, following the `check-feedback-1-*` / `check-integration-1-*` pattern there; each runs with `python3 -I` (the LQR one needs numpy and scipy and takes a few minutes).

What survived is most of the landing: ignorability at the policy's own inputs, the coin-retention clause, the adjustment-at-a-coarsening factorization, the g-formula average, the intention-to-treat reading, the Q-learning and Kalman + LQR placements, the "already tired" repair, and the regression guard against "goal-conditioned policies violate ignorability". Four statements did not survive as written, and each fails on a constructed instance I ran: the deterministic no-go is scoped too wide (F1); "a deterministic policy passes the on-policy sufficiency test for free" is false in canon's own witness (F2); premise 1 of the $M_t$-form, and the scoping-rule record in `#der-directed-separation` that cites it, attribute the collider at $M_t$ to $\kappa \gt 0$ when it opens at $\kappa = 0$ too (F3); and both hypotheses of the right rung of convention monotonicity silently assume the replanner lies in $\Pi$, and fail without it (F5). Each comes with a repair, and three of the repairs are strengthenings. Two smaller structural points (F4, F6) and a set of wording items (F7) follow.

## C1 (check)
- target: segment:der-loop-interventional-access
- act: rederive
- line: derivation
- criterion: Sequential ignorability holds at $Z_t = X_t$ under (P) with fresh coins and at $\mathcal C_t$ for any environment-independent coin source; with a shared source, retaining past actions does not suffice; $R \perp S \mid Z_t$ implies $a_t \perp Y_t^{(a)} \mid Z_t$; under ignorability at $X_t$ the interventional sufficiency condition implies the on-policy one, and the converse holds under positivity at $X_t$.
- committed: after
- at: 9fbfa9ad
- outcome: confirmed
- recheck: three lines each, below; `python3 -I check-feedback-1-lemma1b-pstream.py` in the C2 spike dir

Re-derived, not transcribed. Fresh coins: given $X_t$ the action is a function of $U_t$ alone, and $U_t$ is independent of everything that produced $X_t$ and of the environment's exogenous inputs, so $U_t \perp (Y_t^{(a)}, X_t)$ and hence $a_t \perp Y_t^{(a)} \mid X_t$. This uses only the freshness and environment-independence of $U_t$; mediated access is not needed for this case (it is needed for the chronica and shared-coin cases, where $X_s$ must be a function of what was conditioned on). Factorization: with $Y^{(a)} \perp X_t \mid S$, weak union gives $Y^{(a)} \perp R \mid (S, Z)$; with $R \perp S \mid Z$, contraction gives $R \perp (S, Y^{(a)}) \mid Z$; $a_t = \pi(R, U_t)$ with $U_t$ fresh finishes it. Coincidence: under ignorability at $X_t$, $P(o \mid x, a) = P(Y^{(a)} \mid x)$, so the interventional condition makes $P(o \mid x, a)$ constant over the $Z$-cell and the on-policy condition follows; the converse needs $P(a \mid x) \gt 0$ at every $x$ in the cell. One proviso on the chronica clause: conditioning on $\mathcal C_t$ blocks the back-door paths only if the initial state $X_0$ is itself environment-independent (or conditioned on). A goal set before the trajectory by a principal who knows something about the world — `#def-value-object`'s storm-shelter example — opens $a_t \leftarrow X_t \leftarrow G_0 \leftarrow \Omega \rightarrow o_{t+1}$, which $\mathcal C_t$ does not block. The text should say "any environment-independent coin source and initial state" (F7).

## C2 (check)
- target: segment:der-loop-interventional-access
- act: run
- line: derivation
- criterion: "A decision state rich enough to determine the action — any deterministic policy, $U_t$ absent — … without a restriction on the environment class nothing off-policy is identified there", with `check-integration-1-deterministic-nogo.py` as its witness.
- committed: after
- at: 9fbfa9ad
- outcome: narrowed
- recheck: `python3 -I` on `check-integration-1-deterministic-nogo.py`, `check-part-ii-check-1-nogo-onestep-variant.py` and `check-part-ii-check-1-nogo-scope.py` in the C2 spike dir

The integrator's script reproduces as printed. Its SCM B decides whether an action is "untaken" by testing `a != a1`, where `a1` is the policy's decided action, and it uses `a1` to recover the agent's coin $u$, even when the step-1 action is intervened to `a`. On the one-step reading (the intervention is on $a_1$) the environment is reading the agent's decision state, which canon's coupling does not allow: the agent reaches the environment only through its action channel (`#def-agent-environment`). The variant `check-part-ii-check-1-nogo-onestep-variant.py` restricts SCM B to the executed action. That restriction makes B's flip condition identically false, so B coincides with A. What the variant shows is that the coded B cannot be written from the executed action alone. It does not show that no valid B exists. That stronger statement comes from `check-part-ii-check-1-nogo-scope.py`, which enumerates all 16 deterministic environments of the one-step case: with the coin stored in $X_1$, each has its own on-policy law (F1). The script is valid on a two-step reading: $a_1$ was executed on-policy and revealed $u$, and the intervention is on a later action whose decision state the environment can now reconstruct. Its docstring and labels (interventional "at $X_1$", on-policy law over $(o_1, a_1, o_2)$) do not make that reading explicit. The claim's scope is the larger problem (F1).

## C3 (check)
- target: segment:def-value-object
- act: run
- line: derivation
- criterion: "The agent cannot test premise 3 on-policy when its policy is deterministic given $(M_t, G_t)$ (the on-policy sufficiency test of $M_t$ passes for free)"; the same statement in #der-loop-interventional-access (Formal Expression, "Two limits") and #def-model-sufficiency (Discussion).
- committed: after
- at: 9fbfa9ad
- outcome: broken
- recheck: `python3 -I check-part-ii-check-1-onpolicy-test-detects.py` in the C2 spike dir

I ran the C2 spike's own witness (Beta-count strategy state, $M_t = t$, $\kappa_{\text{processing}} = 0$) at $\varepsilon = 0$ with ties broken deterministically, so that the policy is a deterministic function of $X_t$ (200 000 episodes). Inside a single $M_t$-stratum with $a = 1$, the on-policy $E[o \mid X_t, a = 1]$ ranges from $0.32$ to $0.77$ at $t = 3$ and from $0.19$ to $0.81$ at $t = 7$, over cells with more than 200 samples each. The test does not pass. It detects exactly the premise-3 failure the segment cites the witness for. At $t = 1, 2$ each $(M_t, a)$-cell holds one $X_t$ value, and there the test does pass vacuously. That is the only regime where "for free" is true. See F2.

## C4 (check)
- target: segment:def-value-object
- act: run
- line: derivation
- criterion: Premise 1 of the $M_t$-form: "At $\kappa \gt 0$ the belief update writes goal information into $M_t$, which makes $M_t$ a collider of goal and world … The claim rides only on the zero"; and #der-directed-separation's Claim Record "A result that consumes only the zero …", True of: "at $\kappa_{\text{processing}} = 0$ … conditioning on $M_t$ does not make an exogenous goal outcome-informative — a derivation that uses only the zero".
- committed: after
- at: 9fbfa9ad
- outcome: broken
- recheck: `python3 -I check-part-ii-check-1-kappa0-action-collider.py` in the C2 spike dir (exact, fractions)

Exact enumeration. The world bit $W$ is fair and persistent; the goal $G$ is fair and exogenous. $a_0 = G$ with probability $0.9$, otherwise flipped, so $H(G \mid e_1) = 0.469$ bits and $\kappa$ is well-defined. The event is $e_1 = (a_0, o_1)$ with $o_1 = W \oplus a_0$, and the goal-blind update keeps the observation and drops the action: $M_1 = o_1$. Then $I(G; M_1 \mid e_1, M_0) = 0$, so $\kappa_{\text{processing}} = 0$ exactly. Bounded signaling holds. At step 1 the policy reads $(M_1, G)$, $Y^{(1)} = W$, and $Y^{(0)}$ is a fair coin. On-policy $P(o = 1 \mid a = 1, M_1 = 0) = 0.82$ against interventional $P(Y^{(1)} = 1 \mid M_1 = 0) = 0.50$, and $0.18$ against $0.50$ at $M_1 = 1$. $X_1$-stratified on-policy equals interventional in every cell. This is the V7 mechanism that `#der-directed-separation`'s Scope Condition already carries. See F3.

## C5 (check)
- target: segment:def-value-object
- act: rederive
- line: derivation
- criterion: The $M_t$-form is the g-formula average of the $X_t$-identified effect: $P(o \mid do(a), M_t) = \sum_g P(G_t = g \mid M_t)\, P(o \mid do(a), M_t, g)$, not an extra assumption.
- committed: after
- at: 9fbfa9ad
- outcome: confirmed
- recheck: one line, below

$P(o \mid do(a), M_t) = \sum_g P(g \mid M_t, do(a))\, P(o \mid do(a), M_t, g)$, and $G_t$ is not a descendant of $a_t$, so $P(g \mid M_t, do(a)) = P(g \mid M_t)$. This is exact. Its cost is positivity of $a$ at every $(M_t, g)$ with $P(g \mid M_t) \gt 0$, which the text carries ("under positivity there"). When the policy is deterministic in $X_t$, the cost is paid only through F1's route.

## C6 (check)
- target: segment:def-value-object
- act: rederive
- line: derivation
- criterion: "Three premises deliver it, and each can fail on its own"; the displayed true-law equation conditions on $G_t$; premise 3 is stated on $R = r(G_t)$; "Stratifying on $M_t$ directly is valid exactly when premise 3 holds".
- committed: after
- at: 9fbfa9ad
- outcome: narrowed
- recheck: three lines, F4

Premise 3, formalized as the segment formalizes it ($Y^{(a)} \perp R \mid M_t$ for each $a$), is by itself sufficient for identification at $M_t$, with no further premise. The policy reads $(M_t, R)$, deterministically or with a fresh coin, so $a_t \perp Y^{(a)} \mid M_t$ follows in one step. Premises 1 and 2 are therefore not additional requirements. They are architectural conditions that close two of the routes by which premise 3 fails. And the display conditions on all of $G_t$ while premise 3 covers only the read part $R$. See F4.

## C7 (check)
- target: segment:def-value-object
- act: run
- line: derivation
- criterion: The right rung $A_O^{\text{RH}} \leq A_O^{\text{B}}$ holds when $\Pi$ is closed under first-action prefixing, or when $\pi^\ast$ is optimal over $\Pi$ from every one-step-reachable state (also #deriv-convention-monotonicity's (PC) and (SO)).
- committed: after
- at: 9fbfa9ad
- outcome: broken
- recheck: `python3 -I check-part-ii-check-1-right-rung-rh-not-in-pi.py` in the C2 spike dir; the three-state instance in #def-value-object by hand

First I checked the landed counterexample by hand: $V(\pi_1) = 1$, $V(\pi_2) = 10$, the one-step replanner is $\pi_1$, $A^{\text{RH}} = 100$, $A^{\text{B}} = 10$. It holds. Then the sufficiency direction. Both proofs in `#deriv-convention-monotonicity` use "$\pi_{\text{RH}} \in \Pi$" ("That $\pi_{\text{RH}}$ is drawn from $\Pi$"; "since $\pi_{\text{RH}} \in \Pi$"). But C2's $\pi_{\text{RH}}$ re-optimizes over $\Pi$ at every state, so it is a state-wise composite of members of $\Pi$ and is generally not a member. My instance has $N_h = 3$ and $N_r = 1$; the start $x$ has a single action $z$ leading to $s$; from $s$, action $c$ pays $5$ to $s_1$ and $d$ pays $0$ to $s_2$; at $s_1$, $e_1$ pays $0$ and $e_2$ pays $10$; at $s_2$, $f$ pays $6$. $\Pi = \{\pi_A = (z, c, e_1, f),\ \pi_B = (z, d, e_2, f)\}$. $\Pi$ is prefix-closed, trivially, since $x$ has one action. $\pi^\ast = \pi_B$ (value $6$ against $5$) is $\Pi$-optimal from $x$ and from $s$, the only one-step-reachable state. So (PC) and (SO) both hold. The replanner composes $(z, c, e_2)$, worth $15$, which is not in $\Pi$. $A^{\text{RH}} = 15 \gt A^{\text{B}} = 6$. See F5.

## C8 (check)
- target: segment:def-model-sufficiency
- act: rederive
- line: derivation
- criterion: The echo agent ($a_{t+1} = o_{t+1}$, later actions constant) scores $S(M_t) = 1$ while one-step insufficient by one bit; "numerator $0$, denominator $1$ bit".
- committed: after
- at: 9fbfa9ad
- outcome: narrowed
- recheck: by hand, F6

The spike's two-bit construction (`01-derivation.md` §2) holds by hand. $\mathcal C_t$ carries independent bits $c, c'$; $M_t$ keeps $c'$ and drops $c$; $o_{t+1} = c$ and $o_{t+2} = c'$. The numerator is $0$ because $a_{t+1}$ reveals $o_{t+1}$ and $M_t$ gives $o_{t+2}$. The denominator is $1$ bit, and that bit comes from $c'$. The segment carries only the one-bit half, so its "denominator $1$ bit" is not reproducible from the text. Read with a single bit, the denominator is $0$ and $S$ is undefined by the segment's own well-definedness clause. See F6.

## C9 (check)
- target: segment:impl-causal-access
- act: run
- line: derivation
- criterion: Kalman + LQR: "nothing off-policy identified from its data" (impl-causal-access table; #def-pearl-causal-hierarchy "the effect of any other is not identified from the loop's data"; #der-loop-interventional-access Record 2 False of).
- committed: after
- at: 9fbfa9ad
- outcome: confirmed
- recheck: by hand for full-state feedback; `python3 -I check-part-ii-check-1-lqr-closed-loop.py` (numpy, scipy) for the measurement-noise case

I tested whether the claim survives even inside the linear-Gaussian class, which is a stronger test than the unrestricted class the no-go is stated for. With full-state feedback $u = -Kx$, the closed loop is $x_{t+1} = (A - BK)x_t + w_t$, so only $A - BK$ is identified, exactly. With measurement noise the regulator is dynamic in $y$, and I fitted ARMAX(1,1,1) by prediction error on 40 000 closed-loop samples (scalar $a = 0.9$, $b = 0.5$). The profile over $B$, with $A$ and $C$ re-optimized, is flat to $10^{-4}$ relative over $B \in [0, 1.5]$. Closed-loop data leave $b$ on a ridge. This is numerical evidence for one scalar instance, not a derivation, but it holds in the class where Kalman + LQR actually lives. One placement note: `#der-causal-hierarchy-requirement` puts LQR outside learning-agent scope, and `#der-loop-interventional-access` Record 2's population is "learners in agency scope", so Kalman + LQR in that record's False-of sits outside its own population. `#def-value-object` already moved it to the by-construction record for that reason.

## C10 (check)
- target: segment:der-causal-hierarchy-requirement
- act: rederive
- line: derivation
- criterion: In a fully observed, stationary MDP, $E[R \mid s, do(a)] = E[R \mid s, A = a]$ because stationarity makes the value table outcome-irrelevant given $s$; tabular $\varepsilon$-greedy Q-learning converges to $Q^\ast$ (also #der-loop-interventional-access Record 2 True of).
- committed: after
- at: 9fbfa9ad
- outcome: confirmed
- recheck: by hand

$(r, s') \sim T(\cdot \mid s, a)$ with noise fresh at each step, and the Q-table is a function of past noise, so $Y^{(a)} \perp \text{Q-table} \mid s$, and C1's factorization applies with $Z = s$. Watkins & Dayan's convergence also needs every $(s, a)$ visited infinitely often and Robbins–Monro step sizes. $\varepsilon$-greedy supplies the action half of the visitation; the state half is an ergodicity assumption the text leaves implicit. This is a wording point.

## C11 (check)
- target: segment:causal-access-intro
- act: read-check
- line: reading
- criterion: The "already tired" agent misleads "exactly when it moved the executed action without being in the state the agent decided from or recorded".
- committed: after
- at: 9fbfa9ad
- outcome: confirmed
- recheck: reading

The repair is right in substance and matches `#der-loop-interventional-access` Record 2 False-of. "Exactly when" is stronger than what is shown: a learner can hold tiredness in its decision state and its record and still pool over it when it stratifies, which is a coarsening and not a record gap. Use "when".

## F1 (finding)
- target: segment:der-loop-interventional-access

**The deterministic no-go is scoped to "deterministic in $X_t$"; it holds only for policies deterministic in what the environment can know, and the correction is a strengthening.** Canon places all of an agent's randomness inside $M_t$ ("a retained pseudo-random state is part of $M_t$ under state completeness"), so a canonical randomizing agent is deterministic in $X_t$. As written, the no-go then denies that such an agent identifies anything off-policy. That is false. Take a fresh, environment-independent coin $u$ drawn and stored in $X_t$ (a pre-drawn coin table; a private initial state), with $\pi$ deterministic in $X_t$ and varying with $u$. Under canon's coupling the environment receives the agent only through executed actions, so $Y_t^{(a)} \perp X_t \mid \mathcal C_t$ for any environment-independent private component, revealed or not. The component reaches $\Omega$ only through past actions, and every past action is in $\mathcal C_t$: on a path through $u$ each past action is either a conditioned non-collider or a collider whose other parents are conditioned. Revelation does not touch this sufficiency. What revelation destroys is positivity at $\mathcal C_t$: once past actions pin the component, the current action is determined given the chronica. Where positivity at $\mathcal C_t$ holds, ignorability there (C1) gives $P(Y^{(a')} \mid X_t = x) = P(o \mid a', \mathcal C_t = c(x))$. That identifies the untaken action's effect at a visited decision state with no restriction on the environment class. `check-part-ii-check-1-nogo-scope.py` enumerates all 16 deterministic environments $g(\theta, a)$. With the coin stored in $X_1$, every environment has its own on-policy law, so every untaken-action effect is identified. With the policy deterministic in the history ($\pi(\theta) = \theta$), environments group into 4 on-policy classes and untaken effects differ within a class. The integrator's two-SCM construction needs the environment to reconstruct $\pi(X_t)$ from what it has seen, which is the two-step reading of its script (C2).

What I would write instead, in place of the sentence beginning "A decision state rich enough to determine the action": "A policy whose action is determined by what the environment can know — the actions it has received and its own state, so that no component the action varies with is hidden from it — has on-policy data for one action per such cell, and without a restriction on the environment class nothing off-policy is identified there." Then the boundary. The coarsening that drops an environment-independent private component is outcome-sufficient unconditionally under the coupling; that is not assumed of the environment. It supplies positivity as long as the component is fresh, meaning not yet pinned by executed actions. So the corrected no-go is exactly "positivity fails at the environment-visible coarsening". A shared or scheduled seed is the boundary case: once past actions reveal it, the current action is determined given the chronica and an unrestricted environment can compute the agent's future coins, so positivity fails and the no-go returns. This mirrors the coin-retention clause on the ignorability side. Three consequences to carry. (a) "Identification of an untaken action's effect at a visited decision state therefore rests on a class restriction" and "The restriction identification rests on is therefore an assumption about the environment" are false for the coin route; for that route the restriction is a property of the agent's own construction, checkable by design. (b) Premise (P) need not be "not a consequence of canon": it can be stated as "the policy varies with a fresh, environment-independent component, stored in $M_t$ or arriving from a source the outcome-generating environment does not see", and whether the coin sits inside or outside $X_t$ stops mattering. (c) Record 2's False-of ("every deterministic policy in an unrestricted environment class") and `#def-value-object` Record 2's False-of ("any learner identifying from data with a policy deterministic in its decision state") take the same rescoping. The check script should be rewritten with two explicit actions, so that its reading is the valid one.

## F2 (finding)
- target: segment:def-value-object

**"Passes the on-policy test for free" is false. The true statement is one-sided, and that is a strengthening: the agent can refute premise 3 on-policy; it cannot confirm it.** Three carriers: `#def-value-object` ("The agent cannot test premise 3 on-policy when its policy is deterministic … passes for free"), `#der-loop-interventional-access` Formal Expression ("outcome-sufficiency of a coarsening cannot be tested on-policy when the policy is deterministic … a deterministic policy passes the on-policy test for free"), and `#def-model-sufficiency` Discussion ("passes the on-policy test for free while the interventional condition is unconstrained"). The interventional condition implies the on-policy one, so an on-policy failure refutes sufficiency under any policy. Under determinism, a pass constrains only $Y^{(\pi(x))}$ at each $x$ and says nothing about untaken actions. The test passes vacuously only in $(Z, a)$-cells holding a single $X_t$ value, for instance when the policy is injective in the dropped component. The source is the verifier's §92 ("passes the on-policy sufficiency test of $M_t$ for free"), which generalized the two-point case. The integrator and the B.1 checker carried it forward. In canon's own witness the test fails, decisively (C3). What I would write: "Outcome-sufficiency of a coarsening is refutable on-policy but not confirmable under a deterministic policy: the on-policy test $I(X_t; o_{t+1} \mid Z_t, a_t) = 0$ is implied by the interventional condition, so a failure refutes it; a pass constrains only the action each decision state took, and is vacuous where $(Z_t, a_t)$ determines $X_t$." `#def-value-object`'s last sentence then becomes: the agent can detect, from its own data, that its goal state carries outcome information beyond $M_t$, but cannot certify the opposite. Record 1's falsifier ("$M_t$-stratified differs from $X_t$-stratified on the same data") is this test, and it is runnable by the agent itself; that is worth saying.

## F3 (finding)
- target: segment:def-value-object

**The collider at $M_t$ opens at $\kappa_{\text{processing}} = 0$ as well, through the action channel, so premise 1's gloss and `#der-directed-separation`'s scoping-rule record are wrong to say it "rides only on the zero".** C4 is an exact instance with an exogenous goal, bounded signaling and $\kappa = 0$, in which the $M_t$-stratum is confounded ($0.82$ against $0.50$). The mechanism is the one `#der-directed-separation`'s Scope Condition already demonstrates (V7): an observation is a collider of goal and world when the action depended on the goal, and an update that keeps the observation but not the action carries the collider into $M_t$ while writing no goal information into it beyond $e_\tau$, which is all $\kappa$ measures. Formally this is a premise-3 failure, so the three premises remain jointly sufficient. The defect is in what premise 1 is said to do. The repairs I would make: in `#def-value-object` premise 1, "Causal discipline and the event clause of #der-directed-separation's Scope Condition: $\kappa_{\text{processing}} = 0$, and the update retains the realized action whenever it retains an observation whose law depends on it (more generally, $M_t$ is calibrated under each goal's law); at $\kappa \gt 0$, or with the action dropped, $M_t$ is a collider of goal and world"; delete "The claim rides only on the zero"; add the action-dropping agent to Record 1's False-of. In the same record, qualify the True-of "a fixed setpoint as $G_t$ (the setpoint carries nothing about the world)" with "under the Scope Condition's event clause". C4 is that case, with a setpoint that varies across trajectories and an update that drops the action; left unqualified, the True-of and the new False-of contradict each other. The integrator should also check whether the remaining clause "the architecture-inspection certificate is not consumed" survives once the event clause is part of the premise. In `#der-directed-separation`'s record "A result that consumes only the zero …", the True-of example is refuted, and the record says it is "the one such result currently stated". Either the scoping rule has no stated instance, or "causal discipline" is redefined to include the event clause. Which of these is right needs deciding, not a word swap. `#der-directed-separation` is in the other checker's part; I report it here because `#def-value-object` cites it as premise 1's warrant. `#impl-causal-access`'s "generically yes at the $M_t$-stratum … where a goal-coupled update makes $M_t$ a collider" should name the action-dropping route beside the goal-coupled one. One more observation from the same instance: a model that keeps outcome summaries without the action mix, such as a running average of outcomes regardless of action, is a common practical case of this route.

## F4 (finding)
- target: segment:def-value-object

**The premise structure of the $M_t$-form: one condition, several routes to failing it.** (i) The display $E[V \mid M_t, G_t, do(a), \pi_{\text{cont}}] = E[V \mid M_t, do(a), \pi_{\text{cont}}]$ conditions on all of $G_t$, but premise 3 is stated on the read part $R = r(G_t)$. A part of $G_t$ the policy does not read can carry outcome information, which breaks the display without affecting identification, since an unread part is not a confounder. Write the display with $R_t$, or state premise 3 on $G_t$; identification needs only $R_t$. (ii) Formalized as $Y^{(a)} \perp R \mid M_t$, premise 3 alone gives $a_t \perp Y^{(a)} \mid M_t$ (C6), so premises 1 and 2 are not further requirements. Stronger and simpler: "the $M_t$-stratum is valid when the read part of the goal is outcome-irrelevant given $M_t$; it fails by (a) the collider at $M_t$ (goal-coupled update, or an update that drops the action, F3), (b) the goal reaching the world other than through the action, (c) the goal carrying world information, whether stored outcome statistics (the edge-credence learner) or provenance (the storm-shelter principal)." Directed separation's Scope Condition closes (a), bounded signaling closes (b), and nothing in canon closes (c) except stationarity with full observability. The routes are what an agent can inspect; the condition is what the derivation uses. (iii) "Stratifying on $M_t$ directly is valid exactly when premise 3 holds" repeats the "iff" the integrator refuted for the spike's Proposition 5. Premise 3 is sufficient, not necessary: $Q_O$ is an expectation, so mean-independence suffices, and a policy whose action is independent of $R$ given $M_t$ is valid whatever $R$ carries. Use "when". (iv) The direct condition $Y^{(a)} \perp R \mid Z$ is weaker than $R \perp S \mid Z$, the condition `#der-loop-interventional-access` calls "the general condition". $R \perp S \mid Z$ implies it by contraction, and the converse fails when the outcome laws indexed by $S$ are linearly dependent mixtures. `#der-loop-interventional-access` should call $R \perp S \mid Z$ "a sufficient condition including both sufficiencies" and name $Y^{(a)} \perp R \mid Z$ as the weakest of the stated forms, so that the two segments use one condition. (v) "Goal variation as the agent's own instrument": "instrument" will be read as an instrumental variable, which needs no ignorability of the treatment. Here the goal plays the role of the randomizer under a conditional-independence premise. "The agent's own randomizer" says what is meant.

## F5 (finding)
- target: segment:deriv-convention-monotonicity

**Both right-rung hypotheses, (PC) prefix-closure and (SO) state-wise optimality of $\pi^\ast$, silently assume $\pi_{\text{RH}} \in \Pi$, and the rung fails without it (C7: $A^{\text{RH}} = 15 \gt A^{\text{B}} = 6$ with (PC) and (SO) both holding).** The receding-horizon replanner chooses a member of $\Pi$ afresh at each state, so it ranges over state-wise composites of $\Pi$, a larger class than $\Pi$. For the classes the appendix names (all history-dependent policies; all time-indexed Markov policies), the composite lies in $\Pi$, so those statements stand. For the restricted classes `#def-value-object` says canon uses ("DAG-representable strategies … not closed under prefixing by construction"), $\pi_{\text{RH}} \in \Pi$ is a hypothesis of its own. The repair: add "(and $\pi_{\text{RH}} \in \Pi$, which holds when $\Pi$ is closed under state-wise switching, e.g. a product class of per-state decision rules)" to both (PC) and (SO) in `#deriv-convention-monotonicity`, and to the five carriers in `#def-value-object` (summary paragraph; Monotonicity bold statement; Right-rung derivation; Epistemic Status layer 3; Record 3 True-of). Alternatively, define C2's replanner over $\Pi$-admissible composites. Record 3's falsifier ("a policy class satisfying the closure hypothesis in which $\sup_a Q_O(a; \pi_{\text{RH}}) \gt \sup_a Q_O(a; \pi^\ast)$") is met by C7's instance as the hypotheses are now worded. The appendix's sentence "Neither hypothesis can be dropped" is true. What is new is that each hypothesis also needs $\pi_{\text{RH}} \in \Pi$.

## F6 (finding)
- target: segment:def-model-sufficiency

**The echo counterexample should carry its second bit.** As written ("its model has dropped one bit the next observation carries — numerator $0$, denominator $1$ bit"), a reader reconstructs one bit and gets $0/0$, the undefined case of the segment's own well-definedness clause. The demonstration needs $c'$, retained by $M_t$ and revealed at $t + 2$, to make the denominator $1$ bit (C8). The two-bit version belongs in the segment so that the demonstration does not live only in a spike. Two smaller items in the same paragraph: the condition is stated as independence from "$G_t$", where `#def-value-object` states it on $R = r(G_t)$, so align them; and "Sufficiency relative to $\mathcal C_t$ implies it" reads as predictive sufficiency ($S = 1$), which the paragraph then denies is enough. Write "*Interventional* sufficiency relative to $\mathcal C_t$ implies it, given an environment-independent initial state."

## F7 (finding)
- target: segment:der-loop-interventional-access

Wording items, none of which changes a result. (a) The chronica clause of ignorability needs an environment-independent initial state $X_0$ as well as an environment-independent coin source (C1). (b) "Ignorability … under (P) and mediated access" for fresh coins: mediated access is not used there (C1), and it is used in the chronica and shared-coin clauses; saying which is which helps a reader see what each premise buys. (c) Record 2 lists Kalman + LQR, which sits outside learning-agent scope, under a population of "learners" (C9). (d) The Q-learning True-of needs "every state visited infinitely often" beside $\varepsilon$-greedy's action positivity (C10). (e) `#causal-access-intro`: "exactly when" should be "when" (C11). (f) Record 2's title bundles three claims (identification conditions, free ignorability, the no-go), so its False-of lists premise violators rather than instances where the claim is false. Splitting the no-go into its own record would let each field mean one thing.

## On the brief, the integration's framing, and what I did not check

The places all four hands agreed are where three of the four failures were. "Passes for free" entered at the verifier and was carried by everyone. The right rung's hidden $\pi_{\text{RH}} \in \Pi$ passed the B.1 sub-agent, the integrator and the appendix's own proof. And the $\kappa = 0$ collider was already demonstrated inside `#der-directed-separation` (V7) and still not carried into the premise that cites it. In each case a constructed instance, a dozen lines long, settled the question; re-derivation from the written text had not. The integration's framing, three quantities each claim is about one of, held up well on this side. The failures are all about the scope of an "exact" sentence, not about the frame. Not checked: the horizon-$N_h$ g-formula (open in the integrator's own Working Note); whether `#def-model-sufficiency`'s formula should hold the actions exogenous (an open vsect question; F6 does not touch it); the honest-credit citations (Pearl Thm 3.2.2, Ortega & Braun §3.2, Dawid & Constantinou Def. 5.1, Bareinboim, Zhang & Lee Lemma 1, Hahn, Todd & Van der Klaauw), which I did not open, and the footnote says no one in the project has. The brief was clear and left the method to me; the integrator's §4 checklist was useful as a list of where it was unsure, and I read it only after the cold pass.
