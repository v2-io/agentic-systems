# 06 — Cold read of `#scope-adaptive-system` (as landed in 492a1492)

*Reader: Opus 5.5, 2026-10-30, read-only on the repo apart from this file. Asked by Joseph: under the segment's own clauses, are tabular RL (observed state, unknown kernel) and a Kalman filter (hidden state, known law) in or out, is each "exact" item and the housing result true as stated, and is the framing right.*

*What I read: the segment whole; `#def-agent-environment`, `#def-action-transition`, `#def-observation-function`, `#def-chronica`, `#example-kalman`, `#scope-agency`, the relevant lines of `#hyp-solicitable-escape`, `#deriv-mismatch-budget-attribution` (term (ii′)) and `#disc-law-discovery-ceiling`; NOTATION rows for $\theta$, $\pi_0$, $S_t$, $F_t$, GA-1. I formed the verdicts below before opening `05-integration-checks.md` and the aat-refactored verifier's `de-novo-feedback-1.md` §F2–F4; I read those afterwards to avoid re-reporting what is already tracked, and say where my findings meet theirs.*

*What I computed (script at the end): the Bayes-adaptive twin of a tabular learner, checked by exact rational arithmetic; the decay of the tabular learner's one-step information. Everything else was checked by hand and is marked so.*

## Verdicts on the two test cases

**Kalman filter (hidden state, known law): in**, by item (b), at every $t$ for the random walk of `#example-kalman`, and in general exactly when $C A^j P_t \neq 0$ for some $j \geq 1$. I re-derived (b) by hand, including the multivariate "iff": $x_t$ and $(o_{t+1}, o_{t+2}, \ldots)$ are jointly Gaussian given $\mathcal C_t$ with cross-covariances $P_t (A^j)^\top C^\top$; zero cross-covariance for every $j$ gives independence of every finite block and hence of the whole stream, and any nonzero cross-covariance gives dependence. For `#example-kalman`'s sensor-choice actor the joint law is no longer Gaussian under adaptive sensor schedules, but membership needs only one continuation, and the open-loop "always $H$" schedule is Gaussian with cross-covariance $P_t \gt 0$. The verdict holds only under the declared physical state, which the segment says.

