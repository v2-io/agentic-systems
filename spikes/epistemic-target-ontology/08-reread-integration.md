# 08 — Integrating the independent re-read (07) into `#scope-adaptive-system`

**KR A.1** (`msc/inside-out-2026-10/INTENT.md`), under the top intent *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."*: `#scope-adaptive-system` carries the typed predicate or a defended alternative, and a cold reader checks the membership clauses on standard RL and on a Kalman filter.

*Integrator: Opus 5.5, 2026-10-30. I read 07 whole, the segment and the dependents 07 lists, and 05 and 06. I took 07's §6 as the working rule: each proposed wording, the (h′) sketch and the candidate $\pi_0$ completion was an input to re-derive, not text to transcribe. This file is for the next checker. The canon text is the source; this file holds the reasoning, what I declined, and where I diverge from 07.*

## 1. What changed in canon, and why

### 1.1 Two kinds of warrant (07 §2.1): agreed, re-derived by a different route

07's numbers reproduce (script in the appendix): the next $m$ draws from a Beta(6,6) row carry $0.040, 0.302, 1.115, 2.216, 3.016$ nats for $m = 1, 10, 100, 1000, 5000$. The one-step information matches $(K-1)/(2n)$ to within 0.6% at $n = 1000$ for $K = 2, 3, 5$. The scalar random walk with $q = r = 1$ has a one-step part of $0.1346$ nats and a whole-future value of $0.16175$ nats at steady state.

The infinity needs more than "the posterior is consistent". My argument, now in item (c):

- Represent the draws at successive visits to $(s, a)$ by a pre-drawn i.i.d. stack per pair (the standard skeleton of a tabular MDP). On the event $E$ that the continuation visits the pair infinitely often, the stack's frequencies converge to the row a.s. So the row equals a measurable function $g$ of the stream on $E$.
- If $P(E) \gt 0$, the joint law of (row, stream) gives the graph $\{(\theta, f) : \theta = g(f)\}$ positive probability.
- Under the product of the marginals, each section of that graph is one point, which a continuous (Dirichlet) prior gives probability zero. So the product gives the graph probability zero, the joint is not absolutely continuous with respect to the product, and the KL divergence (the mutual information) is $+\infty$.

Under full-support Dirichlet rows every transition has positive probability a.s. The continuation that always takes $a$ at $s$ then makes the state chain irreducible on a finite space, so $s$ recurs and $P(E) = 1$.

What landed:

- (c): the one-step information decays like $(K-1)/(2n)$ (Clarke–Barron), and the value is $+\infty$ at every finite $t$ under that recurrence hypothesis.
- (b): the one-step part has the closed form $\tfrac12 \log\det(I + C A P_t A^\top C^\top N^{-1})$ with $N = C Q C^\top + R$, $R \succ 0$, from $o_{t+1} = C A x_t + (C w_t + v_{t+1})$. It is continuous in $P_t$, and positive iff $C A P_t \neq 0$ (because $P_t \succeq 0$). So when $P_t \to P_\infty$ with $C A P_\infty \neq 0$, it has a positive limit, and the value, which is at least the one-step part by monotonicity of mutual information, stays bounded away from zero.
- "Two kinds of warrant": compares value against one-step part.

I did not claim that a tracker's value is finite in general. I showed it only for the random walk, numerically. Here is a case where it isn't: a state coordinate with no process noise and $A = 1$ is identified by the stream, so the value is infinite. But under the invariance cut such a coordinate is law, so the "standing vs spent" carve survives. The Discussion says "for the random walk the value is finite".

One correction to 07's own wording. 07 §2.1 says "For the tracker these [increments] are bounded away from zero". If "increments" means the chain-rule terms of the value at a fixed $t$, those are about the fixed $x_t$. Their sum is finite ($0.162$), so they go to zero. What stays bounded away from zero is the predicate's one-step part at each later time, which is about $x_k$, not $x_t$. For the law the two readings coincide, because $\theta$ does not move. The landed Discussion compares value and one-step part at each time, and says the chain-rule identity holds "because the law does not move".

