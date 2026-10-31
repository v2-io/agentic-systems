---
kind: review
author:
  name: Claude Opus 5.5 (A.1 check 7, bare brief)
  role: independent checker
sources:
  - spikes/epistemic-target-ontology/15-check-7.md
written: 2026-10-30
---

# #scope-adaptive-system with fresh noise and fresh transitions, at ed2b07e4: check 7

KR **A.1** (`msc/inside-out-2026-10/INTENT.md`). I re-derived everything from the three segments at `ed2b07e4` (unchanged at `162b941d`) before reading any earlier review. After that I read check 6's review record, and grepped check 6's write-up and integration notes for what they said about non-vacuity. Derivations, numbers and replacement text are in the write-up named above. The items listed here are this record's content. Silence about a part means only that I found nothing there.

## C1 (check)
- target: segment:scope-adaptive-system
- at: ed2b07e4
- act: rederive
- line: derivation
- criterion: Condition 1 implies condition 2; averaged-in iff pointwise-in at some positive-probability history (discrete histories); items (a), (d), (e), (f)
- committed: after
- outcome: confirmed
- recheck: chain rule; actions are functions of the history and independent randomness; choose the continuation per history
- read: segment:scope-adaptive-system, segment:def-chronica, segment:def-observation-function, segment:def-action-transition

## C2 (check)
- target: segment:scope-adaptive-system
- at: ed2b07e4
- act: run
- line: simulation
- criterion: Cold-reader Kalman check, item (b): the criterion $C A^j P_t \neq 0$; the one-step formula; scalar random walk one-step part $0.135$ and whole-future value $0.162$ nats; the renewal of (g′) from $\tilde P_t = 0$ rising to $0.135$ with $\sum_k (u_k - r_k) = 0.162$
- committed: after
- outcome: confirmed
- recheck: value by a route other than check 6's: future-only variance $P_\infty + 1$ (backward filter one step back), smoothed variance $1/\sqrt5$, value $\tfrac12 \log(\sqrt5 P_\infty) = 0.16175$; Gaussian conditioning on 50 future observations agrees to five places
- read: segment:scope-adaptive-system, segment:def-observation-function, segment:def-action-transition

## C3 (check)
- target: segment:scope-adaptive-system
- at: ed2b07e4
- act: rederive
- line: derivation
- criterion: Cold-reader tabular-RL check, item (c) as written: in at every finite $t$; $+\infty$ value under recurrence; full-support Dirichlet rows make every pair recur; the deterministic-successor exit is pointwise; reward in the observed state; bandit; Q-learner by (h′)
- committed: after
- outcome: confirmed
- recheck: $I = H(\bar p) - \mathbb E H(p)$ and strict concavity; the joint law charges the graph of the limit-frequency map while the product does not; irreducibility of the finite chain under positive rows
- read: segment:scope-adaptive-system, segment:def-observation-function, segment:def-action-transition

## C4 (check)
- target: segment:scope-adaptive-system
- at: ed2b07e4
- act: rederive
- line: derivation
- criterion: (g) (law part and whole-target bound, clocked example out for $t \leq K-2$ and in from $K-1$); (g′) identity, its three consequences, and the linear-Gaussian $r_k$; (h)
- committed: after
- outcome: confirmed
- recheck: data processing through $S_k$ under both fresh clauses; two-order chain rule on $I(S_t, S_k; o_{k+1} \mid \mathcal C_k, a_k)$; equivalent reweighting leaves $P(F_t \in \cdot \mid S_t, \mathcal C_t)$ unchanged
- read: segment:scope-adaptive-system, segment:def-chronica, segment:def-observation-function, segment:def-action-transition

## C5 (check)
- target: segment:scope-adaptive-system
- at: ed2b07e4
- act: rederive
- line: derivation
- criterion: (h′): the three support facts, the finite-block reduction, and the clock-and-rationals counterexample; the housing result (Markov twin, policy-free kernel, noiseless channel, agreement with the $\pi_0$-mixture, case (d), mutual singularity under a fixed law)
- committed: after
- outcome: confirmed
- recheck: each support fact re-proved in a second-countable space; $o_2 = 1\{x_1 \in \mathbb Q\}$ a.s. $0$ under Lebesgue and a fair coin under the half-atomic measure; the policy factors cancel from the posterior
- read: segment:scope-adaptive-system, segment:def-observation-function, segment:def-action-transition

Holds given the full-support declaration and a projection step the text leaves implicit (F3).

## C6 (check)
- target: segment:def-action-transition
- at: ed2b07e4
- act: rederive
- line: derivation
- criterion: Fresh-transition clause: coherent with the Markov commitment, without loss of generality as the Epistemic Status claims; the XOR example (Markov in its own past, fresh noise, yet $o_K \oplus o_1 = x$)
- committed: after
- outcome: confirmed
- recheck: $\varepsilon_1$ independent of $x$ makes the state's bit a fair coin given its own past; declaring remembered noise as state only adds coordinates, which by the chain rule can bring a loop in but never put it out
- read: segment:def-action-transition

## C7 (check)
- target: segment:def-observation-function
- at: ed2b07e4
- act: rederive
- line: derivation
- criterion: Fresh-noise clause and the product form of the run's law it gives with fresh transitions; the kernel-is-learnable sentence; the repeated-noise counterexample in the Epistemic Status
- committed: after
- outcome: confirmed
- recheck: product form given $\theta$ read "with the law held fixed"; $\varepsilon_t = \varepsilon_{t-1}$ keeps the one-step kernel, and $o_t - o_{t-1}$ shows the state's change noiselessly for an additive channel
- read: segment:def-observation-function, segment:def-action-transition

The kernel definition's literal reading is F4.

