*KR: C.2 — "Strengthenings C1–C3 (exit time, loop identification, allocation vs distortion coupling) are independently checked, then landed or refuted." Top intent (Joseph, 2026-10-30): "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself."*

# De novo feedback 1 — independent adversarial pass on the loop-identification spike

*Opus 5.5, 2026-10-30, as independent checker (not the spiker, not the integrator). Every file in this directory was read whole. Also read whole or at the cited sections: `#der-loop-interventional-access`, `#def-value-object`, `#def-model-sufficiency`, the policy and update sections of `#form-complete-agent-state`, `#der-recursive-update`, `#der-directed-separation`, `#hyp-edge-update-via-gain`, `#def-strategy-dag`, `#impl-causal-access`, `#der-causal-hierarchy-requirement`, `#def-pearl-causal-hierarchy`, the B.1 commit `8d3d481f`, `doc/sop/spikes.sop.md`, and audit-routing §§0–5. The lemmas were re-derived from §0's commitments before reading the spike's proofs. The scripts named below are in the scratchpad (`/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf/207cfbc3-93fe-48b4-9873-c6f02a94414d/scratchpad/`). Their outputs are quoted here, and each is small enough to rewrite from its description.*

## Verdict in one paragraph

The spike's direction is right and much of it survives. Parent adjustment at the policy's inputs is free. Positivity and coarsening are where the real costs are. The value object's $M_t$-stratum is confounded by outcome statistics held in $G_t$, which I reproduced and strengthened. The realized-action conditioning in $S(M_t)$ is the wrong object for a causal reading. (C3) reads correctly as intention-to-treat. Three of the spike's formal statements are false as written, though, and two of them sit in the headline:

- Lemma 1(b)'s (P-stream) clause. Its "after review" correction is itself wrong.
- Proposition 4, the deterministic no-go. The spike's own witness refutes it.
- The "iff" in Proposition 5, which also drags along Lemma 3's positivity label.

Separately, the sentence the spike targets is no longer in canon. B.1 rewrote it four minutes after the neighborhood map was stamped. The integration plan's §1 therefore has no target, and B.1's replacement records carry two of the same overclaims. None of this calls for softening. Each false statement has a sharper true version, given below, and two of them are strengthenings that make the result more permissive than the spike claimed.

## 1. Lemma 1(b) under (P-stream): "retains the past actions" is not enough **[counterexample, exact]**

The clause reads: ignorability at $X_t$ holds "under (P-stream) when $X_t$ retains the past actions $a_{\lt t}$ (or the past coins)". The proof treats each past action $a_s$ only as a *chain* node on the path $U_t \leftarrow U \to U_s \to a_s \to \Omega_{s+1} \to \cdots$. But $a_s = \pi(X_s, U_s)$ is also a *collider* between the coin side and the environment side. Conditioning on $a_s$ without $X_s$ opens $U_t \leftarrow U \to U_s \to a_s \leftarrow X_s \leftarrow o_s \leftarrow \Omega_{s-1} \to \cdots \to \Omega_t$. In form (a) this path is harmless because $\mathcal C_t$ contains every $o_s$, which blocks it at a chain node. In form (b) nothing blocks it.

Witness (`a_pstream.py`, exact enumeration). The environment has a static bit $\theta \sim \mathrm{Bern}(1/2)$ with $o_1 = \theta$. One coin $u \sim \mathrm{Bern}(1/2)$ is used at both steps, which is (P-stream) with $U$ independent of the environment. The agent sets $X_1 = o_1$ and $a_1 = X_1 \oplus u$. Next it sets $X_2 = a_1$: it retains its past action and drops its observation, a legitimate recursive update under (M). Then $a_2 = u$, so $P(a_2 = a \mid X_2) = 1/2$ and positivity holds. The outcome is $Y_2^{(a)} = \mathbf 1[a = \theta]$.

