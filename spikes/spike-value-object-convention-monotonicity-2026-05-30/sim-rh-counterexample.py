"""
Front-1 counterexample: A_O^(1) > A_O^RH for receding-horizon (N_r < N_h) replanning.

Deterministic finite-horizon MDP. We compute, from a fixed decision point, the
full-N_h-horizon value V_O achieved under three continuation conventions:

  C1 (one-step / frozen): continuation = pi_current (a fixed policy)
  C2 (receding-horizon):  at each step, choose the action maximizing the N_r-step
                          lookahead value, then advance one step (true RH/MPC).
  C3 (Bellman):           continuation = the N_h-optimal policy.

A_O^X = best achievable full-horizon value over the FIRST action under convention X.
(The first action is shared; we just trace the continuation under each rule and
score on the SAME full-horizon objective V_O = sum of stage rewards over N_h steps.)
"""

# States. Transitions keyed by (state, action) -> (reward, next_state).
# 'x' is the post-first-action state we evaluate continuations from.
A = {  # action set per state
    'x': ['g', 'p'],
    'H': ['stay'],
    'D': ['stay'],
}
T = {
    ('x', 'g'): (1.0, 'D'),    # greedy: +1 now, into dead state
    ('x', 'p'): (0.0, 'H'),    # patient: 0 now, into high-reward state
    ('H', 'stay'): (10.0, 'H'),
    ('D', 'stay'): (0.0, 'D'),
}

def step(s, a):
    return T[(s, a)]

def rollout_value(s, policy, n):
    """Full-horizon value of following `policy(state, steps_left)` for n steps."""
    total = 0.0
    for k in range(n):
        a = policy(s, n - k)
        r, s2 = step(s, a)
        total += r
        s = s2
    return total

# ---- C1: frozen pi_current = always 'p' where available, else the lone action ----
def pi_current(s, steps_left):
    if s == 'x':
        return 'p'
    return A[s][0]

# ---- C3: Bellman-optimal over the full horizon n (finite-horizon DP) ----
def optimal_action_value(s, n):
    """Return (best_value, best_action) maximizing the n-step value from s."""
    if n == 0:
        return 0.0, None
    best_v, best_a = float('-inf'), None
    for a in A[s]:
        r, s2 = step(s, a)
        v = r + optimal_action_value(s2, n - 1)[0]
        if v > best_v:
            best_v, best_a = v, a
    return best_v, best_a

def pi_bellman(n_full):
    def policy(s, steps_left):
        return optimal_action_value(s, steps_left)[1]
    return policy

# ---- C2: receding-horizon with replanning window N_r (< N_h) ----
def pi_receding(N_r):
    def policy(s, steps_left):
        # Optimize over an N_r-step lookahead (capped by steps_left), commit the
        # first action only; this is re-evaluated each step -> true RH/MPC.
        window = min(N_r, steps_left)
        return optimal_action_value(s, window)[1]
    return policy

if __name__ == "__main__":
    N_h = 2          # full evaluated horizon (continuation steps after first action)
    N_r = 1          # myopic replanning window
    s0 = 'x'

    A_O_1  = rollout_value(s0, pi_current, N_h)            # C1
    A_O_RH = rollout_value(s0, pi_receding(N_r), N_h)      # C2
    A_O_B  = rollout_value(s0, pi_bellman(N_h), N_h)       # C3

    print(f"N_h = {N_h}, N_r = {N_r}")
    print(f"A_O^(1)  (C1, frozen pi_current) = {A_O_1}")
    print(f"A_O^RH   (C2, receding-horizon)  = {A_O_RH}")
    print(f"A_O^B    (C3, Bellman-optimal)   = {A_O_B}")
    print()
    print(f"Left rung  A_O^(1) <= A_O^RH ?  {A_O_1} <= {A_O_RH} : {A_O_1 <= A_O_RH}")
    print(f"Right rung A_O^RH  <= A_O^B  ?  {A_O_RH} <= {A_O_B} : {A_O_RH <= A_O_B}")
    print()
    if A_O_1 > A_O_RH:
        print("=> LEFT RUNG VIOLATED: frozen current policy strictly beats the myopic replanner.")
    # Sanity: with N_r = N_h, RH coincides with full-horizon optimization and the rung holds.
    A_O_RH_full = rollout_value(s0, pi_receding(N_h), N_h)
    print(f"\nControl: N_r = N_h = {N_h} -> A_O^RH = {A_O_RH_full} "
          f"(>= A_O^(1)={A_O_1}: {A_O_RH_full >= A_O_1}); rung restored when N_r >= N_h.")
