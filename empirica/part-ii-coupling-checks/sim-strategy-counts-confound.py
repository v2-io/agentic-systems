#!/usr/bin/env python3
"""KR C.2 (loop identification given the decision state).

Adversarial instance for the M_t-rung: a directed-separated (kappa_processing = 0) agent whose
purposeful substate G_t holds outcome statistics (Beta-Bernoulli edge counts, as in
#hyp-edge-update-via-gain) that are informative about a latent environment regime and drive
action choice. The learner that conditions on M_t alone (as #def-value-object's Q_O does) sees
a confounded action-outcome conditional; the learner that conditions on the full decision
state X_t = (M_t, G_t) recovers the interventional effect. With epsilon = 0 (deterministic
policy) positivity fails at X_t and the untaken action is unidentified in every visited cell.

Environment: per episode a hidden regime theta in {0,1}, P(theta=1)=1/2, fixed within the
episode and independent of everything the agent records. Action 1 succeeds with probability
q1(theta) = 0.8 if theta=1 else 0.2. Action 0 succeeds with probability 0.5 regardless.
So P(o=1 | do(a=1)) = 0.5 at every step, and P(o=1 | do(a=0)) = 0.5.

Agent: M_t = t (goal-blind, carries nothing about theta; a degenerate but legitimate model).
G_t = Beta counts (alpha_a, beta_a) for each action, updated from outcomes of that action.
Policy: epsilon-greedy on the Beta means. f_M ignores G_t, so kappa_processing = 0.

Run: python3 sim-strategy-counts-confound.py
"""
import random
from collections import defaultdict

def run(epsilon, episodes=40000, T=8, seed=1):
    rng = random.Random(seed)
    # cell -> [n_taken_a1, succ_taken_a1, sum_q1_all, n_all]
    by_M = defaultdict(lambda: [0, 0, 0.0, 0])
    by_X = defaultdict(lambda: [0, 0, 0.0, 0])
    cells_X_both = 0
    cells_X_total = 0
    seen_actions_in_cell = defaultdict(set)
    for _ in range(episodes):
        theta = 1 if rng.random() < 0.5 else 0
        q1 = 0.8 if theta == 1 else 0.2
        counts = {0: [1, 1], 1: [1, 1]}  # Beta(1,1) priors: [alpha, beta]
        for t in range(T):
            M = t
            X = (t, counts[0][0], counts[0][1], counts[1][0], counts[1][1])
            mean = {a: counts[a][0] / (counts[a][0] + counts[a][1]) for a in (0, 1)}
            greedy = 1 if mean[1] > mean[0] else (0 if mean[0] > mean[1] else rng.choice((0, 1)))
            a = greedy if rng.random() >= epsilon else rng.choice((0, 1))
            seen_actions_in_cell[X].add(a)
            p = q1 if a == 1 else 0.5
            o = 1 if rng.random() < p else 0
            for store, key in ((by_M, M), (by_X, X)):
                rec = store[key]
                rec[2] += q1   # interventional P(o=1 | do(a=1), cell) accumulates over ALL visits
                rec[3] += 1
                if a == 1:
                    rec[0] += 1
                    rec[1] += o
            counts[a][0 if o == 1 else 1] += 1
    def summarize(store, label):
        # on-policy-weighted comparison: for cells where a=1 was taken, compare
        # hat P(o=1 | a=1, cell) against P(o=1 | do(a=1), cell) = mean q1 over all visits.
        num_cond = num_int = den = 0.0
        for rec in store.values():
            n1, s1, sq, n = rec
            if n1 == 0:
                continue
            num_cond += s1            # weight by number of a=1 samples
            num_int += n1 * (sq / n)
            den += n1
        print(f"  {label:>12}: on-policy E[o|a=1,cell] = {num_cond/den:.4f}   "
              f"interventional E[o|do(a=1),cell] = {num_int/den:.4f}   gap = {num_cond/den - num_int/den:+.4f}")
    print(f"epsilon = {epsilon}")
    summarize(by_M, "Z = M_t")
    summarize(by_X, "Z = X_t")
    both = sum(1 for s in seen_actions_in_cell.values() if len(s) == 2)
    print(f"  X_t cells visited: {len(seen_actions_in_cell)}; with both actions taken: {both}")

if __name__ == "__main__":
    for eps in (0.2, 0.05, 0.0):
        run(eps)