```
X2=0 a=0: P(a|X2)=1/2  on-policy P(o=1|a,X2)=1  interventional P(Y^a=1|X2)=1/2
X2=0 a=1: P(a|X2)=1/2  on-policy P(o=1|a,X2)=1  interventional P(Y^a=1|X2)=1/2
X2=1 a=0: P(a|X2)=1/2  on-policy P(o=1|a,X2)=0  interventional P(Y^a=1|X2)=1/2
X2=1 a=1: P(a|X2)=1/2  on-policy P(o=1|a,X2)=0  interventional P(Y^a=1|X2)=1/2
```

The confounding is maximal and positivity holds throughout. The true clause is that $X_t$ retains the past coins $U_{\lt t}$, or retains enough to determine every $X_s$ on which an earlier coin acted. The chronica satisfies the second, which is why (a) stands. With the coins retained, $U_t \perp (\text{env}, X_t) \mid U_{\lt t}$ gives $U_t \perp (\Omega_t, N_t) \mid X_t$ directly.

What inherits it:

- the proof of Lemma 2(S), which cites "fresh coins, or past actions retained in $X_t$";
- Lemma 2($\Pi$) and Lemma 3, which use Lemma 1 at $X_t$;
- the §7 table row, which calls the shared-seed case "caught in review";
- the README and the INDEX headline (`66eb1b25`);
- the debrief's "or the agent has to remember its past actions".

The fixed-schedule example in §1 is still a correct illustration of *a* (P-stream) failure. What is wrong is the cure attached to it.

## 2. The target sentence is already gone from canon; re-base the integration on B.1's text **[provenance]**

The neighborhood map is stamped 14:20 against `8ef2862e`. Commit `8d3d481f` (B.1, 14:24:06) rewrote `der-loop-interventional-access` Formal Expression `:41`. The pickaxe on "generic for any agent whose action depends" shows the sentence added in `52d85b28` and deleted in `8d3d481f`. The sentence at HEAD already says that an agent whose decision state is a function of $H_t$ "satisfies (C2) given $H_t$ by construction… what it then needs is (C1), which a policy deterministic in that state fails for every action it does not take". B.1 also added Claim Records to both `der-loop` and `def-value-object` that state the by-construction identification claim and the deterministic no-go.

So the plan's "Delete the sentence at `:41`" has no target. The spike's line references (`:90`, `:118`, `:52`) have also drifted. The `der-loop` Working-Note line about LLM policies is now near `:120`, and the `impl-causal-access` passage is at `:37`. `#der-causal-hierarchy-requirement`'s RL example (A11) was already scoped by B.1, at `:82`. Under `spikes.sop.md` Refinement 4(b), where the core landed by a parallel path, what the integrator routes on is the spike's *distinctive payload*:

- the corrected randomization clause (§1 above);
- Lemmas 2 and 3 and the coarsening trade-off;
- the $G_t$-confounded $Q_O$;
- the collider in $S(M_t)$'s formula;
- (C3) as intention-to-treat;
- the re-typing of "un-introspectable cause".

B.1's new text carries defects the spike would catch, and the integrator should fold them into the same landing:

- **B.1's `der-loop` record falsifier** reads: "an agent that discards its decision context and nonetheless recovers unconfounded effects on-policy." Lemma 2 says this happens whenever the discarded part satisfies (S) or ($\Pi$). Canon's own Discussion asserts it happens: tabular Q-learning conditions on $s$ while its policy also reads the Q-table. As written, the falsifier names a situation canon claims is real. The falsifiable form is an agent that discards a component which fails (S) and drives the action (§4 below gives the exact condition), yet recovers unconfounded effects.
- **B.1's records** list "a cause of the choice the agent did not record or cannot introspect" as a (C2) failure. The spike's re-typing as (F), (E) or a scope exit is better and should replace it.
- **B.1's `der-loop` record** and **`def-value-object` record** state the deterministic no-go in the form §3 below refutes.
- **B.1's `def-value-object` falsifier** ("a disciplined agent whose $Q_O$ varies with $G_t$ at fixed $(M_t, \ldots)$; none has been looked for") is vacuous as stated. $Q_O(M_t, a)$ is defined as an $M_t$-conditional and cannot vary with $G_t$. The substantive form is the spike's witness: $\mathbb E[Y^{(a)} \mid M_t, G_t]$ varies across $G_t$, so the $M_t$-stratified on-policy estimate is confounded.
- **Cascade gap.** `#der-causal-hierarchy-requirement:18` still reads "matters whenever the agent's action-selection policy correlates with unobserved confounders — generic for any agent with internal state, plans, or memory." That is the same refuted genericity, live in canon, and it is not in the spike's touched-segments list. B.1's corrected `:82` also gives the wrong reason: "In a fully observed MDP the policy depends on $s$ alone." That is false for a learning agent whose policy reads its Q-table, a point the spike itself makes in §4. The conclusion holds by stationarity, not by the policy's signature.

