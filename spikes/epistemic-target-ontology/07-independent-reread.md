# 07 — Independent re-read of `#scope-adaptive-system` (as of 7b429bcc)

**KR A.1** (`msc/inside-out-2026-10/INTENT.md`): the front door says only what the bodies support. `#scope-adaptive-system` carries the typed predicate or a defended alternative, and a cold reader checks membership on standard RL and on a Kalman filter.

*Reader: Opus 5.5, 2026-10-30, read-only on canon apart from this file. Asked by the lead coordinator for an independent critical pass on the segment as it now stands and on whatever it touches, re-derived from what is written.*

*What I read: the segment whole; `#def-agent-environment`, `#def-action-transition`, `#def-observation-function`, `#def-chronica`, `#scope-agency`, `#result-mismatch-decomposition`, the (ii′) block of `#deriv-mismatch-budget-attribution`, the scope paragraphs of `#example-kalman` and `#example-bandit`, `#hyp-solicitable-escape`:44, `#scope-logogenic-agent`:44–50; NOTATION rows for $\theta$, $\pi_0$, $S_t$, $F_t$ and GA-1; every file that cites the slug (grep), the terminology entries, `INTRODUCTION.md`, `README*` and `CURRENT-VOL1.md`. I formed findings 1–7 below before opening `05-integration-checks.md` and `06-cold-read.md`, and read those afterwards to check the integrator's landing of 06 and to avoid re-reporting. Two of my findings contradict wording that 06 proposed and the integrator landed (§2.1, §2.2).*

*What I computed (scripts in the appendix): the information a Dirichlet row's future draws carry about the row, one step and $m$ steps ahead; the whole-future information a scalar random-walk Kalman filter's future carries about $x_t$. Everything else is by hand and marked so.*

## 1. Verdicts on the two test cases, on the revised text

- **Kalman filter (hidden state, known law): in**, by item (b). I re-derived the criterion $C A^j P_t \neq 0$ for some $j \geq 1$ by hand (joint Gaussianity given $\mathcal C_t$, future noises independent of $(x_t, \mathcal C_t)$, zero cross-covariance iff independence). The random walk of `#example-kalman` is in at every $t$.
- **Tabular RL (observed state, unknown kernel, independent Dirichlet rows): in at every finite $t$**, by item (c). Strict concavity of entropy gives a positive one-step information whenever the posterior row is not a.s. constant.

Items (a), (b), (d), (e), (f), (g) and the housing result are true as stated; I re-derived each. Item (h) is true as stated, but a sentence in the Definition paragraph claims more than (h) proves (§2.2). Item (c) is true as a membership statement, but its last two clauses misdescribe what decays (§2.1).

## 2. Findings, in order of what they change

### 2.1 The predicate's own quantity does not decay for a law learner. It is infinite. (Formal Expression (c); Discussion, "Two kinds of warrant")

The predicate is $\sup_{\pi'} I_{\pi'}(S_t; F_t \mid \mathcal C_t)$, information about $S_t$ in the *whole* future stream. Item (c) says that what decays, "roughly as $1/(2n)$ after $n$ visits to a pair, is the amount of information". The Discussion says a learner's warrant is *decaying*: "the information tends to zero". Both are true of the *one-step* information $I(\theta; a_t, o_{t+1} \mid \mathcal C_t)$. Neither is true of the quantity the predicate defines.

