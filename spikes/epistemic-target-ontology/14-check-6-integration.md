# Integrating check 6: fresh noise, the agent's own budget, and `#example-kalman`

KR **A.1** (`msc/inside-out-2026-10/INTENT.md`): "`#scope-adaptive-system` carries the typed predicate or a defended alternative, and a cold reader checks the membership clauses on standard RL and on a Kalman filter." Top intent (Joseph): "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." Typed record: `reviews/scope-adaptive-system-integration-6.md`. The landed edit is commit `48cf787e`.

Author: Claude Opus 5.5, the A.1 round-6 integrator. Input: check 6 (`13-check-6.md`, `reviews/scope-adaptive-system-check-6.md`), plus two items the lead handed over for `#example-kalman` from the Part I round-2 check (`msc/inside-out-2026-10/part-i-round-2-check.md`, W4; vsect `review:part-i-round-2-check-1#F14`). I read the segment, `#def-observation-function`, `#def-action-transition`, `#def-chronica`, `#example-kalman`, `NOTATION.md`'s $\theta$, $\pi_0$ and GA-1 rows, check 6 and its record, the findings of checks 4 and 5 and reread 1, the GA-1 sentences of `#result-mismatch-decomposition`, `#deriv-mismatch-budget-attribution`'s Setting and Proposition 1, and the window and exit-time statements of `#result-persistence-condition` and `#deriv-sector-condition`. I did not read write-ups `06`–`12`.

## What changed, in brief

- **Fresh noise is now a definition, in two halves.** `#def-observation-function` carries *[Definition (fresh-noise)]*, and `#def-action-transition` carries *[Definition (fresh-transition)]*. Given the current state, the action and the law, the next observation and the next state are each drawn independently of everything earlier in the run. `#scope-adaptive-system` cites both wherever it said "the Markov commitment, with fresh noise", and says the property does not follow from the weaker statements. `NOTATION.md`'s GA-1 row says GA-1, in the form the results use, follows from fresh noise.
- **Non-vacuity** now speaks of the budget computed under the continuation in question, and adds what holds for the budget the agent actually runs (check-6 F2).
- **(g)'s clocked example** is in from $K - 1$ (check-6 F4).
- **(c)** says where reward goes and that the Dirichlet is a choice of $\pi_0$, not a prior (check-6 F5).
- **Smaller points (check-6 F6):** the collapse map's law row, the cut's "almost surely", and "support" scoped to the finite setting. This also changes `NOTATION.md`'s $\pi_0$ row and both definitions' opacity clauses.
- **`#example-kalman`:** the gain is re-indexed to $r_{a_{t-1}}$ (check-6 F3, check-5 F5). The structural-adaptation trigger now names the discrete analog it uses (W4 item 2). The exit-time sentence is replaced by a discrete exit-certainty argument and a marked remark about the exponent, with numbers (W4 item 1).

## 1. Fresh noise (check-6 F1)

### The finding re-derived

Check 6's world: known law, $\Omega_t = (t, z_t)$ with $z_1$ a uniform bit and $z_t = 0$ for $t \geq 2$, and observations constant except $o_K = \varepsilon_K := z_1$. Given $\Omega_K = (K, 0)$, $o_K$ is a fair coin, so the kernel is well defined. The transition is deterministic in $\Omega$, so it is Markov. GA-1 as worded holds because $\mathcal C_{K-1}$ is constant. At $t = 1$ the value is $I(z_1; o_K) = \log 2$. Every one-step part is zero, because $S_k = (k, 0)$ is known for $k \geq 2$ and $o_{k+1}$ is constant for $k + 1 \neq K$. So (g′)'s identity reads $\log 2 + \sum r_k = 0$, which is false. (h)'s step fails because $o_K = z_1$ given $(S_2, \mathcal C_2)$. The non-vacuity statement fails because every (ii′) is zero, (ii′) at $o_K$ being $I(o_K; S_K \mid \mathcal C_{K-1}) = 0$. Confirmed by hand.