Neither of the two I.3-shaped items the plan names has been filed. `vsect open` shows nothing concerning `der-loop-interventional-access` or `def-value-object` from this spike.

## 3. Proposition 4 is false as stated; the spike's own witness refutes it **[counterexample, exact; simulated]**

The statement is that a deterministic policy, with the learner conditioning on $X_t$, leaves $P(o_{t+1} \mid do(a'), X_t)$ "not determined by the on-policy law". The proof builds two SCMs that differ in $T(\cdot \mid \Omega, a')$ "at every visited $(X_t, \Omega_t)$". But $T$ is indexed by $\Omega$ alone, a direct consequence of (M): the environment does not read the agent's state. If $a'$ is taken at the same $\Omega$ under some other decision state $X'$, the two SCMs no longer agree on-policy. Identification at $X_t$ can run through an outcome-sufficient coarsening $Z$ with positivity, via $P(Y^{(a')} \mid X_t) = P(Y^{(a')} \mid Z) = P(o \mid a', Z)$. That is the spike's own Lemma 2 and Proposition 5.

Two instances:

- **Greedy tabular Q-learning in a fully observed, stationary MDP** at $\varepsilon = 0$. $X_t = (s_t, \text{Q-table})$ and the policy is deterministic in $X_t$. Different Q-tables at the same $s$ pick different actions. $Z = s$ is outcome-sufficient by stationarity, the spike's own "goal-purity by stationarity", so every contrast at $s$ observed under any Q-table is identified at every $X_t$ with that $s$. This is the loop segment's own motivating illustration.
- **The spike's witness at $\varepsilon = 0$.** §4 says "only 16 of 184 visited decision states ever saw both actions … the value object has no identified contrast anywhere else and is running on extrapolation." But $Z = (t, \alpha_1, \beta_1)$ is exactly outcome-sufficient. The likelihood of $\theta$ along any path is $q_1^{\alpha_1 - 1}(1 - q_1)^{\beta_1 - 1} \cdot 2^{-n_0}$, and the policy factors carry no $\theta$. Different action-0 counts inside the same $Z$-cell send the greedy policy to different actions. In `b_eps0.py` (seeds 1, 2, 3) the result is the same each time: of the 168 single-action $X$-cells, 89 have the untaken action's effect identified via $Z$, 46% of their visits. `b2_check.py` estimates $P(o = 1 \mid do(1), X)$ at $a = 0$-only cells from the $Z$-cell's $a = 1$ data and compares it with the hidden-$\theta$ truth. Across 41–61 cells with at least 2000 samples, the maximum deviation is 0.034, 0.020 and 0.021 for seeds 7, 11 and 23, consistent with sampling noise. At cells with $\alpha_1 = \beta_1 = 1$ the identified value is exactly $1/2$ by construction.

The true statement is still a real no-go, and sharper. A contrast at $X_t$ is identified from on-policy data only if some coarsening $Z$ of $X_t$ is outcome-sufficient (or meets the condition in §4) *and* has positivity for that contrast. Positivity at $X_t$ itself is not required. Where no such $Z$ exists, the spike's construction goes through once $\Omega$ is allowed to carry what distinguishes the $X$-cells. Kalman + LQR is the clean instance: the outcome depends on $\hat x$, the action is $-K\hat x$, and no coarsening keeps one without the other. The headline "positivity is the gate no conditioning set removes" becomes "positivity at *some* outcome-sufficient set is the gate". The plan's §0.4 half-anticipated this. Repair (c)'s pointer is also off: "the $0.59$ column, which is the correct $M_t$-marginal once re-weighted by $P(G_t \mid M_t)$". Re-weighted that way, the $X_t$ interventional values average to the $\approx 0.50$ already printed in the $M_t$ interventional column. The $0.59$ is the $n_1$-weighted on-policy conditional.

## 4. Lemma 2's two routes are not exhaustive; Proposition 5's "iff" is false, and the true condition is more permissive **[counterexample + strengthening, exact]**

Proposition 5 says the contrast at $Z$ is identified by adjustment iff positivity holds and (S) or ($\Pi$) holds. Counterexample: $X_t = (Z_t, W^\pi_t, W^Y_t)$ with $W^\pi \perp (W^Y, \Omega_t) \mid Z$. The policy reads $W^\pi$, for example a pure preference component of $G_t$. The outcome-relevant information sits in $W^Y$, for example stale outcome statistics the policy no longer consults. (S) fails because $Y$ depends on $W^Y$. ($\Pi$) fails because $a$ depends on $W^\pi$. Yet $a_t \perp Y^{(a)} \mid Z$, and the graph is faithful.

The general condition, which I derived rather than found in the spike: let $R = r(X_t)$ be a policy-sufficient reduction ($a_t \perp X_t \mid R$, under fresh coins) and $S = s(X_t)$ an outcome-sufficient one ($Y^{(a)} \perp X_t \mid S$). Then $R \perp S \mid Z$ implies $a_t \perp Y^{(a)} \mid Z$, because $P(Y \mid R, Z) = \mathbb E[P(Y \mid S) \mid R, Z] = \mathbb E[P(Y \mid S) \mid Z]$. (S) is the case $S \subseteq Z$ and ($\Pi$) the case $R \subseteq Z$.

For the value object this matters directly. "Goal variation is the agent's own instrument iff goal-purity" ($Y^{(a)} \perp G_t \mid M_t$) overstates what is needed. The instrument works when the *policy-relevant part* of $G_t$ is outcome-independent of the *outcome-relevant part* of $X_t$ given $M_t$. Outcome statistics may sit in $G_t$ harmlessly as long as the policy does not read them. Proposition 5's "iff" should become a sufficient condition, with this condition as the general form. I would also re-examine "goal-purity given the model" before it gets a canon name: the premise that needs naming is about the policy-relevant part, not all of $G_t$.

## 5. Lemma 3 needs positivity at $X_t$, not at $Z$ or $M_t$, and the goal-instrument case is where the two differ **[label slip with consequences]**

Lemma 3(ii) is titled "positivity at $Z$" but states $P(a_t = a \mid X_t) \gt 0$ for every $X_t$, which is positivity at $X_t$. The proof needs the $X_t$ form. The slip propagates in three places:

- §2's third bullet says the on-policy predictive statement coincides with the needed one "under positivity at $M_t$".
- Plan §3 suggests rewriting `def-model-sufficiency` to "for agents with positivity at $M_t$".
- The debrief says "every action has positive probability at every state".

Positivity at $M_t$ does not suffice. Take the goal-variation instrument: $\pi(M_t, G_t)$ is deterministic, so positivity holds at $M_t$ but fails at $X_t$. That is exactly Lemma 3(iii)'s two-point counterexample with $Z = M_t$. An agent whose action variation comes from its goals passes the on-policy sufficiency test of $M_t$ for free, and cannot detect goal-impurity from inside. This is a real consequence worth landing: the agent can *use* goal variation as an instrument only under a premise it cannot *test* on-policy. Testing it needs exogenous variation at $X_t$. A smaller wording point: Lemma 3's "iff positivity" is established in one direction plus an existence counterexample. At cells where the $Z$-cell contains a single $X_t$ value the two notions coincide without positivity.

## 6. (P) is not "already in canon"; under AAT's own completeness every agent is deterministic in its complete state **[framing, consequential]**

§0 says the four commitments are "each already in canon". Canon writes $a_t = \pi(M_t, G_t)$, which is deterministic. Under `#der-recursive-update`'s C3, completeness (" $M_t$ summarizes everything the agent retains"), a retained PRNG state is part of $M_t$. Under C2, mediated access, a fresh external coin reaches the agent as an event, and becomes part of $X_t$ when it is read. Either way, $a_t$ is a deterministic function of the complete state. The spike's $U_t$ sits *outside* $X_t$ and is environment-independent. That is a decomposition of the agent's state into a decision part and a randomizing part, plus a provenance premise on the randomizing part. It is a genuine new premise, and the clock-seeded instance shows it can fail silently.

A consequence the spike should state: Lemma 1 is the special case of Lemma 2 in which the dropped component is the coin and (S) holds for it by provenance. Read this way, the whole result is a single statement about coarsenings, with "the policy's inputs" meaning the complete state minus a known-outcome-irrelevant component. That fits §3's corrected no-go above, and it changes what a (P) landing should say. (P) must be stated as a premise, not cited to `#form-complete-agent-state:38`.

## 7. Directed separation does deliver half the $M_t$-rung; the "mislocated" verdict on `def-value-object:50` is overstated **[exact; enumerated]**

`d_kappa.py` takes an exogenous goal $G$ (pure by construction), a world bit $W$ with $o = W$, and a goal-coupled update in which, with probability $\kappa$, the update writes $G$ into $M$ and otherwise writes $W$. The policy reads $G$ with positivity, and $Y^{(1)} = W$.

```
kappa=0: M=0: on-policy 0.000 vs interventional 0.000; M=1: on-policy 1.000 vs interventional 1.000
kappa=1/10: M=0: on-policy 0.011 vs interventional 0.050; M=1: on-policy 0.917 vs interventional 0.950
kappa=3/10: M=0: on-policy 0.039 vs interventional 0.150; M=1: on-policy 0.782 vs interventional 0.850
kappa=1/2: M=0: on-policy 0.083 vs interventional 0.250; M=1: on-policy 0.679 vs interventional 0.750
```

At $\kappa \gt 0$, $M_t$ is a collider of $G$ and $W$, so conditioning on it makes even an exogenous goal outcome-informative, and the $M_t$-stratum is confounded. Canon's sentence at `def-value-object:50` ("a goal-blind $f_M$ blocks the $G_t \to f_M \to M^+$ confounding path") is a correct statement of exactly this path. So there are two distinct routes to goal-impurity at $M_t$:

- $f_M$ absorbs the goal, which is a collider at $M_t$. Directed separation removes this route.
- $f_G$ absorbs the world, through the strategy counts. Directed separation permits this route.

The canon residual, "latent environment confounders that bypass $M_t$", literally covers the second route, since $\Omega \to e \to f_G \to G_t \to a_t$ bypasses $M_t$. What canon lacks is (i) naming that the bypass runs through the agent's own $G_t$, a route canon's own learner instantiates, and (ii) consistency in its gate. Its (C2) is stated "given history", where ignorability is automatic, while its target is at $M_t$. That inconsistency is the defect. "Mislocated" would invite a rewrite that drops the correct collider clause.

Two related points:

- The spike's LLM corollary says $\kappa \gt 0$ "biases $M_{t+1}$ — a belief-quality problem — and leaves $(a_t, o_{t+1})$ unconfounded given $X_t$". That is true at $X_t$ and false at the $M_t$-rung the value object uses. `impl-causal-access:37`'s open question ("whether Coupled components also fail the loop's sequential-ignorability condition") gets a two-part answer: no at $X_t$, generically yes at $M_t$.
- The premise the spike names, "goal-purity given the model", conflates the two mechanisms. A naming pass should keep them separate.

## 8. The $M_t$-rung witness survives on a single trajectory, and is stronger there **[reproduced; strengthened]**

The original witness pools 40,000 episodes, each with its own $\theta$. That is a population-of-deployments phenomenon, the same `#scope-agent-identity` seam the plan raises for $X_0$. For the singular agent within one episode, $\theta$ is fixed and its own action-1 rate converges to $q_1(\theta)$. `c_singular.py` runs a single long trajectory of 2,000,000 steps. $\theta_t$ switches with hazard $h$, $G_t$ holds Beta counts with forgetting ($\lambda = 0.9$), the policy is $\varepsilon$-greedy with $\varepsilon = 0.1$, and $M_t$ is constant. The interventional target is the time-average of $q_1(\theta_t)$ over the $M$-stratum.

```
h=0.0005: M-stratum on-policy E[o|a=1]=0.7178 interventional=0.5089 gap=+0.2089 | binned-G gap=+0.0024
h=0.005:  M-stratum on-policy E[o|a=1]=0.6902 interventional=0.4939 gap=+0.1963 | binned-G gap=+0.0026
h=0.05:   M-stratum on-policy E[o|a=1]=0.5944 interventional=0.4996 gap=+0.0947 | binned-G gap=-0.0006
```

The gap is two to three times larger than in the episodic version, and conditioning even on a coarse binning of the policy's input closes it. I recommend this variant as the witness of record, because it lives inside the singular-trajectory scope the loop segment claims. The original episodic gaps also reproduce across seeds (seed 2: $+0.0923$ / $+0.1155$; seed 3: $+0.0927$ / $+0.1155$ at $\varepsilon = 0.2 / 0$).

## 9. The $S(M_t)$ finding holds; two overreaches around it

- The two-bit echo-agent checks by hand: numerator $0$, denominator $1$ bit, $S = 1$, and the one-step model is insufficient by $1$ bit.
- §2 also claims the echo agent's "$M_t$-conditioned action-effect estimates are confounded". The example does not show this. Its $a_t$ is constant, so there is no action contrast to confound. That clause should go, or get its own example.
- The proposed repair $I(\mathcal C_t; o_{t+1:\infty} \mid M_t, do(a_{t:\infty}))$ is underspecified. Mutual information "given $do$" of a fixed action sequence still needs a distribution over sequences to average over, or a supremum over sequences.
- The open-loop reading has standard prior art the spike does not credit: predictive state representations, whose "tests" are action sequences held as exogenous (Littman, Sutton & Singh 2002). It is the natural citation for "the actions are held as exogenous inputs."

## 10. Smaller items

- Pearl's statement that the parents of $X$ satisfy the back-door criterion is "Adjustment for Direct Causes", Theorem 3.2.2 in §3.2.3 of *Causality* (2nd ed.), as best I recall. The spike cites "§3.3". Check it against the book before landing.
- arXiv:2606.24160 exists with the stated title, authors and date (Bareinboim, Zhang, Lee, 23 June 2026). I verified existence only and did not read Def. 13 or Lemma 1. The spike's own label says the relata entries are bib-only.
- I confirmed the grep result that NeurIPS Paper 3's `src/` has no "ignorab", "confound" or "d-separat" hits.
- The canon (C1) wording ("every action … taken with nonzero probability *across the agent's history*") is positivity at the coarsest set. After §3 it should name the set it is positivity *at*, like the rest of the A5 relabeling.
- SOP note: the spike reports a found canon defect while being read-only by disposition, which is correct. Audit-routing §4.2's fast path still wants the replacement *wording* checked by an external eye before the write. The B.1 records show a parallel lane already wrote wording on these exact sentences without the spike.

## What I re-derived versus read, and what this pass did not do

Re-derived independently, before reading the spike's proofs:

- Lemma 1(a), which holds.
- Lemma 1(b): it holds under fresh coins and fails under (P-stream) with actions retained (§1).
- Lemma 2: both routes are sound; the "iff" fails (§4).
- Lemma 3(i)–(iii), sound under positivity at $X_t$ (§5).
- Proposition 4, which fails as stated (§3).
- The echo counterexample, which holds.
- The (C3)-as-ITT reading, which holds.
- The collider analysis of §7.

Re-run or newly simulated: the spike's witness over three seeds, and the five scratch scripts named above. Read but not re-derived: the literature attributions other than the arXiv existence check. Not done:

- the horizon-$N_h$ g-formula extension, which the spike also leaves open;
- whether `#def-model-class-fitness` and `#result-structural-adaptation-necessity` lean on the realized-action reading of $S$;
- the C3 sibling spike's use of the shared premise;
- any population-level ($X_0$-correlated) analysis beyond noting the seam.

This pass found and checked the items above. Its silence on anything else in the spike is not a certification that it holds.

I will stay on the line for follow-ups.
