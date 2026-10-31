---
kind: review
author:
  name: Claude Opus 5.5 (A.1 check 8)
  role: independent checker
sources:
  - spikes/epistemic-target-ontology/17-check-8.md
written: 2026-10-30
---

# #scope-adaptive-system after merge 3d17de13, with #def-observation-function and Proposition 1(ii): check 8

KR **A.1** (`msc/inside-out-2026-10/INTENT.md`). I re-derived the scope's items from the three segments at `3d17de13` before reading any earlier write-up, having seen only the ledger's one-line summaries of open findings. Midway I read `16-check-7-integration.md` and the earlier records' findings, to dispose of them. This is a checker's read, not the cold read the KR names. Derivations, numbers and replacement text are in the write-up named above. The items listed here are this record's content. Silence about a part means only that I found nothing there.

## C1 (check)
- target: segment:scope-adaptive-system
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: Condition 1 implies condition 2; averaged-in iff pointwise-in at some positive-probability history (discrete histories); items (a), (d), (e), (f)
- committed: after
- outcome: confirmed
- recheck: chain rule over the stream; actions are functions of the history and independent randomness; the continuation may be chosen per history; a coordinate no continuation's future depends on adds zero by the chain rule
- read: segment:scope-adaptive-system, segment:def-chronica, segment:def-observation-function, segment:def-action-transition

## C2 (check)
- target: segment:scope-adaptive-system
- at: 3d17de13
- act: run
- line: simulation
- criterion: Item (b) for a cold reader's Kalman filter: the criterion $C A^j P_t \neq 0$, the one-step formula, and for the scalar random walk the one-step part $0.135$ and the whole-future value $0.162$ nats; (g′)'s renewal from $\tilde P_t = 0$ rising to $0.135$ with $\sum_k (u_k - r_k) = 0.162$
- committed: after
- outcome: confirmed
- recheck: Gaussian conditioning (cross-covariance $P_t (A^j)^\top C^\top$); a 200-step script: $P_\infty = 0.61803$, one-step $0.13464$, Rauch–Tung–Striebel steady smoothed variance $1/\sqrt5$, value $0.16175$, renewal $0, 0.1116, 0.1312, 0.1341, \ldots$, $\sum (u_k - r_k) = 0.16175$
- read: segment:scope-adaptive-system, segment:def-observation-function, segment:def-action-transition

## C3 (check)
- target: segment:scope-adaptive-system
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: Item (c): the observed-state test under any $\pi_0$ and its twin when the history fixes the state; the lemma; Dirichlet rows never fixed; deterministic successor maps exit pointwise; infinite value under recurrence; reward in the observed state; the real-reward bandit's two mutually singular declarations with the same weak support
- committed: after
- outcome: confirmed
- recheck: $I(S_t; F_t \mid \mathcal C_t) = I(\theta; F_t \mid \mathcal C_t)$ when $\Omega_t$ is $\mathcal C_t$-measurable; chain rule; the draw depends on $\theta$ only through its row; the lemma on a countable generating $\pi$-system with Dynkin, so no finiteness is used; the joint charges the graph of the limit-frequency map, the product does not; $\sqrt 2 (1/m - 1/n) \notin \mathbb Q$; the $Q_m$ are weakly dense; a Dirichlet process with a base that is not finitely supported is a.s. infinitely supported
- read: segment:scope-adaptive-system, segment:def-action-transition, segment:def-observation-function

## C4 (check)
- target: segment:scope-adaptive-system
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: (g)'s law part and its whole-target bound; the clocked example (out for $t \leq K - 2$, in at $K - 1$); (g′)'s identity and its three consequences; the Epistemic Status's part-only counterexample ($\infty$ against $\tfrac12 \log \tfrac32$)
- committed: after
- outcome: confirmed
- recheck: chain rule split at $s$; $I(S_s; F_s \mid S_t, \mathcal C_s) \leq \sum_{k \geq s} r_k$ by data processing through $S_k$; state $(t, y_t, y_{t-1})$ with $o_j = y_{j-1}$ for $j \geq K$; two-order chain rule on $I(S_t, S_k; o_{k+1} \mid \mathcal C_k, a_k)$; posterior variance $\tfrac12$ after $o_1$
- read: segment:scope-adaptive-system, segment:def-action-transition, segment:def-observation-function