**Tabular RL (observed state, unknown kernel): in at every finite $t$**, by item (c), given a $\pi_0$ that is non-degenerate on the rows (the segment's independent Dirichlet priors). Item (c) is true. My computation: for one Beta(1,1) row, the information the next transition carries about the row, averaged over histories, is $0.193, 0.137, 0.0385, 0.00483, 0.000498$ nats after $0, 1, 10, 100, 1000$ visits. It tracks $1/(2n)$ and is positive at every $n$.

Two qualifications on the RL verdict, neither stated in the segment. Both are developed below.

1. The verdict depends on how $\pi_0$ is chosen, and the segment's stated rule for choosing it ("the modeler's viewpoint") points the wrong way for a designer-built benchmark (§3.2).
2. Under the invariance cut as the segment words it, tabular RL has an observationally identical case-(d) twin, just as the Kalman filter does. So its membership is relative to a declaration of the world too (§2).

## 1. The exact items, one by one

- **(a) True.** A point-mass conditional law kills every conditional mutual information with $S_t$.
- **(b) True** (above). One phrase is loose: "terms independent of $x_t$ given the history" should say "independent of $(x_t, \mathcal C_t)$". The future noises are independent of both jointly, and that is what the joint-Gaussian step uses.
- **(c) True for the Dirichlet setup.** Positivity follows from strict concavity of entropy: the predictive's entropy exceeds the expected entropy of the row whenever the row is not a.s. constant. Two problems:
  - The last sentence ("If the rows are deterministic and the agent identifies all reachable ones exactly, it leaves the scope") silently changes the prior. Deterministic rows have Dirichlet measure zero. Under a prior on deterministic successor maps the sentence is true, and it should say that this is the prior it means.
  - The Epistemic Status says each item is "given in full above". The strict-concavity step is in `05` but not in the segment, where (c) asserts that the draw "carries positive information about the row". One clause would fix this.
- **(d) True.**
- **(e) True as a condition; one of its examples is wrong as written.** "A channel that emits pure noise" is out only if the noise law is known. If the noise law is open under $\pi_0$, the observations carry information about $\theta_h$, which is part of $S_t$, and the loop is in. It is then a passive Bayesian learner of the noise distribution. This is the typed target doing its job, but the example as written invites the opposite reading. "Pure noise of known law" fixes it.
- **(f) True.** It is immediate from the predicate.
- **(g) True.** I checked the chain-rule identity and the composition argument: the conduct from $t$ to $s$ followed by any continuation from $s$ is a continuation from $t$, so the sup at $t$ bounds the averaged sup at $s$. The conclusion holds for almost every history reached by time $s$, not pointwise. The averaged-versus-realized remark under the predicate covers this, but (g) does not say it.
- **(h) True.** I checked it in full. Under $\pi_0$, $F_t \perp \Omega_1 \mid (S_t, \mathcal C_t)$, and a density on $(\Omega_1, \theta)$ leaves the conditional kernel of $F_t$ given $(S_t, \mathcal C_t, \Omega_1)$ unchanged. If that kernel is constant in $s$ for $P_0$-a.e. $(s, c)$, it is constant for $P_1$-a.e. $(s, c)$, because the two laws of $(S_t, \mathcal C_t)$ are mutually absolutely continuous. Conditional independence and its failure therefore both transfer, for each continuation separately.
- **Housing result: true**, and it holds more broadly than stated (§2).

So every item labelled exact is true as stated, apart from the example in (e) and the prior switch in (c). The errors are in the Discussion and Working Notes (§3).

## 2. The housing result holds for unknown-law loops too, and so for tabular RL

The housing construction needs neither a known law nor a hidden state. Take any loop, with the law open or not, and let the re-described state be (the Bayes posterior over $S_t$ given $\mathcal C_t$, the latest observation), emitting from the Bayes predictive. For tabular RL this is the Bayes-adaptive MDP (Bellman and Kalaba's adaptive control processes; Martin 1967; Duff 2002), with hyperstate (current state, transition counts). The four facts of the housing result go through unchanged:

- the re-described world is Markov;
- its kernel is policy-free, because the posterior given a history does not depend on the policy;
- its channel is noiseless;
- it gives every action-observation sequence the same probability.

Its state is $\mathcal C_t$-measurable and its law is a point mass, so it is a case-(d) loop.

*Computed:* a two-state tabular world with independent Beta(1,1) rows. The mixture probability of each of the 128 length-8 paths equals the probability the count-hyperstate twin with its fixed Laplace kernel assigns, with exact rational difference 0. History-as-state is an even simpler twin, and it shows the general form: **every loop has an observationally identical case-(d) twin, so no nonempty condition depending only on the interaction law excludes every case-(d) loop.** The segment's "take any loop whose law is known" is a restriction the proof does not need.

**Why this matters beyond tidiness.** Read with the Discussion ("Two kinds of warrant") and Working Note 2 ("What behaviour does determine … exactly the law-learning part"), the segment leaves the impression that law-learning membership is robust to re-description and only tracking membership is declaration-relative. Under the cut as the segment words it, that impression is false:

- **Read as a naming rule over the declared world's constituents.** `05` says this is the reading that landed, and item (f) confirms it: unreachable rows are in $\theta$, yet they are no function of the observation path. Under this reading the Bayes-adaptive twin is admissible. Nothing in the twin's declared world stays the same except its known kernel. Tabular RL's "in" is then exactly as declaration-relative as the Kalman filter's.
- **Read through the tail or invariant $\sigma$-field** ("whatever is a.s. constant along the run is $\theta$"). Under this reading the twin must carry the limiting posterior as $\theta'$, which is not $\mathcal C_t$-measurable, so the twin is back in. Law-learning membership then becomes interaction-law-determined, as the verifier's F2 sharpening proposes. The known-law Kalman twin stays out when its invariant $\sigma$-field is trivial, so the housing result keeps its force for tracking under that condition. I believe the condition holds for the random walk and for stable $A$ with nondegenerate process noise; I have not proved it. It fails when the tracked state has a constant component (a unit-root direction with no process noise). Under this reading that component is $\theta$ anyway, and the belief twin carries its limiting posterior mean as $\theta'$ and comes back in.

So the restriction to known law in the housing result is not where the construction stops. It is where the invariance cut would have to do work, and the segment does not say which reading it uses. Working Note 2 is conditioned on "the invariance cut making $\theta$ a function of the observation path", and that condition is false for the cut as landed, by item (f). The note is a candidate for a *different* $\theta$, roughly the invariant $\sigma$-field of the path, and should say so. My view, held as a hypothesis since I have not worked the closed-loop case: the $\sigma$-field reading, imposed as a constraint ("$\theta$ must contain every invariant function of the declared world's path") alongside the naming rule, is the strengthening to try. It would make RL's verdict declaration-robust without touching the tracking no-go. For actors, the invariant $\sigma$-field depends on the policy, which is the caveat the verifier already flags.

## 3. Errors and overclaims in the Discussion and Working Notes

### 3.1 "Transient" membership contradicts item (c) (clear error; Discussion and WN §4)

"Uncertainty about an invariant law is spent as it is learned, so a learner's membership is *transient*. … the learner of a fixed world eventually becomes a planner." Under the segment's own Dirichlet setup, membership never ends: item (c) says the learner is in at every finite $t$, and my numbers above show $I \approx 1/(2n) \gt 0$. What is transient is the *magnitude* of the law-part information ($\to 0$). Membership lapses in finite time only under priors with atoms that can be resolved in finite time, such as deterministic rows. The same overclaim sits in the Working Notes resolution under §4 ("a learner of a fixed law leaves for good"). (g) is true, but it describes an exit that a stochastic-kernel learner never makes.

What I think the paragraph wants to say, and can say exactly: the state warrant can be **standing** ($\liminf_t$ of the information is positive: the Kalman filter, with $P_t \to P_\infty \gt 0$), while the law warrant is **decaying** (the information tends to 0, and if it ever reaches 0, (g) makes that permanent). Smaller point: the Kalman filter's warrant is standing "while the signal moves" only if the moving part is observable. Process noise confined to an unobservable subspace moves the signal and reveals nothing.

### 3.2 The rule for choosing $\pi_0$ decides the RL verdict, and the stated rule points the wrong way

By (h), $\pi_0$ matters only through its null sets, so the live choice for the law part is whether $\pi_0$ is a point mass on $\theta_T$ or not. That choice alone flips tabular RL between (c) "in" and (d) "out". The segment's rule is that "whatever part of the law the analysis does not fix is random under" $\pi_0$, which "names the class of worlds the analysis ranges over". It adds that the predicate is "evaluated from the modeler's viewpoint", and that this "keeps a designer-known benchmark in scope for the agent that does not know it". What is missing is a rule for what the class *is*. Nothing ties it to what the agent was given rather than to what the modeler knows, so the benchmark sentence is asserted, not derived. A modeler who knows the benchmark's kernel and evaluates from their own viewpoint sets a point mass, and the learner is out. Item (h) does not help: it says which full-support prior you pick does not matter, not why the prior should be full-support.

The opposite case shows the same gap. Give a planner the true kernel at design time, and let the analysis range $\pi_0$ over kernels. By the predicate the planner is in, though the opening sentence ("something it does not yet know") and the first exclusion ("a system that knows both the state and the law") say it is out. The chronica holds no record of what the agent was built knowing, so conditioning on $\mathcal C_t$ cannot see it.

A reading that makes every verdict the segment wants come out right, offered as a candidate: **$\pi_0$ is the law of the world given the information the agent actually holds by design, its knowledge as opposed to its beliefs.** Under this reading:

- a Kalman filter handed $(A, C, Q, R)$ has a point mass on the law;
- a tabular learner not handed $T$ has a non-degenerate measure over kernels;
- the "certain and wrong" agent of "Whose uncertainty" is still in, because a false belief is not information and does not shrink $\pi_0$'s support;
- the planner handed the true kernel is out.

Under this reading $\pi_0$ is agent-relative, but by (h) only through its support. That is a cleaner thing to say than "modeler's viewpoint", which currently does two jobs: whose probability, and whose knowledge. It is also the second declaration the segment needs, next to the physical-state declaration. It matters exactly as much, and the segment currently names only the first.

### 3.3 The (ii′) correspondence is misstated (Discussion, "Why the future stream")

"The quantity is the whole-future form, dated at $t$ and with the law included, of … (ii′)". Term (ii′) at $t+1$ is $I(o_{t+1}; S_{t+1} \mid \mathcal C_t, a_t)$: what the next observation says about the target *it is emitted from*. The predicate's one-step term is $I(o_{t+1}; S_t \mid \mathcal C_t, a_t)$: what it says about the target *now*. By data processing ($S_t \to S_{t+1} \to o_{t+1}$, with $\theta$ in both) the second is at most the first, and they differ in exactly the case the paragraph uses to motivate the stream form. With $A = 0$, (ii′) is $\tfrac12 \log(1 + u/c) \gt 0$ while the predicate is 0. Also, (ii′) already includes the law: `#deriv-mismatch-budget-attribution` labels it "state-and-law information", and this paragraph calls it "state-uncertainty information". A true statement would be: the predicate is the retrospective, whole-future counterpart of (ii′). The two coincide in sign when the target persists and part ways when it is drawn afresh.

A consequence worth noting somewhere, probably not here: the fresh-state loop is out of scope, yet the mismatch decomposition attributes a positive "state-and-law" floor to it. That attribution is the declaration-relative one. The verifier's F4 calls this a trade, with each quantity robust to a different re-description, and I agree.

### 3.4 Smaller points

- **The third exclusion is not an exclusion.** "Three kinds of system sit outside … The third … an agent that knows everything the world will show but cannot compute its consequences fast enough". A compute-bound Kalman tracker is in, on the state warrant. What is true is that a compute shortfall never brings a system in. As written, the sentence lists compute-bound agents among those outside. "Knows everything the world will show" also reads as knowing the future observations; "has in its history everything the world could reveal" is what (d) means.
- **"The observer's own posterior"** (opening, housing paragraph). The twin's state is the Bayes posterior under $\pi_0$, whatever the agent computes. An agent with a bad filter has the same twin.
- **Condition 1 follows from condition 2.** With $\mathcal O = \emptyset$, $F_t$ is actions only, and actions carry nothing about $S_t$ beyond the history. Item (e) half-says this. Keeping $\mathcal O \neq \emptyset$ as an explicit gate may be worth it for continuity and for readers, but then it should be called a restatement, not a second condition.
- **"The same holds for any condition stated on the state …"** (end of the housing result). It is ambiguous what "the same" refers to. $H(S_t \mid \mathcal C_t) \gt 0$ does include known-law tracking and exclude case (d); what it shares is dependence on the declaration. Say that.
- **The $(\text{Agent}, \Omega)$ set.** The predicate depends on the agent only through $\mathcal A$ and its conduct before $t$. A fixed controller that never updates anything is in, if its world has something to reveal. I take that to be intended ("Whose uncertainty" says membership is not about the agent's conduct), but the opening's "Part I's machinery … is the theory of correcting a model" can read as if the scope requires a corrector. One sentence saying the scope is of situations, not of competent adapters, would forestall the question.
- **A stale dividend upstream.** `#def-agent-environment`'s audit-gold "propagation-freedom dividend" ("every downstream theorem may assume genuine uncertainty without re-earning it") is now false as an unconditional reading, since the predicate is dated. The segment's sentence "uses it at the times the result is applied" is the correction. That file's Working Note may want a pointer.

## 4. On the framing

The typed target and the stream form are right for what they are meant to do. Item (c) is the repair the old "full knowledge" exclusion needed, and I could not break any exact item. The challenge I would put to the framing is one the segment half-makes itself. By §2, every loop has an out-of-scope twin with the same interaction law. So the scope does not sort systems at all. It sorts *declarations of a world for a system*, and all of its discriminating power comes from two conventions:

1. the physical-state declaration, which the segment names ("AAT declares the physical world");
2. the choice of $\pi_0$, which it frames as "the modeler's viewpoint" and which, by §3.2, has to mean the agent's knowledge to give the advertised verdicts.

The opening paragraph's plain-language test ("its world can still show it something it does not yet know") is a good test, but only once both conventions are fixed. As written it reads as a property of the system. The honest and stronger framing puts both declarations up front as the scope's real postulates, with the housing result in its general form as the reason they are needed. If the invariant-$\sigma$-field constraint of §2 survives a closed-loop treatment, the second convention gets partly discharged, and law learning becomes behavioural. That would be a real result, and it is the strengthening I would spike.

## 5. What I did not check

- The four-term refinement, the autonomy proposal (WN 1), and the ascent-gating material: these are out of my brief and are marked unverified in the segment.
- Whether any downstream result cites this scope in a way that needs membership uniformly in $t$. I saw no such use in the files I read, but I did not walk the citers (`git grep scope-adaptive-system` lists 21 files).
- The closed-loop version of the invariant-$\sigma$-field claim.

## 6. On the brief

The brief worked well for a cold read. Naming the two test cases gave me a falsifiable target without telling me where to look. That is how §3.2 surfaced: I tried to *derive* RL's verdict, and I could not do it without choosing a $\pi_0$. One suggestion for the lead reviewer: §2 and §3.2 are the two findings that change what the segment claims. The rest are wording fixes that can land with them.

## Appendix — check script

```python
# python3 -I; two-state, one-action tabular world, rows ~ Beta(1,1) independently.
import itertools, math
from fractions import Fraction as F
def beta_int(a,b): return F(math.factorial(a)*math.factorial(b), math.factorial(a+b+1))
def phys_prob(seq):               # physical declaration: theta random, o_t = s_t, s_1 = 0
    n={(s,u):0 for s in (0,1) for u in (0,1)}
    for x,y in zip(seq,seq[1:]): n[(x,y)]+=1
    return beta_int(n[(0,0)],n[(0,1)])*beta_int(n[(1,0)],n[(1,1)])
def twin_prob(seq):               # Bayes-adaptive twin: state (s, counts), one fixed known kernel
    c={(s,u):1 for s in (0,1) for u in (0,1)}; p=F(1)
    for x,y in zip(seq,seq[1:]): p*=F(c[(x,y)], c[(x,0)]+c[(x,1)]); c[(x,y)]+=1
    return p
print(max(abs(phys_prob((0,)+t)-twin_prob((0,)+t)) for t in itertools.product((0,1),repeat=7)))  # 0
def dig(x):
    r=0
    while x<6: r-=1/x; x+=1
    return r+math.log(x)-1/(2*x)-1/(12*x*x)+1/(120*x**4)
def H(p): return 0 if p in (0,1) else -(p*math.log(p)+(1-p)*math.log(1-p))
def mi_after(n):                  # E_hist I(row; next transition) after n visits; Beta-binomial marginal is uniform
    tot=0
    for k in range(n+1):
        a,b=k+1,n-k+1; EH=dig(a+b+1)-(a/(a+b))*dig(a+1)-(b/(a+b))*dig(b+1)
        tot+=(H(a/(a+b))-EH)/(n+1)
    return tot
print([round(mi_after(n),6) for n in (0,1,10,100,1000)])  # 0.193147, 0.136514, 0.038548, 0.004827, 0.000498
```
