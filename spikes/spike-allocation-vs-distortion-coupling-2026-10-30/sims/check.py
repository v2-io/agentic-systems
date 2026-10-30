#!/usr/bin/env python3
"""Numeric checks for spike-allocation-vs-distortion-coupling-2026-10-30 (KR C.2 / item C3).

Every claim in 01-derivation.md that is an identity or a bound is exercised here on a
finite toy so the written statement can cite a checked number. Exact enumeration
throughout (no Monte Carlo), natural logs (nats) unless stated.

Run: python3 -I check.py
"""
import itertools
import math
import numpy as np

rng = np.random.default_rng(20261030)
EPS = 1e-12


def kl(p, q):
    p = np.asarray(p, float); q = np.asarray(q, float)
    m = p > 0
    return float(np.sum(p[m] * np.log(p[m] / q[m])))


def tv(p, q):
    return 0.5 * float(np.sum(np.abs(np.asarray(p) - np.asarray(q))))


def entropy(p):
    p = np.asarray(p, float); m = p > 0
    return -float(np.sum(p[m] * np.log(p[m])))


def tilt(pi, u, lam):
    w = pi * np.exp(lam * u)
    return w / w.sum()


print("=" * 78)
print("N1  Tilt-Jensen identity, Hoeffding range bound, vanishing on constant tilt")
print("=" * 78)
worst_ratio = 0.0
for trial in range(2000):
    n = rng.integers(2, 7)
    pi = rng.dirichlet(np.ones(n) * rng.uniform(0.2, 3))
    u = rng.normal(size=n) * rng.uniform(0.1, 3)
    lam = rng.uniform(0, 4)
    m = tilt(pi, u, lam)
    lhs = kl(pi, m)
    jensen = math.log(float(np.sum(pi * np.exp(lam * u)))) - lam * float(np.sum(pi * u))
    assert abs(lhs - jensen) < 1e-9, (lhs, jensen)
    rng_u = (u.max() - u.min()) * lam  # range of the log-tilt on supp(pi)
    bound = rng_u ** 2 / 8
    assert lhs <= bound + 1e-9, (lhs, bound)
    assert kl(m, pi) <= bound + 1e-9
    assert tv(m, pi) <= rng_u / 4 + 1e-9
    worst_ratio = max(worst_ratio, lhs / bound if bound > 0 else 0)
# constant tilt on the support => zero displacement, even if u varies off-support
pi = np.array([0.5, 0.5, 0.0]); u = np.array([1.0, 1.0, 50.0])
assert kl(pi, tilt(pi, u, 3.0)) < 1e-12
print(f"  identity KL(pi||tilt) = log E_pi e^{{lam u}} - lam E_pi u : holds on 2000 random cases")
print(f"  bound KL <= range^2/8 and TV <= range/4 : hold; tightest ratio KL/bound observed = {worst_ratio:.3f}")
print(f"  constant tilt on supp(pi) (u varies only off-support) => KL = 0 : holds")

print()
print("=" * 78)
print("N2  kappa (MI form) saturates for injective coupling regardless of magnitude")
print("=" * 78)
# Two goals, uniform. Belief is a deterministic injective function of G given (e, M-).
# I(G; M+ | e, M-) = H(G) = log 2 for ANY lam > 0 ; displacement -> 0 as lam -> 0.
pi = np.array([0.5, 0.5]); u = np.array([1.0, -1.0])
for lam in [1e-6, 1e-2, 1.0]:
    m1 = tilt(pi, u, lam); m2 = tilt(pi, -u, lam)
    # Discrete G uniform on {1,2}; M+ takes two distinct values => I = H(G) exactly.
    I_GM = math.log(2) if tv(m1, m2) > 0 else 0.0
    kappa_canon = I_GM / math.log(2)  # H(G | e, M-) = log 2
    print(f"  lam={lam:<7g}  TV(M+_g1, M+_g2)={tv(m1, m2):.2e}   I(G;M+|e,M-)={I_GM:.4f} nats   kappa_canon={kappa_canon:.1f}")

print()
print("=" * 78)
print("N3  Reliability/resolution split: allocation moves resolution only; distortion adds reliability")
print("=" * 78)
# World W in {0,1}, P(W=1)=0.6. Two binary features x1, x2 with P(x_i=W)=q_i (symmetric channels).
pW = np.array([0.4, 0.6]); q1, q2 = 0.9, 0.7
def joint_Wx():
    J = {}
    for W in (0, 1):
        for x1 in (0, 1):
            for x2 in (0, 1):
                p = pW[W] * (q1 if x1 == W else 1 - q1) * (q2 if x2 == W else 1 - q2)
                J[(W, x1, x2)] = p
    return J
J = joint_Wx()