## C5 (check)
- target: segment:scope-adaptive-system
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: (h) (only null sets matter) and (h′) (in finite worlds only the support), its four facts and its rationals counterexample; the Definition's full-support declaration giving $\operatorname{supp} \pi_0 = \overline W$
- committed: after
- outcome: confirmed
- recheck: the conditional law of $F_t$ given $(S_t, \mathcal C_t)$ is unchanged by an equivalent reweighting, and a.s.-measurability in $\mathcal C_t$ survives an equivalent change; $\operatorname{supp}(L\mu) = \overline{\operatorname{supp}\mu \cap \{L \gt 0\}}$ (both inclusions); a continuous map is constant a.e. iff it is constant on the support; the projection of a compact support is closed and equals the image's support
- read: segment:scope-adaptive-system

## C6 (check)
- target: segment:scope-adaptive-system
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: The housing result: the twin is Markov with a policy-free kernel and a noiseless channel, matches the original's action–observation law under every policy as a $\pi_0$ mixture, and is a case-(d) loop
- committed: after
- outcome: confirmed
- recheck: the Bayes predictive is a function of the posterior over $S_t$ and $a_t$ by fresh noise and fresh transitions; the posterior is policy-free; the twin's state is $\mathcal C_t$-measurable with known law; the twin's own transition is fresh
- read: segment:scope-adaptive-system

## C7 (check)
- target: segment:scope-adaptive-system
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: Non-vacuity: under some continuation the (ii′) terms after $t$ sum to at least that continuation's value plus the renewals, using fresh noise only; under the agent's own policy the statement holds in the sufficient direction only; the hidden-bit witness; the Discussion's one-step comparison and its $A = 0$ converse
- committed: after
- outcome: confirmed
- recheck: fresh noise gives $o_{k+1}$ independent of $(S_t, S_k)$ given $(S_{k+1}, \mathcal C_k, a_k)$; data processing; chain rule in $(S_t, S_k)$; with $A = 0$, (ii′) is positive while the value and every $r_k$ are zero, so "exactly when" would be false
- read: segment:scope-adaptive-system, segment:def-observation-function, segment:deriv-mismatch-budget-attribution

## C8 (check)
- target: segment:scope-adaptive-system
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: "Two kinds of warrant": $\log 2 - \tfrac12 \approx 0.193$ nats per fresh uniform two-successor row; $x_{t+1} = -x_t$ has a one-step part falling like $1/(2t)$ with infinite value; the doubling map shows $\log 2$ per step and renews nothing
- committed: after
- outcome: confirmed
- recheck: $\mathbb E\, H_b(p) = \tfrac12$ for uniform $p$; posterior variance $1/(t+1)$; $S_k$ is a function of $S_t$ for the doubling map, so $r_k = 0$
- read: segment:scope-adaptive-system

## C9 (check)
- target: segment:def-observation-function
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: The kernel's definition and the mixture warning; fresh noise with fresh transitions makes the run's law a product, so pairs $(h, \varepsilon)$ inducing one kernel are indistinguishable; the repeated-noise example
- committed: after
- outcome: narrowed
- recheck: product of kernels and policy; for $\varepsilon_t = \varepsilon_{t-1}$ and an additive channel, $o_t - o_{t-1}$ shows the state's change without noise
- read: segment:def-observation-function, segment:def-action-transition

The Formal Expression is right. The opening paragraph still uses the phrase the definition warns against (F3), and the fresh clause conditions on its own kernel only (F4).

## C10 (check)
- target: segment:deriv-mismatch-budget-attribution
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: Proposition 1(ii): the kernels $\hat o^{\mathrm B}$ and $u$ are policy-independent because the policy factors cancel from the posterior over the typed target $S_t = (\Omega_t, \theta)$, given the generation of the declared world by its kernels
- committed: after
- outcome: narrowed
- recheck: write the joint over $(\mathcal C, \Omega_{1:t}, \theta)$ with factor $\pi_0(\Omega_1, \theta)$; the policy factors are constant in the hidden variables given $\mathcal C$; $a \sim \pi(\cdot \mid \mathcal C)$ gives $p(S \mid \mathcal C, a) = p(S \mid \mathcal C)$
- read: segment:deriv-mismatch-budget-attribution, segment:scope-adaptive-system, segment:def-action-transition, segment:def-observation-function

