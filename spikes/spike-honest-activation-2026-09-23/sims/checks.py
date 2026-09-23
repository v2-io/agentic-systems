#!/usr/bin/env python3
"""
Numeric checks for the honest-activation spike (2026-09-23).

Every closed form claimed in 03-derivations.md is checked here against either
exact linear algebra or Monte Carlo. Run:  python3 checks.py > checks-output.txt
Each section prints CLAIM / COMPUTED / PASS-or-FAIL. Nothing here is tuned to
pass: tolerances are stated per check.
"""
import numpy as np
from math import log2

rng = np.random.default_rng(20260923)
fails = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        fails.append(name)

# ---------------------------------------------------------------------------
# S0. Gain is data-independent in the fixed-model linear-Gaussian filter.
#     Two runs with identical noise model, one fed truth, one fed a lie:
#     the gain sequences must be identical to machine precision.
# ---------------------------------------------------------------------------
print("\n=== S0: Kalman gain is content-independent (fixed noise model) ===")
def kalman_gains(obs, U0, R, Q=0.0):
    P, gains = U0, []
    for _ in obs:
        P = P + Q
        K = P / (P + R)
        gains.append(K)
        P = (1 - K) * P
    return np.array(gains)
theta, b = 0.0, 5.0
truth = theta + rng.normal(0, 1, 200)
lie = theta + b + rng.normal(0, 1, 200)
g1, g2 = kalman_gains(truth, 4.0, 1.0, 0.01), kalman_gains(lie, 4.0, 1.0, 0.01)
check("S0 gain sequences identical under truth vs lie", np.max(np.abs(g1 - g2)) == 0.0,
      f"max|dK|={np.max(np.abs(g1-g2))}")

# ---------------------------------------------------------------------------
# S1. False confidence under a zero-bias-variance (trusting / correlation-
#     neglecting) channel model.  Agent believes y_i = theta + eps_i,
#     eps ~ N(0, s2) iid; truth is y_i = theta + b + eps_i.
#     Claims:
#       U_n = 1/(1/U0 + n/s2)
#       E[mu_n] - theta = (U_n/U0)(mu0 - theta) + U_n * n * b / s2  -> b
#       calibration ratio  E[(mu_n-theta)^2] / U_n  ~  1 + n b^2 / s2  (mu0=theta)
#       honest-channel gain after n:  eta_H = U_n/(U_n + sH2)
#     Structured agent (source bias beta ~ N(0,tau2)): posterior var of theta
#       V_n = 1/(1/U0 + 1/(tau2 + s2/n))  -> 1/(1/U0 + 1/tau2)   (confidence floor = tau2)
# ---------------------------------------------------------------------------
print("\n=== S1: false confidence, calibration ratio, honest-gain suppression ===")
U0, s2, sH2, mu0 = 4.0, 1.0, 1.0, 0.0
for n in [1, 10, 100, 1000]:
    Un = 1 / (1 / U0 + n / s2)
    # Monte Carlo of the posterior mean
    reps = 20000
    ybar = theta + b + rng.normal(0, np.sqrt(s2 / n), reps)
    mu_n = Un * (mu0 / U0 + n * ybar / s2)
    mse = np.mean((mu_n - theta) ** 2)
    pred_bias = Un * n * b / s2 + (Un / U0) * (mu0 - theta)
    pred_mse = pred_bias ** 2 + Un**2 * n / s2   # variance of mu_n = Un^2 * n * s2 / s2^2
    ratio = mse / Un
    pred_ratio = pred_mse / Un
    check(f"S1 n={n} MSE matches closed form", abs(mse - pred_mse) / pred_mse < 0.03,
          f"MC={mse:.4f} closed={pred_mse:.4f}")
    etaH = Un / (Un + sH2)
    print(f"      n={n:5d}  believed U_n={Un:.5f}  actual MSE={mse:.4f}  "
          f"calibration ratio={ratio:9.2f} (pred {pred_ratio:9.2f}; ~1+n b^2/s2={1+n*b*b/s2:9.1f})  "
          f"honest-channel gain={etaH:.5f}")
# structured agent floor
for tau2 in [1.0, 0.1, 0.01]:
    Vinf = 1 / (1 / U0 + 1 / tau2)
    # NOTE (recorded): first run checked n=1000, which fails for tau2=0.01 because
    # s2/n is still 10% of tau2 there -- a check-design error (the claim is the n->inf
    # floor). Checking the limit at n=1e6 instead.
    Vn = 1 / (1 / U0 + 1 / (tau2 + s2 / 10**6))
    check(f"S1 structured floor tau2={tau2}: V_(1e6) -> floor", abs(Vn - Vinf) / Vinf < 0.02,
          f"V={Vn:.5f} floor={Vinf:.5f}")

