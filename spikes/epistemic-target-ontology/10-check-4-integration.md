# 10 — Integrating the independent check (09) into `#scope-adaptive-system`

**KR A.1** (`msc/inside-out-2026-10/INTENT.md`), under the top intent *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."*: `#scope-adaptive-system` carries the typed predicate or a defended alternative, and a cold reader checks the membership clauses on standard RL and on a Kalman filter.

*Integrator: Opus 5.5, 2026-10-30. I read 09 and its review record whole, then 08, the segment, its four `depends:` segments and the dependents 09 names. I took the lead's brief at its word: 09's closed/renewing proposal, its proofs and its wordings were inputs to re-derive. Canon is at `c79e1aed`; the typed record is `reviews/scope-adaptive-system-integration-4.md`. This file is for the next checker. It holds the reasoning, where I diverge from 09, and where I am most likely wrong. Every number below comes from the script in the appendix.*

## 1. The strengthening: renewal characterizes "renewing" in general

The lead asked for a general characterization of 09's "renewing", or a no-go. There is a characterization, and it is exact. Fix a continuation and, for $k \geq t$, let $u_k = I(S_k; o_{k+1} \mid \mathcal C_k, a_k)$ be the one-step part at $k$ and $r_k = I(S_k; o_{k+1} \mid S_t, \mathcal C_k, a_k)$ its *renewal* since $t$.

- Given $(S_k, \mathcal C_k, a_k)$, $o_{k+1}$ is independent of $S_t$: $o_{k+1}$ is produced from $(\Omega_k, a_k, \theta)$ by the transition and the channel with noise drawn after everything in the conditioning, and $a_k$ is a function of $\mathcal C_k$ and independent randomness. So the chain rule on $I(S_t, S_k; o_{k+1} \mid \mathcal C_k, a_k)$ taken in both orders gives $u_k = I(S_t; o_{k+1} \mid \mathcal C_k, a_k) + r_k$.
- With $\mathcal C_{k+1} = (\mathcal C_k, a_k, o_{k+1})$ (`#def-chronica`), the chain rule over the stream gives $I(S_t; F_t \mid \mathcal C_t) = \sum_{k \geq t} [I(S_t; a_k \mid \mathcal C_k) + I(S_t; o_{k+1} \mid \mathcal C_k, a_k)]$, and every action term is $0$.
- Hence value $+ \sum_k r_k = \sum_k u_k$ in $[0, \infty]$. For finite horizons this is an identity of finite sums; the infinite form follows because the stream's information is the limit of its blocks' and every term is nonnegative.

Consequences, all landed as item (g′) and in the Discussion:

- **The law never renews.** $\theta$ is in both $S_t$ and $S_k$, so $r_k = I(\Omega_k; o_{k+1} \mid \Omega_t, \theta, \mathcal C_k, a_k)$.
- **Where nothing renews, the value is a stock.** It equals the sum of later one-step parts. A finite stock forces $u_k \to 0$.
- **Finite value, standing one-step part, iff standing renewal.** If the value is finite, $u_k - r_k = I(S_t; o_{k+1} \mid \cdot)$ is a summable nonnegative sequence and tends to $0$.
- **Linear-Gaussian.** Given $(x_t, \mathcal C_k)$, $x_k$ is Gaussian with the covariance $\tilde P_k$ of a filter restarted at $t$ from $\tilde P_t = 0$, because given $x_t$ the observations up to $t$ are independent of what follows. The next observation is $C A x_k$ plus noise independent of $(x_t, x_k, \mathcal C_k)$, so $r_k = \tfrac12 \log\det(I + C A \tilde P_k A^\top C^\top N^{-1})$, positive iff $C A \tilde P_k \neq 0$ by (b)'s argument. The script checks the formula against the conditional mutual information computed from the explicit joint covariance, to $10^{-15}$ on a random 2-D system and $10^{-8}$ on a random 3-D one with a near-singular $Q$. For the scalar random walk, $r_k$ rises $0, 0.112, 0.131, \ldots \to 0.1346$, the steady one-step part, and $\sum_k (u - r_k) = 0.1618$, the value.

**What the infinite-value case does not allow.** Without renewal, an infinite stock can be drawn at a rate that falls or one that does not. That is a no-go for "standing iff renewing" in general, shown on both sides of the cut:

