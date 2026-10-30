# 11 — Independent check of #scope-adaptive-system at 3f3b4ca5

**KR A.1** (`msc/inside-out-2026-10/INTENT.md`): `#scope-adaptive-system` carries the typed predicate, or a defended alternative, under the top intent *the front door says only what the bodies support*. This is the fourth read, on a bare brief. The vsect record is `reviews/scope-adaptive-system-check-5.md`; this file holds the derivations, numbers and replacement text behind it.

Read at commit `3f3b4ca5`. The segment is byte-identical at `70f9f969` (the only change between them is `INTENT.md`). Written by Claude Opus 5.5, 2026-10-30.

## How I read

I read the segment whole, then its four `depends:` (`#def-agent-environment`, `#def-action-transition`, `#def-observation-function`, `#def-chronica`, bodies through Discussion), and re-derived each item from the text before opening any earlier review of it. Only after my own pass did I read `reviews/scope-adaptive-system-reread-1.md` (to see which of its findings are still open in vsect) and the vsect record for the segment. I did not read `07`–`10` in this directory or `reviews/scope-adaptive-system-check-4.md`, so where I agree with them that agreement is independent, and where I repeat them I did not know it.

Beyond the segment I read: the Formal Expression and Epistemic Status of `#result-mismatch-decomposition`; Propositions 1 and 3 of `#deriv-mismatch-budget-attribution`; the scope section of `#example-kalman` and `#example-bandit`; `#hyp-solicitable-escape` line 44; `#disc-structural-imagination` line 54; NOTATION rows for $\theta$, $\pi_0$, $S_t$ and GA-1; the terminology entries `adaptive-system`, `cycle`, `loop`; `doc/audit-routing-instructions.md` §5–§8. I grepped every live citation of the segment (`0*-core/`, NOTATION, terminology, OUTLINE, INTRODUCTION) for the replaced predicate and for readings that disagree with the current one.

Numbers were recomputed in a scratch script (Python, closed-form Riccati and direct joint-Gaussian conditioning); it is not kept, and each number below says how to recompute it.

## What holds

Each item below I re-derived from the definitions as written. I found no error in any of them.

**(a), (d), (e), (f) and condition 2.** A point-mass conditional law kills every mutual information with $S_t$. Under (d) $S_t$ is a function of $\mathcal C_t$. Under (e) the future stream is conditionally independent of $S_t$ for every continuation. Under (f) the chain rule gives $I(U, V; F_t \mid \mathcal C_t) = I(U; F_t \mid \mathcal C_t) + I(V; F_t \mid U, \mathcal C_t)$, and the second term is zero when no continuation's future depends on $V$ given $U$ and the history. With a single symbol, $F_t$ is actions plus a constant, and actions are functions of the history and independent randomness, so condition 1 does imply condition 2.

**(b).** Given $\mathcal C_t$, $x_t$ and $o_{t+j} = C A^j x_t + (\text{noise independent of } x_t, \mathcal C_t)$ are jointly Gaussian with cross-covariance $P_t (A^j)^\top C^\top$, and a Gaussian mutual information is zero iff the cross-covariance is. The one-step part is $\tfrac12 \log\det(I + C A P_t A^\top C^\top N^{-1})$ with $N = C Q C^\top + R$. Scalar random walk, unit variances: $P_\infty = (\sqrt5 - 1)/2 = 0.6180$, one-step part $\tfrac12\log(1 + P_\infty/2) = 0.13464$ nats; whole-future value $\tfrac12 \log(P_\infty / P_{\text{smooth}})$ with $P_{\text{smooth}} = (1/P_\infty + 1/(1 + P_\infty))^{-1} = 0.4472$, giving $0.16175$ nats. Both match the segment's $0.135$ and $0.162$. The value is at least the one-step part because $I(x_t; F_t \mid \mathcal C_t) \geq I(x_t; a_t, o_{t+1} \mid \mathcal C_t)$.

**(c).** Positivity of the one-step information is Jensen with equality iff the row is a.s. constant. The $+\infty$ argument is right: on the recurrence event the row is a measurable function of the stream, so the joint law charges the graph of that function while the product law, under the Dirichlet posterior's density, gives it measure zero; the joint is not absolutely continuous with respect to the product, and the divergence is infinite. Full-support rows: every entry of the true kernel is positive a.s., so under any policy each step reaches $s$ with probability at least $\min_{s', a'} T(s \mid s', a') \gt 0$, and $s$ recurs a.s. The deterministic-successor exit is correctly marked pointwise. $(K-1)/(2n)$ is the per-step increment of the Clarke–Barron expansion $I(p; X^n) = \tfrac{K-1}{2}\log n + O(1)$.