### The transition half is needed on its own

Check 6 put the repair in `#def-observation-function` as the observation-side twin of the Markov commitment. Its proposed sentence covered the next state too, but the place it proposed covered only the observation. I looked for a world that respects every observation-side condition and still breaks the three items. There is one:

- Known law. $\Omega_1 = (1, x)$ with $x$ a uniform bit. $o_1 = x \oplus \varepsilon_1$ with $\varepsilon_1$ a fair coin independent of $x$, so $o_1$ alone says nothing about $x$.
- $\Omega_k = (k, 0)$ for $2 \leq k \leq K - 1$, $\Omega_K = (K, \varepsilon_1)$, and $\Omega_k = (k, 0)$ after $K$.
- $o_K$ reads the bit of $\Omega_K$ without noise. Every other observation is constant.

Then $\Omega_K$'s bit is a fair coin independent of $\Omega_{1:K-1}$, so the world is Markov in its own past. Each observation, given its state, is independent of everything earlier ($o_1$ is a fair coin given $\Omega_1$; $o_K$ is a function of $\Omega_K$), so the observation-side condition holds, and GA-1 with it. But $o_K \oplus o_1 = x$. The value at $t = 1$ is $I(x; F_1 \mid o_1) = \log 2$. Every one-step part is zero, because $S_{K-1} = (K - 1, 0)$ is known. (g′)'s identity fails at $k = K - 1$: $o_K$ is not independent of $S_1$ given $(S_{K-1}, \mathcal C_{K-1})$. (h)'s step fails: given $(S_2, \mathcal C_2)$, $o_K = o_1 \oplus x$ depends on $\Omega_1$. (Non-vacuity happens to survive here: (ii′) at $o_K$ is $I(\varepsilon_1; \varepsilon_1 \mid o_1) = \log 2$.) The world remembers $\varepsilon_1$ outside anything named as state.

So the property the scope needs has two halves. Given $(S_t, a_t)$, the next state is drawn independently of everything earlier, *and* given $(S_{t+1}, a_t)$ the next observation is. I put each half in the definition of the object it constrains.

### Where it lives, and why there

- **`#def-observation-function`.** It already relied on fresh noise in its own claim: "two pairs ($h$, distribution of $\varepsilon_t$) that induce the same kernel produce the same observations under every policy, so no history can tell them apart." That claim needs *both* halves.
  - Without fresh noise: noise that repeats, $\varepsilon_t = \varepsilon_{t-1}$ with a standard normal marginal, has the same one-step kernel as fresh noise, and for $o_t = \Omega_t + \varepsilon_t$ the difference $o_t - o_{t-1}$ shows the state's change without noise.
  - Without fresh transitions: take $o_t = \Omega_t + \varepsilon_t$ against $o_t = \Omega_t - \varepsilon_t$ with $\varepsilon_t$ symmetric (the same kernel), and $\Omega_{t+1} = \varepsilon_t$. The joint law of $(o_t, \Omega_{t+1})$ differs between the two, and $o_{t+1}$ shows $\Omega_{t+1}$.

  The definition now states fresh noise and says the kernel claim follows from it together with fresh transitions, because the run's law is then a product of kernels and policy. Its Epistemic Status says the claim does not follow from the kernel's definition alone and gives the repeating-noise case. A short Discussion paragraph, "Channels with memory", says where a drifting sensor bias goes: into $\Omega_t$. Then $\operatorname{Var}(o_t \mid S_t, a_{t-1})$ is only what each reading draws afresh.
- **`#def-action-transition`.** The Markov commitment was worded as sufficiency "for its own evolution". The world above meets that and still breaks the scope. The new clause states the commitment for the whole run, and a Discussion paragraph, "Sufficient for the run, not only for its own past", works the counterexample. Like the Markov commitment, the clause is without loss of generality: whatever the world remembers is declared as state.
- **`#scope-adaptive-system`.** The cut paragraph now says that, given $\theta$, the world is generated by its kernels, names both clauses, says (g′), (h) and the non-vacuity statement use the property, and says it is not implied by Markov-in-own-past plus noise independent of the chronica. (g′), (h) and the Epistemic Status cite it by that name.

