---
kind: review
author:
  name: Claude Opus 5.5 (A.1 fourth reader, bare brief)
  role: independent adversarial checker
sources:
  - spikes/epistemic-target-ontology/11-independent-check.md
written: 2026-10-30
---

# #scope-adaptive-system at 3f3b4ca5: a fourth independent check

KR **A.1** (`msc/inside-out-2026-10/INTENT.md`). I re-derived from the text at `3f3b4ca5` (the segment is byte-identical at `70f9f969`) before reading any earlier review of it, and I did not read `07`–`10` or check-4. Derivations, numbers and replacement text for each item are in the write-up named above, under the label given at the end of each item. What I did not read is listed there. This record's list of items is its content; its silence about a part means only that I found nothing there.

## C1 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: rederive
- line: derivation
- criterion: Items (a), (d), (e), (f), and condition 1 implying condition 2, each as stated
- committed: after
- outcome: confirmed
- recheck: re-derive from the chain rule and the definition of conditional independence; for (f), $I(U,V;F \mid \mathcal C) = I(U;F \mid \mathcal C) + I(V;F \mid U,\mathcal C)$

Write-up "What holds".

## C2 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: run
- line: derivation
- criterion: Item (b): the criterion $C A^j P_t \neq 0$, the one-step formula $\tfrac12\log\det(I + CAP_tA^\top C^\top N^{-1})$, value at least one-step part, and the scalar random walk's $0.135$ (one-step) and $0.162$ (whole future)
- committed: after
- outcome: confirmed
- recheck: $P_\infty = (\sqrt5-1)/2$; one-step $\tfrac12\log(1+P_\infty/2)$; value $\tfrac12\log(P_\infty/P_s)$ with $P_s = (1/P_\infty + 1/(1+P_\infty))^{-1}$

$0.13464$ and $0.16175$ nats. Write-up "What holds".

## C3 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: rederive
- line: derivation
- criterion: Item (c): positivity by strict concavity; $+\infty$ under recurrence (joint not absolutely continuous with respect to product); every pair qualifies under full-support rows; the deterministic-successor exit is pointwise; one-step decay $(K-1)/(2n)$
- committed: after
- outcome: confirmed
- recheck: re-derive; recurrence from $\min_{s',a'} T(s \mid s',a') \gt 0$ a.s.

Clarke–Barron used as cited, not re-derived. Write-up "What holds".

## C4 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: rederive
- line: derivation
- criterion: Item (g): finality for the law part; the whole-target inequality $I(S_s;F_s \mid \mathcal C_s) \leq I(S_t;F_s \mid \mathcal C_s) + \sum_{k\geq s} r_k$; and the clocked counterexample (out before the report time, in from it)
- committed: after
- outcome: confirmed
- recheck: bound $I(S_s; o_{k+1} \mid S_t, \mathcal C_k, a_k) \leq r_k$ via $S_k$ and the Markov property

Holds as written. It rests on the policy-uniform reading of the cut (C11). Write-up "What holds".

## C5 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: run
- line: derivation
- criterion: Item (g′): the identity $I(S_t;F_t \mid \mathcal C_t) + \sum r_k = \sum u_k$ in $[0,\infty]$, its three consequences, and the linear-Gaussian renewal (filter restarted at $\tilde P_t = 0$), with $\sum_k (u_k - r_k) = 0.162$ for the scalar random walk
- committed: after
- outcome: confirmed
- recheck: iterate $\tilde P$ from $0$, sum $u_\infty - r_k$; separately sum $I(x_t; o_{k+1} \mid \mathcal C_k)$ from the joint covariance of $(x_t, x_k)$

Both routes give $0.16175$. Write-up "What holds".

## C6 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: rederive
- line: derivation
- criterion: Items (h) and (h′): null sets only; support only under the finiteness hypotheses (spot-check of the three support facts and the finite-block reduction); the clock-and-rationals counterexample
- committed: after
- outcome: confirmed
- recheck: the change-of-measure density is $\mathbb E[f \mid S_t, \mathcal C_t]$; each support fact needs only second countability

Write-up "What holds"; (h′)'s hypothesis wording is F1.

## C7 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: rederive
- line: derivation
- criterion: The housing result: Markov twin, policy-free kernel, noiseless channel, equal sequence laws as a $\pi_0$ mixture, twin out
- committed: after
- outcome: confirmed
- recheck: Bayes-filter recursion is policy-free under chronica-measurable policies

Write-up "What holds".

## C8 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: run
- line: derivation
- criterion: Numbers and examples in Discussion and Epistemic Status: $\log 2 - \tfrac12$ for a fresh uniform row; $x_{t+1} = -x_t$ one-step part like $1/(2t)$ with infinite value; doubling map $\log 2$ per step with no renewal; the part-of-target counterexample ($\infty$ against $\tfrac12\log\tfrac32$) and the step of (g′) that fails for it
- committed: after
- outcome: confirmed
- recheck: closed forms in the write-up

$0.1931$; $\tfrac12\log(1+1/(1+t))$; $0.2027$. For $z$ alone, $z_k = 0$ does not screen $o_{k+1} = w + v$ off from $z_1 = w$. Write-up "What holds".