**(g).** The chain-rule split, and the argument that conduct from $t$ to $s$ followed by any continuation is a continuation from $t$, are both correct. For the whole-target inequality I re-derived $I(S_s; F_s \mid \mathcal C_s) \leq I(S_t; F_s \mid \mathcal C_s) + \sum_{k \geq s} I(S_s; o_{k+1} \mid S_t, \mathcal C_k, a_k)$ and then $I(S_s; o_{k+1} \mid S_t, \mathcal C_k, a_k) \leq r_k + I(S_s; o_{k+1} \mid S_k, S_t, \mathcal C_k, a_k) = r_k$ by the Markov property. The clock example: with $\Omega_k = (k, x_k, x_{k-1})$ and $o_k = x_{k-1}$ from $k = \tau$ on, the loop is out for $t \lt \tau - 1$ (later observations report draws made after $t$) and in from $t = \tau - 1$. Its renewal is zero before $k = \tau - 1$ and positive from it, consistent with the condition.

**(g′).** The two-order chain rule gives $u_k = I(S_t; o_{k+1} \mid \mathcal C_k, a_k) + r_k$ once $I(S_t; o_{k+1} \mid S_k, \mathcal C_k, a_k) = 0$, and the infinite chain rule (mutual information with a sequence is the limit over prefixes) gives the identity in $[0, \infty]$. Linear-Gaussian renewal: conditioning on $x_t$ restarts the filter at covariance $0$, and $\mathcal C_t$ is then irrelevant to later states. Scalar random walk: $r_t = 0$, $r_{t+1} = 0.1116$, $r_{t+2} = 0.1312$, rising to $0.13464$; $\sum_k (u_k - r_k) = 0.16175$, and a direct computation of $\sum_k I(x_t; o_{k+1} \mid \mathcal C_k)$ by tracking the joint covariance of $(x_t, x_k)$ gives the same $0.16175$. The identity holds numerically by two routes.

**(h).** The new joint of $(S_t, \mathcal C_t, F_t)$ has density $\mathbb E[f(\Omega_1, \theta) \mid S_t, \mathcal C_t, F_t] = \mathbb E[f \mid S_t, \mathcal C_t]$ with respect to the old, by $\Omega_1 \perp F_t \mid (S_t, \mathcal C_t)$ and $\theta \subset S_t$. The conditional kernel of $F_t$ is untouched, and "the kernel is a.e. a function of $\mathcal C_t$ alone" is a null-set property of the law of $(S_t, \mathcal C_t)$.

**(h′).** I spot-checked the three support facts (each needs only second countability: the complement of a support is null) and the reduction to finite blocks. With $\Omega_1$ finite, the posterior over $(s, \theta)$ is a finite sum of $L \cdot \pi_0(\omega_1, \cdot)$ terms, so fact 1 applies term by term. The counterexample is right: under Lebesgue $o_2 = 0$ a.s.; under the half-atomic prior, which has the same support, $o_2$ is a fair coin determined by $x_1$.

**Housing.** The Bayes filter's recursion is policy-free, so the twin's kernel is one function of state and action. The twin agrees with the declared mixture on every one-step predictive and so on every sequence law. $\Omega'_t$ is a function of $\mathcal C_t$ with a known law, so the twin is out.

**Discussion and Epistemic Status numbers.** A fresh uniform Bernoulli row: $\log 2 - \mathbb E[h(p)] = \log 2 - \tfrac12 = 0.1931$ nats. For $x_{t+1} = -x_t$: after $t$ observations the posterior variance of $x_1$ is $1/(1+t)$, the one-step part is $\tfrac12\log(1 + 1/(1+t))$ ($0.0435$ at $t = 10$, $0.000499$ at $t = 1000$), and the value is infinite. Doubling map: each step shows one fresh binary digit of $x_t$, $\log 2$ nats, with no renewal because the map is deterministic. Epistemic Status counterexample: $I(z_1; F_1 \mid \mathcal C_1) = I(w; o_{2:\infty} \mid o_1) = \infty$, and the one-step parts of $z$ sum to $I(w; o_2 \mid o_1) = \tfrac12\log\tfrac32 = 0.2027$. The identity fails here for the stated reason: the step $I(z_1; o_{k+1} \mid z_k, \mathcal C_k) = 0$ is false, because $z_k = 0$ for $k \geq 2$ does not screen $o_{k+1} = w + v_{k+1}$ off from $z_1 = w$.