With both halves, each step follows by weak union. $(\Omega_{k+1}, o_{k+1})$ is independent of $(S_t, \mathcal C_k)$ given $(S_k, a_k)$ (the agent's randomness, independent of the world, sits in "everything earlier"), so $o_{k+1}$ is independent of $S_t$ given $(S_k, \mathcal C_k, a_k)$. That is (g′)'s step. The data-processing step needs $o_{k+1}$ independent of $(S_k, \mathcal C_k)$ given $(S_{k+1}, a_k)$, which is fresh noise directly. (h)'s step follows by induction over the stream.

### GA-1 and the other users of "fresh noise"

GA-1 is stated on $\varepsilon_t$. The results use it only through the observation's law, $p(o_t \mid S_t, a_{t-1}, \mathcal C_{t-1}) = p(o_t \mid S_t, a_{t-1})$. I phrased the new definition on $o_t$ (the kernel level, which is what is identifiable), so it implies that form, not GA-1's $\varepsilon$-wording literally. The GA-1 row now says this in one sentence and names the run-wide property as what the scope and `#deriv-mismatch-budget-attribution`'s Proposition 1 use. I did not rewrite GA-1 itself. It stays the named assumption that a dozen Epistemic Statuses cite ("exact under GA-1"), and those citations remain true.

Grep of the corpus for "fresh noise" and GA-1, read at each hit:

- `#result-mismatch-decomposition`, `#def-mismatch-signal`, `#internal-external-decomposition` use only the chronica form. They are unaffected.
- `#deriv-mismatch-budget-attribution`, Proposition 1(ii), writes $\mathbb P_\pi(\mathcal C, \Omega_{0:t}) = [\prod_s \pi(a_s \mid \mathcal C_s)] \cdot [\text{environment and channel factors}]$. That is the run-wide property, asserted as following from GA-1 and (P), which do not give it. It now rests on the two new definitions. Its GA-1 line is also still in the state-only form, $(\Omega, a)$, while its own Setting and `NOTATION.md` condition on $S_t$. This is outside my lane, so I filed it as `item:deriv-mismatch-budget-attribution-1-prop-1-ii-s` (owner A.1), as the lead asked.
- `#deriv-tempo-additivity` uses "fresh noise" for noise independent across events, against a persistent bias. Under the new definitions a persistent bias is either an invariant (in $\theta$) or state, which is how that segment already treats it. Consistent.
- `#deriv-mechanism-counterfactual-separation` uses "fresh noise" in the structural-causal-model sense, for a replacement mechanism's exogenous noise. Unrelated.
- `#result-mismatch-decomposition`'s Working Notes keep "sensor drift that varies over time" open as a GA-1 failure. Under the new definition that drift is state, GA-1 holds, and the drift's contribution falls in term (ii). This bears on that open item. It is not my segment, so I record it here for whoever holds that segment.

Strengthen-first: nothing was softened. The items' conclusions stand as they were. What changed is that the declared world is now defined so that they are exact, and the definitions say what the scope had been assuming.

## 2. The agent's own budget (check-6 F2)

Re-derived. Along any continuation $\pi'$, $u_k \leq$ (ii′) at $o_{k+1}$ (data processing over $S_k \to S_{k+1} \to o_{k+1}$ given $(\mathcal C_k, a_k)$, which needs fresh noise). With (g′), the (ii′) terms after $t$ computed under $\pi'$ sum to at least $I_{\pi'}(S_t; F_t \mid \mathcal C_t) + \sum_k r_k$. Taking $\pi'$ to be the agent's own policy gives the statement for the running budget. The converse fails ($A = 0$: (ii′) is positive while the value is zero), which is why the text says "whenever" and not "exactly when", matching the annotation on check-6's C7. Witness that membership alone does not reach the running budget: an invariant hidden bit $b$ shown only after an action "look" that the agent never takes. Some continuation looks, so the loop is in at every $t$. Under the agent's policy every observation is constant, so every (ii′) is zero. Landed in the Epistemic Status, close to check 6's proposed wording.

## 3. (g)'s clocked example (check-6 F4)

Re-derived. $\Omega_t = (t, x_t, x_{t-1})$ with $x_t$ fresh, and $o_t = x_{t-1}$ for $t \geq K$, constant before. At $t = K - 1$ the target holds $x_{K-1}$, and $o_K$ reports it, so the loop is in. At $t \leq K - 2$ the target holds $x_t$ and $x_{t-1}$, neither of which is ever reported (the first report is $x_{K-1}$), so the loop is out. At $t \geq K$ the target holds $x_t$, which $o_{t+1}$ reports. The new wording says "out before $K - 1$ and in from $K - 1$, the step whose draw the first report shows."

## 4. Standard RL as the reader brings it (check-6 F5)

Both points were already true of the segment's ingredients and absent where an RL reader looks, so I added them at the end of (c):

- **Reward.** Drawn by the transition into the observed state, $\Omega_t = (s_t, \text{reward}_t)$. The row at $(s, a)$ is then a joint law of successor and reward, and (c)'s strict-concavity argument applies to it. A bandit, with one state and unknown reward laws, is in on those laws alone.
- **No prior.** The Dirichlet is a choice of $\pi_0$, not the learner's prior. A learner not given its transition probabilities has every row possible. With finitely many states, actions and reward values, (h′) makes every $\pi_0$ with that support give the same membership, so a Q-learner is in. With real-valued rewards, (h) gives the same membership for every $\pi_0$ with the declared one's null sets.

## 5. Smaller points (check-6 F6)

- **Collapse map.** The law row now reads "law that some conduct can still show". By (f), law that no conduct can show is out.
- **The cut's "$\pi_0$-almost surely".** Now "under every policy over $\mathcal A$, stays the same along the run almost surely (under the law of the run that $\pi_0$ and that policy induce)".
- **Support and topology.** I did not name a topology outside (h′). The Definition now says $\pi_0$ is "declared on" the set of possible worlds. By (h), only its null sets matter, and the declaration fixes them. In the finite setting the kernel entries carry the Euclidean topology, and the support is the closure of the possible worlds. I considered "carried by the set" for the general case and rejected it for the finite one: it is weaker than "support is the closure of the set", and (h′)'s "the set alone fixes membership" needs the stronger statement. `NOTATION.md`'s $\pi_0$ row matches. Both definitions said "whose support only the agent's design-time knowledge cuts down" and now say "whose set of possible worlds"; the Epistemic Status's "fixing the support" is changed the same way.

## 6. `#example-kalman`

- **Index (check-6 F3, check-5 F5).** $K_t = P^-_t / (P^-_t + r_{a_{t-1}})$ and $U_o = r_{a_{t-1}}$, with one sentence giving the reason: the gain applied to $\delta_t$ carries the noise of the reading it corrects. No number changes. The causal paragraph's $P(y_{t+1} \mid do(a_t))$ through $r_{a_t}$ was already right.
- **W4 item 2, the structural-adaptation trigger.** The sentence cited the continuous feasibility condition $R^2 \gt n\sigma_{\text{env}}\sigma_\nu$. It now says this filter runs in discrete time and uses the discrete analog, stated in place: some fixed gain keeps the stationary prior error $V(K)$ inside the region iff the smallest such error, the Kalman prior $P^-$, fits. I checked numerically that $V(K) = (q + K^2 r)/(1 - (1 - K)^2)$ has its minimum at $K = 0.390$, equal to $P^- = 0.6404$. $R^2 = 0.0064$ is a hundredth of that, so the verdict stands with a wide margin.
- **W4 item 1, the exit sentence.**
  - The old text cited Prop A.1S and Corollary A.1S.1 for "the error will leave it", and Prop A.1S-τ for the exponent, all continuous-time. Exit now has its own discrete argument. Inside the region $\lvert (1 - K)e_t \rvert \leq R$, so any step whose disturbance $v_t - K n_t$ exceeds $2R$ in size exits. That has the same positive probability at every step, so the error leaves with probability one.
  - The Kalman-gain claim is a marked *[Discussion]* remark. For a stationary Gaussian AR(1) the expected stay grows like $\exp(R^2/(2V(K)))$, the discrete counterpart of $\kappa_R = \alpha R^2/\sigma_w^2 = R^2/(2\,\mathrm{Var}_{ss})$ for the linear corrector. $V$ is smallest at the Kalman gain, so the exponent is largest there.
  - The remark says the claim is about the exponent, not the stay at this $R$, and gives the numbers. I solved the exit-time integral equation on a grid (trapezoid rule; 401, 801 and 1601 nodes agree to three decimals). The expected stay from zero error at $R = 1.4$ is $17.50$ steps at $K = 0.39$ and peaks at $19.15$ near $K = 0.275$; it is $6.91$ at $K = 0.81$. At $R = 3$ and $R = 4$ the log stay is $8.69$ and $14.38$ at $K = 0.39$, against $8.06$ and $13.09$ at $K = 0.25$, so the exponent's ordering takes over as the region widens. The script is in my scratchpad, not committed. Its recipe is the one in this paragraph.
- `#deriv-sector-condition`:303's "exponent capped at the Kalman gain" is the Part I integrator's. The lead is routing it.

## 7. The ledger

- **Revisions.** All four segments are revised as REDEFINED. `NOTATION.md` is not a vsect record. The `example-kalman` revise also classified the earlier unclassified edit, `043a44c9`, against the new text, which check 6 had flagged as "(no revise event)". Redefined is the true classification for that pair, since it includes this round's change. Editing the two definitions lapses checks across most of the corpus, through `#def-chronica` and everything that depends on the loop. The lead knew this before I recorded it.
- **Disposals I made, as a second mind to revision `48dd5554`** (I did not author it), each reason recorded with the act:
  - check-5: C11/finding, C12/finding, F1, F2, F3, F4, F6;
  - check-4: C6/finding, C7/finding, F1, F2, F3, F4, F5, F6.

  I re-read each finding against that text. C12/finding is answered as far as it asked: the overclaim it named was replaced by an exact statement. What remained of that clause was check-6's C7, landed here.
- **Not disposed by me:**
  - Check-5 F5 and all of check-6's findings are answered by my own revision, so they are for a different mind.
  - Reread-1 F1 is answered in part. The class of possible worlds is now named, but its hard-coded-guess and pretrained cases live in the open question `question:where-is-the-line-between-what-an-agent-s-design`, and a finding cannot be closed in part.
  - Reread-1 F5 needs `CURRENT-VOL1.md` and two terminology entries I did not read.
  - Check-4 F7 and F8 target other segments.
- **Filed.** `item:deriv-mismatch-budget-attribution-1-prop-1-ii-s` (owner A.1).

## What I did not check

- Downstream segments beyond the "fresh noise"/GA-1 grep. Whether any result elsewhere quietly allows a world with memory outside $\Omega$ and is now narrowed by definition, for example in Volume 3, where the context window is state.
- `#def-agent-environment`, beyond what the definitions cite.
- The cited literature (the relata item for it is still open).
- Whether `#result-mismatch-decomposition`'s open drift item should now be closed. That needs whoever holds that segment.

## On the brief and the process

The brief left the choices open and gave the coordination facts, and that is what made the transition half findable. I was looking for where the repair *belongs*, not for how to land a proposed sentence. One process note. Check 6's own repair sentence was right in content, and its proposed home would have shipped half of it. The counterexample that shows the second half is the first one's mirror image: memory kept outside $\Omega$ on the transition side instead of the channel side. A checker's habit of asking "what is the twin of my counterexample on the other kernel?" would have caught it a round earlier.
