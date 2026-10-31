---
kind: review
author:
  name: Claude Opus 5.5 (A.1 round-7 integrator)
  role: integrator
sources:
  - spikes/epistemic-target-ontology/16-check-7-integration.md
written: 2026-10-30
---

# #scope-adaptive-system, #def-observation-function and #deriv-mismatch-budget-attribution at 7c1dd6a3: the integrator's re-derivations after check 7

KR **A.1** (`msc/inside-out-2026-10/INTENT.md`). These are what the integrator landed at `9648363b` and `7c1dd6a3`, re-derived for a different mind to confirm or break. The derivations are in the write-up named above, under the section given after each item. The integrator authored these revisions, so these checks are evidence to confirm, not confirmation.

## C1 (check)
- target: segment:scope-adaptive-system
- at: 7c1dd6a3
- act: rederive
- line: derivation
- criterion: The non-vacuity statement needs only fresh noise. Along any continuation, (ii′) at $o_{k+1}$ is at least $I(S_t; o_{k+1} \mid \mathcal C_k, a_k) + r_k$, and these sum over $k \geq t$ to the value plus the renewals. #def-action-transition's XOR world satisfies non-vacuity and breaks (g′) and (h). A remembering channel (check 6's world) breaks all three. Both claims are as the cut paragraph and the Discussion now state them.
- committed: after
- outcome: confirmed
- recheck: $o_{k+1}$ independent of $(S_t, S_k, \mathcal C_k)$ given $(S_{k+1}, a_k)$ by fresh noise, since $S_{k+1}$ holds the whole law; data processing; chain rule in $(S_t, S_k)$; chain rule over the stream with the action terms zero. XOR world at $t = 1$: value $\log 2$, all $u_k = r_k = 0$, (ii′) at $o_K$ is $H(\varepsilon_1 \mid o_1) = \log 2$
- read: segment:scope-adaptive-system, segment:def-action-transition, segment:def-observation-function, segment:deriv-mismatch-budget-attribution

Write-up §1.

## C2 (check)
- target: segment:scope-adaptive-system
- at: 7c1dd6a3
- act: rederive
- line: derivation
- criterion: The cut paragraph lists the users of the run-wide property: (c)'s draw step and test, (g)'s whole-target bound, (g′), (h), (h′)'s block law given $(s, \theta, c)$, and the housing result's compressed state. (g)'s law part does not use it. Neither does the Discussion's comparison of the one-step part with (ii′), which uses fresh noise only.
- committed: after
- outcome: confirmed
- recheck: for each item, the step that drops earlier variables from a conditional law, and which of the two fresh clauses that step needs
- read: segment:scope-adaptive-system, segment:def-action-transition, segment:def-observation-function

Write-up §1.

## C3 (check)
- target: segment:scope-adaptive-system
- at: 7c1dd6a3
- act: rederive
- line: derivation
- criterion: (c)'s membership test for observed-state loops, under any $\pi_0$: the loop is in at $t$ iff some continuation, with positive probability, takes at some $k \geq t$ an action whose row the history $\mathcal C_k$ does not fix. The same holds with the law of the next observation in place of the row whenever the history fixes the state at every time. The Dirichlet, deterministic-successor, bandit and unreachable-row instances agree with it.
- committed: after
- outcome: confirmed
- recheck: chain rule over the stream, each term non-negative at every history; given $\theta$ and $\mathcal C_k$, $o_{k+1}$ is a fresh draw from a law that is a function of $\theta$; lemma: for $X \mid K \sim K$, $I(K; X) = 0$ iff $K$ is a.s. constant ($K(B) = P(X \in B)$ a.s. on a countable generating $\pi$-system)
- read: segment:scope-adaptive-system, segment:def-action-transition, segment:def-observation-function

Write-up §2.

## C4 (check)
- target: segment:scope-adaptive-system
- at: 7c1dd6a3
- act: rederive
- line: derivation
- criterion: (c)'s real-reward bandit. Under a Dirichlet process with a full-support base, the posterior is never a point mass, so the loop is in at every $t$. Under $Q_m$ (rational finitely supported laws, each recurring infinitely often, shifted by $\sqrt 2/m$) drawn with probability $2^{-m}$, the supports $\mathbb Q + \sqrt 2/m$ are disjoint and the first reward identifies the law: in at $t = 1$, out from $t = 2$. Both measures have full weak support and they are mutually singular.
- committed: after
- outcome: confirmed
- recheck: $\sqrt 2 (1/m - 1/n) \notin \mathbb Q$; the shift by $\sqrt 2/m$ moves a law by at most $\sqrt 2/m$ in the Lévy–Prokhorov metric; the posterior Dirichlet process keeps a non-atomic base part; a Dirichlet process with non-atomic base gives probability zero to any countable set of laws
- read: segment:scope-adaptive-system

Write-up §2.

## C5 (check)
- target: segment:scope-adaptive-system
- at: 7c1dd6a3
- act: rederive
- line: derivation
- criterion: $\pi_0(W) = 1$ does not give $\operatorname{supp} \pi_0 = \overline W$. The Definition now requires, in the finite case, that $\pi_0$ charge every open set meeting $W$, and then $\operatorname{supp} \pi_0 = \overline W$. (h′)'s fourth fact holds: the posterior over $(\Omega_t, \theta)$ is the image of $L \cdot \pi_0$ under a projection of a compact space, and its support is the projection of the support.
- committed: after
- outcome: confirmed
- recheck: $\overline W$ is closed with full measure, so $\operatorname{supp} \subseteq \overline W$; charging every open set meeting $W$ gives $W \subseteq \operatorname{supp}$. A continuous image of a compact set is closed; an open set meeting the image pulls back to an open set meeting the support
- read: segment:scope-adaptive-system

Write-up §3.

## C6 (check)
- target: segment:def-observation-function
- at: 7c1dd6a3
- act: rederive
- line: derivation
- criterion: The observation kernel is the law of $o_t$ that $h$ and the noise's law induce at $(\omega, a)$. Under $\pi_0$ with $\theta_h$ random, the conditional law given $(\Omega_t, a_{t-1})$ alone is a mixture over $\theta_h$, so the old wording named the mixture. A channel memory that never changes along the run is named into $\theta_h$ by the invariance cut, not into $\Omega_t$.
- committed: after
- outcome: confirmed
- recheck: the conditional law given $(\omega, a)$ integrates the kernel against the conditional law of $\theta_h$ given $(\Omega_t, a_{t-1})$; the cut names every variable constant along every run under every policy into $\theta$
- read: segment:def-observation-function, segment:scope-adaptive-system

Write-up §4.

## C7 (check)
- target: segment:deriv-mismatch-budget-attribution
- at: 7c1dd6a3
- act: rederive
- line: derivation
- criterion: Proposition 1(ii)'s factorization $\mathbb P_\pi(\mathcal C, \Omega_{0:t}) = [\prod \pi] \cdot [\text{environment and channel factors}]$ follows from fresh transitions, fresh noise and (P), and not from GA-1 and (P) alone. The GA-1 line, with $\Omega = S_t$ as the Setting defines it, conditions on the law as well as the state.
- committed: after
- outcome: confirmed
- recheck: sequential factorization of the joint law, each world factor reduced to its kernel by the matching fresh clause, each action factor to $\pi(a_s \mid \mathcal C_s)$ by (P). Without fresh transitions, #def-action-transition's XOR world has a world factor that depends on $\varepsilon_1$, which GA-1 permits
- read: segment:deriv-mismatch-budget-attribution, segment:def-action-transition, segment:def-observation-function

Write-up §5.