*Computed.* For one Beta(6,6) row (ten visits on a uniform prior), the information in the next $m$ draws about the row is $0.040, 0.302, 1.115, 2.216, 3.016$ nats for $m = 1, 10, 100, 1000, 5000$. This tracks $\tfrac12 \log((n+m)/n)$ and grows without bound. *By hand:* the posterior is consistent, so infinitely many draws pin a continuous $\theta$ exactly, and the information a sample carries about a continuous parameter it identifies is infinite. So whenever some continuation can revisit the pair $(s, a)$ without bound (any communicating finite MDP), $\sup_{\pi'} I(\theta; F_t \mid \mathcal C_t) = +\infty$ at *every* finite $t$. It is finite only when the pair can be visited only finitely often.

*Computed, for contrast.* For the scalar random walk with $q = r = 1$ at the steady-state $P_t = 0.618$, the information in the next $m$ observations about $x_t$ is $0.1346, 0.1617, 0.16175$ nats for $m = 1, 5, \geq 20$. It is finite and constant.

So under the predicate's own measure the contrast in "Two kinds of warrant" is inverted. The tracker's warrant is finite and standing; the law learner's is infinite at every finite time. What actually separates them is the *increments*. By the chain rule already used in (g), the predicate's value is the sum over $k \geq t$ of the one-step terms $I(\theta; a_k, o_{k+1} \mid \mathcal C_k)$. For the tracker these are bounded away from zero. For the law learner they decay like $(K-1)/(2 n_k)$, and their sum diverges like $\tfrac{K-1}{2} \log$. That is a sharper and exact statement of what the paragraph wants: *the law warrant is spent one step at a time and is never used up*. It replaces "the information tends to zero", which is false for the defined quantity.

Two smaller corrections ride along:

- **The rate is $(K-1)/(2n)$, not $1/(2n)$, for a row with $K$ possible successors** (computed: $K = 3$, $n = 1000$ gives $0.000996$ against $(K-1)/(2n) = 0.000997$; $K = 5$ gives $0.001988$ against $0.001990$). $1/(2n)$ is the $K = 2$ case, which is what 06 computed. This is the Clarke–Barron rate.
- **`#example-bandit`:46 still calls the stationary variant's warrant "transient".** 9ca09dbc deleted that word from the scope segment because it contradicts (c). The stationary bandit's means are law under a continuous (Gaussian) prior, so the agent never leaves; and by the above, its whole-future warrant is infinite.

06 §3.1 proposed "the information tends to 0" and computed only one-step information, so this error came in with the correction of "transient".

### 2.2 "Only the support of $\pi_0$ affects membership" is not what (h) proves, and is false in general. A strengthening makes it true where it is needed. (Formal Expression, the Definition paragraph; Discussion, "Whose uncertainty"; NOTATION)

Item (h) proves that membership is the same under any prior **with the same null sets** as $\pi_0$ (mutual absolute continuity). I re-derived it, and it is correct. NOTATION's $\pi_0$ row says the same ("only through its null sets"). But the Definition paragraph says "By item (h) below, only the *support* of $\pi_0$ affects membership", and the Discussion says "$\pi_0$ matters only through which worlds it allows". Two measures can share a support without sharing null sets, so this is a strictly stronger claim. 06 §3.2 introduced the wording.

**Counterexample (by hand).** The state is a known clock $\Omega_t = t$, observed. The law $\theta \in [0, 1]$ is invariant. The channel emits $o_t = (t, b_t)$ with $b_2 = 1\{\theta \in \mathbb Q\}$ and $b_t = 0$ otherwise. Under $\pi_0 = $ Lebesgue, $b_2 = 0$ a.s., so at $t = 1$ no continuation reveals anything: out. Under $\pi_0' = \tfrac12 \text{Lebesgue} + \tfrac12 \sum_k 2^{-k} \delta_{q_k}$ (the $q_k$ enumerating the rationals in $[0,1]$), $b_2$ is a fair coin correlated with $\theta$: in. Both measures have support $[0, 1]$.

**Strengthening (sketch, by hand; I believe it is right but have not written it out in full).** *(h′) If the observation and action spaces are finite (so histories are discrete), $\Omega$ is discrete, and the kernels $T$ and $p_h$ depend continuously on $\theta$, then membership depends on $\pi_0$ only through its support.*

Sketch: for each history $c$, the likelihood $(\omega_1, \theta) \mapsto P(c, \Omega_t = s \mid \omega_1, \theta)$ and the conditional law of $F_t$ given $(s, \theta, c)$ are continuous in $\theta$. The averaged predicate is zero iff, for every $c$ with $P(c) \gt 0$, that conditional law is constant almost everywhere under the posterior given $c$. For a continuous non-negative likelihood $L$, the support of $L \cdot \pi_0$ is the closure of $\operatorname{supp} \pi_0 \cap \{L \gt 0\}$. Almost-everywhere constancy of a continuous function then equals constancy on that closure. And $P(c) \gt 0$ iff the open set $\{L \gt 0\}$ meets $\operatorname{supp} \pi_0$. Every condition depends only on $\operatorname{supp} \pi_0$. The tabular case is covered, since its likelihoods are polynomials in the kernel entries. The Kalman case is covered trivially, since its law has a point mass and the Gaussian state a full-support density. My counterexample fails the continuity hypothesis.

Why this matters beyond wording: the $\pi_0$ rule ("fixed by what the agent knows by design") is only well posed if knowledge, which naturally says *which worlds are possible*, is enough to fix membership. With null sets it is not, because a set of possible worlds does not fix a measure's null sets (§2.3). With (h′), it is enough for every regular world. So (h′) is what completes the rule. My recommendation, offered for the integrator to weigh: keep (h) as stated and exact; add (h′) at the tier its proof earns; make the Definition and Discussion sentences cite (h′) with its hypothesis, or say "null sets".

### 2.3 The $\pi_0$ rule presupposes a base measure it does not name. (Formal Expression; intro, "the second declaration")

"The law of the world given the information the agent holds by design" is a conditional probability, so it needs a probability over worlds to condition. A physical world has one law. Conditioning a point mass at the true law on anything leaves a point mass, which would put every law learner out. The segment's own examples show the intent: a tabular learner "has a non-degenerate measure over" the kernels. That measure comes from a class of possible worlds plus a base measure on it, and both are the modeler's. The intro calls the second declaration "fixed by what the agent knows by design", but knowledge restricts the support. It does not fix a measure.

The gap shows up in three places:

- **The misspecified filter.** For a Kalman filter built with the wrong $A$, the rule says a false belief does not shrink $\pi_0$. Then $\pi_0$ is the base measure over the declared class. The segment never says what that class is, and whether the filter is in depends on whether the class gives its model positive probability. The verdict "in, about to be surprised" is right only under a class wide enough to make it so.
- **True content without evidence.** A model hard-coded with a guess that happens to be right is neither clearly knowledge nor clearly belief.
- **Learned designs.** For a learned system (pretraining, then deployment), the "design" is itself the output of an earlier learning process. Whether its content counts as knowledge is exactly the knowledge/belief question, for the systems `03-llm-core` cares about.

**A candidate completion, untested, for the integrator to weigh.** $\pi_0$ is the declared base measure over the declared class of worlds, conditioned on the *evidence* the design process had and built in (a pre-chronica), not on the conclusions it reached. Under this reading:

- a filter whose matrices came from measurement has evidence that pins the law, so it has a point mass;
- a guessed or false model brings no evidence and shrinks nothing;
- a pretrained model's $\pi_0$ is the posterior given its pretraining evidence;
- "knowledge, not belief" becomes "evidence, not conclusions", which is checkable;
- with (h′), the base measure matters only through its support.

The declarations then read as three objects, the world's variables, the class of possible worlds with its support, and the agent's design-time evidence. The segment currently names two.

### 2.4 Two predicates are in play: averaged and pointwise. (Formal Expression, under the predicate; (c); (g))

The set definition is the average over histories, and it depends on the agent's past policy only through the law of $\mathcal C_t$. The next sentence, "on a single run, condition on the realized history $\mathcal C_t = c_t$ instead", reads as a reformulation, but it is a different predicate. Pointwise-in on a positive-probability set of histories is equivalent to averaged-in. A run can be pointwise-out while the average is in.

Item (c)'s deterministic-prior sentence ("an agent that has visited every reachable pair … leaves the scope") is a pointwise statement. Under the averaged definition the agent stays in at time $t$ as long as some positive-probability history at $t$ has an unvisited reachable pair. Item (g) is stated a.e., which is the averaged reading.

What would help: name both, say which is *the* scope (results are expectations, which suggests averaged), and mark (c)'s exit as pointwise. For continuous observation spaces, the pointwise predicate is defined only up to null sets of histories, which "on a single run" glosses over.

### 2.5 A third way to be outside, and a collapse-map row that contradicts (b). (Intro; Discussion, "The collapse map")

The intro says "Two kinds of system sit outside": a world fully observed with its law given, and a channel that carries nothing. Item (b)'s $A = 0$ case (a hidden state drawn afresh each step) and item (f) (unreachable law) are outside for a third reason. The world holds something the agent does not know, but no future observation will ever bear on it. The first kind's gloss ("a fully observed process whose transition probabilities it was given") does not cover them.

The collapse-map table then says "Behind on state … In this scope? yes". Item (b) says a fresh hidden state is out. The row needs "state that persists into what is later seen", or an extra row: *behind on what the world will never show again — out*.

### 2.6 The state/law cut does not affect membership, so it is not one of the declarations membership rests on. (Intro; Epistemic Status)

The predicate is a function of the joint $S_t = (\Omega_t, \theta)$, and $\pi_0$ lives on $(\Omega_1, \theta)$. Moving an invariant coordinate between $\Omega$ and $\theta$ re-coordinatizes both without changing any mutual information (by hand). So in/out depends on *which variables the declared world comprises*, not on which of them are state and which law.

The cut matters for the labels: the two warrants, (g), and the split of the mismatch floor into a state part and a law part. The intro's "The first [declaration] is what the world is: which variables are its state and which its law" therefore overstates what membership rests on. The Epistemic Status line "Not claimed: that the cut between $\Omega_t$ and $\theta$ … can be read off the observations. The housing result shows it cannot" misattributes. The housing result re-declares the whole state, not the cut. The cut is fixed by the invariance rule once the world is declared, though "stays the same along the whole run" should say a.s. (a regime that switches on some runs and not others is state).

### 2.7 Smaller points

- **"Why the future stream" overstates the re-description argument.** It contrasts the entropy verdict, which flips when a fresh state is re-described as channel noise, with the stream verdict, which is "out both ways". True, but the housing result, twenty lines earlier, gives a re-description that flips the stream verdict too, so a reader may infer a general robustness that is false. The exact distinguishing property: the stream predicate is invariant under adding or removing target coordinates that no continuation's future depends on (the (f) argument), and the entropy predicate is not. Both flip under the belief-state twin. Saying that is shorter and true.
- **"They are positive together when the target persists"** ((ii′) paragraph). This fails when the persisting part is unobserved: $A = 1$, $C = 0$ makes both zero. It needs "persists into what is later observed".
- **The housing twin is observationally identical as a mixture.** For an open law, the Bayes-adaptive twin gives every sequence the same probability as the *declared* world, with $\theta$ drawn from $\pi_0$. For each fixed true law the two are mutually singular: the original's limiting frequencies equal $\theta^\ast$, and the twin's are random. This is de Finetti's point, and it is exactly why the Working Notes' invariant-$\sigma$-field strengthening would bring the twin back in. The segment is internally consistent (it reads $\Omega$ as including $\pi_0$), but the intro's "produces exactly the same observations" and the Discussion's "cannot be settled from the agent's data" read stronger than that. One clause, "the same probabilities, averaged over the worlds $\pi_0$ allows", would make the result and the open strengthening visibly the same subject.
- **(h)'s "a measure with a positive density on $(\Omega_1, \theta)$"** should say *with respect to $\pi_0$*. That is what makes the two measures equivalent.
- **Citations.** Åström 1965, Kaelbling–Littman–Cassandra 1998, Martin 1967 and Duff 2002, cited in an exact block, are not in `relata` (my searches by author and title returned nothing). Kalman and Pearl entries are there, so this is a gap in the citation library rather than an untracked convention.

## 3. The integrator's landing of 06, checked

Landed as claimed:

- the general housing result;
- the $\pi_0$ rule;
- the prior named in (c), and (c)'s strict-concavity step;
- known-law noise in (e);
- (g) a.e.;
- the (ii′) relation by data processing;
- the compute sentence;
- condition 2 called a restatement;
- "situations, not competent adapters";
- "Bayes posterior under $\pi_0$" for "the observer's own posterior";
- (b)'s independence of $(x_t, \mathcal C_t)$.

Two landed corrections carry errors that originate in 06's own proposed wording: "the information tends to zero" (§2.1) and "only through its support" (§2.2). The deletion of "transient" did not reach `#example-bandit` (§2.1).

## 4. Dependents and the front door

Body sentences, not Working Notes, unless marked.

- **Residual uncertainty stated as the condition.** The lead fixed this at the front door in 7b429bcc, but it remains in:
  - `#def-agent-environment`:43: an Adaptive System is "the coupling under a perception channel plus residual uncertainty";
  - `terminology/entries/agency.md`:19: "any system that observes under residual uncertainty";
  - `terminology/entries/agent.md`:22: "perception channel + residual uncertainty";
  - `#scope-composite-agent`:85: "it observes under residual uncertainty";
  - `#deriv-recursive-update`:27: "with residual uncertainty";
  - `#example-strategy`:52: "residual uncertainty persists. *Exact.*"

  By item (a), residual uncertainty is necessary only.
- **`CURRENT-VOL1.md`:22** still reads "an *adaptive system*: observation under residual uncertainty". The snapshot was rebuilt at 13:33, before 7b429bcc fixed `INTRODUCTION.md`:39 at 14:01. It needs a rebuild. `README.md` and `README-auditor.md` are current.
- **`#deriv-mismatch-budget-attribution`:78**: "(ii′) vanishes iff residual *state* uncertainty does not change the one-step predictive". The term directly above is labelled "state-and-law information".
- **`#scope-agency`:25**: $\mathcal S_\text{agency} = \mathcal S_\text{adaptive} \cap \ldots$ is undated, while $\mathcal S_\text{adaptive}(t)$ now is.
- **`#example-bandit`:46**: "transient" (§2.1).
- **`#example-strategy`:52** uses $\theta_k(t)$ for drifting *state*. The Working Notes' glyph item names only `#der-mood-timescale`.
- **`03-llm-core/src/disc-framework-self-diagnostic.md`**:
  - :35 calls the self-application "exact (… the framework applies to its users by construction)". Under the housing result, membership is relative to a declared world, so it is not by construction.
  - :80 records the scope as "claims-verified"; it is `draft`.
- **`#form-agent-model`:64 (WN)** says the scope "includes thermostats/PID as adaptive examples". The segment no longer mentions them. Harmless, but stale.

## 5. What I did not check

- The four-term refinement, the autonomy proposal, the invariant-$\sigma$-field strengthening and ascent gating (all marked open or unverified in the segment).
- (h′) beyond the sketch in §2.2, and in particular its continuous-observation version.
- Whether any downstream result uses membership uniformly in $t$. I walked every citer for wording, not for that.

On stage: every labelled-exact item survives. §2.1, §2.2 and §2.4 are changes to sentences around those items, one of them (§2.2) asserted as following from (h). I would land those before the segment leaves `draft`, and have someone who has not read this file check the result.

## 6. On the brief

The open brief let §2.1 surface. I went looking for what "the information" in "Two kinds of warrant" was, and the definition on the page answered differently from the paragraph. The two 06-originated errors suggest one thing worth carrying forward: a correction proposed by a cold reader deserves the same re-derivation from the page as the text it replaces. Here both were landed in the reader's wording.

## Appendix — check scripts

```python
# python3 -I ; Dirichlet row information, one-step and m-step
import numpy as np
from scipy.special import digamma
from scipy.stats import betabinom, binom, beta
def H(p): p=np.asarray(p); p=p[p>0]; return -(p*np.log(p)).sum()
def one_step(al):  # H(predictive) - E H(row), row ~ Dir(al)
    A=al.sum(); return H(al/A)-(digamma(A+1)-(al/A*digamma(al+1)).sum())
for K in (2,3,5):
    for n in (10,100,1000):
        al=np.ones(K)+n/K; print(K,n,one_step(al),(K-1)/(2*(n+K)))
def m_step(a,b,m):  # I(p; X_1..X_m), p ~ Beta(a,b)
    k=np.arange(m+1); xs,ws=np.polynomial.legendre.leggauss(400); ps=(xs+1)/2; ws=ws/2
    return H(betabinom.pmf(k,m,a,b))-(ws*beta.pdf(ps,a,b)*np.array([H(binom.pmf(k,m,p)) for p in ps])).sum()
for m in (1,10,100,1000,5000): print(m,m_step(6.,6.,m),0.5*np.log((12+m)/12))

# scalar random-walk Kalman, q=r=1: I(x_t; next m obs | C_t) at steady state
q=r=1.; P=1.
for _ in range(1000): Pm=P+q; P=Pm*r/(Pm+r)
for m in (1,5,20,100,400):
    i=np.arange(1,m+1); S=P+q*np.minimum.outer(i,i)+r*np.eye(m); c=np.full(m,P)
    print(m,0.5*np.log(P/(P-c@np.linalg.solve(S,c))))
```