`#example-bandit`'s stationary variant: under a Gaussian prior on a mean $\mu$, with pull noise $\sigma^2$, the posterior variance after $n$ pulls is $s_n^2 = \sigma^2/(n + \sigma^2/s_0^2)$. The one-step information is $\tfrac12 \log(1 + s_n^2/\sigma^2) \sim 1/(2n)$, and $I(\mu; r_1, \ldots, r_m) = \tfrac12 \log(1 + m s^2/\sigma^2) \to \infty$. Landed, replacing "transient".

### 1.2 Support versus null sets (07 §2.2): agreed on the conclusion; 07's counterexample does not work; (h′) re-derived and landed

**07's counterexample fails under the segment's definition.** The segment defines $\theta = (\theta_T, \theta_h)$ as the kernel pair itself, not a parameter that indexes it. In 07's construction the channel's law depends on $\theta \in [0, 1]$ only through $b = 1\{\theta \in \mathbb Q\}$. So the law, as the segment defines it, takes two values, $K_0$ and $K_1$. The two priors push forward to $\delta_{K_0}$ (Lebesgue) and $\tfrac12 \delta_{K_0} + \tfrac12 \delta_{K_1}$, which have different supports. The construction shows that support in a *parametrization* does not fix membership. It does not show that for $\pi_0$ on $(\Omega_1, \theta)$ as written.

**The claim is still false in general.** Move the irregularity to the state, where the segment's own objects can carry it:

- the law is known (a point mass);
- $\Omega_1 = x \in [0, 1]$ is hidden and never moves;
- observations are constant except $o_2 = 1\{x \in \mathbb Q\}$.

Under the Lebesgue prior $o_2 = 0$ a.s., so $F_1$ is independent of $x$: out at $t = 1$. Under $\tfrac12$ Lebesgue $+ \tfrac12 \sum_k 2^{-k} \delta_{q_k}$, $o_2$ is a fair coin determined by $x$: in. Both priors have support $[0, 1]$. This is the counterexample that (h′) carries in canon.

**(h′), re-derived.** Hypotheses: $\Omega$, $\mathcal O$, $\mathcal A$ finite; $\theta$ is the tuple of kernel entries, in the Euclidean topology on the product of simplices. I reached it independently of 07's sketch, and it agrees with the sketch where they overlap. Steps:

