# Check 7: `#scope-adaptive-system` with its two new definitions, at `ed2b07e4`

KR **A.1** (`msc/inside-out-2026-10/INTENT.md`): "`#scope-adaptive-system` carries the typed predicate or a defended alternative, and a cold reader checks the membership clauses on standard RL and on a Kalman filter." Top intent, Joseph's: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."

Typed record: `reviews/scope-adaptive-system-check-7.md`.

## How this was done

I read `#scope-adaptive-system`, `#def-observation-function` and `#def-action-transition` whole, as they stand at `ed2b07e4` (all three unchanged at `162b941d`), the Formal Expression of `#def-chronica` (`c0d9c504`), and Proposition 3 of `#deriv-mismatch-budget-attribution` for the definition of (ii′). I re-derived everything below from those pages before reading any earlier check. Only then did I read check 6's review record (`reviews/scope-adaptive-system-check-6.md`) and grep `13-check-6.md` and `14-check-6-integration.md` for what they said about non-vacuity, to avoid re-reporting what check 6 found. I did not read `00`–`12` of this spike. Numbers were recomputed by script; derivations are by hand and are written out here so the integrator can re-derive them from this page.

## Verdict

The predicate, the typed target and the two new definitions hold up. Every membership item I re-derived is correct as written, and the cold-reader checks the KR names go through on the page: item (b) for a Kalman filter (the criterion, the one-step formula, $0.135$ and $0.162$ nats, the renewal rising to $0.135$) and item (c) for tabular reinforcement learning. The two definitions are coherent, are without loss of generality in the sense their Epistemic Status claims, and `#def-action-transition`'s XOR example does what it says.

Two findings would change sentences in canon:

- **F1.** The non-vacuity statement needs only fresh noise, not fresh transitions. So the sentence in the cut paragraph saying a remembering *transition* "breaks all three" is false for non-vacuity, and `#def-action-transition`'s own XOR example is a witness. The list of items that use the run-wide property is also incomplete in the other direction. This is a weaker premise for an existing result, not a softening.
- **F2.** For the reader the KR names, item (c) settles tabular RL but does not give a membership test a cold reader can apply to standard RL as practiced, with continuous states or real-valued rewards. There is an exact two-line criterion for every observed-state loop, under any $\pi_0$. I give it with its proof, and an example showing what it exposes: in a continuous world, "not given its transition law" does not settle membership.

F3–F5 are smaller.

## What holds (re-derived)

