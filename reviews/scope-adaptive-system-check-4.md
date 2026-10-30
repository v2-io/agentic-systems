---
kind: review
author:
  name: Claude Opus 5.5 (independent adversarial checker)
  role: independent-reviewer
sources:
  - spikes/epistemic-target-ontology/09-independent-check.md
written: 2026-10-30T21:23:38Z
---

# `#scope-adaptive-system` as of 1a98d12b: an independent adversarial check

KR A.1. The full write-up, with each computation and the check script, is the source above. The checks below were made by re-deriving from the text at 1a98d12b; the segment and the dependents named here are unchanged at 094a41d2. I read 08 and the open ledger only after forming these, to avoid duplicating what is already open.

## C1 (check)
- target: segment:scope-adaptive-system
- at: 1a98d12b
- act: rederive
- line: derivation
- criterion: Item (b): $I(x_t; F_t \mid \mathcal C_t) \gt 0$ iff $C A^j P_t \neq 0$ for some $j \geq 1$; the one-step closed form $\tfrac12 \log\det(I + C A P_t A^\top C^\top N^{-1})$; the scalar random walk's $0.135$ and $0.162$ nats; $A = 0$ out
- committed: before
- outcome: confirmed
- recheck: 09 §1 and appendix (1); whole-future value as $\tfrac12 \log(P_\infty / P_s)$ with the backward predictor, and by a 200-step block determinant

## C2 (check)
- target: segment:scope-adaptive-system
- at: 1a98d12b
- act: rederive
- line: derivation
- criterion: Item (c): membership at every finite $t$; the $+\infty$ value under recurrence; one-step decay like $(K-1)/(2n)$
- committed: before
- outcome: confirmed
- recheck: 09 §1 and appendix (4); the rate follows from Clarke–Barron's cumulative form only together with monotone increments (exchangeability), which holds

## C3 (check)
- target: segment:scope-adaptive-system
- at: 1a98d12b
- act: rederive
- line: derivation
- criterion: Items (h) and (h′), including (h′)'s three support facts, the finite-block reduction, the averaged/pointwise equivalence, and the clock-and-rationals counterexample
- committed: before
- outcome: confirmed
- recheck: 09 §1

## C4 (check)
- target: segment:scope-adaptive-system
- at: 1a98d12b
- act: rederive
- line: derivation
- criterion: The housing result (four facts, the mixture sense of agreement, mutual singularity, the case-(d) conclusion) and the Definition's claim that moving an invariant coordinate between $\Omega_t$ and $\theta$ changes no mutual information
- committed: before
- outcome: confirmed
- recheck: 09 §1; the reduced target is a sufficient statistic of the other

## C5 (check)
- target: segment:scope-adaptive-system
- at: 1a98d12b
- act: rederive
- line: derivation
- criterion: Items (a), (d), (e), (f), and (g) as a statement about $\theta$; the three ways out in the intro are exhaustive; the (ii′) sentence in "Why the future stream" (one-step part at most (ii′) at $t+1$ by data processing, converse failing at $A = 0$)
- committed: before
- outcome: confirmed
- recheck: 09 §1

## C6 (check)
- target: segment:scope-adaptive-system
- at: 1a98d12b
- act: rederive
- line: derivation
- criterion: Item (g), tagged exact, last sentence: "a state that keeps moving keeps renewing what can be revealed about it"
- committed: before
- outcome: broken
- recheck: 09 §2 and appendix (2); $x_{t+1} = -x_t$, $o_t = x_t + v_t$, known law: in at every $t$, one-step part $\sim 1/(2t)$, value $+\infty$

The state moves and its uncertainty is not renewed. No coordinate is invariant, so $x_t$ is state under the coordinate reading. Under the functional reading $\lvert x \rvert$ goes to $\theta$, and the remaining sign is still not renewed. What's worked instead: (g)'s own argument goes through for any target component that is *closed*, meaning its later values are functions of its value at $t$ and the history. So (g) can be stated for closed components rather than for $\theta$ alone, and the contrast drawn with renewing ones: those whose dynamics inject fresh randomness that later observations see.

## C7 (check)
- target: segment:scope-adaptive-system
- at: 1a98d12b
- act: rederive
- line: derivation
- criterion: Discussion, "Two kinds of warrant": that the state/law cut sorts warrants by their behavior in time (moving state renewed every step, hence standing; invariant law spent, with one-step decay like $(K-1)/(2n)$; a drifting law keeps a standing warrant)
- committed: before
- outcome: broken
- recheck: 09 §2 and appendix (2), (3); counterexamples from both sides

The thesis fails in both directions:

- *State that is spent.* A noise-free sign-flip or rotation of a hidden state (orbit determination under a known law) has a one-step part decaying to zero and an infinite value.
- *Law that stays standing.* Rows first-visited at every step, each with an i.i.d. uniform parameter, give a one-step part fixed at $\log 2 - \tfrac12 = 0.1931$ nats. Unbounded static terrain is the physical case.
- *Drifting law.* A law that drifts on a known deterministic schedule with an unknown phase is spent.

