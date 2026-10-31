# KR C.2 / C.1 -- independent check of the Part II integration (identification side), reviews/part-ii-check-1-identification.md, 2026-10-30. Run: python3 -I <this file>
"""#def-value-object right rung: is "pi* optimal over Pi from every state reachable in one step" sufficient for
A^RH <= A^B?  Deterministic finite instance, N_h = 3, N_r = 1 (one-step replanning over Pi at each state).
States: x --z(0)--> s ; s --c(5)--> s1, s --d(0)--> s2 ; s1 --e1(0)/e2(10)--> end ; s2 --f(6)--> end.
Pi = {piA: x->z, s->c, s1->e1, s2->f ;  piB: x->z, s->d, s1->e2, s2->f}."""
T = {('x','z'):('s',0), ('s','c'):('s1',5), ('s','d'):('s2',0), ('s1','e1'):('end',0), ('s1','e2'):('end',10), ('s2','f'):('end',6)}
Pi = {'piA': {'x':'z','s':'c','s1':'e1','s2':'f'}, 'piB': {'x':'z','s':'d','s1':'e2','s2':'f'}}
def V(state, pol, steps):
    tot = 0
    for _ in range(steps):
        if state == 'end': break
        state, r = T[(state, pol[state])]; tot += r
    return tot
Nh, Nr = 3, 1
piRH = {st: Pi[max(Pi, key=lambda n: V(st, Pi[n], Nr))][st] for st in ('x','s','s1','s2')}   # replan over Pi at each state
def Q(a, cont, state='x'):
    s2, r = T[(state, a)]; return r + V(s2, cont, Nh - 1)
pistar = max(Pi, key=lambda n: V('x', Pi[n], Nh))
print("pi_RH =", piRH, "; in Pi:", piRH in Pi.values())
print("pi* =", pistar, "; V_x:", {n: V('x', p, Nh) for n, p in Pi.items()}, "; V_s:", {n: V('s', p, Nh-1) for n, p in Pi.items()},
      "-> pi* optimal over Pi from x and from s (the only one-step-reachable state):", V('s', Pi[pistar], 2) == max(V('s', p, 2) for p in Pi.values()))
acts = [a for (st, a) in T if st == 'x']
print("A^RH =", max(Q(a, piRH) for a in acts), " A^B =", max(Q(a, Pi[pistar]) for a in acts))
