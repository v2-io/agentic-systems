# Check 8: `#scope-adaptive-system` after merge `3d17de13`, with `#def-observation-function` and Proposition 1(ii)

KR **A.1** (`msc/inside-out-2026-10/INTENT.md`): "`#scope-adaptive-system` carries the typed predicate or a defended alternative, and a cold reader checks the membership clauses on standard RL and on a Kalman filter." Top intent, Joseph's: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."

Typed record: `reviews/scope-adaptive-system-check-8.md`. Author: Claude Opus 5.5, A.1 check 8.

## How this was done, and what that costs

I read `#scope-adaptive-system` and `#def-observation-function` whole at `3d17de13`, `#def-action-transition` whole, the Formal Expression of `#def-chronica`, and the Setting and Propositions 1 and 3 of `#deriv-mismatch-budget-attribution`. I did not read `#def-agent-environment`. Before reading any earlier write-up I re-derived the scope's items from the page, but I had already seen the ledger's one-line summaries of the open findings (`vsect open`). Midway, the lead asked me to dispose of check 6's and check 7's findings, and I then read `16-check-7-integration.md` whole and the finding and narrowed-check items of the check-6, check-7 and reread-1 records. So this is a checker's read of landed text by a reader who had seen the ledger's summaries, not the cold read the KR names. Every item below was re-derived or run, and the record's `act:` fields say which.

## Verdict

The scope holds up at `3d17de13`. Every membership item I re-derived is correct as written:

- the predicate and its two conditions, items (a)–(h′), and the housing result;
- the non-vacuity statement and its own-policy form;
- the constants in (b), (g′) and "Two kinds of warrant".

A cold reader can check the KR's two cases on the page: item (b) for a Kalman filter, item (c) for tabular reinforcement learning. Item (c)'s new test also settles any observed-state loop exactly, under any $\pi_0$.

Findings:

