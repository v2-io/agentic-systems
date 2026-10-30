# 09 — An independent adversarial check of `#scope-adaptive-system` at 1a98d12b

**KR A.1** (`msc/inside-out-2026-10/INTENT.md`), under the top intent *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."*: `#scope-adaptive-system` carries the typed predicate or a defended alternative, and a cold reader checks the membership clauses on standard RL and on a Kalman filter.

*Checker: Opus 5.5, 2026-10-30, independent of the integrator and of 07's reader. I re-derived the segment from its text at 1a98d12b (unchanged at 094a41d2) and its four `depends:` segments, formed my findings, and only then read 08 §1.1, §1.6 and §2 and the open ledger, to avoid duplicating what is already open. The typed record is `reviews/scope-adaptive-system-check-4.md`. Every number below comes from the script in the appendix.*

## 1. What holds

Re-derived by hand, numbers reproduced by script:

- **(b).** Given $\mathcal C_t$, $x_t$ and each $o_{t+j}$ are jointly Gaussian with cross-covariance $P_t (A^j)^\top C^\top$, and later noise is independent of $(x_t, \mathcal C_t)$. Zero cross-covariance for every $j \geq 1$ is independence from every finite block, hence from the stream. The one-step closed form is $\tfrac12 \log \det N_{\text{tot}} - \tfrac12 \log \det N$, with $N_{\text{tot}} = C A P_t A^\top C^\top + N$. For the scalar random walk, $P_\infty = (\sqrt5 - 1)/2$, the one-step part is $0.1346$ and the whole-future value is $\tfrac12 \log(P_\infty / P_s) = 0.1618$, where $1/P_s = 1/P_\infty + 1/(P_\infty + 1)$ (forward filter combined with the backward predictor).
- **(c).** Membership by strict concavity; the $+\infty$ value by the singularity of joint and product on the graph of the frequency limit; the $(K-1)/(2n)$ rate. On the rate, Clarke–Barron gives the cumulative $I(\text{row}; X^n) = \tfrac{K-1}{2} \log n + O(1)$, which alone does not fix the increments. They are fixed because the increments $I(\text{row}; X_{n+1} \mid X^n)$ are non-increasing: by exchangeability, $H(X_{n+1} \mid X^n)$ is non-increasing. A monotone sequence whose partial sums are $\tfrac{K-1}{2} \log n + O(1)$ is asymptotic to $\tfrac{K-1}{2n}$, by comparing the block sums over $(n, \lambda n]$ and letting $\lambda \to 1$. The script shows the ratio to $(K-1)/(2n)$ at $0.98$ and $0.97$ by $n = 200$ for $K = 2, 3$.
- **(h).** A reweighting by a density in $(\Omega_1, \theta)$ that is positive $\pi_0$-a.e. changes the law of $(S_t, \mathcal C_t)$ to an equivalent one and leaves the kernel of $F_t$ given $(S_t, \mathcal C_t)$ alone, so conditional independence transfers both ways.
- **(h′).** All three support facts, the finite-block reduction, and the clock counterexample.
- **The housing result.** Also the claim that moving an invariant coordinate between $\Omega_t$ and $\theta$ changes no mutual information: the reduced target is a sufficient statistic of the other.
- **(a), (d), (e), (f).** Also (g) as stated for $\theta$.
- **The (ii′) sentence.** Given $(\mathcal C_t, a_t)$, $S_t \to S_{t+1} \to o_{t+1}$ is Markov, so the one-step part is at most (ii′) at $t+1$. With $A = 0$ the converse fails.

**Downstream use of membership in $t$ (07 §5).** I read every line of the 21 files that cite the slug. None of them takes membership uniformly in $t$ as a premise:

- `#result-mismatch-decomposition` step 1 says its identity does not use the scope.
- The examples (`#example-kalman`, `#example-bandit`, `#example-strategy`) assert membership at every $t$ for their own worlds.
- The rest cite the scope descriptively.

I did not walk second-hop dependents.

## 2. The finding that changes the most: the two kinds of warrant are not state and law

The Discussion's "Two kinds of warrant" opens: *"A system can be in scope because the state is unknown, or because the law is unknown, and the two behave differently in time."* It says a moving state's uncertainty *"is renewed every step, so a Kalman filter's warrant is standing"*. It says an invariant law's uncertainty is *"spent one step at a time"*, with the one-step part decaying like $(K-1)/(2n)$. Item (g), tagged exact, ends: *"a state that keeps moving keeps renewing what can be revealed about it."* The paragraph closes: *"A drifting law is slow state, which is why the realistic case … keeps a standing warrant."* 08 §1.1 considered one counterexample: a state coordinate with no process noise and $A = 1$. It noted that the invariance cut names that coordinate law, so "the standing vs spent carve survives", and it listed as its own open worry (§2 item 5) whether the paragraph says anything beyond the random walk. It does not survive, from either side.

