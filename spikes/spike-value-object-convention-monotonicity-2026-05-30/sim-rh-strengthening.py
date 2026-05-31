"""
Front-1 strengthening verification on the SAME counterexample MDP.

We confirm:
  (RH-2) value-compared fallback (rollout guard) restores A_O^(1) <= A_O^RH.
  (RH-3) a terminal cost V_f that lower-bounds the baseline tail and satisfies the
         CLF decrease inequality restores the rung.
"""

A = {'x': ['g', 'p'], 'H': ['stay'], 'D': ['stay']}
T = {
    ('x', 'g'): (1.0, 'D'),
    ('x', 'p'): (0.0, 'H'),
    ('H', 'stay'): (10.0, 'H'),
    ('D', 'stay'): (0.0, 'D'),
}
def step(s, a): return T[(s, a)]

def rollout_value(s, policy, n):
    total = 0.0
    for k in range(n):
        a = policy(s, n - k); r, s2 = step(s, a); total += r; s = s2
    return total

def optimal_av(s, n):
    if n == 0: return 0.0, None
    best = (float('-inf'), None)
    for a in A[s]:
        r, s2 = step(s, a)
        v = r + optimal_av(s2, n - 1)[0]
        if v > best[0]: best = (v, a)
    return best

def pi_current(s, steps_left):
    return 'p' if s == 'x' else A[s][0]

# Baseline tail value: value of following pi_current for `n` steps from s.
def baseline_tail(s, n):
    return rollout_value(s, pi_current, n)

# (RH-2) value-compared fallback: among {replanned action via N_r lookahead, current action},
# commit whichever has the higher FULL-horizon value (current action's full value = immediate
# reward + baseline tail; replanned candidate's full value = immediate + baseline tail too,
# i.e. evaluate each candidate first action by its rollout-with-baseline value -> rollout improvement).
def pi_rh_guarded(N_r):
    def policy(s, steps_left):
        cand = set([optimal_av(s, min(N_r, steps_left))[1], pi_current(s, steps_left)])
        # score each candidate first action by: r + baseline_tail(next, steps_left-1)  (rollout w/ base policy)
        best = (float('-inf'), None)
        for a in cand:
            r, s2 = step(s, a)
            v = r + baseline_tail(s2, steps_left - 1)
            if v > best[0]: best = (v, a)
        return best[1]
    return policy

# (RH-3) terminal cost. Use V_f that lower-bounds the baseline tail and satisfies CLF decrease.
# Baseline tails: from H, tail = 10*remaining; from D, tail = 0; from x, pi_current goes to H.
# Choose V_f(H)=10, V_f(D)=0, V_f(x)=10 (the baseline tail values for 1 step) as an admissible
# lower bound. N_r-step replanning objective gets V_f added at the truncation boundary.
Vf = {'H': 10.0, 'D': 0.0, 'x': 10.0}
def optimal_av_terminal(s, n, Vf):
    if n == 0: return Vf.get(s, 0.0), None
    best = (float('-inf'), None)
    for a in A[s]:
        r, s2 = step(s, a)
        v = r + optimal_av_terminal(s2, n - 1, Vf)[0]
        if v > best[0]: best = (v, a)
    return best
def pi_rh_terminal(N_r, Vf):
    def policy(s, steps_left):
        return optimal_av_terminal(s, min(N_r, steps_left), Vf)[1]
    return policy

if __name__ == "__main__":
    N_h, N_r, s0 = 2, 1, 'x'
    A_O_1 = rollout_value(s0, pi_current, N_h)
    A_O_RH_naive = rollout_value(s0, pi_rh_terminal(N_r, {'H':0,'D':0,'x':0}), N_h)  # no terminal cost
    A_O_RH_guard = rollout_value(s0, pi_rh_guarded(N_r), N_h)
    A_O_RH_term  = rollout_value(s0, pi_rh_terminal(N_r, Vf), N_h)

    print(f"A_O^(1)                                  = {A_O_1}")
    print(f"A_O^RH naive (N_r=1, no terminal cost)   = {A_O_RH_naive}  (rung holds: {A_O_1 <= A_O_RH_naive})")
    print(f"A_O^RH (RH-2 value-compared fallback)    = {A_O_RH_guard}  (rung holds: {A_O_1 <= A_O_RH_guard})")
    print(f"A_O^RH (RH-3 terminal cost V_f)          = {A_O_RH_term}   (rung holds: {A_O_1 <= A_O_RH_term})")