- law: 09's novel-row world, $\log 2 - \tfrac12 = 0.1931$ nats per step;
- state: the doubling map $x_{t+1} = 2 x_t \bmod 1$ from a uniform start, read through the first binary digit of $x_t$. Given $\mathcal C_k$, the first digit of $x_k$ is known and the next digit is uniform, and $o_{k+1}$ is that digit, so $u_k = \log 2$ for every $k$; $x_k$ is a function of $x_t$, so $r_k = 0$.

The doubling map is the physical case 09's list lacked: chaos read coarsely. It is the reason the Discussion says "the state/law cut ... puts the law on one side", not "state renews".

I also checked monotonicity, $r_k(t) \geq r_k(s)$ for $t \lt s \leq k$: $r_k(t) - r_k(s) = I(S_s; o_{k+1} \mid \cdot) - I(S_t; o_{k+1} \mid \cdot) \geq 0$, because given $(S_s, \mathcal C_k, a_k)$, $o_{k+1}$ is independent of $S_t$ (everything after $s$ is a function of $S_s$, $\mathcal C_s$ and randomness drawn after $s$; weak union). It holds numerically (minimum difference $5 \times 10^{-6}$ on the 3-D system). Canon does not need it: (g) follows directly from $I(S_s; o_{k+1} \mid \cdot) \leq u_k$.

## 2. Where I diverge from 09

