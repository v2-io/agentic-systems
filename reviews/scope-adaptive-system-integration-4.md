---
kind: review
author:
  name: Claude Opus 5.5 (A.1 check-4 integrator)
  role: integrator
sources:
  - spikes/epistemic-target-ontology/10-check-4-integration.md
written: 2026-10-30T22:08:51Z
---

# 2026-10-30: rederive of segment:scope-adaptive-system after check-4

KR A.1. The integrator's own re-derivations of what it landed at c79e1aed, recorded so a different mind can confirm or break them. Reasoning and the check script are in the source above.

## C1 (check)
- target: segment:scope-adaptive-system
- at: c79e1aed
- act: rederive
- line: derivation
- criterion: Item (g′): $u_k = I(S_t; o_{k+1} \mid \mathcal C_k, a_k) + r_k$ by the chain rule in two orders and the Markov commitment, and value $+ \sum_k r_k = \sum_k u_k$ in $[0, \infty]$; the law never renews; with a finite value, $u_k - r_k \to 0$
- committed: after
- outcome: confirmed
- recheck: 10 §1; identity to $10^{-13}$ or better on the scalar random walk and a random 2-D system, $8 \times 10^{-8}$ on a random 3-D system with near-singular $Q$; sign flip renewal $4 \times 10^{-10}$ (all autonomous; the proof covers actions)

## C2 (check)
- target: segment:scope-adaptive-system
- at: c79e1aed
- act: rederive
- line: derivation
- criterion: Item (g′), linear-Gaussian renewal $r_k = \tfrac12 \log\det(I + C A \tilde P_k A^\top C^\top N^{-1})$ with $\tilde P$ the filter restarted at $t$ from zero; scalar random walk renewal rising to $0.135$ and $\sum_k (u_k - r_k) = 0.162$
- committed: after
- outcome: confirmed
- recheck: 10 §1; formula against the direct conditional MI from the joint covariance, $1.4 \times 10^{-15}$ (2-D) and $8.4 \times 10^{-8}$ (3-D)

## C3 (check)
- target: segment:scope-adaptive-system
- at: c79e1aed
- act: rederive
- line: derivation
- criterion: Item (g): the law-part statement; the whole-target bound $I(S_s; F_s \mid \mathcal C_s) \leq I(S_t; F_s \mid \mathcal C_s) + \sum_{k \geq s} r_k$ and its consequence (out at $t$ with no renewal implies out later); the clocked fresh-state example showing leaving need not be final otherwise
- committed: after
- outcome: confirmed
- recheck: 10 §1 and §4 item 1; the clocked example worked by hand, not in the script

## C4 (check)
- target: segment:scope-adaptive-system
- at: c79e1aed
- act: rederive
- line: derivation
- criterion: Epistemic Status: the component counterexample ($w$ invariant standard normal seen through unit noise, $z_1 = w$, $z_k = 0$ after): $I(z_1; F_1 \mid \mathcal C_1) = \infty$ while $z$'s one-step parts sum to $\tfrac12 \log \tfrac32$
- committed: after
- outcome: confirmed
- recheck: 10 §2; closed form

## C5 (check)
- target: segment:scope-adaptive-system
- at: c79e1aed
- act: rederive
- line: derivation
- criterion: Discussion, "Two kinds of warrant": the sign flip (one-step part like $1/(2t)$, value infinite, no renewal); the novel-row law ($\log 2 - \tfrac12$ per step); the doubling map read through its first digit ($\log 2$ per step, no renewal); the random walk (value $0.162$, one-step $0.135$, renewal rising to it); a known drift schedule from an unknown phase renews nothing
- committed: after
- outcome: confirmed
- recheck: 10 §1; script lines for the sign flip, novel row and random walk; the doubling map by hand

## C6 (check)
- target: segment:scope-adaptive-system
- at: c79e1aed
- act: rederive
- line: derivation
- criterion: Working Notes regression guard: tail-measurable iff at each $n$ a function of the path from $n$ on (Doob–Dynkin); the sign flip's sign is tail- but not invariant-measurable; the doubling map's tail $\sigma$-field is trivial (i.i.d. binary digits, Kolmogorov zero–one), so the tail rule leaves it as state that renews nothing
- committed: after
- outcome: confirmed
- recheck: 10 §2