## C8 (check)
- target: segment:scope-adaptive-system
- at: ed2b07e4
- act: rederive
- line: derivation
- criterion: Which items use the run-wide property, and does a world that is Markov in its own past with noise independent of the chronica, but with a remembering transition, break all three of (g′), (h) and non-vacuity?
- committed: after
- outcome: narrowed
- recheck: non-vacuity from fresh noise alone: (ii′) at $o_{k+1} \geq I(S_t, S_k; o_{k+1} \mid \mathcal C_k, a_k) = I(S_t; o_{k+1} \mid \mathcal C_k, a_k) + r_k$, summed over $k \geq t$; #def-action-transition's XOR world at $t = 1$: value $\log 2$, all $u_k = r_k = 0$ ((g′) fails), (h)'s step fails at $1 \lt t \lt K$, $\sum$ (ii′) $= \log 2$ (non-vacuity holds); (ii′) as defined in Proposition 3 of #deriv-mismatch-budget-attribution
- read: segment:scope-adaptive-system, segment:def-action-transition, segment:def-observation-function

F1.

## C9 (check)
- target: segment:scope-adaptive-system
- at: ed2b07e4
- act: run
- line: simulation
- criterion: Discussion and Epistemic Status numbers: fresh uniform row $\log 2 - \tfrac12$; sign flip one-step part like $1/(2t)$ with infinite value; doubling map $\log 2$ per step with no renewal; part-of-target $\infty$ against $\tfrac12 \log \tfrac32$
- committed: after
- outcome: confirmed
- recheck: $2 \int_0^1 (-p \ln p)\, dp = \tfrac12$; $\tfrac12 \log(1 + 1/(t+1))$ at $t = 10, 100, 1000$; posterior variance $1/2$ after one unit-noise reading
- read: segment:scope-adaptive-system

## C10 (check)
- target: segment:scope-adaptive-system
- at: ed2b07e4
- act: rederive
- line: derivation
- criterion: Can a cold reader settle membership for standard RL with continuous states or real-valued rewards from (c) and (h)?
- committed: after
- outcome: narrowed
- recheck: observed-state criterion (in iff some continuation, with positive probability, acts where the row is not fixed by the history), from the chain rule and the lemma that $I(K; X) = 0$ for $X \mid K \sim K$ iff $K$ is a.s. constant; real-reward bandit under a Dirichlet process (in at every $t$) against a countable dense atomic family on disjoint countable sets (out from $t = 2$), same weak support
- read: segment:scope-adaptive-system, segment:def-action-transition

F2.

## F1 (finding)
- target: segment:scope-adaptive-system
- at: ed2b07e4

The cut paragraph says the run-wide property is used by "(g′) and (h), and the non-vacuity statement", and that "a channel or a transition that remembers something outside $\Omega_t$ … breaks all three". Non-vacuity needs only fresh noise: by data processing through $S_{k+1}$ and the chain rule, (ii′) at $o_{k+1}$ is at least $I(S_t; o_{k+1} \mid \mathcal C_k, a_k) + r_k$, and these sum to the value plus the renewals. A remembering transition with fresh noise, such as #def-action-transition's own XOR example, breaks (g′) and (h)'s step but not non-vacuity. Check 6's remembering channel breaks all three. The list of users is also incomplete: (g)'s whole-target bound, (h′)'s block-law step, the compressed housing twin and (c)'s draw step use the property too. Replacement text for the cut paragraph and for the Discussion's derivation: write-up F1.

## F2 (finding)
- target: segment:scope-adaptive-system
- at: ed2b07e4

For KR A.1's cold reader. Item (c) settles tabular RL, but gives no membership test for standard RL with continuous states or real-valued rewards; (h) says only that null sets decide. An exact criterion holds for every observed-state loop under any $\pi_0$: the loop is in at $t$ exactly when some continuation, with positive probability, takes an action whose row the history at that moment does not fix. And "not given its transition law" does not settle membership in continuous worlds: for a real-reward bandit, a Dirichlet-process $\pi_0$ gives in at every $t$, while a countable dense family of finitely supported laws on disjoint countable sets gives out once one reward is seen, with the same weak support. Proof, corollaries and replacement text for (c): write-up F2.

## F3 (finding)
- target: segment:scope-adaptive-system
- at: ed2b07e4

"The support of $\pi_0$ is the closure of the set of possible worlds" is stated as following from $\pi_0$ being "declared on" that set. A measure with $\pi_0(W) = 1$ can have a smaller support, so this is a requirement on the declaration, and (h′)'s "the declared set of possible worlds fixes membership" depends on it. The same applies to `NOTATION.md`'s $\pi_0$ row. Also, (h′) leaves implicit the step from $L \cdot \pi_0$ on $(\Omega_1, \Omega_t, \theta)$ to the posterior over $(\Omega_t, \theta)$; the step holds by compactness. Replacement text: write-up F3.

## F4 (finding)
- target: segment:def-observation-function
- at: ed2b07e4

The observation kernel is defined as "the conditional law of $o_t$ given $\Omega_t = \omega$ and $a_{t-1} = a$". Under $\pi_0$ with $\theta_h$ random, that is the mixture over $\theta_h$, not the kernel the fresh-noise clause conditions on. The scope's gloss ("that $h$ and $\varepsilon_t$ jointly induce") is the right reading. Replacement text: write-up F4.

## F5 (finding)
- target: segment:scope-adaptive-system
- at: ed2b07e4

Small points. (g)'s "leaving need not be final" introduces an example that is never in first; "being out need not be final" fits it. In (c), "and has at least two possible successors" is implied by "not a.s. constant". In #def-observation-function's "Channels with memory", a memory that never changes goes into $\theta_h$ by the invariance cut, not into $\Omega_t$. Write-up F5.
