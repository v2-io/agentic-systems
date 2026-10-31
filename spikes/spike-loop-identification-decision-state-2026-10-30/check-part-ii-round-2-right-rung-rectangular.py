# KR C.2 / B.1 / C.1 -- Part II round 2, right-rung cluster (reviews/part-ii-round-2-right-rung.md), 2026-10-30. Run: python3 -I <this file>
"""Brute-force check of the rectangularity claim for the right rung A^RH <= A^B of #deriv-convention-monotonicity.

A *rectangular* class is the set of all time-indexed Markov policies pi(s, k) with pi(s, k) in A_Pi(s) for given
state-wise admissible sets A_Pi(s); the first-action supremum ranges over A_Pi(x). The claim checked: for every
rectangular class on a small deterministic instance, (M) the stitched receding-horizon policy is a member,
(PC) a (+) pi is a member for every a in A_Pi(x), and the rung A^RH <= A^B holds on both readings of A^B for
*every* maximizer pi* of V from x (not only the backward-induction one). Also checked: which maximizers satisfy
(SO), to show (SO) is not automatic for an arbitrary maximizer even in a rectangular class.

The instance is the one whose two-member non-rectangular subclass fails the rung in #deriv-convention-monotonicity
(15 > 6), extended with a second first action so that prefix-closure is non-trivial, and with every state-wise
admissible set enumerated. The two-member subclass is re-run at the end as the control.
"""
import itertools

# x --z(0)--> s ; x --z'(0)--> s ; s --c(5)--> s1, s --d(0)--> s2 ; s1 --e1(0)/e2(10)--> end ; s2 --f(6)--> end
T = {('x', 'z'): ('s', 0), ('x', "z'"): ('s', 0), ('s', 'c'): ('s1', 5), ('s', 'd'): ('s2', 0),
     ('s1', 'e1'): ('end', 0), ('s1', 'e2'): ('end', 10), ('s2', 'f'): ('end', 6)}
STATES = ['x', 's', 's1', 's2']
ACTS = {st: sorted(a for (q, a) in T if q == st) for st in STATES}
Nh, Nr = 3, 1
STEPS = range(Nh)          # time index k = number of steps already taken (0 .. Nh-1)


def step(state, a):
    return T[(state, a)]


def V(state, pol, k0, steps):
    """Value of following time-indexed policy pol (dict (state, k) -> action) from state at time k0 for `steps` steps."""
    tot, st, k = 0, state, k0
    for _ in range(steps):
        if st == 'end':
            break
        st, r = step(st, pol[(st, k)])
        tot += r
        k += 1
    return tot


def rectangular_class(adm):
    """All time-indexed Markov policies with pol[(s, k)] in adm[s]."""
    keys = [(st, k) for st in STATES for k in STEPS]
    for choice in itertools.product(*[adm[st] for (st, k) in keys]):
        yield dict(zip(keys, choice))


def replanner(Pi, adm_x):
    """C2: at each (state, k), the first action of the argmax over Pi of the N_r-step window value (ties: first in list)."""
    pol = {}
    for st in STATES:
        for k in STEPS:
            window = min(Nr, Nh - k)
            best = max(Pi, key=lambda p: V(st, p, k, window))
            pol[(st, k)] = best[(st, k)]
    return pol


def Q(a, cont):
    s1, r = step('x', a)
    return r + V(s1, cont, 1, Nh - 1)


def check_class(Pi, adm, label):
    Pi = list(Pi)
    first_acts = adm['x']
    piRH = replanner(Pi, first_acts)
    M = piRH in Pi
    PC = all(({**p, ('x', 0): a} in Pi) for a in first_acts for p in Pi)
    vals = {i: V('x', p, 0, Nh) for i, p in enumerate(Pi)}
    vstar = max(vals.values())
    maximizers = [Pi[i] for i, v in vals.items() if v == vstar]
    A_RH = max(Q(a, piRH) for a in first_acts)
    results = []
    for pstar in maximizers:
        A_B_Q = max(Q(a, pstar) for a in first_acts)
        A_B_V = vstar
        # (SO): pi* attains the class supremum from every state a first action reaches, with Nh-1 steps left
        reach = {step('x', a)[0] for a in first_acts}
        SO = all(V(s1, pstar, 1, Nh - 1) == max(V(s1, p, 1, Nh - 1) for p in Pi) for s1 in reach)
        G = Q(pstar[('x', 0)], pstar) == A_B_Q
        results.append((A_B_Q, A_B_V, SO, G))
    rung_Q = all(A_RH <= r[0] for r in results)
    rung_V = all(A_RH <= r[1] for r in results)
    n_SO = sum(r[2] for r in results)
    n_G = sum(r[3] for r in results)
    print(f"{label}: |Pi|={len(Pi)} M={M} PC={PC} A^RH={A_RH} sup_Pi V={vstar} "
          f"maximizers={len(maximizers)} (SO holds for {n_SO}, G for {n_G}) rung_Q={rung_Q} rung_V={rung_V}")
    return M, PC, rung_Q, rung_V


