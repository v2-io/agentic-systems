# 05 — Integration checks and the decision record for the root-ontology landing

**KR A.1** (`msc/inside-out-2026-10/INTENT.md`): `#scope-adaptive-system` carries the typed predicate or a defended alternative, the GA registry names $\theta$, and a cold reader can check membership on standard RL and on a Kalman filter.

*Integrator: Opus 5.5, 2026-10-30. This file is for the verifier of the landing and for anyone who later asks why canon says what it says. The canon text is the source; this file holds the reasoning and the checks re-run before landing.*

## The decision, as three separate questions

The July brief posed one choice (typed target or not). It is three questions, and they have different answers and different evidence.

1. **The target: adopt $S_t = (\Omega_t, \theta)$.** Evidence-decided. With an unknown observation law and a state-only conditioning object, GA-1 has no determinate truth value: two descriptions of one observation process satisfy and violate it (`01-ga1-verification.md` §4, refute-posture agent plus Monte Carlo, re-run below). Typing the target restores the identity and its labels together, and every ad hoc housing of $\theta$ in canon (the bandit inside $\Omega$, exploit-explore-deliberate outside it) is adjudicated by the invariance cut (`02-typed-predicate.md` §4.3). `~/src/aat-refactored/` adopted it in its Chapter 1 (`src/adaptive-scope.md`).

2. **The functional: the future-stream predicate $\sup_{\pi'} I_{\pi'}(S_t; F_t \mid \mathcal C_t) \gt 0$, not $H(S_t \mid \mathcal C_t) \gt 0$.** This is the "defended alternative" A.1 licenses. Typed residual entropy is kept as a necessary condition (item (a) of the segment). The defence is three cases where residual entropy counts uncertainty the world can never show, each elementary:
   - a channel that carries nothing about state or law ($\mathcal O \neq \emptyset$ but blind). `#hyp-solicitable-escape` already asserted this case is outside scope; under typed entropy it would be inside, and the escape segment would contradict the scope it cites;
   - law at state–action pairs no policy can reach (`02-typed-predicate.md` §9.2 flagged this as a standing problem for the entropy form);
   - a state drawn afresh each step and seen through noise. Re-describing it as channel noise changes no observable and flips the entropy verdict, while the stream verdict is "out" both ways (`aat-refactored` spike 02a L5, re-derived by its verifier).

   The stream form also needs no reference measure for continuous or kernel-valued targets. Its cost is more machinery at the front door (a future stream and a sup over continuations). The segment pays that cost in plain language first: "the world can still show it something it does not know".

   **Modal, not own-policy.** The sup over continuations is chosen on the scope's own grounds: the scope asks what the world can still show, not what this agent's habits will show. A second reason is that with randomized own policies the observation-only own-policy form excludes a loop that learns its whole target next step (`de-novo-feedback-1.md` F1, the XOR case, re-run below). The rewrite's argument that the own-policy/modal gap "is the stuck population" is false in the generic case (F5) and is not used.

3. **The housing: a declared-world scope, with the no-go stated as present truth.** The belief-state twin (`de-novo-feedback-1.md` F2; classical belief-state reduction, Åström 1965, Kaelbling–Littman–Cassandra 1998) shows that no condition depending only on the interaction law can include known-law tracking. That holds for every state-based predicate, the old one and typed entropy included. So the fork (a) behavioural scope / (b) declared-world scope is orthogonal to questions 1 and 2. It is not an alternative to the typed predicate. On the merits it decides for (b): `#def-agent-environment` already treats the decomposition as a modeling choice, `#example-kalman` is the calibration anchor at "Mapping: exact", and Part I's persistence race is about keeping up with a moving physical state. A behavioural scope would put every known-law tracker out. The rewrite's "policy-invariance recovers determinacy for actors" is false (F2) and is not used; the no-go is stated for every known-law loop, acting or passive.

**Compute-shortfall** is out by design. Both spikes agree it is a ratio between agent and world, not a property of the coupling; the segment says so in one sentence and records a compute-relative scope as open.

## Checks re-run by the integrator

Script below, run with `python3 -I`; all four reproduce.

| Check | Result |
| --- | --- |
| Kalman membership, scalar, $P_t = 0.3$, $q = 0.25$, $r = 1$, horizon 5 | random walk ($A = 1$): $I = 0.190$ nats, in; fresh state ($A = 0$): $I = 0$, out |
| XOR case (F1): $\theta$ a fair bit, action a fair coin, $o = \theta \oplus a$ | $I(\theta; o) = 0$, $I(\theta; (a, o)) = 1$ bit |
| Belief-state twin (F2): two sensors $r \in \{0.2, 3.0\}$, $a = 0.9$, $q = 0.5$; one fixed kernel on $(m, P)$ | observation covariance equal to the physical housing's for all 64 six-step sensor schedules, max difference $8.9 \times 10^{-16}$ |
| GA-1 twin (`01` §4), $\tau = 1$, $q = 0.5$, $r = 0.7$ | state-only description B overstates $\mathbb E[\delta_t^2]$ by exactly $\tau^2 - \sigma_{t-1}^2$ ($0.575, 0.844, 0.931$ at $t = 2, 5, 11$); typed conditioning exact (difference $0$); Monte Carlo ($N = 4 \times 10^5$) Bayes MSE $0.806$ against closed form $0.809$ at $t = 11$ |

Derived by hand for the segment and checked in writing there:

- item (g), absorption of the law part, by the chain rule;
- item (h), prior equivalence. The future stream is independent of $\Omega_1$ given $(S_t, \mathcal C_t)$, so a positive density on $(\Omega_1, \theta)$ reweights only the law of $(S_t, \mathcal C_t)$;
- the tabular-RL item (c), by strict concavity of entropy under a non-degenerate Dirichlet posterior.