**"Why the future stream".** Against Proposition 3 of `#deriv-mismatch-budget-attribution`, term (ii′) at $t+1$ is $I(o_{t+1}; S_{t+1} \mid \mathcal C_t, a_t)$. Given $(\mathcal C_t, a_t)$, $S_t \to S_{t+1} \to o_{t+1}$ is a Markov chain, so the one-step part is at most (ii′), and $A = 0$ makes (ii′) positive with the predicate zero. Both statements hold.

**Downstream consistency.** No live segment, NOTATION row, terminology entry, OUTLINE row or INTRODUCTION sentence still states the replaced predicate as the scope. `#hyp-solicitable-escape`:44, `#scope-agency` (dated), `#example-kalman`, `#example-bandit`, `#result-mismatch-decomposition` step 1 and NOTATION's GA-1 all read the current segment correctly. `doc/readme/src/_lexicon-full-archive.md` still states the old predicate, but nothing in `bin/` or `doc/readme/` consumes it.

## What does not hold, or holds only under a reading the text does not state

### C11 — the invariance cut has no quantifier over conduct

The cut reads: "Each declared variable that stays the same along the whole run, almost surely, is named into $\theta$." The run is generated by a policy, and the text does not say which. The predicate ranges over every continuation $\pi'$, and three statements need $\theta$ to stay fixed under each of them:

- the Markov commitment, "Given $\theta$, $\Omega_t$ is sufficient for its own evolution";
- (g)'s step "because $\theta$ is invariant the last term is the law part at $s$";
- (g′)'s "the law never renews: it sits in both $S_t$ and $S_k$".

A minimal case. Take a lever $c \in \{0, 1\}$ with $c_1 \sim \text{Bern}(\tfrac12)$, actions $\{\text{wait}, \text{press}\}$, where pressing redraws $c$ fresh, and observations $o_k = c_k$ flipped with probability $0.1$. The agent's own policy always waits. Under that policy $c$ is constant a.s., so on the reading "the run the agent produces" it is named into $\theta$. The continuation that presses is in the range of the $\sup$, and under it $c$ changes. That leaves two ways to read the result, and neither works:

- If $S_k$ holds the current value $c_k$, then $r_k = I(c_k; o_{k+1} \mid c_t, \mathcal C_k, a_k) \gt 0$ after the press. The law component renews, and "the law never renews" is false.
- If $\theta$ is the fixed variable $c_1$, then $S_k$ does not contain $c_k$. The Markov commitment fails, and $\theta$ is no longer the law of anything ("the rules by which the state moves").

Membership is untouched either way: $S_t$ holds the same variables at time $t$ under either label, as the segment says. The labels and the two (g)/(g′) consequences are what break.

`#disc-structural-imagination`:54 already reads the cut as "$\theta$ holds only what no action changes", so the intended reading is the policy-uniform one, and on that reading all three statements hold. The text does not say it, and NOTATION's row ("stays the same along the run") does not either.

Replacement text for the cut's sentence (the Formal Expression paragraph after the display of $S_t$): "Each declared variable that stays the same along every run, under every policy over $\mathcal A$, $\pi_0$-almost surely, is named into $\theta$; each that varies, however slowly, on only some runs, or only under some conduct, is state." NOTATION row $\theta$ wants the same quantifier. With this rule a mechanism an action can change is state, which is what `#disc-structural-imagination`:54 already assumes.

### C12 — what "non-vacuity" membership delivers

The Epistemic Status sentence reads: "What the conditions supply is non-vacuity: they make mismatch, gain, tempo and persistence statements about adapting to a world rather than about chance or the agent's own errors." Read with "a result that cites this scope uses it at the times the result is applied", it says more than the predicate gives.

Counterexample: an invariant hidden bit $b \sim \text{Bern}(\tfrac12)$ (so, by the cut, part of $\theta$), a state that is a clock, and observations constant except $o_K = b$. The loop is in at every $t \lt K$. Yet at every step before $K$ the one-step predictive is the same under every value of $b$, so term (ii) of `#result-mismatch-decomposition` and term (ii′) of `#deriv-mismatch-budget-attribution` are both zero. Any mismatch at those steps is chance or the model's own error. Membership at $t$ does not make the mismatch at $t$, or at any fixed later step, about the world.