1. Write $\pi_0 = \sum_{\omega_1} \delta_{\omega_1} \otimes \mu_{\omega_1}$, so $\operatorname{supp} \pi_0 = \bigcup_{\omega_1} \{\omega_1\} \times \operatorname{supp} \mu_{\omega_1}$.
2. For a continuation $\pi'$, a block length $m$ and a history $c$, two quantities are polynomials in $\theta$:
   - the likelihood $\ell_c(\omega_1, s, \theta) = P(\mathcal C_t = c, \Omega_t = s \mid \omega_1, \theta)$ (a sum over hidden paths of products of kernel entries, times the agent's own policy factors, which do not depend on $\theta$);
   - the block law $g_c(s, \theta)$ of the next $m$ steps given $(s, \theta, c)$.
3. $I(S_t; F_t \mid \mathcal C_t) \gt 0$ iff some finite block has positive information, because the stream's information is the limit over blocks. With discrete histories, that holds iff some $c$ with $P(c) \gt 0$ has $g_c$ non-constant on a set of positive posterior measure.
4. The posterior given $c$ is $\nu_c(s, d\theta) \propto \sum_{\omega_1} \ell_c(\omega_1, s, \theta) \mu_{\omega_1}(d\theta)$. Its support at each $s$ is $\bigcup_{\omega_1} \overline{\operatorname{supp} \mu_{\omega_1} \cap \{\ell_c(\omega_1, s, \cdot) \gt 0\}}$. The support lemma: if $x \in \operatorname{supp} \mu \cap \{L \gt 0\}$, every neighborhood meets the open set $\{L \gt 0\}$ around $x$ in positive $\mu$-measure, where $L \gt 0$. Conversely, an open set missing that set has $\int L \, d\mu = 0$, since $\mu$ is null off its support in a second-countable space.
5. A continuous $g$ into a finite simplex is $\nu$-a.e. constant iff constant on $\operatorname{supp} \nu$. The set $\{g \neq g_0\}$ is open, so if it is null it misses the support.
6. $P(c) \gt 0$ iff some open $\{\ell_c(\omega_1, s, \cdot) \gt 0\}$ meets $\operatorname{supp} \mu_{\omega_1}$.

Every condition is a function of $\{\operatorname{supp} \mu_{\omega_1}\}$, so of $\operatorname{supp} \pi_0$. The pointwise predicate at a positive-probability history has the same structure. I label (h′) exact on this derivation, with its hypotheses stated in the item.

What (h′) does not cover: continuous $\Omega$ or $\mathcal O$, including the linear-Gaussian case. For the Kalman example the segment does not need it: the law is a point mass, and any prior on the state with an everywhere-positive density is equivalent to the Gaussian one, so (h) suffices. Whether a continuous version holds (for instance under Feller-continuous kernels with everywhere-positive densities) is open; recorded in vsect (§3).

### 1.3 The $\pi_0$ rule (07 §2.3): restated as fixing a set of possible worlds; 07's candidate completion declined as written

07 is right that "the law of the world given what the agent holds by design" presupposes a measure to condition. My resolution uses (h′) rather than adding a third declared object. In finite worlds membership depends only on the support, so the rule needs to fix only the *set* of possible worlds: the declared class of worlds, less those the design rules out. Outside finite worlds a reference measure on that set must be declared as well, and only its null sets matter (h). The segment now says exactly this, in the intro, the Definition paragraph, "Whose uncertainty", the Epistemic Status, and NOTATION's $\pi_0$ row. The declarations are now: what the world comprises; and which worlds were possible for the agent, meaning the declared class cut down by design-time knowledge.

I declined 07's candidate ("$\pi_0$ conditioned on the evidence the design process had, not its conclusions") as written, for a reason (h′) supplies. 07's bullet "a filter whose matrices came from measurement has evidence that pins the law, so it has a point mass" is false under its own reading whenever the measurement is noisy:

- A finite noisy calibration gives a posterior over the law with full support.
- Every likelihood is positive, so by the support lemma conditioning excludes no world.
- So under the evidence reading, every filter calibrated from noisy measurements would be a law learner, and in.

That may even be the truer description of real filters. But it is not what the reading claims, and it makes "known-law tracking" a declared idealization in every real case. The segment now says a Kalman filter "declared to be built with its exact model" has a point mass, which names the idealization as a declaration.

The knowledge/belief boundary itself (a hard-coded guess that happens to be true; a pretrained design) is not settled on the merits here. It is recorded in vsect as a question, not in prose.

The misspecified filter (07's first bullet): the predicate never sees the agent's beliefs. A false belief rules out no world, so the agent is classified as if it held no such belief, and whether it is in on the law rests on the declared class. "Whose uncertainty" now says this. It replaces "is still in scope … and it is about to be surprised", which asserted a verdict the declaration does not fix.

### 1.4 Averaged versus pointwise (07 §2.4): landed

The averaged predicate is named as the scope, and the pointwise one as a different predicate. With discrete histories, averaged-in iff pointwise-in at some positive-probability history: $I(S; F \mid \mathcal C) = \sum_c P(c) \, I(S; F \mid \mathcal C = c)$, and $P(c)$ depends on the agent's past policy, not on $\pi'$. So a run can be pointwise-out while the loop is in. With continuous histories, the pointwise predicate is defined up to null sets. (c)'s deterministic-prior exit is marked pointwise. (g) was already stated a.e.

Which predicate "the" scope should be was a judgment. I chose averaged because the set definition already is averaged, and the Part I results it gates are expectations. A result that needs a per-run warrant should use the pointwise one explicitly.

### 1.5 Third way outside, collapse map (07 §2.5): landed

The intro now says a system is outside when its world can show it nothing more, and names three ways: nothing unknown; a blind channel; unknown but never shown. The state row of the collapse map reads "state that later observations still bear on". The chance row now says a hidden state drawn afresh and never seen again is the same case under another name. That is true by the coordinate-removal argument of §1.7.

### 1.6 The state/law cut (07 §2.6): landed, with the argument made exact

07 says membership is invariant under the cut "by hand". Since $\theta$ is defined as the kernel pair, moving an invariant $\zeta$ from $\Omega$ into the law does not literally give $\theta' = (\theta, \zeta)$. It gives the reduced world's kernel pair $\theta' = f(\theta, \zeta)$, which can lose $\zeta$ where $\zeta$ is irrelevant. The mutual information is still unchanged, for two reasons:

- the future stream's conditional law given the cut-1 target is a function of $(\tilde\Omega_t, \theta')$;
- $(\tilde\Omega_t, \theta')$ is itself a function of the cut-1 target.

So it is a sufficient statistic, and $I(\text{cut-1 target}; F \mid \mathcal C) = I((\tilde\Omega_t, \theta'); F \mid \mathcal C)$. Landed as one sentence in the Definition paragraph. The intro's first declaration now reads "which variables it comprises", and the Epistemic Status no longer attributes the cut's non-observability to the housing result. "Almost surely" was added to the invariance rule, with "on only some runs" for the switching regime.

### 1.7 Smaller points (07 §2.7)

- **"Why the future stream"** now states the exact distinguishing property. The stream predicate is invariant under adding or removing a target coordinate $Z$ on which, given the rest of the target and the history, no continuation's future depends: by the chain rule, $I((S, Z); F \mid \mathcal C) = I(S; F \mid \mathcal C) + I(Z; F \mid S, \mathcal C)$, and the second term is $0$. The entropy predicate is not invariant. Both flip under the housing twin.
- **The (ii′) relation:** "positive together when the target persists" is deleted. It fails at $A = 1$, $C = 0$, where the target persists and both are zero. What replaces it is what data processing gives: the predicate's one-step part is positive only where (ii′) is, and the converse fails for fresh state.
- **Housing twin as a mixture:** the fourth bullet now says "with $(\Omega_1, \theta)$ drawn from $\pi_0$". One sentence states mutual singularity for a law left open under a continuous $\pi_0$ with pairs visited without bound: under a fixed law $\theta^\ast$, the original concentrates on {frequencies $= \theta^\ast$}, which the mixture gives probability $\pi_0(\{\theta^\ast\}) = 0$. The intro and "The declared world" now say "the same probability, averaged over the worlds it allows".
- **(h)'s density** is now "with respect to $\pi_0$". (h) is retitled "Only the prior's null sets matter", because its old title claimed the support form. The possible-worlds title moved to (h′).
- **Citations:** Åström 1965, Kaelbling–Littman–Cassandra 1998, Martin 1967, Duff 2002, and Clarke–Barron 1990 (cited by the new (c) text) are not in relata; I searched each. I did not add them from memory: entering bibliographic details from recall is the generative-citation failure. Recorded as a vsect item for whoever can fetch them by identifier.

### 1.8 Dependents (07 §4)

Edited, Part I and III:

- `#def-agent-environment`:43, `#scope-composite-agent`:85, `#deriv-recursive-update`:27: residual uncertainty no longer stated as the condition;
- `terminology/entries/agency.md`:19 and `agent.md`:22 (bodies only; `bin/term render` leaves `LEXICON.md` unchanged);
- `#example-bandit`:46 ("transient" replaced, §1.1);
- `#deriv-mismatch-budget-attribution`:78: (ii′) vanishes iff the channel law equals the Bayes predictive a.s. This is the plain reading of the mutual information $I(o_t; S_t \mid \mathcal C_{t-1}, a_{t-1})$;
- `03-llm-core/src/disc-framework-self-diagnostic.md`:35 ("by construction" replaced by "relative to a declared world") and :80 (stage `draft`);
- `#form-agent-model`:64 (Working Note): the PID claim restated to what is true now. A PID loop is inside when it measures, through noise, a plant whose disturbed state persists. An exactly measured plant under a known law is case (d), and out.
- NOTATION: the $\pi_0$ row states the support rule and (h′); the $\theta$ row names `#example-strategy`'s $\theta_k(t)$ beside `#der-mood-timescale`.
- The segment's own Working Notes: two resolution notes that repeated the §2.1 error were corrected, and the glyph item now names `#example-strategy`.

Edited, Part II, minimal, in a separate commit so the lead can reconcile with the Part II claim-records worktree:

- `#scope-agency`:25: dated as $\mathcal S_\text{agency}(t) = \mathcal S_\text{adaptive}(t) \cap \ldots$
- `#example-strategy`:52: "residual uncertainty persists" replaced by the actual warrant. The arm probabilities are drifting state that persists into later pulls (it moves only occasionally, so the next reward's law is a non-constant function of the current probability). The "Exact" tag is unchanged. I did not assert distinct-arm contrast there: the drift moves in steps of $\pm 0.05$, so arms can coincide.

Not edited: `CURRENT-VOL1.md` (generated; the lead rebuilds). `#result-mismatch-decomposition`:34 reads correctly as it stands.

## 2. What a checker who has not read 07 may want

The places where I am most likely to be wrong, in order:

1. **(h′)'s proof**, especially step 3 (finite blocks suffice, and the averaged/pointwise equivalence with discrete histories) and the support lemma's use of second-countability. Also: is "Euclidean topology on kernel entries" the right hypothesis if someone parametrizes kernels differently? The proof works in any parametrization where the kernels are continuous; the item states the kernel-entry case only.
2. **(c)'s infinity argument**, specifically the stack representation on the event of infinitely many visits, and the claim that the product measure gives the graph probability zero (each section is a single point under a continuous prior).
3. **(b)'s closed form and the "positive iff $C A P \neq 0$" step.**
4. Whether "redefined" (scope) and "reworded" (the three dependents whose own definitions did not change) are the right vsect classifications. The commit body says what I chose.
5. Whether the Discussion's "Two kinds of warrant" now says anything a reader could take beyond the random walk for the tracker.
6. Whether the intro's three-ways-out and the restated declarations read as one consistent picture to a cold reader.

07's findings F1–F13 are open in vsect under the reader's name. I believe the landing answers F1 (in part: the knowledge/belief boundary is now a question), F2–F13, and C3/C4's broken items. Confirming that is for a mind other than me.

## 3. Open, recorded in vsect rather than prose

- A continuous-space (h′): does membership depend only on the support for continuous $\Omega$ or $\mathcal O$ under, say, Feller-continuous kernels with everywhere-positive densities, covering the linear-Gaussian case?
- The knowledge/belief boundary for the set of possible worlds: a hard-coded true guess; a pretrained design. Also the evidence reading's consequence that every noisily calibrated filter is a law learner.
- The citations missing from relata (§1.7).
- Not mine, and not checked: whether any downstream result uses membership uniformly in $t$ (07 §5).

## 4. On the brief

The brief's framing of 07's text as "inputs to re-derive" is what caught §1.2's error. I went to write (h′)'s hypothesis in the segment's own terms, and "$\theta \in [0, 1]$" did not type-check against "$\theta = (\theta_T, \theta_h)$". The same discipline applies to this file: the counterexample I substituted, the infinity argument and (h′)'s proof are mine, and want the same treatment.

## Appendix — check script

`python3 -I` on this file reproduces every number above.

```python
import numpy as np
from scipy.special import digamma
from scipy.stats import betabinom, binom, beta
def H(p):
    p = np.asarray(p, float); p = p[p > 0]; return -(p * np.log(p)).sum()
def one_step(al):  # I(row; next draw) = H(mean row) - E H(row), row ~ Dir(al)
    A = al.sum(); return H(al / A) - (digamma(A + 1) - (al / A * digamma(al + 1)).sum())
for K in (2, 3, 5):
    for n in (10, 100, 1000, 10000):
        v = one_step(np.ones(K) + n / K); print(K, n, v, v * 2 * n / (K - 1))
def m_step(a, b, m):  # I(p; X_1..X_m), p ~ Beta(a, b)
    k = np.arange(m + 1); xs, ws = np.polynomial.legendre.leggauss(600); ps = (xs + 1) / 2; ws = ws / 2
    return H(betabinom.pmf(k, m, a, b)) - (ws * beta.pdf(ps, a, b) * np.array([H(binom.pmf(k, m, p)) for p in ps])).sum()
print([(m, m_step(6., 6., m), 0.5 * np.log((12 + m) / 12)) for m in (1, 10, 100, 1000, 5000)])
q = r = 1.; P = 1.
for _ in range(2000):
    Pm = P + q; P = Pm * r / (Pm + r)
for m in (1, 5, 20, 200):  # I(x_t; next m observations | C_t) at steady state
    i = np.arange(1, m + 1); S = P + q * np.minimum.outer(i, i) + r * np.eye(m); c = np.full(m, P)
    print(m, 0.5 * np.log(P / (P - c @ np.linalg.solve(S, c))))
print("one-step closed form", 0.5 * np.log(1 + P / (q + r)))
```