## C9 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: read-check
- line: derivation
- criterion: "Why the future stream": the one-step part is at most term (ii′) of #deriv-mismatch-budget-attribution Proposition 3 by data processing, and $A = 0$ makes (ii′) positive with the predicate zero
- committed: after
- outcome: confirmed
- recheck: (ii′) at $t+1$ is $I(o_{t+1}; S_{t+1} \mid \mathcal C_t, a_t)$; Markov chain $S_t \to S_{t+1} \to o_{t+1}$ given $(\mathcal C_t, a_t)$

Write-up "What holds".

## C10 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: read-check
- line: derivation
- criterion: Does any live segment, NOTATION row, terminology entry, OUTLINE row or INTRODUCTION sentence that cites this scope still state the replaced predicate, or a reading that disagrees with the current one?
- committed: after
- outcome: confirmed
- recheck: grep `0*-core/`, NOTATION, terminology, OUTLINE, INTRODUCTION for `scope-adaptive-system`, `H(\Omega`, `\mathcal O = \emptyset`

None do. Exceptions noted as F2 (this segment's own Working Notes) and F6 (two terminology pointers). Write-up "What holds".

## C11 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: rederive
- line: derivation
- criterion: Is the invariance cut ("stays the same along the whole run, almost surely") fixed under every continuation the predicate ranges over, as the Markov commitment, (g)'s "because $\theta$ is invariant", and (g′)'s "the law never renews" require?
- committed: after
- outcome: narrowed
- recheck: the lever example: $c$ constant under the agent's own (waiting) policy, redrawn by a continuation that presses, seen through a 0.1 flip channel

The text names no policy for "the run". Read as the run the agent's own policy produces, a variable some continuation can change is named into $\theta$. Then either $\theta$'s component renews ($r_k \gt 0$ after the press, so "the law never renews" is false), or $S_k$ omits the current value and the Markov commitment fails. Membership is unaffected. All three statements hold under the policy-uniform reading, which `#disc-structural-imagination`:54 already assumes ("$\theta$ holds only what no action changes"). Replacement sentence, and the NOTATION row: write-up C11.

## C12 (check)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5
- act: rederive
- line: derivation
- criterion: Epistemic Status: do the conditions make mismatch, gain, tempo and persistence statements "about adapting to a world rather than about chance or the agent's own errors" at the times a result applies them?
- committed: after
- outcome: narrowed
- recheck: invariant hidden bit $b$, clock state, observations constant except $o_K = b$; terms (ii) and (ii′) at steps before $K$

The loop is in at every $t \lt K$, while terms (ii) and (ii′) are zero at every step before $K$. Exact replacement: in at $t$ implies that, under some continuation, (ii′) is positive at some later step $k+1$, via (g′) and data processing. The stronger "(ii′) positive at $t+1$" is refuted by the same example. Replacement text: write-up C12.

## F1 (finding)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5

$\theta$ is typed twice: as the kernel pair $(\theta_T, \theta_h)$ (Definition paragraph) and as the declared variables the cut finds invariant (cut paragraph; item (b)'s constant coordinate). NOTATION's row carries both readings. (h′)'s hypothesis "$\theta$, the tuple of kernel entries" does not cover an invariant finite coordinate named into $\theta$; the proof survives with it discretely topologized. Two repairs, either of which leaves membership unchanged: write-up F1.

## F2 (finding)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5

The Working Notes' "Incidental audit gold" offers, unmarked, candidate Brief prose ("$H(\Omega_t \mid \mathcal C_t) = 0$ is an omniscient agent", false of tabular RL by item (c)), a candidate Discussion and a candidate figure built on the $\mathcal O = \emptyset$ and $H(\Omega_t \mid \mathcal C_t) = 0$ walls, and a readers-ask item on the "$\mathcal O = \emptyset$ exclusion". Their neighbors carry Landed/Resolved/Answered markers, so these read as current. A promotion pass would reintroduce the replaced predicate at the front door. The "Integration record" subsection's first line is history. Write-up F2.

## F3 (finding)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5

Two places in the body use change-chronicle voice: the heading "What the old exclusion got right and wrong", and the housing result's "the state-only predicate it replaces". The content is domain content, so this is a change of register and not of status. Candidate wording: write-up F3.

## F4 (finding)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5

Smaller precision points:

- "has then become a planner" and "a planner handed its true law is out" hold only with the state observed;
- the intro's three ways to be outside overlap and combine;
- "$u_k - r_k$" is $\infty - \infty$ when a noiseless channel reports a fresh continuous draw (write $I(S_t; o_{k+1} \mid \mathcal C_k, a_k)$);
- the display sentence defines the set where it means membership in it;
- the doubling map's "starting point" is $x_t$, not $x_1$.

Write-up F4.

## F5 (finding)
- target: segment:example-kalman
- at: 3f3b4ca5

$y_t = x_t + n_t^{(a_t)}$ and "$P(y_t \mid do(a_t))$" make the observation at $t$ depend on $a_t$. #def-observation-function has $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$, and #def-chronica orders $a_{t-1}$ before $o_t$. Re-index to $a_{t-1}$. No verdict changes. Write-up F5.

## F6 (finding)
- target: segment:scope-adaptive-system
- at: 3f3b4ca5

`terminology/entries/cycle.md` and `loop.md` name this segment as `primary_source` and send readers here for "the cycle as the operational unit of an adaptive system" and "the loop as the defining feature of adaptive systems". The segment does not carry either. `LEXICON.md` is generated from these entries. Write-up F6.