# ---------------------------------------------------------------------------
# S2. Attribution floor (Gaussian persistent-bias model).
#     K honest channels (true bias 0, prior tau_H2) + 1 adversary (true bias b,
#     prior tau_A2), infinitely many messages per channel => channel means known.
#     Claim: posterior mean error = b * w_A, w_A = (1/tau_A2)/(1/U0 + 1/tau_A2 + K/tau_H2)
#     and it does not shrink with more data (only relative biases identified).
# ---------------------------------------------------------------------------
print("\n=== S2: attribution floor, Gaussian bias prior ===")
def post_mean_error(K, tauA2, tauH2, U0, b, n_per=10**9, s2=1.0):
    # channel mean observations m_j = theta + beta_j + noise/sqrt(n)
    # exact Gaussian conditioning with theta=0, beta_H=0, beta_A=b
    prec = 1 / U0 + 1 / (tauA2 + s2 / n_per) + K / (tauH2 + s2 / n_per)
    return (b / (tauA2 + s2 / n_per)) / prec
for K in [0, 1, 3, 10]:
    for tauA2 in [1.0, 0.01]:
        e = post_mean_error(K, tauA2, 1.0, 4.0, b)
        wA = (1 / tauA2) / (1 / 4.0 + 1 / tauA2 + K / 1.0)
        check(f"S2 K={K} tauA2={tauA2}", abs(e - b * wA) < 1e-6, f"error={e:.4f}  b*w_A={b*wA:.4f}")
# More data does not help: compare n_per = 1e3 vs 1e9
e3, e9 = post_mean_error(3, 0.01, 1.0, 4.0, b, 1000), post_mean_error(3, 0.01, 1.0, 4.0, b, 10**9)
check("S2 error saturates with data (1e3 vs 1e9 msgs/channel)", abs(e3 - e9) < 0.01 * e9,
      f"{e3:.4f} vs {e9:.4f}")

# ---------------------------------------------------------------------------
# S2b. Attribution in a spike-and-slab (honest / liar mixture) source model.
#      Source j honest w.p. p_j (bias exactly 0) else liar with bias ~ N(0, L2).
#      Channel means known exactly.  Adversary says b, K honest channels say 0.
#      Compute posterior P(adversary is the liar) exactly by enumerating which
#      subset is lying (theta integrated against a N(mu0,U0) prior).
# ---------------------------------------------------------------------------
print("\n=== S2b: attribution in honest/liar mixture ===")
from itertools import product
from scipy.stats import multivariate_normal as mvn

def p_adv_liar(K, pA, pH, b, U0=4.0, L2=25.0, eps2=1e-6):
    # observed channel means: adversary first
    m = np.array([b] + [0.0] * K)
    J = K + 1
    ps = np.array([pA] + [pH] * K)
    num = 0.0; den = 0.0
    for liar_mask in product([0, 1], repeat=J):
        lm = np.array(liar_mask)
        prior = np.prod(np.where(lm == 1, 1 - ps, ps))
        # m = theta*1 + beta, beta_j ~ N(0, L2) if liar else N(0, eps2)
        cov = U0 * np.ones((J, J)) + np.diag(np.where(lm == 1, L2, eps2))
        like = mvn.pdf(m, mean=np.zeros(J), cov=cov)
        w = prior * like
        den += w
        if lm[0] == 1:
            num += w
    return num / den
for K in [0, 1, 2, 3]:
    for pA in [0.5, 0.9, 0.99, 0.999]:
        print(f"      K={K}  prior P(adv honest)={pA:<6}  ->  posterior P(adv is liar) = {p_adv_liar(K, pA, 0.5, b):.4f}")
# NOTE (recorded): the first run used a content prior N(0, 4) centred on the TRUE
# value, so the agent's own prior knowledge acted as an extra channel voting against
# the lie (K=1, pA=0.99 gave P(adv liar)=0.24, not <0.1).  That is a finding, not a
# bug: attribution is set by source priors AND by the lie's plausibility under the
# content prior.  Separate the two effects:
print("      -- diffuse content prior (U0=1e4, eps2=1e-4): pure source-prior attribution --")
for K in [0, 1, 2]:
    for pA in [0.5, 0.9, 0.99]:
        print(f"      K={K}  pA={pA:<5} pH=0.5  -> P(adv liar) = {p_adv_liar(K, pA, 0.5, b, U0=1e4, eps2=1e-4):.4f}")