- **Condition 1 implies condition 2.** With $\lvert\mathcal O\rvert = 1$, $F_t$ is actions and a constant, and actions depend only on the history and independent randomness.
- **Averaged vs pointwise.** For a fixed continuation the averaged information is the mean of the pointwise ones over histories; choosing the continuation per history gives "in iff pointwise-in at some history of positive probability" for discrete histories.
- **(b), the Kalman filter.** $o_{t+j} = C A^j x_t + (\text{noise independent of } x_t, \mathcal C_t)$, so $x_t$ and $F_t$ are jointly Gaussian given $\mathcal C_t$ with cross-covariance $P_t (A^j)^\top C^\top$, and a jointly Gaussian pair has zero information exactly when the cross-covariance vanishes. The one-step part is $\tfrac12 \log\det\big((C A P_t A^\top C^\top + N) N^{-1}\big)$. Scalar random walk with unit variances: $P_\infty = (\sqrt5 - 1)/2 = 0.6180$, one-step part $\tfrac12 \log(1 + P_\infty/2) = 0.13464$. For the whole-future value I used a route other than check 6's: the future alone gives $x_t$ variance $P_\infty + 1$ (the backward filter of a reversible walk, one step back), so the smoothed variance is $\big(1/P_\infty + 1/(P_\infty + 1)\big)^{-1} = 1/\sqrt5$ and the value is $\tfrac12 \log(\sqrt5\, P_\infty) = 0.16175$. Direct Gaussian conditioning on $50$ future observations gives the same to five places. The restarted filter from $\tilde P_t = 0$ gives $r_t = 0$, then $0.1116, 0.1312, 0.1341, \ldots \to 0.13464$, and $\sum_k (u_k - r_k) = 0.16175$. $A = 0$ is out.
- **(c), tabular RL, as written.** The one-step information is $H(\bar p) - \mathbb E\, H(p)$, positive by strict concavity whenever the row is not a.s. constant (the clause "and has at least two possible successors" is implied by that). The $+\infty$ argument is right: the joint law charges the graph of the limit-frequency map, which the product of marginals does not when the row's law is continuous, so the joint is not absolutely continuous with respect to the product. Full-support Dirichlet rows make every entry positive a.s., so under any stationary policy the finite chain is irreducible and returns to $s$ infinitely often. The deterministic-successor exit, the reward-in-state reading and the Q-learner reading via (h′) are correct.
- **(g).** The law part by the chain rule and invariance; the whole-target bound $I(S_s; F_s \mid \mathcal C_s) \leq I(S_t; F_s \mid \mathcal C_s) + \sum_{k \geq s} r_k$ by data processing through $S_k$ (which needs both fresh clauses), with the first term bounded by the value at $t$ of the composite continuation. The clocked example is out for $t \leq K - 2$ and in from $K - 1$, as now written.
- **(g′).** The two-order chain rule on $I(S_t, S_k; o_{k+1} \mid \mathcal C_k, a_k)$, with $o_{k+1}$ independent of $S_t$ given $(S_k, \mathcal C_k, a_k)$, which needs both fresh clauses. All three consequences follow. The linear-Gaussian $r_k$ is right: given $x_t$, the observations before $t$ say nothing more about $x_k$, so the conditional covariance is the filter restarted from $0$.
- **(h).** Under the factorization, the conditional law of $F_t$ given $(S_t, \mathcal C_t)$ is unchanged by a reweighting of $\pi_0$ with a positive density; the law of $(S_t, \mathcal C_t)$ moves to an equivalent one; so "$P(F_t \in \cdot \mid S_t, \mathcal C_t)$ is a.s. a function of $\mathcal C_t$ alone" is preserved in both directions.
- **(h′).** The three support facts are right in a second-countable space (I re-proved each). The counterexample is right: $o_2 = 1\{x_1 \in \mathbb Q\}$ is a.s. $0$ under Lebesgue and a fair coin under the half-atomic measure, which has the same support. F3 notes one implicit step and one convention.
- **Housing.** The compressed twin state (posterior over $S_t$, latest observation) works because the predictive given $\mathcal C_t$ is a function of the posterior over $S_t$ and $a_t$, which uses both fresh clauses. The twin is Markov with a policy-free kernel; it agrees with the $\pi_0$-mixture under every policy; it is case (d). Mutual singularity against any one fixed law under a continuous $\pi_0$ holds by the frequency argument. (Remark: the housing result itself needs neither clause, since the twin whose state is the whole chronica already works. Only the compressed form uses them.)
- **The two definitions.** Fresh noise and fresh transition together give the product form of the run's law given $\theta$, read as the scope reads them, "with the law held fixed". They are without loss of generality in the sense claimed: putting remembered noise into the state only adds coordinates, and by the chain rule an added coordinate can only bring a loop in, never put it out. It brings one in only when the remembered thing is later shown, which is the right answer. `#def-action-transition`'s XOR example is correct: the state is Markov in its own past ($\varepsilon_1$ is independent of $x$), every observation's noise is fresh given its state, and yet $o_K \oplus o_1 = x$. `#def-observation-function`'s repeated-noise sentence is correct: $\varepsilon_t = \varepsilon_{t-1}$ has the same one-step kernel, and $o_t - o_{t-1}$ shows the state's change noiselessly for an additive channel.
- **Discussion numbers.** Fresh uniform Bernoulli row: $\log 2 - 2 \int_0^1 (-p \ln p)\, dp = \log 2 - \tfrac12 = 0.1931$. Sign-flip one-step part $\tfrac12 \log(1 + 1/(t+1))$: $0.0435, 0.00493, 0.000499$ at $t = 10, 100, 1000$, against $1/(2t)$, with an infinite value. Doubling map: $u_k = \log 2$, $r_k = 0$, infinite value. Part-of-target counterexample: $\infty$ against $\tfrac12 \log \tfrac32$.