**A moving state that is spent.** Take a known law and $x_{t+1} = -x_t$ (no process noise), $o_t = x_t + v_t$, $v_t \sim \mathcal N(0, 1)$, $x_1 \sim \mathcal N(0, 1)$. Nothing about $x_t$ is constant along the run, so under the coordinate reading of the invariance rule $x_t$ is state and $\theta$ is a point mass. Item (b)'s criterion holds ($C A^j P_t = (-1)^j P_t \neq 0$), so the loop is in at every $t$. But $P_t = 1/(1 + t) \to 0$. The one-step part is $\tfrac12 \log(1 + P_t) \sim 1/(2t)$ ($0.000499$ at $t = 1000$), and the information the next $n$ observations carry about $x_t$ is $\tfrac12 \log(1 + n P_t)$, unbounded in $n$, so the value is $+\infty$. That is the law-learning signature under a state label. Under the functional reading of "whatever about the world stays the same", $\lvert x \rvert$ is invariant and goes to $\theta$. What stays state is the sign, whose uncertainty is at most $\log 2$ and is resolved exponentially fast: not standing either. A 2-D noise-free rotation gives the same picture with a continuous phase in place of the sign. The physical instance is orbit determination under a known gravitational law with no process noise. The sentence in (g) is therefore false as written, and so is the Discussion's "renewed every step". The motion is real; the renewal is not.

**An invariant law that stays standing.** Take states $1, 2, 3, \ldots$, where the row at $n$ sends the state to $n+1$ or $n+2$ with an unknown probability $p_n$, the $p_n$ i.i.d. uniform. Every $p_n$ is constant along the run, so $\theta$ under any reading. The state strictly increases, so each step is a first visit to a new row. The one-step part is $\log 2 - \tfrac12 = 0.1931$ nats at every step: bounded away from zero, never decaying. The value is $+\infty$, as a sum of constant terms. The physical instance is an agent exploring an unbounded static terrain, which the invariance cut makes law. The Discussion's $(K-1)/(2n)$ decay is item (c)'s, and it carries (c)'s recurrence hypothesis; stated for invariant laws in general, it is false. The closing sentence on drifting laws inherits the first gap: a law that drifts by a known deterministic schedule with an unknown phase is slow state and is spent.

**What's worked instead (strengthening, single-agent, unverified by another mind).** What separates the two behaviors is whether the target gains fresh randomness, not whether it is invariant. Call a target component $Z$ *closed* from $t$ when, for every $k \geq t$, $Z_k$ is a measurable function of $(Z_t, \mathcal C_k)$. Then two exact statements hold.

1. *The value is a stock drawn down by the one-step parts.* For a closed component, $\sup$ aside, $I(Z_t; F_t \mid \mathcal C_t) = \sum_{k \geq t} I(Z_k; o_{k+1} \mid \mathcal C_k, a_k)$. By the chain rule the left side is $\sum_k I(Z_t; a_k, o_{k+1} \mid \mathcal C_k)$, and the action term is zero. Each remaining term equals $I(Z_k; o_{k+1} \mid \mathcal C_k, a_k)$ for two reasons. Data processing in one direction: $Z_k$ is a function of $(Z_t, \mathcal C_k)$. Data processing in the other: given $(\mathcal C_k, a_k)$, $o_{k+1}$ depends on $Z_t$ only through $Z_k$, by the Markov commitment and fresh noise, with $Z$ the whole target or a component the rest of the target does not feed. In the sign-flip example the script checks the telescoping to six decimals. Consequence: a finite value forces the one-step parts to zero; an infinite value allows decay (recurrence) or not (novelty).
2. *(g) holds for every closed component, not only for $\theta$.* If $Z_s = f(Z_t, \mathcal C_s)$, then $I(Z_s; F_s \mid \mathcal C_s) \leq I(Z_t; F_s \mid \mathcal C_s) \leq I(Z_t; F_t \mid \mathcal C_t)$. The argument is (g)'s own, with "invariant" replaced by "closed".