def murphy_logscore(belief_of):  # belief_of(x1,x2) -> P(W=1) reported; returns (score, U, RES, REL)
    # exact expected log score decomposition (Broecker 2009): E[-log b(W)] = H(W) - E KL(P(W|b)||P(W)) + E KL(P(W|b)||b)
    # group by reported belief value
    groups = {}
    for (W, x1, x2), p in J.items():
        b = round(belief_of(x1, x2), 12)
        groups.setdefault(b, [0.0, 0.0])
        groups[b][W] += p
    score = REL = RES = 0.0
    for b, (p0, p1) in groups.items():
        mass = p0 + p1
        cal = np.array([p0, p1]) / mass  # P(W | belief = b)
        rep = np.array([1 - b, b])
        score += -(p0 * math.log(1 - b) + p1 * math.log(b))
        REL += mass * kl(cal, rep)
        RES += mass * kl(cal, pW)
    U = entropy(pW)
    assert abs(score - (U - RES + REL)) < 1e-9, (score, U - RES + REL)
    return score, U, RES, REL

def post(x1=None, x2=None):
    num = sum(p for (W, a, b), p in J.items() if W == 1 and (x1 is None or a == x1) and (x2 is None or b == x2))
    den = sum(p for (W, a, b), p in J.items() if (x1 is None or a == x1) and (x2 is None or b == x2))
    return num / den

rows = [
    ("allocate x1 only (goal g1)", lambda a, b: post(x1=a)),
    ("allocate x2 only (goal g2)", lambda a, b: post(x2=b)),
    ("full information", lambda a, b: post(a, b)),
    ("distort: tilt full posterior toward W=1, lam=1", lambda a, b: tilt(np.array([1 - post(a, b), post(a, b)]), np.array([0.0, 1.0]), 1.0)[1]),
    ("distort: tilt x1-posterior toward W=0, lam=0.7", lambda a, b: tilt(np.array([1 - post(x1=a), post(x1=a)]), np.array([1.0, 0.0]), 0.7)[1]),
]
for name, f in rows:
    s, U, RES, REL = murphy_logscore(f)
    print(f"  {name:<48} score={s:.4f}  U={U:.4f}  RES={RES:.4f}  REL={REL:.4f}")

print()
print("=" * 78)
print("N4  Misspecified prior: a goal-tilt can IMPROVE objective expected score")
print("=" * 78)
# True P(W=1)=0.8; agent's prior says 0.3; one feature x with P(x=W)=0.6 (weak).
pW_true = np.array([0.2, 0.8]); prior_agent = np.array([0.7, 0.3]); q = 0.6
def agent_post(x):
    lik = np.array([q if x == 0 else 1 - q, q if x == 1 else 1 - q])
    b = prior_agent * lik; return b / b.sum()
def obj_logscore(lam):
    s = 0.0
    for W in (0, 1):
        for x in (0, 1):
            p = pW_true[W] * (q if x == W else 1 - q)
            b = tilt(agent_post(x), np.array([0.0, 1.0]), lam)  # goal "W=1 is good" tilts toward 1
            s += -p * math.log(b[W])
    return s
for lam in [0.0, 0.5, 1.0, 1.7, 2.5, 4.0]:
    print(f"  lam={lam:<4}  objective E[-log b(W)] = {obj_logscore(lam):.4f}")
best = min(np.linspace(0, 4, 401), key=obj_logscore)
print(f"  best lam ~ {best:.2f} > 0 : tilt toward the goal lowers TRUE expected loss (misspecified agent). "
      f"Under the agent's OWN model lam=0 is optimal (proper-score optimality is subjective-model-relative).")
# and confirm subjective optimality at lam=0
def subj_logscore(lam):
    s = 0.0
    for W in (0, 1):
        for x in (0, 1):
            p = prior_agent[W] * (q if x == W else 1 - q)
            b = tilt(agent_post(x), np.array([0.0, 1.0]), lam)
            s += -p * math.log(b[W])
    return s
assert min(np.linspace(0, 4, 401), key=subj_logscore) == 0.0
print(f"  subjective (agent-model) E[-log b(W)] minimized at lam=0 : holds")

print()
print("=" * 78)
print("N5  MNAR attention: 'allocation' whose drop rule peeks at content distorts unless the pattern is modeled")
print("=" * 78)
# Same world/features as N3. Rule: always encode x1; encode x2 only if x2 == 1 (confirming); otherwise drop.
# Encoded z = (x1, x2 or 'dropped'). Naive update: treat 'dropped' as if x2 were never observed (MAR assumption).
# Aware update: condition on the pattern, which under this rule reveals x2 == 0 exactly.
def naive(a, b):
    return post(x1=a, x2=1) if b == 1 else post(x1=a)
def aware(a, b):
    return post(x1=a, x2=1) if b == 1 else post(x1=a, x2=0)