What membership does deliver is exact and worth stating. If the loop is in at $t$, the identity of (g′) gives some continuation and some $k \geq t$ with $I(S_t; o_{k+1} \mid \mathcal C_k, a_k) \gt 0$. Data processing along $S_t \to S_k \to S_{k+1} \to o_{k+1}$ (given $\mathcal C_k, a_k$) then gives

$$I(o_{k+1}; S_{k+1} \mid \mathcal C_k, a_k) \geq I(S_t; o_{k+1} \mid \mathcal C_k, a_k) \gt 0,$$

so under that continuation term (ii′) is positive at step $k+1$. The scope guarantees a later step at which the mismatch budget's state-and-law term is positive. It does not guarantee one at the step a result is applied.

Replacement text for that sentence: "What the conditions supply is non-vacuity in one exact sense: if the loop is in at $t$, then under some continuation some later observation carries information about the target at $t$, and by data processing the state-and-law information term (ii′) of #deriv-mismatch-budget-attribution is positive at that observation. Membership does not make the mismatch at a given step about the world: a loop whose only revealing observation comes late is in at every earlier time, while every earlier mismatch is chance or the agent's own error. Nor do the conditions by themselves deliver Part I's results, which carry their own assumptions (the global assumptions in NOTATION.md)."

Before proposing this I tried the stronger statement: membership at $t$ implies term (ii′) is positive at $t+1$. The late-reveal bit refutes it, so it is a no-go and not a softening. The exact statement above is the strongest I could derive.

### F1 — $\theta$ is typed twice

The Definition paragraph makes $\theta$ the kernel pair $(\theta_T, \theta_h)$. The cut paragraph names invariant declared *variables* "into $\theta$", and (b) names a constant coordinate of $x$ into it. A constant coordinate is not a kernel. The two readings agree only if the invariant variables are absorbed as an index of the kernels of the varying variables, and the text does not say so. NOTATION's row carries both readings in one cell ("Random kernel pair … each declared variable that stays the same along the run is named into it"). (h′)'s hypothesis, "$\theta$, the tuple of kernel entries, carries the Euclidean topology", does not cover an invariant finite coordinate named into $\theta$. The proof survives with that coordinate carried in the discrete topology, but the hypothesis as written does not say so.

Either repair works:

- "$\theta = (\theta_T, \theta_h)$ are the kernels of the varying variables, indexed by the invariant ones", with (h′)'s hypothesis reading "the kernel entries, after the invariant variables are absorbed";
- or $\theta = (\theta_T, \theta_h, \iota)$ with $\iota$ the invariant declared variables, and (h′) adding "and $\iota$ finite, discretely topologized".

Membership is unaffected by the choice.

### F2 — Working Notes carry the replaced predicate as material to promote

The "Incidental audit gold" subsection offers several items as candidate canon without marking that the predicate under them was replaced:

- candidate Brief prose ("a system with $H(\Omega_t \mid \mathcal C_t) = 0$ is an omniscient agent; it has nothing to adapt *about*"), which is false of tabular RL under item (c);
- a candidate Discussion "two-axis open-region geometry" with the $\mathcal O = \emptyset$ wall and the $H(\Omega_t \mid \mathcal C_t) = 0$ wall;
- a readers-ask item about the "$\mathcal O = \emptyset$ exclusion" for AI mathematicians;
- a candidate figure whose axes are those two walls.

Each is unmarked. Three neighbors carry a "Landed", "Resolved" or "Answered" marker, which makes the unmarked ones read as still current. A pedagogy pass that promotes them, which the subsection's own preamble invites, would reintroduce the replaced predicate at the front door. Each wants either a marker naming what replaced it (residual uncertainty is necessary, not sufficient, item (a); the lower wall is $\lvert\mathcal O\rvert \geq 2$, implied by condition 1) or re-expression in current terms. The figure could become a three-region picture: known (case (d)), unreachable or fresh (cases (b) with $A = 0$, (e), (f)), and open-and-reachable (in).

The first line of "Integration record and open items" ("replaced the state-only predicate … on 2026-10-30; CHANGELOG carries the history") is history, which the effort's standing puts in CHANGELOG and commit bodies only.

### F3 — two places in the body speak in change-chronicle voice