print("=== every rectangular class on the instance (state-wise admissible sets, nonempty) ===")
all_ok = True
n = 0
for adm_x in (['z'], ["z'"], ['z', "z'"]):
    for adm_s in (['c'], ['d'], ['c', 'd']):
        for adm_s1 in (['e1'], ['e2'], ['e1', 'e2']):
            adm = {'x': adm_x, 's': adm_s, 's1': adm_s1, 's2': ['f']}
            n += 1
            M, PC, rq, rv = check_class(rectangular_class(adm), adm, f"adm={adm_x},{adm_s},{adm_s1}")
            all_ok &= (M and PC and rq and rv)
print(f"rectangular classes checked: {n}; (M), (PC), rung on both readings for every maximizer in all: {all_ok}")

print("\n=== control: the two-member non-rectangular subclass of #deriv-convention-monotonicity (expect M false, rung false) ===")
tailA = {('s', k): 'c' for k in STEPS} | {('s1', k): 'e1' for k in STEPS} | {('s2', k): 'f' for k in STEPS}
tailB = {('s', k): 'd' for k in STEPS} | {('s1', k): 'e2' for k in STEPS} | {('s2', k): 'f' for k in STEPS}
piA = {('x', k): 'z' for k in STEPS} | tailA
piB = {('x', k): 'z' for k in STEPS} | tailB
check_class([piA, piB], {'x': ['z'], 's': ['c', 'd'], 's1': ['e1', 'e2'], 's2': ['f']}, "two-member {A,B}")

print("\n=== non-vacuous prefix-closure: four policies {z, z'} x {tail A, tail B} (expect PC true, SO true, M false, rung false) ===")
four = [{**piA, ('x', 0): a} for a in ('z', "z'")] + [{**piB, ('x', 0): a} for a in ('z', "z'")]
check_class(four, {'x': ['z', "z'"], 's': ['c', 'd'], 's1': ['e1', 'e2'], 's2': ['f']}, "four-member product")

# --- instance 2: the first actions reach different states, so a maximizer of V from x is unconstrained at the state
# its own first action does not reach. Shows (SO) is NOT automatic for an arbitrary maximizer in a rectangular class,
# while (M) and (PC) are, so the rung still holds through the (PC) branch for every maximizer.
print("\n=== instance 2: x --a1(0)--> s1 (b: 10) ; x --a2(0)--> s2 (c1: 5, c2: 0); full rectangular class, N_h = 2 ===")
T = {('x', 'a1'): ('s1', 0), ('x', 'a2'): ('s2', 0), ('s1', 'b'): ('end', 10), ('s2', 'c1'): ('end', 5), ('s2', 'c2'): ('end', 0)}
STATES = ['x', 's1', 's2']
Nh, Nr = 2, 1
STEPS = range(Nh)
adm = {'x': ['a1', 'a2'], 's1': ['b'], 's2': ['c1', 'c2']}
check_class(rectangular_class(adm), adm, "instance 2, full rectangular class (expect SO to fail for some maximizers, rung true)")

# --- instance 3: the B.1 checker's C1 instance (51 against 12): (M) and (SO) hold, (PC) fails, the two readings differ.
print("\n=== instance 3 (b1-records C1): x --p(2)--> H (u: 10) ; x --g(1)--> D (d1: 0, d2: 50); Pi = {A=(p,u,d2), B=(g,u,d1)}, N_h = 2 ===")
T = {('x', 'p'): ('H', 2), ('x', 'g'): ('D', 1), ('H', 'u'): ('end', 10), ('D', 'd1'): ('end', 0), ('D', 'd2'): ('end', 50)}
STATES = ['x', 'H', 'D']
piA = {('x', k): 'p' for k in STEPS} | {('H', k): 'u' for k in STEPS} | {('D', k): 'd2' for k in STEPS}
piB = {('x', k): 'g' for k in STEPS} | {('H', k): 'u' for k in STEPS} | {('D', k): 'd1' for k in STEPS}
check_class([piA, piB], {'x': ['p', 'g'], 'H': ['u'], 'D': ['d1', 'd2']}, "two-member {A,B} (expect M true, PC false, SO true, rung_Q true, rung_V false)")