$\theta$ is closed by construction, which is why the Discussion's chain-rule sentence is right for it. A state driven by process noise is not closed, and a finite value with a one-step part bounded away from zero (the random walk) is possible only there. So the honest carve is *closed* (spent: a stock drawn down, with standing draws possible when the future keeps reaching untouched parts of it) against *renewing* (standing because fresh randomness keeps entering the variables later observations see). The state/law cut is a sufficient condition for closedness on the law side only. What I have not done: characterize "renewing" beyond the linear-Gaussian case, where it reads as process noise reaching the directions later observations see ($P_\infty$ with $C A P_\infty \neq 0$).

**Bearing on the Working Notes' strengthening item.** The item proposes requiring every invariant function of the declared world's path to be in $\theta$, and believes the tracking no-go stands when the tracked state's invariant $\sigma$-field is trivial. In the sign-flip example the invariant $\sigma$-field holds $\lvert x \rvert$ and not the sign. The sign is measurable in the tail $\sigma$-field, because $x_1 = (-1)^{n-1} x_n$ for every $n$. So a rule built on the invariant $\sigma$-field still leaves a periodic phase as state, with a spent warrant. A rule built on the tail $\sigma$-field captures it. For Markov chains the gap between the two is the cyclic structure. I recall a Blackwell–Freedman result on the tail $\sigma$-field of a Markov chain, but I have not read it, and I am not citing it. Whichever $\sigma$-field the strengthening adopts, 06 used "tail or invariant" interchangeably, and the two differ here.

## 3. Smaller findings

- **The invariance rule's wording and item (b)'s label.** "Whatever about the world stays the same" reads as any function of the path. The Working Notes say the landed rule is narrower: it names declared variables. The reading changes labels, not membership, but (b)'s *"$A, C$ and the noise covariances $Q, R$ known, so $\theta$ is fixed and $S_t = x_t$"* is wrong under either reading when a coordinate is invariant. Take $A = I$ and $Q = \operatorname{diag}(1, 0)$: the second coordinate is constant, so it is law. Under the functional reading, any $A$ and $Q$ with an invariant direction ($c^\top A = c^\top$, $c^\top Q c = 0$) are the same case. (b)'s criterion is unaffected, because membership does not depend on the cut. A qualifier such as "with no invariant direction, for example $Q \succ 0$" fixes the label.
- **(c) and the Discussion overstate identification.** (c) says the deterministic-prior agent *"knows its law exactly"*, and the Discussion says the law part reaches zero *"only when the law can be identified exactly"*. Under (f), unreachable rows stay uncertain forever, and the law part still reaches zero. Both should say: identified wherever some continuation can reveal it.
- **Condition 2 gates nothing.** A loop with $\mathcal O = \emptyset$ has no observation function ($h$ would map into the empty set) and no chronica. Every well-formed loop therefore satisfies condition 2. "No channel" is $\lvert \mathcal O \rvert = 1$, which is case (e). The live, necessary form is $\lvert \mathcal O \rvert \geq 2$, which condition 1 implies. (e)'s *"The empty channel is the extreme case"* inherits this.
- **"The agent's conduct" where the predicate says "some continuation".** The Discussion has *"whenever the agent's conduct can return to what it is learning without bound"*. The value is a supremum over continuations, as (c) states. The agent's own conduct is not the condition.
- **"Whatever part of the law the analysis does not fix".** This phrase in the Definition paragraph, and *"the analysis leaves open"* / *"random under the modeler's reference measure"* in `#def-action-transition` (lines 12, 33), `#def-observation-function` (lines 15, 37) and NOTATION's $\theta$ row, read as the modeler's knowledge. The rule two sentences later, and "Whose uncertainty", say the support is cut by the agent's design-time knowledge: the benchmark designer who knows the law does not take the learner out. A reader who stops at the upstream definitions gets the opposite rule.
- **`#def-agent-environment` lines 13, 31 and 35 (Epistemic Status).** These gloss the scope as *"systems facing genuine uncertainty"* and say the scope *"states it exactly"*. By item (a), residual uncertainty is necessary, not sufficient (the fresh state with $A = 0$ faces genuine uncertainty and is out). This extends open finding F7 of `reviews/scope-adaptive-system-reread-1.md`, which named line 43; line 43 is now fixed, and these three are not.
- **`#disc-framework-self-diagnostic` line 19.** *"the agent receives observations under uncertainty and runs the cycle"* is the same residual-uncertainty gloss. Line 35, fixed after reread-1's F13, states it correctly.

## 4. What I did not check

- The citations: Åström, Kaelbling–Littman–Cassandra, Martin, Duff and Clarke–Barron are not in relata (08 §1.7). I did not fetch them.
- A continuous-space (h′).
- The knowledge/belief boundary for the set of possible worlds, beyond noting that the support rule depends on which world is actual. This is intended, and it means membership is not a function of the design alone.
- Second-hop dependents.
- Whether `#scope-agency`'s $P(o \mid do(a))$ is meant under $\pi_0$ or under the actual world. The housing twin preserves it either way.