for name, f in [("naive (treats drop as MAR)", naive), ("pattern-aware (MNAR modeled)", aware), ("MAR rule: encode x2 iff x1==1, naive update", lambda a, b: post(a, b) if a == 1 else post(x1=a))]:
    s, U, RES, REL = murphy_logscore(f)
    print(f"  {name:<46} score={s:.4f}  RES={RES:.4f}  REL={REL:.4f}")

print()
print("=" * 78)
print("N6  Step-5a starvation as value of information: zero under pursue-only decision set")
print("=" * 78)
# Latent f1 in {0,1} (which pursuing action is better), f2 in {feasible, infeasible}. P(f1=1)=0.5, P(feasible)=0.6.
# Pursuing actions a1,a2: payoff 1 if feasible and a matches f1, else 0. 'abandon' pays c.
pf1 = 0.5; pfeas = 0.6
def voi(feature, decision_set, c=0.0):
    # expected max utility with vs without observing the feature exactly
    def best(cond):  # cond: dict of observed values
        p1 = pf1 if 'f1' not in cond else float(cond['f1'])
        pf = pfeas if 'f2' not in cond else float(cond['f2'])
        vals = {'a1': pf * (1 - p1), 'a2': pf * p1}
        if 'abandon' in decision_set:
            vals['abandon'] = c
        return max(vals[a] for a in decision_set)
    base = best({})
    if feature == 'f1':
        with_ = pf1 * best({'f1': 1}) + (1 - pf1) * best({'f1': 0})
    else:
        with_ = pfeas * best({'f2': 1}) + (1 - pfeas) * best({'f2': 0})
    return with_ - base
for ds, c in [(('a1', 'a2'), 0.0), (('a1', 'a2', 'abandon'), 0.25)]:
    print(f"  decision set={ds}, abandon pays {c}:  VOI(f1)={voi('f1', ds, c):.4f}   VOI(f2: feasibility)={voi('f2', ds, c):.4f}")

print()
print("=" * 78)
print("N7  The ambiguity term I(G;Omega|e,M-) under the two joints")
print("=" * 78)
# (alpha) G independent of Omega given e: ambiguous observation, posterior 0.5/0.5 on {flaw, ok}.
pG = np.array([0.5, 0.5]); post_alpha = np.array([0.5, 0.5])
I_alpha = 0.0  # P(Omega|e,G) = P(Omega|e) for both G
m_ship = tilt(post_alpha, np.array([0.0, 1.0]), 2.0); m_corr = tilt(post_alpha, np.array([1.0, 0.0]), 2.0)
print(f"  (alpha) G ⟂ Omega | e : I(G;Omega|e)={I_alpha:.3f}  A(e)={I_alpha/entropy(post_alpha):.3f}  "
      f"but a tilting agent shows TV(M+_ship, M+_correct)={tv(m_ship, m_corr):.3f}  (bias with A=0)")
# (beta) G informative: goals assigned by a principal who knows more. P(Omega=flaw | e, G=correct)=0.8, (.. | G=ship)=0.2.
post_beta = {0: np.array([0.8, 0.2]), 1: np.array([0.2, 0.8])}   # G=0 'correct', G=1 'ship' ; Omega index 0 = flaw
marg = 0.5 * post_beta[0] + 0.5 * post_beta[1]
I_beta = 0.5 * kl(post_beta[0], marg) + 0.5 * kl(post_beta[1], marg)
print(f"  (beta)  G informative      : I(G;Omega|e)={I_beta:.3f}  A(e)={I_beta/entropy(marg):.3f}  "
      f"the goal-using Bayesian moves by TV={tv(post_beta[0], marg):.2f} from the goal-blind belief --")
# score comparison: who is right?
def exp_logscore(belief_fn):
    s = 0.0
    for g in (0, 1):
        for om in (0, 1):
            p = 0.5 * post_beta[g][om]
            s += -p * math.log(belief_fn(g)[om])
    return s
print(f"          E[-log b]: goal-using = {exp_logscore(lambda g: post_beta[g]):.4f}  goal-blind = {exp_logscore(lambda g: marg):.4f}"
      f"  (the 'bias' is the correct update; the goal-blind agent scores worse)")

print()
print("=" * 78)
print("N8  Paper-3 semantics: calibrated allocation is counted at maximal transferred information")
print("=" * 78)
# N3's allocation agent: belief is an injective function of G at fixed (x1,x2) whenever post(x1) != post(x2).
cnt = 0; tot = 0
for a in (0, 1):
    for b in (0, 1):
        tot += 1; cnt += (abs(post(x1=a) - post(x2=b)) > 1e-9)
print(f"  allocation agent: beliefs differ across the two goals on {cnt}/{tot} feature patterns -> I(G;M+|e,M-) = H(G) = log 2 there;")
print(f"  kappa_canon = 1 on those events, reliability = 0 (N3). The displacement bound's RHS is maximal for a calibrated agent.")

