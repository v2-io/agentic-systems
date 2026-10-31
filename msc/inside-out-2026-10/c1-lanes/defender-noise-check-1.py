"""KR C.1, defender-noise lane (merge 60d2e8f6), independent check 1.

Written by the verifier without importing the lane's script. Run as
    python3 -I defender-noise-check-1.py
from any directory; about one second. Output is quoted in defender-noise-check-1.md.

1. The Variant-E closed form, to four places, both recorded columns and the split.
2. Defender-only noise raises the ratio at every tempo ratio, for s on a grid in (0, 3].
3. Which side of the ratio moves when Variant E lowers the base gain (s = 1).
4. Continuous-time asymptotics: gain-raised attacker tempo (exponent 1/2) and
   event-rate attacker tempo (exponent 1).
5. The attacker's own mean-square window caps its gain at 2 R_A^2 / (n sigma_nu,A^2),
   checked on random draws; and neither damage V_B nor the ratio V_B/V_A has an
   interior maximum in the attacker's gain.
"""
import numpy as np
from scipy.optimize import brentq

q, g, eta = 0.05, 0.5, 0.1
r = np.logspace(np.log10(0.5), np.log10(4), 12)
x = np.log(r)


def V(a, rho, s):
    return (rho ** 2 + a ** 2 * s ** 2) / (a * (2 - a))


def riccati_gain(s):
    if s == 0:
        return eta
    f = lambda P: P * P * (P + 2 * s * s) / (P + s * s) ** 2 - q * q
    P = brentq(f, 1e-15, max(q * q / (2 * eta - eta ** 2), q * q + s * s) * 10)
    return P / (P + s * s)


def pair(base, sA, sB):
    aB, aA = base, np.minimum(r * base, 0.9)
    VA, VB = V(aA, q + g * aB, sA), V(aB, q + g * aA, sB)
    return VA, VB


def slope(y):
    return np.polyfit(x, np.log(y), 1)[0]


print("## 1. Variant-E closed form")
for s in [0, 0.1, 0.2, 0.5, 1.0]:
    out = []
    for base, sA, sB in [(eta, s, s), (riccati_gain(s), s, s), (eta, 0, s), (eta, s, 0)]:
        VA, VB = pair(base, sA, sB)
        out.append(slope(np.sqrt(VB / VA)))
    print(f"s={s:4.2f}  both fixed {out[0]:.4f}  both Riccati {out[1]:.4f} (gain {riccati_gain(s):.4f})"
          f"  defender only {out[2]:.4f}  attacker only {out[3]:.4f}")

print("\n## 2. Defender-only noise raises the ratio at every tempo ratio")
VA0, VB0 = pair(eta, 0, 0)
ok = all(np.all(np.sqrt(pair(eta, 0, s)[1] / pair(eta, 0, s)[0]) > np.sqrt(VB0 / VA0))
         for s in np.linspace(0.01, 3, 300))
print("ratio(s) > ratio(0) at all 12 tempo ratios, 300 values of s in (0, 3]:", ok)

print("\n## 3. Slopes of each side, s = 0 and 1, base gain 0.1 and Riccati 0.035")
for base in [0.1, riccati_gain(1.0)]:
    for s in [0, 1.0]:
        VA, VB = pair(base, s, s)
        b_B, b_A = slope(np.sqrt(VB)), slope(np.sqrt(VA))
        print(f"base {base:.3f} s {s}: defender {b_B:+.3f}  attacker {b_A:+.3f}  exponent {b_B - b_A:.3f}")

print("\n## 4. Continuous-time asymptotics (n = 1, gamma = 0.5, alpha_B = 1, s = 1)")
gA = gB = 0.5
aB, sn, h = 1.0, 1.0, 0.1
prev = None
for T in [1e2, 1e3, 1e4, 1e5]:
    VA = ((gB * aB) ** 2 + T ** 2 * sn ** 2) / (2 * T)
    VB = (gA * T) ** 2 / (2 * aB)
    R = np.sqrt(VB / VA)
    print(f"gain-raised   T_A={T:8.0f}  ratio {R:12.3f}" + (f"  local exponent {np.log10(R / prev):.3f}" if prev else ""))
    prev = R
prev = None
for T in [1e2, 1e3, 1e4, 1e5]:
    # event rate nu = T/h at per-event gain h; channel intensity s^2/nu, so injected T*h*s^2
    VA = ((gB * aB) ** 2 + T * h * sn ** 2) / (2 * T)
    VB = (gA * T) ** 2 / (2 * aB)
    R = np.sqrt(VB / VA)
    print(f"event-rate    T_A={T:8.0f}  ratio {R:12.3f}" + (f"  local exponent {np.log10(R / prev):.3f}" if prev else ""))
    prev = R

print("\n## 5. Attacker persistence caps its gain; no interior optimum for damage or ratio")
rng = np.random.default_rng(1)
n_ok = 0
for _ in range(20000):
    n = int(rng.integers(1, 6))
    RA, sA, senvA = rng.uniform(.1, 5), rng.uniform(.01, 3), rng.uniform(0, 3)
    a = np.logspace(-4, 4, 4001)
    Va = n * (senvA ** 2 + a ** 2 * sA ** 2) / (2 * a)
    pers = a[Va < RA ** 2]
    if len(pers) == 0:
        continue
    ap = (RA ** 2 + np.sqrt(max(RA ** 4 - n ** 2 * senvA ** 2 * sA ** 2, 0))) / (n * sA ** 2)
    assert pers.max() <= ap * (1 + 1e-3) + 1e-12
    assert ap <= 2 * RA ** 2 / (n * sA ** 2) + 1e-12
    n_ok += 1
print("draws with a nonempty attacker window; largest persisting gain <= alpha_+ <= 2R^2/(n s^2) in all:", n_ok)
a = np.logspace(-2, 3, 200)
sb, aB, sA, sB = 0.05, 0.1, 1.0, 0.3
VB = ((sb + gA * a) ** 2 + aB ** 2 * sB ** 2) / (2 * aB)
VA = ((sb + gB * aB) ** 2 + a ** 2 * sA ** 2) / (2 * a)
print("V_B increasing in alpha_A:", bool(np.all(np.diff(VB) > 0)),
      " V_B/V_A increasing in alpha_A:", bool(np.all(np.diff(VB / VA) > 0)))