## Appendix — check script

`python3 -I` on this file's code reproduces every number above.

```python
import numpy as np
from scipy.special import digamma, gammaln
# (1) Item (b): scalar random walk A=C=Q=R=1 at steady state
P = 1.0
for _ in range(200): P = (P + 1) / (P + 2)
print("RW  P_inf=%.4f one-step=%.4f whole-future=%.4f" % (P, 0.5*np.log(1 + P/2), 0.5*np.log(P*(1/P + 1/(P+1)))))
# (2) Noise-free sign-flipping hidden state: x_{k+1} = -x_k, o_k = x_k + v_k, R = 1, known law, x_1 ~ N(0,1)
for t in (1, 10, 100, 1000):
    Pt = 1/(1 + t)
    print("A=-1,Q=0  t=%5d one-step=%.6f 1/(2t)=%.6f  next-n info n=1e2,1e4,1e6: %.3f %.3f %.3f" % (
        t, 0.5*np.log(1 + Pt), 1/(2*t), *(0.5*np.log(1 + n*Pt) for n in (1e2, 1e4, 1e6))))
t, n = 10, 10**5; Pk = 1/(1 + t + np.arange(n))
print("telescoping sum of one-step parts over n steps = %.6f ; 0.5 log(1+n P_t) = %.6f" % ((0.5*np.log(1 + Pk)).sum(), 0.5*np.log(1 + n/(1 + t))))
# (3) Law novelty: each step a first visit to a row Bernoulli(p_n), p_n ~ Beta(1,1)
print("novel-row one-step part, every step: %.4f nats (= log 2 - 1/2)" % (np.log(2) - 0.5))
# (4) Item (c): one-step information about a Dirichlet(1,...,1) row after n draws vs (K-1)/(2n)
def comps(n, K):
    if K == 1: yield (n,); return
    for i in range(n + 1):
        for r in comps(n - i, K - 1): yield (i,) + r
def one_step(n, al):
    al = np.array(al, float); a0 = al.sum(); EH = 0.0
    for c in comps(n, len(al)):
        c = np.array(c); lp = gammaln(n+1) - gammaln(c+1).sum() + gammaln(a0) - gammaln(n+a0) + (gammaln(c+al) - gammaln(al)).sum()
        pr = (c + al)/(n + a0); EH += np.exp(lp) * -(pr*np.log(pr)).sum()
    return EH - (al/a0*(digamma(a0+1) - digamma(al+1))).sum()
for al in ((1, 1), (1, 1, 1)):
    for n in (10, 50, 200):
        v = one_step(n, al); print("Dir%s n=%3d one-step=%.5f ratio to (K-1)/(2n)=%.3f" % (al, n, v, v/((len(al)-1)/(2*n))))
```

Output:

```text
RW  P_inf=0.6180 one-step=0.1346 whole-future=0.1618
A=-1,Q=0  t=    1 one-step=0.202733 1/(2t)=0.500000  next-n info n=1e2,1e4,1e6: 1.966 4.259 6.561
A=-1,Q=0  t=   10 one-step=0.043506 1/(2t)=0.050000  next-n info n=1e2,1e4,1e6: 1.156 3.407 5.709
A=-1,Q=0  t=  100 one-step=0.004926 1/(2t)=0.005000  next-n info n=1e2,1e4,1e6: 0.344 2.303 4.600
A=-1,Q=0  t= 1000 one-step=0.000499 1/(2t)=0.000500  next-n info n=1e2,1e4,1e6: 0.048 1.198 3.454
telescoping sum of one-step parts over n steps = 4.557570 ; 0.5 log(1+n P_t) = 4.557570
novel-row one-step part, every step: 0.1931 nats (= log 2 - 1/2)
Dir(1, 1) n= 10 one-step=0.03855 ratio to (K-1)/(2n)=0.771
Dir(1, 1) n= 50 one-step=0.00937 ratio to (K-1)/(2n)=0.937
Dir(1, 1) n=200 one-step=0.00245 ratio to (K-1)/(2n)=0.981
Dir(1, 1, 1) n= 10 one-step=0.07035 ratio to (K-1)/(2n)=0.703
Dir(1, 1, 1) n= 50 one-step=0.01826 ratio to (K-1)/(2n)=0.913
Dir(1, 1, 1) n=200 one-step=0.00487 ratio to (K-1)/(2n)=0.974
```
