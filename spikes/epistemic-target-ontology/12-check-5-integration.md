# 12 — Integrating the fourth independent check (11) into `#scope-adaptive-system`

**KR A.1** (`msc/inside-out-2026-10/INTENT.md`), under the top intent *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."*: `#scope-adaptive-system` carries the typed predicate or a defended alternative, and a cold reader checks the membership clauses on standard RL and on a Kalman filter.

*Integrator: Opus 5.5, 2026-10-30, the same mind that landed 10, so a different mind checks after. I read 11 whole and re-derived each proposal from the segment's own definitions before landing it. Canon is at `97205749` on branch `a1-round-4`; the typed record is `reviews/scope-adaptive-system-integration-5.md`. This file holds the reasoning and where I diverge from 11.*

## 1. C11: the cut quantifies over conduct

Agreed, re-derived. The predicate takes a supremum over continuations, and three statements need $\theta$ fixed under each of them: the Markov commitment, (g)'s "the last term is the law part at $s$", and (g′)'s "the law never renews". 11's lever is constant under the agent's own policy and reset by another, and it breaks all three if it is named law. Under the quantified rule (constant along every run, under every policy over $\mathcal A$, $\pi_0$-a.s.) the lever is state, and each of the three holds again, because a variable no conduct can change is one random variable under every continuation. The segment now says why the quantifier is there, and NOTATION's row carries it. This is the reading `#disc-structural-imagination`:54 already uses ("$\theta$ holds only what no action changes").

## 2. F1: one type for $\theta$

I took 11's first repair: invariant variables are absorbed into the other variables' kernels as indices, so $\theta$ is always a kernel pair. Two reasons:

- It is the reading the cut paragraph already relies on. "Moving an invariant coordinate … changes no mutual information" holds because the reduced world's kernel pair, a function of $(\theta, \zeta)$, is a sufficient statistic of the larger target for the stream (08 §1.6). Absorption is that construction named.
- (h′)'s hypothesis stays true as written: after absorption $\theta$ is still a tuple of kernel entries, and a finite invariant coordinate becomes a finite set of kernel values, which the Euclidean topology handles. The second repair (a separate $\iota$ in the discrete topology) would have changed the hypothesis.

The absorption can forget an invariant variable that no kernel depends on. That loses nothing the predicate sees, by item (f). The Epistemic Status counterexample (an invariant $w$ seen through noise, with $z_1 = w$) still types: $w$ indexes the observation kernel, and $\pi_0$ couples it with $z_1$.

## 3. C12: what membership delivers, strengthened past 11's text

11 proposes that membership gives some later observation at which (ii′) is positive, and refutes the per-step form with a late-reveal bit. Both are right. The same data processing gives a quantitative statement:

- given $(\mathcal C_k, a_k)$, $S_k \to S_{k+1} \to o_{k+1}$ is Markov, so $u_k = I(S_k; o_{k+1} \mid \mathcal C_k, a_k) \leq I(o_{k+1}; S_{k+1} \mid \mathcal C_k, a_k)$, which is (ii′) at $o_{k+1}$ under the continuation;
- summing and using (g′): the (ii′) terms after $t$ sum to at least $I_{\pi'}(S_t; F_t \mid \mathcal C_t) + \sum_k r_k$.

So the state-and-law terms of the mismatch budget, summed over the future, are bounded below by the predicate's value under that continuation. Landed in "Why the future stream", with the late-reveal bit as the no-go for the per-step form. The Epistemic Status sentence now states only this. Check of the bound on the scalar random walk at steady state: (ii′) per step is $\tfrac12 \log(1 + (P_\infty + q)/r) = 0.481$ nats against $u = 0.135$.

## 4. The findings

- **F2.** I did not add "superseded" markers. The effort's standing keeps history out of Working Notes, and a marker over a false sentence is a softened ghost. Each of the four items is restated in current terms with the reader's attribution kept: what of the reader's idea carries over, and what the scope's line actually is. Where it served, I used 11's three-region figure: nothing left unknown, unknown but never shown, open and reachable. The AI-mathematician question now has a real answer from the segment's own principles. A prover built knowing its rules and checker, reading its proof state exactly, is case (d), and its errors are computation (the speed row). It is inside only where its declared world holds something its design did not fix. The integration record's history sentence is deleted. Not done: the existing "Resolved / Answered / Landed" markers on other audit-gold items are history too. They belong to I.5's Working Notes pass, so I left them.
- **F3, F4.** Landed as 11 proposed, re-derived. "Become a planner" now holds only with the state observed; a learner with a hidden state "may still be in, as a tracker". I wrote "may" because renewal does not guarantee membership at every time. The second way out (a blind channel) is a special case of the first or third, so the intro now says the three "can overlap and combine".
- **F5.** `#example-kalman` now has $y_t = x_t + n_t^{(a_{t-1})}$, $P(y_{t+1} \mid do(a_t))$, and the innovation's noise at $a_{t-1}$. No verdict or number in it changes.
- **F6.** For `cycle`, the defining text is NOTATION's "The Adaptive Cycle" section, and the first body use is `#the-cycle-in-motion-intro`. `#form-information-bottleneck`'s "cycle" is a book title. For `loop`, the defining text is `#def-action-transition`'s "Closing the loop", and the first body use is `#def-agent-environment`:41. Both entries' frontmatter and pointers are updated. `bin/term render` leaves `LEXICON.md` unchanged.

## 5. Not mine, noticed

`vsect revise --dry-run` on main shows an edit to `#def-causal-information-yield` that nobody has taken in. I did not touch that segment.

## 6. Where a checker may want to look

1. Whether absorption (F1) is well defined when an invariant variable enters only the *initial* law and no kernel. I believe item (f) makes it harmless, but the segment does not say so.
2. Whether "every policy over $\mathcal A$" should also range over the conduct *before* $t$. As written it does ("every run"), which is the stronger and, I think, the right rule.
3. The AI-mathematician restatement, which is a substantive claim in a Working Note.