The $(K-1)/(2n)$ decay is (c)'s, under (c)'s recurrence hypothesis, which the Discussion drops.

What's worked instead, single-agent and not yet checked by another mind: for a closed target, the value at $t$ equals the sum of the later one-step parts exactly (chain rule plus data processing both ways; the script checks the telescoping to six decimals). This is the identity the Discussion already uses "because the law does not move". It follows that a finite value forces the one-step parts to zero, while an infinite value allows decay (recurrence) or not (novelty). A finite value with a one-step part bounded away from zero, as in the random walk, needs fresh randomness. The carve is closed (a stock drawn down) against renewing, and invariance is a sufficient condition for closedness on the law side.

## F1 (finding)
- target: segment:scope-adaptive-system
- at: 1a98d12b

The Working Notes' strengthening item proposes requiring every invariant function of the path to be in $\theta$, with the tracking no-go standing where the invariant $\sigma$-field is trivial. The sign-flip example separates the invariant $\sigma$-field (which holds $\lvert x \rvert$) from the tail $\sigma$-field (which holds $x_1 = (-1)^{n-1} x_n$). An invariant-$\sigma$-field rule leaves a periodic phase as state with a spent warrant; a tail rule captures it. 06 used "tail or invariant" interchangeably. The difference is the cyclic structure. I recall a Blackwell–Freedman result on the tail $\sigma$-field of Markov chains, but I have not read it, and I am not citing it. 09 §2.

## F2 (finding)
- target: segment:scope-adaptive-system
- at: 1a98d12b

Line 31: "Whatever about the world stays the same" reads as any function of the path, while the Working Notes say the landed rule names declared variables. Line 49, item (b): "$A, C$ and the noise covariances $Q, R$ known, so $\theta$ is fixed and $S_t = x_t$" is wrong under either reading when a direction is invariant. Example: $A = I$ with $Q = \operatorname{diag}(1, 0)$, whose second coordinate is law under the cut. The criterion is unaffected (membership does not depend on the cut). A qualifier such as "with no invariant direction, for example $Q \succ 0$" fixes the label. 09 §3.

## F3 (finding)
- target: segment:scope-adaptive-system
- at: 1a98d12b

Two sentences say the law is learned exactly where the text means "wherever some continuation can reveal it". Line 50, (c): the deterministic-prior agent "knows its law exactly". Line 73, Discussion: the law part reaches zero "only when the law can be identified exactly". Under (f), rows at unreachable pairs stay uncertain while the law part is zero. 09 §3.

## F4 (finding)
- target: segment:scope-adaptive-system
- at: 1a98d12b

Line 42, condition 2: $\mathcal O \neq \emptyset$ holds for every well-formed loop. With $\mathcal O = \emptyset$ there is no observation function into it and no chronica. "No channel" is $\lvert \mathcal O \rvert = 1$, case (e). The live necessary form is $\lvert \mathcal O \rvert \geq 2$, which condition 1 implies. (e)'s "The empty channel is the extreme case" inherits this. 09 §3.

## F5 (finding)
- target: segment:scope-adaptive-system
- at: 1a98d12b

Line 73: "whenever the agent's conduct can return to what it is learning without bound". The value is a supremum over continuations, as (c) states, so the agent's own conduct is not the condition.

## F6 (finding)
- target: segment:scope-adaptive-system
- at: 1a98d12b

Line 27, "Whatever part of the law the analysis does not fix", reads as the modeler's knowledge. So do "the analysis leaves open" and "random under the modeler's reference measure" in `#def-action-transition` (lines 12, 33) and `#def-observation-function` (lines 15, 37), and "where the analysis leaves them open" in NOTATION's $\theta$ row. The segment's own rule, and "Whose uncertainty", cut the support by the agent's design-time knowledge: a benchmark designer who knows the law does not take the learner out. A reader who stops at the upstream definitions gets the opposite rule. 09 §3.

## F7 (finding)
- target: segment:def-agent-environment
- at: 1a98d12b

Line 13 ("systems facing genuine uncertainty about their environment's state or law"), line 31 ("#scope-adaptive-system states it exactly") and line 35 (Epistemic Status, "systems where the agent faces genuine uncertainty") gloss the scope as residual uncertainty. Under the scope's item (a) that is necessary, not sufficient: a fresh state with $A = 0$ faces genuine uncertainty and is out. This extends reread-1's F7, which named line 43; line 43 is now fixed, and these three lines are not.

## F8 (finding)
- target: segment:disc-framework-self-diagnostic
- at: 1a98d12b

Line 19: "the agent receives observations under uncertainty and runs the cycle" is the residual-uncertainty gloss, which `#scope-adaptive-system` item (a) calls necessary, not sufficient. Line 35, fixed after reread-1's F13, states the scope correctly.
