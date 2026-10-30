# KR C.2 / C.1 -- independent check of the Part II integration (identification side), reviews/part-ii-check-1-identification.md, 2026-10-30. Run: python3 -I <this file>
"""Scope of the deterministic no-go (#der-loop-interventional-access): deterministic in X_t, or in the chronica?
Under canon's coupling the environment receives the agent only through executed actions
(#def-agent-environment: perception, internal state, action channels).  One decision step:
theta ~ Bern(1/2) is the world bit, o_1 = theta.  Outcome of the step's action: Y^(a) = g(theta, a) with g an
arbitrary function {0,1}^2 -> {0,1} (an unrestricted deterministic environment; noise would not change the point).
Case P (private content): X_1 = (theta, u), u a fair coin the agent drew and stored (env-independent, never shown).
    pi(theta, u) = theta XOR u -- deterministic in X_1.
Case H (history-determined): X_1 = (theta,), pi(theta) = theta -- deterministic in the chronica.
For each case: enumerate all 16 environments g; group them by the on-policy law; report whether every
P(Y^(a') | X_1 = x) for untaken a' is constant within each group (identified) or not."""
from itertools import product
from fractions import Fraction as F
envs = [dict(zip(product((0, 1), (0, 1)), bits)) for bits in product((0, 1), repeat=4)]
def analyse(states, pi, label):
    groups = {}
    for g in envs:
        law = {}
        for x, p in states:
            th = x[0]; a = pi(x); key = (th, a, g[(th, a)])
            law[key] = law.get(key, F(0)) + p
        groups.setdefault(tuple(sorted(law.items())), []).append(g)
    identified = True
    for gs in groups.values():
        for x, p in states:
            a_un = 1 - pi(x)
            if len({g[(x[0], a_un)] for g in gs}) > 1: identified = False
    print(f"{label}: {len(groups)} on-policy-law classes over 16 environments; "
          f"untaken-action effect at every visited X_1 identified: {identified}")
analyse([((th, u), F(1, 4)) for th in (0, 1) for u in (0, 1)], lambda x: x[0] ^ x[1], "Case P (coin stored in X_1, deterministic in X_1)")
analyse([((th,), F(1, 2)) for th in (0, 1)], lambda x: x[0], "Case H (deterministic in the chronica)        ")