# NOTE (recorded): second run checked "attribution = prior odds (~0.010)" and got
# 0.0189 -- my prediction dropped the both-sources-lying configuration.  With a
# diffuse content prior only the discrepancy d = m_A - m_H is informative, and the
# exact posterior is the closed form below.  What survives (and is the claim): at
# K=1 attribution is a function of priors and d only -- never of data volume.
from scipy.stats import norm as _n
def k1_closed(pA, pH, d, L2=25.0):
    f1, f2 = _n.pdf(d, 0, np.sqrt(L2)), _n.pdf(d, 0, np.sqrt(2 * L2))
    num = pH * (1 - pA) * f1 + (1 - pA) * (1 - pH) * f2
    den = pA * (1 - pH) * f1 + num
    return num / den
for pA in [0.5, 0.9, 0.99]:
    pr = p_adv_liar(1, pA, 0.5, b, U0=1e4, eps2=1e-4)
    cf = k1_closed(pA, 0.5, b)
    check(f"S2b K=1 diffuse prior pA={pA}: enumeration matches closed form", abs(pr - cf) < 0.002,
          f"enum={pr:.4f} closed={cf:.4f}")
print("      -- content-prior plausibility of the lie (K=1, pA=0.99, pH=0.5) --")
for U0_ in [1e4, 100.0, 4.0, 1.0]:
    print(f"      content prior sd={np.sqrt(U0_):8.1f} (lie is {b/np.sqrt(U0_):.2f} prior-sd from truth) -> P(adv liar) = {p_adv_liar(1, 0.99, 0.5, b, U0=U0_, eps2=1e-4):.4f}")
check("S2b K=2 agreeing honest channels overturn even pA=0.99",
      p_adv_liar(2, 0.99, 0.5, b) > 0.9, f"P={p_adv_liar(2, 0.99, 0.5, b):.4f}")

# ---------------------------------------------------------------------------
# S3. Retroactive correction after discovery: pooled vs provenance memory.
#     n_A adversary messages and n_H honest messages were absorbed under a
#     trusting model. Discovery: "source A is a liar".
#     Provenance memory (per-source n_j, S_j): drop A exactly.
#     Pooled memory (mu, U): cannot separate; best available = keep (biased)
#     or reset to prior (lose honest info).  Show that for fixed pooled (mu,U)
#     different (S_A, S_H) splits are consistent => non-identifiable.
# ---------------------------------------------------------------------------
print("\n=== S3: pooled vs provenance memory after discovery ===")
nA, nH = 50, 20
yA = theta + b + rng.normal(0, 1, nA)
zH = theta + rng.normal(0, 1, nH)
U = 1 / (1 / U0 + (nA + nH) / 1.0)
mu = U * (mu0 / U0 + yA.sum() + zH.sum())
# provenance correction
U_c = 1 / (1 / U0 + nH)
mu_c = U_c * (mu0 / U0 + zH.sum())
print(f"      pooled belief mu={mu:.3f} (truth 0), provenance-corrected mu={mu_c:.3f}, corrected U={U_c:.4f}")
# non-identifiability: construct a different split with same pooled stats
S_total = yA.sum() + zH.sum()
alt_SA = S_total - (nH * 3.0)   # pretend honest channel said 3.0 on average
alt_mu_c = U_c * (mu0 / U0 + nH * 3.0)
check("S3 same pooled (mu,U) admits different honest-channel sums", abs(alt_mu_c - mu_c) > 1.0,
      f"corrected estimates {mu_c:.3f} vs {alt_mu_c:.3f} from identical pooled memory")

# ---------------------------------------------------------------------------
# S4. Recovery by dilution (pooled trusting agent, adversary silenced):
#     bias(m) = b*(nA/s2)/(1/U0 + nA/s2 + m/sH2).  Honest messages needed to
#     get bias <= eps:  m* = sH2*( (b/eps)*(nA/s2) - 1/U0 - nA/s2 ).
#     Persistent adversary at rate share: Berk-type limit
#     bias_inf = b*(nuA/s2)/(nuA/s2 + nuH/sH2).
# ---------------------------------------------------------------------------
print("\n=== S4: recovery by dilution, and the persistent-deceiver limit ===")
for nA_ in [10, 100, 1000]:
    eps = 0.1
    mstar = sH2 * ((b / eps) * (nA_ / s2) - 1 / U0 - nA_ / s2)
    m_int = int(np.ceil(mstar))
    bias_at = b * (nA_ / s2) / (1 / U0 + nA_ / s2 + m_int / sH2)
    check(f"S4 nA={nA_}: m*={m_int} honest msgs gives bias<=eps", bias_at <= eps + 1e-9,
          f"bias={bias_at:.4f}")