The heading "What the old exclusion got right and wrong" and the housing result's "the state-only predicate it replaces" narrate the theory's own revision. The content is domain content, why "full knowledge of the environment" is the wrong boundary (routing §5B), so this is register and not status. Candidate heading: "Full knowledge of the environment, as a boundary". Candidate clause: "including $H(S_t \mid \mathcal C_t) \gt 0$ and the state-only $H(\Omega_t \mid \mathcal C_t) \gt 0$".

### F4 — smaller precision points

- *"Has then become a planner"* (Discussion, "Two kinds of warrant"; also "a planner handed its true law is out" in "Whose uncertainty") is true only with an observed state. A law learner with a hidden state that renews (a Kalman filter that has fixed its noise level) is still in, as a tracker. "With its state observed" makes both exact.
- *The three ways to be outside* (intro) overlap and combine. The second (a channel that carries nothing) is a case of the third whenever there is residual uncertainty, and a loop can be out with some coordinates fixed by the history and the rest unreachable. "Three ways, which can combine" would match (a)–(f).
- *$u_k - r_k$* in (g′)'s third consequence is $\infty - \infty$ when a noiseless channel reports a fresh continuous draw. That is harmless because the identity per $k$ is $u_k = I(S_t; o_{k+1} \mid \mathcal C_k, a_k) + r_k$ in $[0, \infty]$, but writing the term as $I(S_t; o_{k+1} \mid \mathcal C_k, a_k)$ avoids the subtraction.
- *The display sentence* "The loop is in the adaptive scope at time $t$ if $\mathcal S_\text{adaptive}(t) = \{\ldots\}$" defines the set where it means to test membership in it. "…at time $t$ if it belongs to" reads as intended.
- *The doubling map* "shows one fresh digit of the starting point": the target is $x_t$, so "of $x_t$" is exact; "starting point" reads as $x_1$.

### F5 — `#example-kalman` indexes the sensor choice against the chronica

`#example-kalman` writes $y_t = x_t + n_t^{(a_t)}$ and "changes $P(y_t \mid do(a_t))$". `#def-observation-function` has $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$, and `#def-chronica` orders $a_{t-1}$ before $o_t$, so an observation at $t$ that depends on $a_t$ would require the agent to choose $a_t$ before receiving $o_t$, which the chronica forbids. Re-index to $n_t^{(a_{t-1})}$ (or say the mode for $y_t$ is chosen at $t-1$). Nothing in its scope verdict or the adaptive segment's (b) changes.

### F6 — two terminology entries point here for content this segment does not carry

`terminology/entries/cycle.md` says "See #scope-adaptive-system for the cycle as the operational unit of an adaptive system", and `loop.md` says "See #scope-adaptive-system for the loop as the defining feature of adaptive systems". Both name it as `primary_source`. The segment says nothing about cycles (the one occurrence of the word is in the audit gold), and it uses "loop" without defining it. `LEXICON.md` is generated from these entries, so the pointers reach the front door. They want either the segments that do carry those senses, or the claim dropped.

## The vsect ledger for this segment

On my reading at `3f3b4ca5`, these findings, all still open in `vsect open`, no longer describe the text:

- from `reviews/scope-adaptive-system-reread-1.md`: F2, F3, F4, the bullets of F5 other than relata (which has its own item) and `CURRENT-VOL1.md` (a generated snapshot), and the C3 and C4 findings;
- downstream from the same review: F6 (`#example-bandit`), F7 (`#def-agent-environment`:43), F9 (`#scope-agency`), F10 (`#scope-composite-agent`:85), F11 (`#deriv-recursive-update`:27), F13 (`#disc-framework-self-diagnostic`), and F12's scope-warrant half (its $\theta_k(t)$ glyph half is still open, routed to naming).

F1's remaining substance is the open knowledge-versus-belief question already in vsect. I have not disposed of any of them. That belongs to whoever holds the ledger, and I can do it on request with the evidence above.

## What I did not do

The list above is the content of this check. Silence about a part means only that I found nothing there, and here is what I did not cover. I did not read `07`–`10`, check-4, or the aat-refactored spike. I did not re-derive Clarke–Barron itself or de Finetti's representation; I used them as cited. I did not test the Working Note's tail-$\sigma$-field claims beyond the doubling-map and $x \mapsto -x$ facts. I did not check `CURRENT-VOL1.md` or other generated snapshots. I did not read the cited primary sources (Åström, Kaelbling–Littman–Cassandra, Martin, Duff, Clarke–Barron).
