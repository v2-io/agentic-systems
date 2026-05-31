#!/usr/bin/env python3
"""Reproduce the convention dependence of the strategic-persistence hard ceiling.

Spike: spike-strategic-persistence-hard-ceiling-convention-2026-05-31.md (F72).

AAT's edge update is Beta-Bernoulli conjugate (deriv-edge-credence-dynamics Prop B.1):
    alpha += y, beta += (1-y); n = alpha+beta; phat = alpha/n; gain eta = 1/(n+1).
The gain 1/(n+1) IS the sector parameter alpha_Sigma. Under exponential forgetting the
steady-state gain depends on WHERE the discount lands relative to the +1 unit increment:

  SEG  (discount prior, add current full-weight):  n <- lam*n + 1   => n_eff = 1/(1-lam)
                                                    gain = (1-lam)/(2-lam),  sup_lam = 1/2
  ALT1 (add current, then discount pool):          n <- lam*(n+1)   => n_eff = lam/(1-lam)
                                                    gain = 1-lam,            sup_lam = 1
  EWMA (constant-gain estimate):                   phat <- lam*phat + (1-lam)*y
                                                    gain = 1-lam (constant), sup_lam = 1

The nontrivial hard ceiling rho_Sigma >= R_Sigma/2 exists ONLY under SEG.
"""

import numpy as np


def steady_count(recursion, lam, steps=200_000):
    n = 0.0
    for _ in range(steps):
        n = recursion(n, lam)
    return n


rec_seg = lambda n, lam: lam * n + 1.0          # discount-then-add
rec_alt1 = lambda n, lam: lam * (n + 1.0)        # add-then-discount


def main():
    print("Steady-state sector parameter alpha_Sigma = 1/(n_eff + 1) by convention:\n")
    for lam in (0.5, 0.9, 0.99):
        n_seg = steady_count(rec_seg, lam)
        n_alt = steady_count(rec_alt1, lam)
        g_seg = 1.0 / (n_seg + 1.0)
        g_alt = 1.0 / (n_alt + 1.0)
        print(f"lambda = {lam}")
        print(f"  SEG : n_eff = {n_seg:8.4f}  gain = {g_seg:.6f}  "
              f"(1-lam)/(2-lam) = {(1 - lam) / (2 - lam):.6f}")
        print(f"  ALT1: n_eff = {n_alt:8.4f}  gain = {g_alt:.6f}  "
              f"(1-lam)        = {1 - lam:.6f}")
        print()

    print("Suprema over lambda in [0,1):")
    print("  SEG  sup (1-lam)/(2-lam) -> 1/2  => hard ceiling rho/R < 1/2 EXISTS")
    print("  ALT1 sup (1-lam)         -> 1    => ceiling dissolves to trivial rho/R < 1\n")

    print("lambda = 1 (no forgetting) reduction test:")
    print("  SEG  alpha <- lam*alpha + y     => alpha += y   (AAT conjugate)  MATCH")
    print("  ALT1 alpha <- lam*(alpha + y)   => alpha += y   (AAT conjugate)  MATCH")
    print("  EWMA phat  <- lam*phat+(1-lam)y => phat <- phat  (NO UPDATE)     FAILS\n")

    print("Weight structure (why the conventions differ):")
    for lam in (0.5, 0.9):
        w_seg = [lam ** k for k in range(200)]      # current obs weight 1
        w_alt = [lam ** (k + 1) for k in range(200)]  # current obs weight lam
        print(f"  lambda = {lam}: SEG total mass = {sum(w_seg):7.4f} "
              f"(current-obs weight {w_seg[0]:.3f});  "
              f"ALT1 total mass = {sum(w_alt):7.4f} "
              f"(current-obs weight {w_alt[0]:.3f})")


if __name__ == "__main__":
    main()
