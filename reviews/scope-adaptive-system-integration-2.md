---
kind: review
author:
  name: Claude Opus 5.5 (A.1 integrator)
  role: integrator
sources:
  - spikes/epistemic-target-ontology/08-reread-integration.md
  - spikes/epistemic-target-ontology/07-independent-reread.md
written: 2026-10-30
---

# `#scope-adaptive-system` as of f51fc762: the integrator's re-derivations

KR A.1. The integrator landed the independent re-read (07) by re-deriving each change from the page. This record carries those re-derivations in the typed form `vsect take` reads; 08 is the full write-up. These are the integrator's own checks on text the integrator wrote, so they are not independent. A different mind should re-derive them before they count for much. Criteria were written after the derivations, hence `committed: after`.

## C1 (check)
- target: segment:scope-adaptive-system
- at: f51fc762
- act: rederive
- line: derivation
- criterion: Item (c): under independent Dirichlet rows, if some continuation visits a pair infinitely often with positive probability, is $\sup_{\pi'} I_{\pi'}(\theta; F_t \mid \mathcal C_t) = +\infty$ at every finite $t$? And does every pair qualify under full-support rows?
- committed: after
- outcome: confirmed
- recheck: 08 §1.1; the stack representation, then the KL divergence of the joint against the product on the graph of the limiting-frequency map; irreducibility under the policy that always takes $a$ at $s$

Under the stack representation, the visit draws are i.i.d. from the row, so on the event of infinitely many visits the row is a measurable function of the stream. That event's graph has positive joint probability. Under the product of the marginals each section is a single point, which the continuous prior makes null. So the KL divergence is infinite.

## C2 (check)
- target: segment:scope-adaptive-system
- at: f51fc762
- act: run
- line: simulation
- criterion: The numbers in (b) and (c): one-step Dirichlet information against $(K-1)/(2n)$; the Beta(6,6) $m$-step information growing like $\tfrac12 \log((n+m)/n)$; scalar random walk ($q = r = 1$) one-step part $0.135$ nats and whole-future value $0.162$ nats
- committed: after
- outcome: confirmed
- recheck: the appendix script of 08, `python3 -I`

The ratio to $(K-1)/(2n)$ is 0.9975, 0.9963 and 0.9940 at $n = 1000$ for $K = 2, 3, 5$. The $m$-step values are $0.040, 0.302, 1.115, 2.216, 3.016$. The Kalman values are $0.1346$ and $0.16175$.

## C3 (check)
- target: segment:scope-adaptive-system
- at: f51fc762
- act: rederive
- line: derivation
- criterion: Item (h′): with $\Omega$, $\mathcal O$, $\mathcal A$ finite and $\theta$ the kernel entries in the Euclidean topology, does membership (averaged, and pointwise at positive-probability histories) depend on $\pi_0$ only through its support?
- committed: after
- outcome: confirmed
- recheck: 08 §1.2, steps 1–6; likelihoods and block laws are polynomial in kernel entries; the support lemma for $L \cdot \mu$; a.e.-constancy of a continuous map equals constancy on the support (second-countable); $P(c) \gt 0$ iff $\{L \gt 0\}$ meets the support

## C4 (check)
- target: segment:scope-adaptive-system
- at: f51fc762
- act: rederive
- line: derivation
- criterion: (h′)'s hypotheses are needed. A frozen hidden $x \in [0, 1]$ under a known law, observed once as $o_2 = 1\{x \in \mathbb Q\}$, is out at $t = 1$ under Lebesgue and in under half Lebesgue plus half a dense atomic measure on the rationals, which has the same support. Separately: does 07 §2.2's own counterexample (law parameter $\theta \in [0, 1]$, $b_2 = 1\{\theta \in \mathbb Q\}$) separate support from null sets under the segment's definition of $\theta$?
- committed: after
- outcome: confirmed
- recheck: 08 §1.2, first two paragraphs

This item records a divergence from 07, so that the next checker re-derives both versions rather than inheriting either. 07's counterexample does **not** work under the segment's definition. $\theta$ is the kernel pair, and the kernel depends on 07's parameter only through $1\{\theta \in \mathbb Q\}$. So the two priors push forward to $\delta_{K_0}$ and $\tfrac12 \delta_{K_0} + \tfrac12 \delta_{K_1}$ on kernels, which have different supports. The general falsity of "only the support matters" survives through the replacement above, which puts the irregularity in a continuous hidden state and so violates (h′)'s finiteness hypothesis. The confirmed outcome refers to the replacement; the answer to the "separately" question is no.

## C5 (check)
- target: segment:scope-adaptive-system
- at: f51fc762
- act: rederive
- line: derivation
- criterion: Item (b): with $R \succ 0$ and $N = C Q C^\top + R$, is the one-step part $\tfrac12 \log\det(I + C A P_t A^\top C^\top N^{-1})$, positive iff $C A P_t \neq 0$, with a positive limit when $P_t \to P_\infty$ and $C A P_\infty \neq 0$, so that the value stays bounded away from zero?
- committed: after
- outcome: confirmed
- recheck: $o_{t+1} = C A x_t + (C w_t + v_{t+1})$ with independent Gaussian noise; Gaussian mutual information; $C A P A^\top C^\top = 0$ iff $C A P^{1/2} = 0$ iff $C A P = 0$ for $P \succeq 0$; the value bounds the one-step part by monotonicity

## C6 (check)
- target: segment:scope-adaptive-system
- at: f51fc762
- act: rederive
- line: derivation
- criterion: The surrounding statements now in the segment: (i) membership is invariant under the state/law cut; (ii) with discrete histories, averaged-in iff pointwise-in at some positive-probability history; (iii) the stream predicate is invariant under adding or removing target coordinates no continuation's future depends on, given the rest and the history; (iv) the predicate's one-step part is at most (ii′) by data processing; (v) the housing twin matches the original as a $\pi_0$ mixture, and is mutually singular with it under a fixed law left open under a continuous $\pi_0$ with unbounded visits
- committed: after
- outcome: confirmed
- recheck: 08 §1.4, §1.6, §1.7. For (i), sufficiency of the reduced world's $(\tilde\Omega_t, \theta')$. For (ii), $I = \sum_c P(c) I(\cdot \mid c)$ with $P(c)$ free of $\pi'$. For (iii), the chain rule. For (v), the frequency set $\{\text{frequencies} = \theta^\ast\}$ has mixture probability $\pi_0(\{\theta^\ast\}) = 0$

## C7 (check)
- target: segment:example-bandit
- at: f51fc762
- act: rederive
- line: derivation
- criterion: Stationary variant under a Gaussian prior on the means, with pull noise $\sigma^2$: is the agent in at every finite $t$, with one-step information about a mean decaying like $1/(2n)$ after $n$ pulls of its arm, never reaching zero, and the information in unboundedly many further pulls infinite?
- committed: after
- outcome: confirmed
- recheck: $s_n^2 = \sigma^2/(n + \sigma^2/s_0^2)$; one-step $\tfrac12 \log(1 + s_n^2/\sigma^2)$; $I(\mu; r_1, \ldots, r_m) = \tfrac12 \log(1 + m s^2/\sigma^2) \to \infty$
