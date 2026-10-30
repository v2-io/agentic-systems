"""Integration check (C.2 / C2, 2026-10-30): the corrected no-go for deterministic policies.

Claim checked: in an environment class that is unrestricted apart from (M) -- so it
contains environments whose state records the interaction history -- two SCMs can agree
on every on-policy quantity and disagree on P(Y^{(a')} | X_t = x) for an action a' the
deterministic policy never takes at x.  Hence that quantity is not identified from the
on-policy law alone; identification needs a restriction on the class (e.g. outcome-
sufficiency of some coarsening of X_t with positivity inside its cell, or stationarity).

Construction.  Two steps.  Step 1: theta ~ Bern(1/2), o_1 = theta (so the agent learns
theta).  A fresh fair coin u sets a nuisance component of the decision state: X_1 =
(theta, u).  Deterministic policy a_1 = theta XOR u (so both actions are taken at both
theta, and each X_1 cell takes exactly one action).  Step 2 outcome: Y^{(a)} = g(Omega, a, N).
The environment state Omega records (theta, a_1, u_seen) where u_seen is u as read off
from the executed action (Omega records the history: a_1 and theta determine u = a_1 XOR
theta).  SCM A: g(Omega, a) = 1[a = theta].  SCM B: g(Omega, a) = 1[a = theta] XOR 1[a !=
a_1 and u = 1] -- i.e. B flips the outcome of the UNTAKEN action in the cells with u = 1.
The on-policy law (joint of o_1, a_1, o_2 under the policy) is identical; the interventional
P(Y^{(a')} | X_1) differs at the u = 1 cells.

Run: python3 -I check-integration-1-deterministic-nogo.py
"""
from itertools import product
from fractions import Fraction as F


def world():
    for theta in (0, 1):
        for u in (0, 1):
            yield theta, u, F(1, 4)


def g_A(theta, u, a1, a):
    return int(a == theta)


def g_B(theta, u, a1, a):
    # the environment recorded a1 and theta, hence u = a1 ^ theta; it flips the
    # untaken action's outcome where u = 1.
    u_rec = a1 ^ theta
    return int(a == theta) ^ int(a != a1 and u_rec == 1)


def onpolicy_law(g):
    law = {}
    for theta, u, p in world():
        a1 = theta ^ u
        o2 = g(theta, u, a1, a1)
        key = (theta, a1, o2)  # everything the agent ever sees on-policy (o_1, a_1, o_2)
        law[key] = law.get(key, F(0)) + p
    return law


def interventional(g, a):
    out = {}
    for theta, u, p in world():
        a1 = theta ^ u
        x = (theta, u)
        out[x] = g(theta, u, a1, a)
    return out


lawA, lawB = onpolicy_law(g_A), onpolicy_law(g_B)
print("on-policy laws identical:", lawA == lawB)
for k in sorted(lawA):
    print("  P(o1=%d, a1=%d, o2=%d) = %s" % (k + (lawA[k],)))

print("interventional P(Y^(a)=1 | X_1=(theta,u)), SCM A vs SCM B:")
differ = False
for a in (0, 1):
    iA, iB = interventional(g_A, a), interventional(g_B, a)
    for x in sorted(iA):
        taken = (x[0] ^ x[1]) == a
        flag = "" if iA[x] == iB[x] else "   <-- differs (untaken action)"
        if iA[x] != iB[x]:
            differ = True
            assert not taken, "a taken action's effect must not differ"
        print("  a=%d X=%s taken=%s: A=%d B=%d%s" % (a, x, taken, iA[x], iB[x], flag))
print("some untaken-action effect differs while on-policy laws agree:", differ)

# The class restriction that blocks the construction: outcome-sufficiency of Z = theta
# (drop u) with positivity inside the cell.  Under SCM A, Y^(a) is independent of u given
# theta, and both actions are taken within each theta-cell, so the contrast is identified
# by adjustment on Z.  Under SCM B the dropped component u is outcome-relevant for the
# untaken action, so (S) fails for Z = theta -- which is exactly the restriction B violates.
for name, g in (("A", g_A), ("B", g_B)):
    S_holds = all(
        interventional(g, a)[(th, 0)] == interventional(g, a)[(th, 1)]
        for a in (0, 1) for th in (0, 1)
    )
    print("SCM %s: outcome-sufficiency of Z=theta (Y^(a) indep. of u | theta): %s" % (name, S_holds))