## Tier basis

- *Exact*, landed:
  - the membership items (a)–(h), each a short computation shown in the segment;
  - the housing result, a classical reduction re-run here;
  - the GA-1 twin in `#result-mismatch-decomposition`, which `01` verified and this file re-ran;
  - the total-variance split of term (ii), which is the law of total variance.
- Not landed, single-agent and unverified:
  - the four-term decomposition (`02` §6);
  - the invariance cut's canonicity as a theorem (`02` §3.1). The cut is landed as a naming rule, which needs no theorem;
  - "behaviour determines exactly the law part" (`de-novo-feedback-1.md` F2 sharpening);
  - the autonomy declaration as what pins the physical housing (F3);
  - everything in `04-ascent-gating.md` and §8 of `00-spike.md`.

  The open items are listed in the segment's Working Notes.

## Where the landing touched

`#scope-adaptive-system` (rewritten), `#def-agent-environment`, `#def-action-transition`, `#def-observation-function` (observation kernel; atoms typed), `#result-mismatch-decomposition` (GA-1 on $S_t$, label of term (ii), the twin), `#deriv-mismatch-budget-attribution`, `#emp-update-gain`, `#deriv-adaptive-gain-dynamics`, `#deriv-recursive-update` and `#der-recursive-update` (C2's rationale), `#hyp-solicitable-escape`, `#example-kalman`, `#example-bandit`, `#scope-logogenic-agent`, `#disc-structural-imagination` (Working Note), NOTATION (primitives and GA-1), three terminology entries, OUTLINE rows. `#def-strategy-dag:187` cites this scope for content it does not hold ("the defining feature of an adaptive agent is that it revises its strategy"); that file belongs to the concurrent strategy-DAG integrator and was flagged to the lead rather than edited.

## Appendix — the check script

```python
import numpy as np, itertools, math
from collections import Counter
def kalman_mi(a,q,r,P,k=5):  # I(x_t; o_{t+1..t+k} | C_t), scalar, x_t | C_t ~ N(m, P)
    Cxo=np.array([a**j*P for j in range(1,k+1)]); Coo=np.zeros((k,k))
    for i in range(1,k+1):
        for j in range(1,k+1):
            Coo[i-1,j-1]=a**i*a**j*P+sum(a**(i-s)*a**(j-s)*q for s in range(1,min(i,j)+1))+(r if i==j else 0)
    post=P-Cxo@np.linalg.solve(Coo,Cxo); return 0.5*math.log(P/post)
print(kalman_mi(1,0.25,1.0,0.3), kalman_mi(0,0.25,1.0,0.3))
jo,jao=Counter(),Counter()
for th in (0,1):
    for aa in (0,1): jo[(th,th^aa)]+=.25; jao[(th,(aa,th^aa))]+=.25
def mi(j):
    px,py=Counter(),Counter()
    for (x,y),p in j.items(): px[x]+=p; py[y]+=p
    return sum(p*math.log2(p/(px[x]*py[y])) for (x,y),p in j.items())
print(mi(jo), mi(jao))
a,q=0.9,0.5; rs={0:0.2,1:3.0}
def phys(s,P1):
    N=len(s); C=np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            C[i,j]=a**i*a**j*P1+sum(a**(i-u)*a**(j-u)*q for u in range(1,min(i,j)+1))+(rs[s[i]] if i==j else 0)
    return C
def belief(s,P1):  # world state (m, P); emits m + innovation; moves by the Kalman update
    N=len(s); L=np.zeros((N,N)); m=np.zeros(N); P=P1; S=[]
    for t in range(N):
        r=rs[s[t]]; St=P+r; L[t]=m.copy(); L[t,t]+=1; S.append(St)
        e=np.zeros(N); e[t]=1; m=a*(m+(P/St)*e); P=a*a*P*r/(P+r)+q
    return L@np.diag(S)@L.T
print(max(np.abs(phys(s,1.3)-belief(s,1.3)).max() for s in itertools.product([0,1],repeat=6)))
tau,qq,rr=1.0,0.5,0.7; v=qq**2+rr**2
for t in (2,5,11):
    s2=tau**2*v/(v+(t-1)*tau**2); lhs=s2+qq**2+rr**2
    print(t, (qq**2+tau**2+rr**2)-lhs, tau**2-s2, (qq**2+s2+rr**2)-lhs)
```

## After the cold read (`06-cold-read.md`)

Two statements above were narrower or looser than the truth, and the segment now carries the corrected forms:

- **The housing result holds for every loop, not only known-law loops.** Re-housing as the Bayes posterior over all of $S_t$ gives, for tabular RL, the Bayes-adaptive MDP: a case-(d) twin with the same observations. "A behavioural scope would put every known-law tracker out" above should read "would put every loop out". The fork's resolution to a declared world is unchanged, and it now covers law learning as well as tracking. Whether a stronger invariance rule, one that requires every invariant function of the path to be in $\theta$, makes law learning behaviour-determined is the strengthening the segment's Working Notes record.
- **$\pi_0$ needed a rule.** Item (h) shows that only its support matters, but the support decides RL's verdict, and "the modeler's viewpoint" did not fix it. The segment now fixes $\pi_0$ as the law of the world given what the agent knows by design.

The integrator re-derived both points before landing them, and the cold reader's script reproduces. The cold reader's smaller findings were all landed: the transient/decaying correction, the prior switch in (c), the known-noise condition in (e), the (ii′) relation, the compute sentence, and condition 1 as a restatement.