# persistent-deceiver simulation (sequential)
nuA, nuH, T = 3, 1, 20000
precA, precH = 1 / s2, 1 / sH2
P, m_ = U0, mu0
for t in range(T):
    for _ in range(nuA):
        y = theta + b + rng.normal(0, np.sqrt(s2)); K_ = P / (P + s2); m_ += K_ * (y - m_); P *= (1 - K_)
    for _ in range(nuH):
        z = theta + rng.normal(0, np.sqrt(sH2)); K_ = P / (P + sH2); m_ += K_ * (z - m_); P *= (1 - K_)
berk = b * (nuA * precA) / (nuA * precA + nuH * precH)
check("S4 persistent deceiver: belief converges to Berk-type point, not truth", abs(m_ - berk) < 0.05,
      f"final mean={m_:.3f}  predicted limit={berk:.3f}  truth=0")

# ---------------------------------------------------------------------------
# S5. Forgetting (fading memory, factor lam) as defense.
#     Believed precision after long exposure at rate nu*prec: <= nu*prec/(1-lam) + ...
#     After the adversary stops, its weight decays like lam^t.
# ---------------------------------------------------------------------------
print("\n=== S5: fading memory bounds false confidence and speeds recovery ===")
lam = 0.95
prec_sum, wsum = 0.0, 0.0
for t in range(5000):
    prec_sum = lam * prec_sum + 1 / s2
check("S5 believed precision bounded by 1/((1-lam) s2)", abs(prec_sum - 1 / ((1 - lam) * s2)) < 1e-6,
      f"{prec_sum:.4f} vs {1/((1-lam)*s2):.4f}")
# recovery: stats (A-weight, H-weight) with forgetting after adversary silenced
wA, wH = 1 / ((1 - lam) * s2), 0.0
for t in range(200):
    wA *= lam; wH = lam * wH + 1 / sH2
bias_forget = b * wA / (wA + wH)
check("S5 with forgetting, adversary weight decays geometrically", bias_forget < 1e-3,
      f"bias after 200 honest steps={bias_forget:.2e}")
# cost: steady-state variance in an honest static world with forgetting
# (effective sample size (1+lam)/(1-lam) for exponential weights -> var s2*(1-lam)/(1+lam))
w = lam ** np.arange(5000)
ess = w.sum() ** 2 / (w ** 2).sum()
check("S5 cost: effective sample size = (1+lam)/(1-lam)", abs(ess - (1 + lam) / (1 - lam)) < 1e-6,
      f"ESS={ess:.3f}")

# ---------------------------------------------------------------------------
# S6. Verbatim repetition read as precision by a noise-estimating agent
#     (Normal-Inverse-Gamma conjugate).  n identical messages -> posterior
#     expected noise variance -> 0 like b0/(a0+n/2-1).
# ---------------------------------------------------------------------------
print("\n=== S6: verbatim repetition looks like a precise channel ===")
a0, b0, k0, m0 = 2.0, 1.0, 1.0, 0.0
for n in [1, 10, 100, 1000]:
    x = np.full(n, 7.0)  # the same claim, verbatim
    xbar = x.mean(); ss = ((x - xbar) ** 2).sum()
    an = a0 + n / 2; bn = b0 + 0.5 * ss + k0 * n * (xbar - m0) ** 2 / (2 * (k0 + n))
    Esig2 = bn / (an - 1)
    xv = 7.0 + rng.normal(0, 1, n)  # same claim with natural variation
    xbv = xv.mean(); ssv = ((xv - xbv) ** 2).sum()
    bnv = b0 + 0.5 * ssv + k0 * n * (xbv - m0) ** 2 / (2 * (k0 + n))
    print(f"      n={n:5d}  E[sigma^2 | verbatim]={Esig2:8.4f}   E[sigma^2 | varied]={bnv/(an-1):8.4f}")
check("S6 verbatim repetition drives estimated noise toward 0",
      (b0 + 1000 * 49 / (2 * 1001)) / (a0 + 500 - 1) < 0.1)