## F1. Non-vacuity rests on fresh noise alone

**Where.** The cut paragraph of the Formal Expression: "Items (g′) and (h), and the non-vacuity statement in the Epistemic Status, use this property. It does not follow from a world that is Markov in its own past together with noise independent of the chronica. A channel or a transition that remembers something outside $\Omega_t$ satisfies both and breaks all three." The Discussion, "Why the future stream", derives non-vacuity through (g′): "each one-step part $u_k$ of (g′) is at most (ii′) at $o_{k+1}$, so the (ii′) terms after $t$ … sum to at least its value … plus the renewals."

**The shorter derivation.** Fix a continuation and $k \geq t$. Fresh noise says that given $\Omega_{k+1}$, $a_k$ and the observation kernel, $o_{k+1}$ is independent of everything earlier. Since $S_{k+1} = (\Omega_{k+1}, \theta)$ contains the kernel, $o_{k+1}$ is independent of $(S_t, S_k)$ given $(S_{k+1}, \mathcal C_k, a_k)$. Data processing then gives

$$\text{(ii′) at } o_{k+1} = I_{\pi'}(S_{k+1}; o_{k+1} \mid \mathcal C_k, a_k) \geq I_{\pi'}(S_t, S_k; o_{k+1} \mid \mathcal C_k, a_k) = I_{\pi'}(S_t; o_{k+1} \mid \mathcal C_k, a_k) + r_k ,$$

where the equality is the chain rule and nothing else. The chain rule over the stream, with the action terms vanishing (a property of policies, not of the world), gives $\sum_{k \geq t} I_{\pi'}(S_t; o_{k+1} \mid \mathcal C_k, a_k) = I_{\pi'}(S_t; F_t \mid \mathcal C_t)$. Summing,

$$\sum_{k \geq t} \text{(ii′) at } o_{k+1} \;\geq\; I_{\pi'}(S_t; F_t \mid \mathcal C_t) + \sum_{k \geq t} r_k .$$

That is the full non-vacuity statement, for some continuation and for the agent's own policy alike. It uses fresh noise and the chain rule. Fresh transitions are not used, and neither is the (g′) identity.

**Witness: a remembering transition does not break it.** Take `#def-action-transition`'s XOR world: known law, $\Omega_1 = x$ a fair bit, $o_1 = x \oplus \varepsilon_1$ with $\varepsilon_1$ a fair coin, a clocked state that carries nothing between $1$ and $K$, $\Omega_K$'s bit $b := \varepsilon_1$, $o_K = b$, and the other observations constant. At $t = 1$:

- value $I(x; F_1 \mid o_1) = \log 2$, since $o_K \oplus o_1 = x$ and $o_1$ alone is independent of $x$;
- every $u_k = 0$ and every $r_k = 0$ (for $1 \lt k \lt K$ the state carries nothing, and after $K$ the observations are constant), so (g′)'s identity fails: $\log 2 + 0 \neq 0$;
- (h)'s first step fails at $1 \lt t \lt K$: given $(S_t, \mathcal C_t)$, $o_K = o_1 \oplus x$ depends on $\Omega_1$;
- (ii′) at $o_K$ is $I(o_K; S_K \mid \mathcal C_{K-1}) = H(\varepsilon_1 \mid o_1) = \log 2$, so $\sum$ (ii′) $= \log 2 \geq \log 2 + 0$. **Non-vacuity holds.**

Check 6's counterexample, a remembering *channel* ($o_K = \varepsilon_K := z_1$ with nothing in the state), does break non-vacuity, because there the observation's noise is not fresh. So "breaks all three" is true of a remembering channel and false of a remembering transition.

**Which items use the run-wide property.** By my reading of each derivation: (g)'s whole-target bound (data processing through $S_k$); (g′)'s identity; (h)'s first step; (h′)'s step "the law of the block given $(s, \theta, c)$" (without the factorization, that law also depends on $\Omega_1$ and is not determined by $(s, \theta, c)$); the housing result's compressed twin state; and in (c), the step "taking action $a$ makes the next observation a draw from $T(\cdot \mid s, a)$" given the history. Non-vacuity uses only fresh noise.

**Replacement text.** In the cut paragraph, replace "Items (g′) and (h), and the non-vacuity statement in the Epistemic Status, use this property. It does not follow from a world that is Markov in its own past together with noise independent of the chronica. A channel or a transition that remembers something outside $\Omega_t$ satisfies both and breaks all three." with:

> Items (g), (g′), (h) and (h′) and the compressed twin of the housing result use this property; the non-vacuity statement in the Epistemic Status uses only its observation half, fresh noise. The property does not follow from a world that is Markov in its own past together with noise independent of the chronica. A transition that remembers something outside $\Omega_t$ satisfies both and breaks (g′) and (h) (the example in #def-action-transition); a channel that does also breaks non-vacuity.

In the Discussion, "Why the future stream", replace "Summed, the same comparison says more: along any continuation each one-step part $u_k$ of (g′) is at most (ii′) at $o_{k+1}$, so the (ii′) terms after $t$, computed under that continuation, sum to at least its value $I_{\pi'}(S_t; F_t \mid \mathcal C_t)$ plus the renewals." with:

> Summed, the same comparison says more. Fresh noise makes $o_{k+1}$ independent of $(S_t, S_k)$ given $(S_{k+1}, \mathcal C_k, a_k)$, so (ii′) at $o_{k+1}$ is at least $I_{\pi'}(S_t, S_k; o_{k+1} \mid \mathcal C_k, a_k)$, which by the chain rule is $I_{\pi'}(S_t; o_{k+1} \mid \mathcal C_k, a_k) + r_k$. Summed over $k \geq t$, the (ii′) terms after $t$, computed under that continuation, are at least its value $I_{\pi'}(S_t; F_t \mid \mathcal C_t)$ plus the renewals. Fresh transitions are not needed for this.

(The Epistemic Status sentence "the same sum is at least $I_\pi(S_t; F_t \mid \mathcal C_t)$ plus the renewals" can stay as is.)

## F2. A membership test for standard RL that a cold reader can apply

**The gap.** Item (c) is stated for a finite state space with Dirichlet rows. A reader bringing standard RL, with continuous states or real-valued rewards, is sent to (h): membership is the same for every $\pi_0$ with the declared one's null sets. That is true, but it does not say what the membership is, and the reader has no measure class to declare. Most of (c)'s length (Clarke–Barron, the $+\infty$ value) is about the *value's* behavior, which "Two kinds of warrant" uses, not about membership.

**The criterion.** Let the state be observed ($o_t = \Omega_t$), so $S_t$ carries no information beyond $\theta$ given $\mathcal C_t$, and the channel is known. Then:

> The loop is in at $t$ exactly when some continuation, with positive probability, takes at some time $k \geq t$, at the current state $s = \Omega_k$, an action $a$ whose row $T(\cdot \mid s, a)$ the history $\mathcal C_k$ does not fix (its posterior is not a point mass).

*Lemma.* If $K$ is a random probability measure on a standard Borel space and $X \mid K \sim K$, then $I(K; X) = 0$ exactly when $K$ is a.s. constant. If $I = 0$, then $X$ is independent of $K$, so $K(B) = P(X \in B \mid K) = P(X \in B)$ a.s. for each $B$ in a countable generating $\pi$-system, and $K$ is a.s. equal to the marginal. The converse is immediate.

*Proof.* By the chain rule over the stream, with the action terms zero, $I_{\pi'}(\theta; F_t \mid \mathcal C_t) = \sum_{j \geq t} \mathbb E\, I(\theta; o_{j+1} \mid \mathcal C_j = c, a_j)$, each term pointwise non-negative. Given $\theta$ and $\mathcal C_j$, fresh transitions make $o_{j+1} = \Omega_{j+1}$ a draw from the row at $(\Omega_j, a_j)$, so the pointwise term is $I(T(\cdot \mid \Omega_j, a_j); o_{j+1} \mid c, a_j)$. By the lemma, this is positive exactly when that row's posterior given $c$ is not a point mass. So the sum is positive exactly when, with positive probability, the continuation takes an action whose row the history at that moment has not fixed. ∎

*Corollaries, each one line.* Full-support Dirichlet rows: no row's posterior is ever a point mass, so taking any action now suffices, and the learner is in at every $t$. Deterministic-successor rows: a row is fixed by one visit, so the learner is in exactly while some pair that some continuation can still reach is unvisited, and the exit is pointwise. A bandit is in while some arm's reward law is unfixed. Rows no continuation reaches never enter (item (f)).

**What it exposes in continuous worlds.** "Not given its transition law" does not settle membership once (h′)'s finiteness fails. Take a one-armed bandit with real-valued rewards, the state being the latest reward and starting from a fixed $\Omega_1 = 0$, and two declarations:

- $\pi_0^{\mathrm A}$: the reward law is drawn from a Dirichlet process with a full-support base measure. Its posterior after any finite history is again a Dirichlet process, never a point mass, so by the criterion the loop is in at every $t$.
- $\pi_0^{\mathrm B}$: choose pairwise disjoint countable dense sets $D_m = \mathbb Q + \alpha_m$ (with $\alpha_m - \alpha_n$ irrational for $m \neq n$), and laws $Q_m$, each finitely supported on $D_m$, forming a weakly dense family. This is possible because $\mathcal P(\mathbb R)$ is separable and finitely supported laws on a dense set are weakly dense. Put $\pi_0^{\mathrm B} = \sum_m 2^{-m} \delta_{Q_m}$. The first reward, $o_2$, lies in exactly one $D_m$ and so fixes the law: by the criterion the loop is in at $t = 1$ and out from $t = 2$ on, at every history.

Both measures have every law on $\mathbb R$ in their weak support. They are mutually singular ($\pi_0^{\mathrm A}$ has no atoms in law space, while $\pi_0^{\mathrm B}$ is purely atomic), which is why (h) lets them disagree. This is the law-side twin of (h′)'s rationals counterexample, in the form an RL reader meets.

**Replacement text.** Open (c) with the criterion and keep the rest as its instance and the value's behavior. Proposed first sentences of (c), replacing "Take $o_t = \Omega_t$ on a finite state space, with the rows $T(\cdot \mid s, a)$ unknown under independent Dirichlet priors. The state is read off the history, so all the information is about $\theta_T$.":

> Take $o_t = \Omega_t$. The state is read off the history, so all the information is about $\theta_T$, and the loop is in at $t$ exactly when some continuation, with positive probability, takes at some state an action whose row $T(\cdot \mid s, a)$ the history at that moment does not fix. (By the chain rule the information is a sum over later steps of what each draw shows about the row it is drawn from, and a draw from a random law shows something about it exactly when that law is not a point mass.) On a finite state space with the rows under independent Dirichlet laws, no row is ever fixed, so the learner is in at every $t$.

Then keep the rest of (c) from "At the current state $s$, taking action $a$ makes the next observation a draw …", lightly trimmed of what the criterion now says. At the end of (c), replace "With real-valued rewards (h′) does not apply, and (h) gives the same membership for every $\pi_0$ with the declared one's null sets." with:

> With real-valued rewards (h′) does not apply, and the declaration does real work. A bandit whose reward law is drawn from a Dirichlet process is in at every $t$; one whose law is drawn from a countable dense family of finitely supported laws on disjoint countable sets is out once it has seen one reward, because that reward identifies the law. Both measures have every law in their support. By (h), membership is the same for every $\pi_0$ with the declared one's null sets.

**Judgment, not a finding.** With the criterion leading, (c) reads as a membership clause, and the value's behavior can be its second half. The KR asks that a cold reader *check* the clause, and at present the check for standard RL runs through about 400 words, most of them about something else.

## F3. "Declared on" and the support, and one step in (h′)

**Support.** The Definition says $\pi_0$ is "declared on the set of worlds possible for the agent", and later "When the state, observation and action spaces are finite, … the support of $\pi_0$ is the closure of the set of possible worlds". A measure with $\pi_0(W) = 1$ can have a support strictly smaller than $\overline W$ (for example, all its mass on half of a finite $W$). Nothing defines "declared on" to rule this out. So the closure statement is a requirement on the declaration, presented as a fact. (h′)'s conclusion, "the declared set of possible worlds fixes membership with no further choice of measure", leans on it. `NOTATION.md`'s $\pi_0$ row repeats it ("its support, which is then the closure of that set"). Check 6's F4 was about the word "closure" and the topology; this is about the full-support requirement itself.

Replacement: "When the state, observation and action spaces are finite, the kernel entries carry the Euclidean topology, and $\pi_0$ is declared to charge every open set that meets the possible worlds, so its support is their closure." The same clause would go in `NOTATION.md`'s row.

**One step in (h′).** The posterior that has to be "constant almost everywhere" is over $(\Omega_t, \theta)$. It is the image, after dropping $\Omega_1$, of $L \cdot \pi_0$ on $(\Omega_1, \Omega_t, \theta)$. The three facts handle $L \cdot \pi_0$; that the image's support is a function of $\operatorname{supp} \pi_0$ is a fourth step. It is easy, since the space is compact and the image of a compact support under a continuous projection is closed and equals the support of the image. A clause would do: "and the posterior over $(\Omega_t, \theta)$, an image of $L \cdot \pi_0$ under a projection of a compact space, has the projection of that support as its own."

## F4. The observation kernel, as defined, is the mixture under $\pi_0$

`#def-observation-function`: "The **observation kernel** $p_h(\cdot \mid \omega, a)$ is the conditional law of $o_t$ given $\Omega_t = \omega$ and $a_{t-1} = a$." Once the scope makes $\theta_h$ random under $\pi_0$, the conditional law of $o_t$ given $(\Omega_t, a_{t-1})$ alone is the mixture over $\theta_h$, not the kernel. The fresh-noise clause then conditions on "the kernel" as a separate random object. The scope's own gloss, "the conditional law of $o_t$ that $h$ and $\varepsilon_t$ jointly induce", is the right reading. A cold reader holding the definition literally gets the mixture. Replacement for the definition sentence:

> The **observation kernel** $p_h(\cdot \mid \omega, a)$ is the conditional law of $o_t$ given $\Omega_t = \omega$ and $a_{t-1} = a$ that $h$ and the law of $\varepsilon_t$ induce. Where the agent was not built knowing them, it is the random kernel $\theta_h$ of #scope-adaptive-system, and the conditional law given $(\omega, a)$ alone is its mixture.

`#def-action-transition` does not have this problem, since it defines $T$ as the kernel itself.

## F5. Small points

- (g): "Without that condition, leaving need not be final" introduces an example that is never in before $K - 1$. It shows that being out is not absorbing; nothing is left. Suggested: "Without that condition, being out need not be final: …".
- `#def-observation-function`, "Channels with memory": a channel memory that never changes (a fixed bias) goes into $\theta_h$ by the invariance cut, not into $\Omega_t$. Suggested: "places that memory in $\Omega_t$, or in $\theta_h$ if it never changes, where later observations can show it".
- (c): "whenever the row is not a.s. constant and has at least two possible successors": the second clause is implied by the first.

## On the KR

A.1 asks for the typed predicate or a defended alternative, and a cold reader's check of the membership clauses on standard RL and a Kalman filter. The predicate is there and correct. The Kalman check goes through on the page. The tabular-RL check goes through. With F2's criterion, the standard-RL check becomes a one-line test that works for any declared $\pi_0$. Without it, a reader with a continuous-state learner can find out that the answer depends on the declaration, but not what the answer is.

## What I did not do

I did not read `00`–`12` of this spike or the aat-refactored spike, and did not test the Working Notes' open items (the tail-rule strengthening, the sensor-autonomy candidate). I did not re-derive the Clarke–Barron constant (I took it as the standard asymptotic) or check `#example-kalman`. F2's $\pi_0^{\mathrm B}$ construction is argued, not computed; the density step relies on the separability of $\mathcal P(\mathbb R)$ under the weak topology. This record's findings are its content. Silence about a part means only that I found nothing there.

## On the brief

The bare brief worked: it left me free to spend the time on the integration's own new claims, which is where both of the larger findings came from. The record-kind `vsect claim` on segments I was not editing felt like the right signal, but I wasn't sure it was what you intended. If a review-only checker should claim nothing, a word in the next brief would settle it.
