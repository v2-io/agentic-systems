import numpy as np
rng = np.random.default_rng(7)
n_ok = n_viol = 0
# P4: attacker persists in mean square => alpha_A < alpha_plus <= 2 R_A^2/(n s_A^2)
for _ in range(20000):
    n = rng.integers(1, 6); RA = rng.uniform(0.1, 5); sA = rng.uniform(0.01, 3); envA = rng.uniform(0, 3)
    a = np.logspace(-4, 4, 400)
    V = n * (envA**2 + a**2 * sA**2) / (2 * a)
    ok = a[V < RA**2]
    if ok.size:
        n_ok += 1
        if ok.max() > 2 * RA**2 / (n * sA**2) * (1 + 1e-9):
            n_viol += 1
print("P4 cap: persistent draws", n_ok, "violations", n_viol)
# combined: if 2 gA RA^2/(n sA^2) <= RB^2/(n sB) - sbase, defender persists at its Kalman gain vs every persistent attacker gain
bad = tested = 0
for _ in range(20000):
    n = rng.integers(1, 4); RA, RB = rng.uniform(0.2, 4, 2); sA, sB = rng.uniform(0.05, 3, 2)
    gA, gB = rng.uniform(0.01, 2, 2); sbase = rng.uniform(0, 1)
    if 2 * gA * RA**2 / (n * sA**2) > RB**2 / (n * sB) - sbase:
        continue
    tested += 1
    aB = None
    a = np.logspace(-4, 4, 300)
    for aA in a:
        envA = sbase + gB * 1.0  # attacker's env: any value; cap is independent of it
        VA = n * (envA**2 + aA**2 * sA**2) / (2 * aA)
        if VA >= RA**2:
            continue
        envB = sbase + gA * aA
        VBstar = n * envB * sB  # defender at its Kalman gain
        if VBstar >= RB**2:
            bad += 1
            break
print("combined condition: tested", tested, "failures", bad)
# event rate, continuous: V_A = n env^2/(2T) + n h s^2/2 ; V_B coupling-dominant ~ n (gA T)^2/(2 TB)
T = np.logspace(0, 8, 200); h, s, env, gA, TB = 0.01, 1.0, 1.0, 1.0, 1.0
VA = env**2 / (2 * T) + h * s**2 / 2; VB = (gA * T)**2 / (2 * TB)
y = 0.5 * np.log(VB / VA); x = np.log(T)
print("event-rate local exponent low/high:", (y[5]-y[0])/(x[5]-x[0]), (y[-1]-y[-6])/(x[-1]-x[-6]))
# discrete Kalman per-event: tempo at optimal gain vs event rate
for nu in [1, 4, 16, 64, 256]:
    q = 1.0 / nu; s2 = 1.0
    P = 1.0
    for _ in range(100000):
        K = P / (P + s2); P = P * (1 - K) + q
    print(f"nu={nu:4d}  tempo nu*K={nu*P/(P+s2):.3f}  sqrt(nu)*env/s={np.sqrt(nu):.3f}")