- **F1 (strengthening, for the KR's RL reader).** The test in (c) is exact but leaves the RL reader with continuous dynamics asking which declarations of $\pi_0$ put the loop in. One sufficient condition settles the usual case, including laws tied across states, such as unknown linear dynamics: rows dominated by one measure, and a row whose law under $\pi_0$ has no atom. Its two hypotheses are the two ways (c)'s examples exit: deterministic rows are not dominated, and the atomic bandit has atoms. Proposed text below.
- **F2.** Proposition 1(ii) of `#deriv-mismatch-budget-attribution` writes its factorization over $(\mathcal C, \Omega_{0:t})$. The posterior it then cancels the policy from is over $S_t = (\Omega_t, \theta)$, so the display needs $\theta$ and the factor $\pi_0(\Omega_1, \theta)$, and the run starts at $\Omega_1$, not $\Omega_0$. The argument is right; the display says less than it uses.
- **F3.** `#def-observation-function`'s opening paragraph still calls the observation kernel "the conditional law of $o_t$ given state and action". Its own Formal Expression now says that phrase names the mixture over $\theta_h$, not the kernel. This is check-7 F4 at the one site the revision missed.
- **F4.** The fresh-noise and fresh-transition clauses each condition on their own kernel only. The scope's cut paragraph reads both "with the law held fixed", and (g′), (h) and Proposition 1(ii) need independence given the whole law. The text leaves that step to the reader. Two words in each definition would carry it.
- **F5.** Two small points in the scope.

## What holds (re-derived)

**Conditions and the averaged predicate.** With $\lvert \mathcal O \rvert = 1$, $F_t$ holds only actions and a constant. Actions are functions of the history and independent randomness, so $I(S_t; F_t \mid \mathcal C_t) = 0$, and condition 1 implies condition 2. For discrete histories, "in" is equivalent to "pointwise-in at some history of positive probability", because the continuation may be chosen per history. Items (a), (d), (e) and (f) are immediate. For (f), a coordinate on which no continuation's future depends adds zero by the chain rule.

**(b), the Kalman filter.** $o_{t+j} = C A^j x_t$ plus noise independent of $(x_t, \mathcal C_t)$, so the cross-covariance given $\mathcal C_t$ is $P_t (A^j)^\top C^\top$, and jointly Gaussian variables are independent exactly when it vanishes. The one-step part is $\tfrac12 \log\det\big(I + C A P_t A^\top C^\top N^{-1}\big)$. Scalar random walk with unit variances, run to steady state:

- $P_\infty = (\sqrt5 - 1)/2$, so the one-step part is $\tfrac12 \log(1 + P_\infty / 2) = 0.13464$ nats;
- the smoothed variance at steady state (Rauch–Tung–Striebel) is $1/\sqrt5$, so the whole-future value is $\tfrac12 \log(\sqrt5\, P_\infty) = 0.16175$ nats;
- the renewal of (g′), from $\tilde P_t = 0$, runs $0, 0.1116, 0.1312, 0.1341, \ldots \to 0.13464$, and $\sum_k (u_k - r_k) = 0.16175$ over 200 steps.

All match the segment.

**(c), observed state.** Since $\Omega_t$ is a function of $\mathcal C_t$, $I(S_t; F_t \mid \mathcal C_t) = I(\theta; F_t \mid \mathcal C_t)$. The chain rule with zero action terms makes this $\sum_{k \geq t} \mathbb E\, I(\theta; o_{k+1} \mid \mathcal C_k, a_k)$. Given $(\theta, \mathcal C_k, a_k)$, the draw $o_{k+1}$ depends on $\theta$ only through its row, so each term is the information the draw carries about the row. The lemma ($I(K; X) = 0$ for $X \mid K \sim K$ forces $K$ to be a.s. the marginal, on a countable generating $\pi$-system and then by Dynkin) holds on any standard Borel observation space. So the test does not use finiteness. The twin for "the history fixes the state" holds because $o_{k+1}$ is independent of $\theta$ given its own conditional law.

The instances check out:

- Dirichlet rows are never fixed.
- Deterministic successor maps exit pointwise.
- $+\infty$ under recurrence: the joint law charges the graph of the limit-frequency map, which the product of the marginals gives measure zero.
- Full-support Dirichlet rows make every pair recur on a finite state space.
- In the bandit, $\sqrt 2 (1/m - 1/n) \notin \mathbb Q$ for $m \neq n$, so the supports are disjoint and the first reward fixes $m$.
- The $Q_m$ are weakly dense, because each rational finitely supported law recurs with shifts tending to zero.
- The Dirichlet process (base not finitely supported) is a.s. infinitely supported, so the two measures are mutually singular.

**(g) and (g′).** The law part of (g) follows from the chain rule split at $s$ and invariance. The bound on the whole target holds: $I(S_s; F_s \mid \mathcal C_s) \leq I(S_t; F_s \mid \mathcal C_s) + I(S_s; F_s \mid S_t, \mathcal C_s)$, and each term of the second piece is at most $r_k$ by data processing through $S_k$. The clocked example, with state $(t, y_t, y_{t-1})$ and $o_j = y_{j-1}$ for $j \geq K$, is out for $t \leq K - 2$ and in at $K - 1$. (g′) is the two-order chain rule on $I(S_t, S_k; o_{k+1} \mid \mathcal C_k, a_k)$. The part-only counterexample in the Epistemic Status gives $I(z_1; F_1 \mid \mathcal C_1) = \infty$ against one-step parts summing to $\tfrac12 \log \tfrac32$ (posterior variance $\tfrac12$ after $o_1$).

**(h) and (h′).** For (h): the conditional law of $F_t$ given $(S_t, \mathcal C_t)$ is unchanged by an equivalent reweighting of $\pi_0$, and "it is a.s. a function of $\mathcal C_t$" survives an equivalent change of the law of $(S_t, \mathcal C_t)$. For (h′), each of the four facts holds:

- $\operatorname{supp}(L \mu) = \overline{\operatorname{supp} \mu \cap \{L \gt 0\}}$, both inclusions using second countability;
- "constant a.e." is the same as "constant on the support", for a continuous map;
- a history has positive probability iff the open set $\{L \gt 0\}$ meets the support;
- the projection of a compact support is closed and is the support of the image.

The rationals counterexample is right, and the full-support requirement in the Definition is what makes "the declared set fixes membership" true.

**Housing.** The twin's kernel is a fixed function, because the Bayes posterior is policy-free. Its predictive matches the original given every history, so the laws of action–observation sequences agree under every policy, and the twin's state is a function of $\mathcal C_t$ with known law: case (d). The twin's transition is itself fresh, so it is a declared world in the segment's own sense.

**Non-vacuity.** Fresh noise alone makes $o_{k+1}$ independent of $(S_t, S_k)$ given $(S_{k+1}, \mathcal C_k, a_k)$. Then (ii′) at $o_{k+1}$ is at least $I(S_t; o_{k+1} \mid \mathcal C_k, a_k) + r_k$, and these sum to the value plus the renewals. Under the agent's own policy the statement is correctly one-directional. The converse "exactly when" that check 6 once proposed is false: with $A = 0$, (ii′) is positive while the value and every $r_k$ are zero. The hidden-bit witness is right.

**"Two kinds of warrant".** A fresh uniform Bernoulli row carries $\log 2 - \tfrac12 = 0.19315$ nats per step. For $x_{t+1} = -x_t$ the posterior variance is $1/(t+1)$, so the one-step part falls like $1/(2t)$. The doubling map read through its first digit shows $\log 2$ per step with $S_k$ a function of $S_t$, so it renews nothing.

**`#def-observation-function`.** I checked:

- the kernel's definition and the mixture warning;
- the fresh-noise clause, which with fresh transitions makes the run's law a product, so pairs $(h, \varepsilon)$ with one kernel are indistinguishable;
- the repeated-noise example ($o_t - o_{t-1}$ shows the state's change without noise for an additive channel).

All are correct.

**Proposition 1(ii).** The cancellation argument is right once the joint includes $\theta$ (F2): the policy factors are constant in the hidden variables given $\mathcal C$, and the posterior given $(\mathcal C, a)$ equals the posterior given $\mathcal C$, because $a \sim \pi(\cdot \mid \mathcal C)$.

## F1. A sufficient condition for continuous RL

**Why it is wanted.** KR A.1's cold reader checks membership "on standard RL". (c)'s test is exact, but for a continuous-state learner it asks whether the posterior of a row at the current state can be a point mass, and (c) shows that the answer depends on the declaration. A reader with $s_{t+1} = f(s_t, a_t) + w_t$ and an unknown $f$ wants to know which declarations put the loop in.

**The condition.** Suppose that for $\pi_0$-almost every law, every row has a density with respect to one $\sigma$-finite measure on the state space, jointly measurable in the law and the successor. Then the posterior of $\theta$ given any history is absolutely continuous with respect to its law under $\pi_0$, by Bayes' formula with densities. Its image under the map from $\theta$ to the row at $(s, a)$ is absolutely continuous with respect to that row's law under $\pi_0$. A point mass can be absolutely continuous with respect to a measure only at one of its atoms. So: **in a dominated model, a row's posterior can be a point mass only at an atom of the row's law under $\pi_0$.** By (c)'s test, the loop is in at $t$ if, with positive probability, the current state has an action whose row has an atomless law under $\pi_0$.

**Why it covers tied laws.** The condition is stated on $\theta$, not on rows taken one at a time. With rows independent across a continuous state space, the current state has never been visited, so the test is passed trivially. That is not the RL case. The usual case shares parameters. For $s_{t+1} = A s_t + B a_t + w_t$ with Gaussian $w_t$ and a non-degenerate Gaussian prior on $(A, B)$:

- the row at $(s, a)$ is $\mathcal N(A s + B a, Q)$, dominated by Lebesgue measure;
- its law under $\pi_0$ is that of $A s + B a$, which is Gaussian and atomless whenever $(s, a) \neq 0$;
- so the learner is in at every $t$, since any continuation that takes $a \neq 0$ passes the test.

**Both hypotheses are needed, and (c) already exhibits the two failures.**

- *Domination.* With $w_t = 0$ and $B = 0$ known, scalar $A$ under a Gaussian prior: the rows are point masses at different successors, no $\sigma$-finite measure dominates them, and one transition from $s \neq 0$ fixes $A$. This is the continuous form of (c)'s deterministic successor maps.
- *No atoms.* The bandit's atomic declaration is dominated, by counting measure on the countable set $\bigcup_m (\mathbb Q + \sqrt 2 / m)$. It exits because its law has atoms, $Q_m$ with probability $2^{-m}$.

The Dirichlet-process bandit is in for a different reason: it is not dominated, but its posterior is again a Dirichlet process. So the condition is sufficient, not necessary.

Both hypotheses are null-set properties of $\pi_0$, since equivalent measures have the same atoms. They sit inside (h) and make concrete (c)'s sentence that "the declaration does work that the set of possible worlds cannot".

**Proposed text**, for (c) after the bandit and before "By (h), membership is the same…":

> One sufficient condition settles the usual continuous case. Suppose that, for $\pi_0$-almost every law, every row has a density with respect to one $\sigma$-finite measure on the state space, as for dynamics with additive Gaussian noise. Then the posterior of $\theta$ given a history is absolutely continuous with respect to its law under $\pi_0$, and so is the posterior of each row. A row's posterior can then be a point mass only at an atom of that row's law under $\pi_0$, and the loop is in at $t$ whenever, with positive probability, the current state has an action whose row has an atomless law under $\pi_0$. For $s_{t+1} = A s_t + B a_t + w_t$ with Gaussian $w_t$ and a non-degenerate Gaussian prior on $(A, B)$, the row at $(s, a)$ is atomless whenever $(s, a) \neq 0$, so the learner is in at every $t$. Both hypotheses are needed. With $w_t = 0$ the rows are point masses that no measure dominates, and one transition from $s \neq 0$ fixes a scalar $A$. The bandit's atomic declaration is dominated, by counting measure on the union of the countable supports, and fails by its atoms.

The integrator might also mention this in the Epistemic Status's list of what is derived. It is a short computation from Bayes' formula, at the same tier as the rest.

## F2. Proposition 1(ii)'s factorization display

`#deriv-mismatch-budget-attribution`, line 44: "(ii) The joint law factorizes as $\mathbb P_\pi(\mathcal C, \Omega_{0:t}) = \big[\prod_{s \lt t} \pi(a_s \mid \mathcal C_s)\big] \cdot \big[\text{environment and channel factors}\big]$." The Setting defines $\Omega := S_t = (\Omega_t, \theta)$, and the derivation cancels the policy from "the posterior $p(\Omega \mid \mathcal C, a)$", the posterior over the typed target. So the joint must include $\theta$ and the factor $\pi_0(\Omega_1, \theta)$; otherwise the display does not show that the posterior over the law is policy-free. Within the same Proposition, $\Omega$ also switches between the typed target (the Setting, the kernels) and the state process ($\Omega_{0:t}$). The world's first state is $\Omega_1$ (`#scope-adaptive-system`, and `#def-chronica` starts at $o_1$), so the index 0 is off by one. A grep of `01-aat-core/src` finds $\Omega_{0:\cdot}$ only here.

Proposed: "(ii) Writing $\Omega_s$ here for the state process, the joint law factorizes as $\mathbb P_\pi(\mathcal C, \Omega_{1:t}, \theta) = \big[\prod_{s \lt t} \pi(a_s \mid \mathcal C_s)\big] \cdot \big[\pi_0(\Omega_1, \theta) \cdot \text{transition and channel factors at } \theta\big]$." Later in the paragraph, "constant in $\Omega_{0:t}$" becomes "constant in $(\Omega_{1:t}, \theta)$".

## F3. `#def-observation-function`, opening paragraph

Line 15: "What observations can teach it about that law is the conditional law of $o_t$ given state and action, the *observation kernel*…". Line 33 now defines the kernel as the law "that $h$ and the law of $\varepsilon_t$ induce" and warns that "the conditional law of $o_t$ given $(\Omega_t, a_{t-1})$ alone is then a mixture over it, not the kernel." The opening paragraph uses the very phrase line 33 warns against. Proposed: "…is the law of $o_t$ given state and action that $h$ and the noise induce, the *observation kernel*…". I disposed of check-7 F4 as answered, because the definition it targeted is fixed; this finding carries the residue.

## F4. The fresh clauses condition on their own kernel only

`#def-observation-function`: "given $\Omega_t$, $a_{t-1}$ and the kernel, $o_t$ is drawn from $p_h(\cdot \mid \Omega_t, a_{t-1})$ independently of everything earlier in the run (earlier states, observations and actions, …)". `#def-action-transition`: "given $\Omega_t$, $a_t$ and $T$, the next state … independently of everything earlier in the run". Neither lists the *other* kernel, which is not "earlier in the run". Under the generative reading, a world drawn from its kernels, this is harmless. But as worded, the transition clause does not exclude $\Omega_{t+1}$ depending on $\theta_h$ given $(\Omega_t, a_t, \theta_T)$, which would happen if $\pi_0$ correlates the two kernels and the world uses the correlation. The scope's cut paragraph states the needed form, "given $(S_t, a_t)$ … each read with the law held fixed". (g′), (h)'s first step and Proposition 1(ii) all condition on the whole $\theta$. Proposed, in each definition: "given $\Omega_t$, $a_{t-1}$ and the law $\theta$" (respectively "given $\Omega_t$, $a_t$ and the law $\theta$"), with "drawn from its own kernel" kept. I found no case in canon that the gap breaks. It is a step the reader has to supply.

## F5. Small points in `#scope-adaptive-system`

- "Two kinds of warrant": "if each step reaches a fresh row of the transition law, whose parameter is independent and uniform, every one-step part is $\log 2 - \tfrac12$." The value needs rows with two successors. "A fresh two-successor row" says it.
- The Definition declares $\pi_0$ on $(\Omega_1, \theta)$ before the cut paragraph says which declared variables go into $\theta$, and the cut uses $\pi_0$'s path law to decide. A cold reader may see a circle. There is none in substance, because $\pi_0$ is a law on the declared world's initial variables and the cut only labels them, which the paragraph says ("the cut fixes labels"). One clause at the declaration, "on the declared world's initial variables, split into $\Omega_1$ and $\theta$ by the cut below", would forestall it.

## The ledger

**Disposed as answered.** Each was re-read against the text at `3d17de13`, by a mind other than the reviser of the answering revision:

- Check 6: C5/finding, C7/finding, F2, F3 and F4, all by `55f592c5` (commit `ed2b07e4`). On C7/finding: the landed own-policy statement is one-directional ("whenever"). That is the correct form, since the "exactly when" check 6 proposed is false, as the non-vacuity paragraph above shows.
- Check 7: F1 with its C8, F2 with its C10, F3 and F5, all by `aa9487fa`. Check 7's F4, by `3d4c1822` on `#def-observation-function`. F3 above carries F4's residue in the opening paragraph.
- Reread 1: F1 and F5, by `5e613630` (commit `cb79735b`) as carried forward.

On reread-1 F1 specifically: "answered" means the named class of worlds and the wrong-model filter. The hard-coded true guess and the pretrained design, two of the three cases it raised, are **not** settled in the segment. They live in `question:where-is-the-line-between-what-an-agent-s-design`, which states them and remains open.

**Confirmed as second mind.** Integration 7's C1–C5 had lapsed on its own reword `9fde935e` (commit `40754025`). That reword names (c)'s lemma's generating class as a $\pi$-system and adds Ferguson to the imported results. Neither touches what those checks tested, and I re-derived each on the current text, so I confirmed them as equivalent (`vsect confirm --from 6e778ade`).

**Not touched.** The other lapsed checks from earlier rounds that await `vsect confirm`, and the four open A.1 items.

## What I did not check

- Ferguson 1973 against the paper, and the belief-state and Bayes-adaptive citations (Åström 1965; Kaelbling, Littman & Cassandra 1998; Martin 1967; Duff 2002). Their relata items are open.
- The Clarke–Barron constant $(K - 1)/(2n)$, beyond its being the derivative of the $\tfrac{K-1}{2} \log n$ cumulative term.
- `#def-agent-environment`, which is in the scope's `depends:` and which I did not read.
- The four open A.1 items: tail $\sigma$-field, physical housing, compute-relative extension, four-term decomposition.
- Downstream readers of the observation kernel's old literal definition (the round-7 integrator also left this).

## On the brief

The brief gave the KR, the three segments and the coordination facts, and left the rest open, which fit. The lead's mid-run note about `--by-revision` made disposing of check 6's findings possible; without it I would have been unsure whether vsect would accept them.