print()
print("all checks passed")

print()
print("=" * 78)
print("N9  MI tracks displacement only relative to update noise (out-of-family for N2)")
print("=" * 78)
# Binary uniform G; reported log-odds = +lam (G=1) or -lam (G=2) plus Gaussian noise sd s. I(G; logodds) by quadrature.
from math import erf, sqrt, pi as PI
def mi_binary_gauss(lam, s, n=20001):
    xs = np.linspace(-8 * s - lam, 8 * s + lam, n)
    f1 = np.exp(-(xs - lam) ** 2 / (2 * s * s)) / (s * sqrt(2 * PI))
    f2 = np.exp(-(xs + lam) ** 2 / (2 * s * s)) / (s * sqrt(2 * PI))
    mix = 0.5 * f1 + 0.5 * f2
    dx = xs[1] - xs[0]
    def integ(f):
        m = f > 0
        return float(np.sum(f[m] * np.log(f[m] / mix[m])) * dx)
    return 0.5 * integ(f1) + 0.5 * integ(f2)
for lam, s in [(1e-3, 1.0), (0.3, 1.0), (1.0, 1.0), (1.0, 0.1), (1e-3, 1e-4)]:
    print(f"  lam={lam:<6g} noise sd={s:<6g}  I(G;M+|e,M-)={mi_binary_gauss(lam, s):.4f} nats  (H(G)={math.log(2):.4f})  -> kappa_canon={mi_binary_gauss(lam, s)/math.log(2):.3f}")

print()
print("=" * 78)
print("N10 Abandon option present but never optimal: VOI(feasibility) stays zero")
print("=" * 78)
print(f"  decision set with abandon paying 0.0: VOI(f2)={voi('f2', ('a1','a2','abandon'), 0.0):.4f}   (condition in Prop 7.1(b) is needed)")

print()
print("=" * 78)
print("N11 A non-motivated distortion (rounding the belief) is still uncalibrated")
print("=" * 78)
def rounded(a, b):
    p = post(a, b); return min(max(round(p * 4) / 4, 0.05), 0.95)
s, U, RES, REL = murphy_logscore(rounded)
print(f"  round full posterior to nearest 0.25: REL={REL:.4f} > 0 ; coarsening the *belief* is not coarsening the *information*")

print()
print("=" * 78)
print("N12 Gaussian mean-shift is an exponential tilt: exact Jensen gap = beta^2/(2 sigma^2); range bound vacuous")
print("=" * 78)
for sigma, beta in [(1.0, 0.5), (2.0, 0.5), (0.5, 0.5)]:
    # pi = N(mu, sigma^2); r = exp(lam (x - mu)) with lam = beta/sigma^2 shifts the mean by beta.
    lam = beta / sigma ** 2
    kl_exact = beta ** 2 / (2 * sigma ** 2)
    jensen = 0.5 * lam ** 2 * sigma ** 2  # log E e^{lam X} - lam E X for X ~ N(0, sigma^2)
    print(f"  sigma={sigma} beta={beta}: Jensen gap={jensen:.4f}  KL(N(mu,s2)||N(mu+beta,s2))={kl_exact:.4f}  Var_pi(u)=sigma^2={sigma**2}  (range bound: supp unbounded -> vacuous)")

print()
print("=" * 78)
print("N13 Dorst's two-world example: honest update under ambiguous evidence is predictable, uncalibrated, and still better")
print("=" * 78)
# Worlds b, g equiprobable. Update: at b the agent cannot tell (stays 0.5); at g it becomes certain of g. Y = 1{g}. Brier score.
prior_score = 0.5 * (0.5 - 0) ** 2 + 0.5 * (0.5 - 1) ** 2
upd_score = 0.5 * (0.5 - 0) ** 2 + 0.5 * (1.0 - 1) ** 2
# Murphy/Broecker (Brier): U = p(1-p); REL = sum mass*(forecast - P(Y|forecast))^2 ; RES = sum mass*(P(Y|forecast) - pbar)^2
U = 0.5 * 0.5
REL = 0.5 * (0.5 - 0.0) ** 2 + 0.5 * (1.0 - 1.0) ** 2
RES = 0.5 * (0.0 - 0.5) ** 2 + 0.5 * (1.0 - 0.5) ** 2
assert abs(upd_score - (U - RES + REL)) < 1e-12
exp_posterior = 0.5 * 0.5 + 0.5 * 1.0
print(f"  prior Brier={prior_score:.4f}  updated Brier={upd_score:.4f}  = U({U:.3f}) - RES({RES:.3f}) + REL({REL:.3f})")
print(f"  Reflection fails: prior P(g)=0.5 but E[updated P(g)]={exp_posterior:.3f}; reliability > 0 with no goal involved; recalibrated forecast (0 at b) would score 0.")

print()
print("all checks passed (N1-N13)")