# ---------------------------------------------------------------------------
# S7. Out-of-family drill: robust (Student-t) observation model.  Gain IS
#     data-dependent here.  Does a lie on the only channel still get absorbed?
#     Grid posterior with t_3 likelihood; adversary is the only channel.
# ---------------------------------------------------------------------------
print("\n=== S7: out-of-family (Student-t) filter, single-channel lie ===")
from scipy.stats import t as tdist, norm
grid = np.linspace(-20, 20, 8001)
logp = norm.logpdf(grid, 0, 2.0)
ys = theta + b + rng.normal(0, 1, 200)
means = []
for y in ys:
    logp = logp + tdist.logpdf(y - grid, df=3)
    p = np.exp(logp - logp.max()); p /= p.sum()
    means.append((grid * p).sum())
check("S7 t-filter still converges to the lie on a sole channel (L1-equivalence)", abs(means[-1] - b) < 0.3,
      f"final mean={means[-1]:.3f}, lie={b}")
# with one honest channel present and equal trust: t-model splits/bimodal
logp = norm.logpdf(grid, 0, 2.0)
for i in range(200):
    logp = logp + tdist.logpdf(ys[i] - grid, df=3) + tdist.logpdf(rng.normal(0, 1) - grid, df=3)
p = np.exp(logp - logp.max()); p /= p.sum()
sd = np.sqrt((grid**2 * p).sum() - ((grid * p).sum()) ** 2)
print(f"      t-filter with one conflicting honest channel: posterior mean={(grid*p).sum():.3f}, sd={sd:.3f}")

# ---------------------------------------------------------------------------
# S8. Detected deception and channel capacity.  A source whose binary claims
#     are false at rate q in contexts the receiver cannot distinguish is a
#     BSC(q): capacity 1 - H(q).  And the type-mixture update on discovering
#     one deliberate lie.
# ---------------------------------------------------------------------------
print("\n=== S8: discovered deception -> channel capacity and type posterior ===")
def H(q):
    return 0.0 if q in (0, 1) else -q * log2(q) - (1 - q) * log2(1 - q)
for q in [0.0, 0.01, 0.05, 0.1, 0.25]:
    print(f"      lie rate q={q:<5}  capacity per binary claim = {1-H(q):.4f} bits")
# type mixture: honest type deliberately lies w.p. d_H (~0), strategic type w.p. q_S
piH = 0.95
for dH in [0.0, 1e-4, 1e-2]:
    qS = 0.2
    post = piH * dH / (piH * dH + (1 - piH) * qS)
    print(f"      prior P(honest)={piH}, P(deliberate lie|honest)={dH}: after one discovered deliberate lie P(honest)={post:.4f}")
check("S8 one discovered deliberate lie collapses honest-type posterior when dH<<qS",
      piH * 1e-4 / (piH * 1e-4 + (1 - piH) * 0.2) < 0.01)

# ---------------------------------------------------------------------------
# S9. Type-pooled trust: impersonation, once discovered, taxes the genuine
#     type-holder.  Beta reliability shared across all "authority-presenting"
#     sources vs token-indexed reliability.
# ---------------------------------------------------------------------------
print("\n=== S9: impersonation depletes the honest type's credibility under type-pooled trust ===")
a, bb = 20.0, 1.0   # caretaker earned: 20 verified-true, ~1 false
pooled_before = a / (a + bb)
# impersonator using the same presentation is caught in 5 lies
pooled_after = a / (a + bb + 5)
token_after = a / (a + bb)   # token-indexed: caretaker unaffected
print(f"      caretaker reliability: before={pooled_before:.3f}; after impersonator caught (pooled)={pooled_after:.3f}; (token-indexed)={token_after:.3f}")
check("S9 pooled trust transfers the impersonator's discovered lies to the caretaker", pooled_after < pooled_before)

print("\n=== SUMMARY ===")
print("ALL PASS" if not fails else f"FAILURES: {fails}")

# ---------------------------------------------------------------------------
# S10. Corroboration scaling: each additional independent honest channel that
#      agrees multiplies the odds against a lone dissenting source by a
#      "coincidence factor" ~ (pH/(1-pH)) * sqrt(L2/eps2)  (agreement sharpness
#      relative to liar spread).  Measure odds ratio per added channel.
# ---------------------------------------------------------------------------
print("\n=== S10: corroboration factor per independent agreeing channel ===")
for eps2_ in [1e-4, 1e-2, 1.0]:
    odds = []
    for K in [1, 2, 3]:
        p = p_adv_liar(K, 0.99, 0.5, b, U0=1e4, eps2=eps2_)
        odds.append(p / (1 - p))
    r12, r23 = odds[1] / odds[0], odds[2] / odds[1]
    print(f"      honest agreement var={eps2_:<7} odds(adv liar) K=1..3: {[f'{o:.3g}' for o in odds]}  "
          f"factor per added channel ~ {r12:.3g}, {r23:.3g}   (sqrt(L2/eps2)={np.sqrt(25/eps2_):.3g})")