The argument holds. The display omits $\theta$ and $\pi_0$, and indexes the run from 0 (F2).

## C11 (check)
- target: segment:scope-adaptive-system
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: KR A.1's cold-reader clause: can a reader settle membership on the page for a Kalman filter, for tabular RL, and for standard RL with continuous dynamics?
- committed: after
- outcome: narrowed
- recheck: (b) settles the Kalman filter and (c) tabular RL; (c)'s test is exact for continuous observed-state loops but leaves open which declarations put them in; the dominated, atomless-row condition of F1 settles the usual case
- read: segment:scope-adaptive-system, segment:def-action-transition, segment:def-observation-function

F1.

## F1 (finding)
- target: segment:scope-adaptive-system
- at: 3d17de13

For KR A.1's RL reader, (c) wants one sufficient condition for continuous dynamics. Suppose that, for $\pi_0$-almost every law, every row has a density with respect to one $\sigma$-finite measure. Then the posterior of $\theta$ is absolutely continuous with respect to its law under $\pi_0$, so a row's posterior can be a point mass only at an atom of that row's law under $\pi_0$. The loop is therefore in whenever the current state has an action whose row is atomless under $\pi_0$. This covers laws tied across states: $s_{t+1} = A s_t + B a_t + w_t$ with Gaussian $w_t$ and a Gaussian prior on $(A, B)$ is in at every $t$. Both hypotheses are needed, and (c) already shows how each one fails. Noiseless rows are not dominated, and one transition fixes a scalar $A$. The atomic bandit is dominated, by counting measure on a countable set, and fails by its atoms. Proposed text: write-up F1.

## F2 (finding)
- target: segment:deriv-mismatch-budget-attribution
- at: 3d17de13

Proposition 1(ii) writes the factorization as $\mathbb P_\pi(\mathcal C, \Omega_{0:t})$. The posterior from which it cancels the policy is over $S_t = (\Omega_t, \theta)$, so the joint should be over $(\mathcal C, \Omega_{1:t}, \theta)$, with the factor $\pi_0(\Omega_1, \theta)$ named among the environment factors. The run starts at $\Omega_1$, not $\Omega_0$. Within the Proposition, $\Omega$ also switches between the typed target and the state process. Replacement text: write-up F2.

## F3 (finding)
- target: segment:def-observation-function
- at: 3d17de13

The opening paragraph (line 15) calls the observation kernel "the conditional law of $o_t$ given state and action". The Formal Expression (line 33) says that phrase names the mixture over $\theta_h$, not the kernel. This is the one site check-7 F4's revision missed. Proposed: "the law of $o_t$ given state and action that $h$ and the noise induce".

## F4 (finding)
- target: segment:def-observation-function
- at: 3d17de13

The fresh-noise clause conditions on $(\Omega_t, a_{t-1})$ and the observation kernel. #def-action-transition's fresh-transition clause conditions on $(\Omega_t, a_t)$ and $T$. Neither names the other kernel, which is not "earlier in the run". #scope-adaptive-system's cut paragraph reads both "with the law held fixed", and (g′), (h) and Proposition 1(ii) need independence given the whole $\theta$. The step is left to the reader. Proposed in both definitions: "given … and the law $\theta$".

## F5 (finding)
- target: segment:scope-adaptive-system
- at: 3d17de13

Small points. "Two kinds of warrant": the value $\log 2 - \tfrac12$ needs two-successor rows; "a fresh two-successor row" says it. The Definition declares $\pi_0$ on $(\Omega_1, \theta)$ before the cut sorts the variables, and the cut uses $\pi_0$'s path law to sort them. There is no circle in substance, since the cut only labels, but a cold reader may see one. A clause would forestall it: "$\pi_0$ on the declared world's initial variables, split into $\Omega_1$ and $\theta$ by the cut below".