- **09's component telescoping is false.** 09 §2 item 1 states the identity for a closed component $Z$ "the rest of the target does not feed". Prior correlation is enough to break it. Take an invariant $w \sim \mathcal N(0, 1)$, seen through unit Gaussian noise, and a state coordinate $z$ with $z_1 = w$, $z_k = 0$ for $k \geq 2$. $z$ is closed, and $w$ never feeds it. Yet $I(z_1; F_1 \mid \mathcal C_1) = I(w; o_2, o_3, \ldots \mid o_1) = \infty$, while $z$'s one-step parts are $\tfrac12 \log \tfrac32$ at $k = 1$ and $0$ after. The data-processing step 09 cites needs $o_{k+1}$ independent of $Z_t$ given $(Z_k, \mathcal C_k, a_k)$, which fails when the rest of the target carries $Z_t$. Canon states the identity for the whole target and gives this counterexample in the Epistemic Status.
- **09's (g) for closed components is right**, and needs no Markov condition: data processing and the chain rule suffice. I did not land it in that form. The whole-target statement with renewal is stronger in the direction that matters, giving the bound $I(S_s; F_s \mid \mathcal C_s) \leq I(S_t; F_s \mid \mathcal C_s) + \sum_{k \geq s} r_k$. The law-part statement already covers the one component canon names.
- **"Closed" is a sufficient condition for zero renewal, not a characterization.** Fresh randomness in directions no observation ever sees gives $r = 0$ without closedness. So canon defines the carve by $r$, and gives measurable closedness as "for instance".
- **Condition 2: kept numbered, not dropped.** The advisor I consulted suggested dropping it. `#scope-agency` numbers its added conditions 3 and 4, and `#scope-logogenic-agent` lists all four, so dropping would renumber Part II, which has its own worktree. $\lvert\mathcal O\rvert \geq 2$ is true, necessary, implied by condition 1, and says what "no channel" is formally. `#scope-logogenic-agent`:45 restated the vacuous form and now reads $\lvert\mathcal O\rvert \geq 2$.
- **The tail rule (09 F1).** 09 says a tail rule "captures" the sign flip's phase. True. But even the tail rule does not make "state" coincide with "renews": the doubling map's tail $\sigma$-field is trivial (its state at $n$ is $0.b_n b_{n+1} \ldots$, the binary digits are i.i.d., and $\sigma(x_n, x_{n+1}, \ldots) = \sigma(b_n, b_{n+1}, \ldots)$, so Kolmogorov's zero–one law applies), so the state stays state and renews nothing. In the Working Notes, as a regression guard. The equivalence "tail-measurable iff at each $n$ a function of the path from $n$ on" is Doob–Dynkin applied to $\sigma(X_n, X_{n+1}, \ldots)$ at each $n$; I cite nothing for it. I did not look up Blackwell–Freedman either.

## 3. The smaller findings

- **F2 (cut wording, (b)'s label).** The invariance rule now says it applies to the declared world's variables, which is what the Working Notes said it was. (b) is qualified with "no coordinate of $x$ constant along the run (for example $Q \succ 0$)", and says a constant coordinate is law with the criterion unchanged. Under the coordinate rule, 09's functional-reading example (an invariant direction that is no coordinate) leaves the label "$\theta$ fixed" true. The functional/tail form is the Working Notes' strengthening.
- **F3.** (c) and the Discussion now say "fixed every part of its law that any continuation could show", and (c) names the unreachable rows that stay uncertain.
- **F4.** Above.
- **F5.** The Discussion sentence is rewritten; it now says "whenever some continuation returns to a pair without bound".
- **F6.** The Definition paragraph, `#def-action-transition`:12, 33, `#def-observation-function`:15, 37 and NOTATION's $\theta$ row now say "whatever of it the agent was not built knowing is random under $\pi_0$". I swept `01`–`04`, NOTATION and `terminology/entries` for "the analysis leaves", "analysis does not fix" and "modeler's reference measure"; none remain.
- **F7, F8.** `#def-agent-environment`:13, 31, 35 now say the information-loss boundary is necessary and the scope states the exact condition. `#disc-framework-self-diagnostic`:19 is now conditional, on the declared world still having something to show.
- **Not in 09:** `#example-bandit`:42 justified its (true) standing warrant by motion, "each mean keeps moving". It now cites the fresh Gaussian step, which is renewal. `#example-kalman`:43 justifies its warrant by (b)'s criterion, which is correct, so I left it.

## 4. Where a checker who has not read this may want to look

In the order I think I am most likely wrong:

1. **(g)'s clocked example.** A state drawn afresh at every step, carrying a clock, which from time $m$ on the channel reports one step late (so the state at $k$ must also carry the previous draw). For $t \lt m$, nothing later bears on $x_t$; from $t = m$, $o_{t+1}$ is $x_t$. I worked it in my head, not in the script.
2. **The infinite-sum form of (g′)** when some $u_k$ is infinite (noise-free continuous channels). Then $r_k$ is infinite too, and the identity holds in $[0, \infty]$. Whether every consequence I drew is stated so that it survives infinite terms is worth a look.
3. **The linear-Gaussian restart argument**, if a checker reads (b) as allowing actions (sensor choice in `#example-kalman`). With actions that depend on the history, $\tilde P_k$ still conditions on $x_t$ and $\mathcal C_k$ only. I believe the restart argument goes through, because a sensor schedule fixed by the history changes $C$ per step but not the conditional independence. The script is autonomous throughout, and the proof covers actions by its construction.
4. **The reworded/redefined classifications** (commit body).
5. **Whether the Discussion's two paragraphs read as one picture** to a reader who did not see the old state/law thesis.

## 5. Open, in vsect rather than prose

Nothing new that I could not settle. Already open, and still open: the continuous-space (h′), the knowledge/belief boundary, and the five citations not in relata (08 §3). 09's findings stay open under its name for a different mind to confirm against `c79e1aed`.

## 6. On the brief

The brief's warning about the pattern ("typed against a parametrization or a reading rather than the segment's own definitions") fired here in a new form. 09's component claim was typed against a component of the target rather than the target the predicate is defined on, and failed exactly there. Re-deriving from the predicate's own object, the whole $S_t$, is what made the general identity fall out. My first draft of the answered-question Working Note claimed that a tracker keeps a standing warrant only where renewal does. That is false without a finite value: the doubling map came from checking it.

## Appendix — check script

`python3 -I` on this code reproduces every number above. The component-$z$ lines are closed-form expressions, not simulation. numpy's `slogdet` prints spurious divide-by-zero warnings on stderr on this machine.

```python
import numpy as np
rng = np.random.default_rng(0)
def ld(M): return np.linalg.slogdet(M)[1]

def gauss_check(A, C, Q, R, P0, t, n):
    """Linear-Gaussian loop, known law, no actions. Joint Gaussian over states and observations built
    explicitly from (x_1, w_1.., v_1..). Returns V = I(x_t; o_{t+1..t+n} | C_t), sum_k u_k, sum_k r_k(t),
    for k = t..t+n-1, with u_k = I(x_k; o_{k+1} | C_k) and r_k = I(x_k; o_{k+1} | x_t, C_k)."""
    d, p = A.shape[0], C.shape[0]; T = t + n
    nz = d + d*(T-1) + p*T
    Sig = np.zeros((nz, nz)); Sig[:d, :d] = P0
    for j in range(T-1): Sig[d+d*j:d+d*(j+1), d+d*j:d+d*(j+1)] = Q
    for k in range(T): o0 = d+d*(T-1)+p*k; Sig[o0:o0+p, o0:o0+p] = R
    X = []
    for k in range(1, T+1):
        M = np.zeros((d, nz)); M[:, :d] = np.linalg.matrix_power(A, k-1)
        for j in range(1, k): M[:, d+d*(j-1):d+d*j] = np.linalg.matrix_power(A, k-1-j)
        X.append(M)
    O = []
    for k in range(1, T+1):
        M = (C @ X[k-1]).copy(); o0 = d+d*(T-1)+p*(k-1); M[:, o0:o0+p] += np.eye(p); O.append(M)
    def H(blocks):
        if not blocks: return 0.0
        B = np.vstack(blocks); return 0.5*ld(B @ Sig @ B.T)
    def cmi(a, b, c): return H(a+c) + H(b+c) - H(a+b+c) - H(c)
    V = cmi([X[t-1]], O[t:t+n], O[:t])
    U = sum(cmi([X[k-1]], [O[k]], O[:k]) for k in range(t, t+n))
    Rn = sum(cmi([X[k-1]], [O[k]], [X[t-1]] + O[:k]) for k in range(t+1, t+n))  # r_t = 0: S_t given S_t
    return V, U, Rn

V, U, Rn = gauss_check(np.eye(1), np.eye(1), np.eye(1), np.eye(1), np.eye(1), 5, 30)
print("scalar RW t=5 n=30:   V=%.6f sumU=%.6f sumR=%.6f  V+sumR-sumU=%.1e" % (V, U, Rn, V+Rn-U))
A = rng.normal(size=(2, 2))*0.7; C = rng.normal(size=(1, 2)); q = rng.normal(size=(2, 1))
Q = q@q.T + 1e-9*np.eye(2); R = np.eye(1)*0.5
V, U, Rn = gauss_check(A, C, Q, R, np.eye(2), 4, 25)
print("random 2-D t=4 n=25:  V=%.6f sumU=%.6f sumR=%.6f  V+sumR-sumU=%.1e" % (V, U, Rn, V+Rn-U))
A3 = rng.normal(size=(3, 3))*0.6; C3 = rng.normal(size=(2, 3)); Q3 = np.diag([1.0, 0.3, 1e-9]); R3 = np.diag([0.4, 1.3])
V, U, Rn = gauss_check(A3, C3, Q3, R3, np.eye(3), 3, 20)
print("random 3-D t=3 n=20:  V=%.6f sumU=%.6f sumR=%.6f  V+sumR-sumU=%.1e" % (V, U, Rn, V+Rn-U))
# sign flip, Q ~ 0: closed, so renewal ~ 0 and V = sum U
V, U, Rn = gauss_check(-np.eye(1), np.eye(1), 1e-12*np.eye(1), np.eye(1), np.eye(1), 10, 40)
print("sign flip t=10 n=40:  V=%.6f sumU=%.6f sumR=%.2e   0.5log(1+40/11)=%.6f" % (V, U, Rn, 0.5*np.log(1+40/11)))

# RW renewal via the filter restarted at t from P~ = 0: r_k = 0.5 log(1 + P~_k / N), N = Q + R = 2
Pt = 0.0; rs = []
for k in range(60):
    rs.append(0.5*np.log(1 + Pt/2.0)); Pm = Pt + 1; Pt = Pm/(Pm + 1)
print("RW renewal, k-t = 0,1,2,5,59:", [round(rs[i], 4) for i in (0, 1, 2, 5, 59)], " P~ ->", round(Pt, 4))
Pinf = (np.sqrt(5)-1)/2; u = 0.5*np.log(1 + Pinf/2)
print("RW steady: sum_k (u - r_k) over 60 steps = %.4f   (V = 0.5 log(P_inf/P_s) = 0.1618)" % sum(u - r for r in rs))

# 09's component telescoping, with the rest of the target not feeding Z: z_1 ~ N(0,1), z_k = 0 for k >= 2
# (closed: a function of z_1), w = z_1 invariant, o_k = w + v_k, unit noise. Rest (w) never feeds z.
for n in (10, 1000, 10**6):
    VZ = 0.5*np.log(1 + n/2)   # I(z_1; o_2..o_{n+1} | o_1): posterior var 1/2 after o_1
    UZ = 0.5*np.log(1 + 0.5)   # only k = 1 term: I(z_1; o_2 | o_1); z_k = 0 constant afterwards
    print("component z, n=%7d: V^Z=%.3f   sum_k u^Z_k=%.3f" % (n, VZ, UZ))
# novelty row: one-step part log 2 - 1/2
print("novel row one-step part = %.4f" % (np.log(2) - 0.5))

# Linear-Gaussian renewal formula: r_k(t) = 0.5 logdet(I + C A P~_k A^T C^T N^{-1}), N = C Q C^T + R,
# with P~ the filter covariance restarted at t from 0. Compared with the direct conditional MI.
def gauss_parts(A, C, Q, R, P0, t, n):
    d, p = A.shape[0], C.shape[0]; T = t + n
    nz = d + d*(T-1) + p*T
    Sig = np.zeros((nz, nz)); Sig[:d, :d] = P0
    for j in range(T-1): Sig[d+d*j:d+d*(j+1), d+d*j:d+d*(j+1)] = Q
    for k in range(T): o0 = d+d*(T-1)+p*k; Sig[o0:o0+p, o0:o0+p] = R
    X = []
    for k in range(1, T+1):
        M = np.zeros((d, nz)); M[:, :d] = np.linalg.matrix_power(A, k-1)
        for j in range(1, k): M[:, d+d*(j-1):d+d*j] = np.linalg.matrix_power(A, k-1-j)
        X.append(M)
    O = []
    for k in range(1, T+1):
        M = (C @ X[k-1]).copy(); o0 = d+d*(T-1)+p*(k-1); M[:, o0:o0+p] += np.eye(p); O.append(M)
    def H(blocks):
        if not blocks: return 0.0
        B = np.vstack(blocks); return 0.5*ld(B @ Sig @ B.T)
    def cmi(a, b, c): return H(a+c) + H(b+c) - H(a+b+c) - H(c)
    return [cmi([X[k-1]], [O[k]], [X[t-1]] + O[:k]) for k in range(t+1, t+n)]
def riccati_r(A, C, Q, R, steps):
    d = A.shape[0]; P = np.zeros((d, d)); N = C@Q@C.T + R; out = []
    for _ in range(steps):
        out.append(0.5*ld(np.eye(C.shape[0]) + C@A@P@A.T@C.T@np.linalg.inv(N)))
        Pm = A@P@A.T + Q; K = Pm@C.T@np.linalg.inv(C@Pm@C.T + R); P = (np.eye(d) - K@C)@Pm
    return out
for (A_, C_, Q_, R_, P0_, t_, lab) in [(A, C, Q, R, np.eye(2), 4, "2-D"), (A3, C3, Q3, R3, np.eye(3), 3, "3-D")]:
    rr = riccati_r(A_, C_, Q_, R_, 25); dr = gauss_parts(A_, C_, Q_, R_, P0_, t_, 15)
    print(lab, "renewal: max |restarted-Riccati formula - direct MI|, k=t+1..t+14: %.1e" % max(abs(a - b) for a, b in zip(rr[1:15], dr)))
# monotonicity r_k(t) >= r_k(s), t < s <= k, on the 3-D system
d1 = gauss_parts(A3, C3, Q3, R3, np.eye(3), 3, 12)   # r_k(3), k = 4..14
d2 = gauss_parts(A3, C3, Q3, R3, np.eye(3), 6, 9)    # r_k(6), k = 7..14
print("monotonicity r_k(3) >= r_k(6), k=7..14: min difference %.3e" % min(a - b for a, b in zip(d1[3:], d2)))
```

Output:

```text
scalar RW t=5 n=30:   V=0.161741 sumU=4.039134 sumR=3.877393  V+sumR-sumU=-3.8e-14
random 2-D t=4 n=25:  V=0.038040 sumU=0.854427 sumR=0.816387  V+sumR-sumU=-1.7e-14
random 3-D t=3 n=20:  V=1.364797 sumU=17.247611 sumR=15.882814  V+sumR-sumU=-8.4e-08
sign flip t=10 n=40:  V=0.766965 sumU=0.766965 sumR=3.90e-10   0.5log(1+40/11)=0.766965
RW renewal, k-t = 0,1,2,5,59: [np.float64(0.0), np.float64(0.1116), np.float64(0.1312), np.float64(0.1346), np.float64(0.1346)]  P~ -> 0.618
RW steady: sum_k (u - r_k) over 60 steps = 0.1618   (V = 0.5 log(P_inf/P_s) = 0.1618)
component z, n=     10: V^Z=0.896   sum_k u^Z_k=0.203
component z, n=   1000: V^Z=3.108   sum_k u^Z_k=0.203
component z, n=1000000: V^Z=6.561   sum_k u^Z_k=0.203
novel row one-step part = 0.1931
2-D renewal: max |restarted-Riccati formula - direct MI|, k=t+1..t+14: 1.4e-15
3-D renewal: max |restarted-Riccati formula - direct MI|, k=t+1..t+14: 8.4e-08
monotonicity r_k(3) >= r_k(6), k=7..14: min difference 5.259e-06
```