print("\n=== SUMMARY (after S10) ===")
print("ALL PASS" if not fails else f"FAILURES: {fails}")

# ---------------------------------------------------------------------------
# S11. Out-of-family drill for R1: Beta-Bernoulli (non-Gaussian; Fisher
#      information depends on the estimate).  Here content DOES move the gain:
#      unanimous claims give a smaller posterior variance than balanced ones.
#      R1's general form must therefore be the L1-equivalence statement: the
#      gain trajectory under a consistent liar equals the trajectory under a
#      truthful source in the world the liar simulates.
# ---------------------------------------------------------------------------
print("\n=== S11: Beta-Bernoulli drill (content moves gain; L1-equivalence survives) ===")
def beta_var(a, b_):
    return a * b_ / ((a + b_) ** 2 * (a + b_ + 1))
n = 50
v_unan = beta_var(1 + n, 1)          # liar: "yes" every time
v_bal = beta_var(1 + n / 2, 1 + n / 2)  # truthful source in a p=0.5 world
print(f"      after {n} claims: posterior var (unanimous)={v_unan:.2e}  (balanced)={v_bal:.2e}")
check("S11 unanimous claims read as more certain than balanced (content moves gain)", v_unan < v_bal / 10)
# L1-equivalence: a liar simulating a p=0.95 world vs an honest source in a real p=0.95 world
sims = 4000
liar = rng.random((sims, n)) < 0.95       # liar samples from the simulated world
honest = rng.random((sims, n)) < 0.95     # honest source in a world where p really is 0.95
vl = beta_var(1 + liar.sum(1), 1 + n - liar.sum(1)).mean()
vh = beta_var(1 + honest.sum(1), 1 + n - honest.sum(1)).mean()
check("S11 gain trajectory identical in distribution to the simulated world's", abs(vl - vh) / vh < 0.05,
      f"mean post var liar={vl:.3e} honest-in-simulated-world={vh:.3e}")
print("\n=== SUMMARY (after S11) ===")
print("ALL PASS" if not fails else f"FAILURES: {fails}")

# ---------------------------------------------------------------------------
# S12. Sequential dissenters (divide-and-conquer isolation).  Entrenched source A
#      (prior P(honest)=0.99) asserts b.  Honest sources H1, H2, H3 arrive one at
#      a time, each asserting 0.  Two memories:
#        (full)    keeps every source's claim; posterior over all liar-subsets.
#        (discard) at each arrival, MAP-judges the newcomer vs the current belief;
#                  a newcomer judged a liar is discarded (its claim not kept).
#      Claim: full memory escapes once two dissenters are held together;
#      discard memory stays captured however many dissenters arrive singly.
# ---------------------------------------------------------------------------
print("\n=== S12: sequential dissenters, full vs judge-and-discard memory ===")
pA, pH_, U0d, eps2d = 0.99, 0.5, 1e4, 1e-2
# full memory: P(A liar) with K honest sources held simultaneously
full = [p_adv_liar(K, pA, pH_, b, U0=U0d, eps2=eps2d) for K in [1, 2, 3, 4]]
# discard memory: each newcomer faces A alone (K=1 contest), is judged liar if
# P(A liar | A vs newcomer) < 0.5, and discarded; A's standing is unchanged.
discard = []
for k in range(4):
    p1 = p_adv_liar(1, pA, pH_, b, U0=U0d, eps2=eps2d)
    discard.append(p1)   # the same contest every time; nothing accumulates
print(f"      full memory, dissenters held together K=1..4: P(A liar) = {[f'{x:.3f}' for x in full]}")
print(f"      discard memory, dissenters one at a time:      P(A liar) = {[f'{x:.3f}' for x in discard]}")
check("S12 full memory escapes with >=3 held dissenters", full[2] > 0.9, f"{full[2]:.3f}")
check("S12 discard memory remains captured after 4 dissenters", max(discard) < 0.5, f"{max(discard):.3f}")
print("\n=== SUMMARY (after S12) ===")
print("ALL PASS" if not fails else f"FAILURES: {fails}")
