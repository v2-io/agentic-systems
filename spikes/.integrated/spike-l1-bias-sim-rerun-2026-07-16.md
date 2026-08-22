# Spike: L1' update-bias Monte Carlo rerun — verification + AND-root extension (2026-07-16)

**Status: LANDED 2026-07-16** — carrier: `#deriv-l1-update-bias` (Monte Carlo verification block restated + strengthened). Reasoning trail + preserved script below.

**Why this exists.** The bulk-64 verify-pass (ledger: `.integrated/VERIFICATION-2026-07-16.md`) confirmed that `#deriv-l1-update-bias`'s *[Empirical claim (monte-carlo-confirmation)]* block did not match the simulation record it cited (`.integrated/spike-l1-update-bias.md` §7): the block described "four scenarios: OR-cooperative, OR-adversarial, AND-cooperative, AND-adversarial" (a taxonomy from other segments' sims, absent from the record) and a grid "$\rho \in \{0.1, 0.3, 0.5, 0.7, 0.9\}$" that is partly infeasible under the spike's own definition ($\rho = \operatorname{Cov}(Y_1,Y_2) = \theta_C(1-\theta_C)\Delta_1\Delta_2 \leq 1/4$; the record's actual maximum was $0.16$). Diagnosis: a confabulated summary written at landing (the four-scenario text entered with the original commit, pre-AAD→AAT-rename; no later cycle reran anything). The original script lived at `/tmp/l1sim/sim.py` and is lost. Strengthen-first resolution: re-implement fresh from the record's §7.1 protocol + §2 closed form, verify, and extend to the AND-root case the segment claimed but the record never simulated.

## Results (fresh implementation, seed 20260716)

**1. Original record validated.** Scenario A ($\theta_C = 0.4$, $p_{j\mid C} = 0.9$, $p_{j\mid\neg C} = 0.1$, 400 trials × 5000 cycles, OR-root): cumulative drift $-0.3996$ vs the 2026-04-23 record's $-0.3997$ — reproduction to 4 significant figures from an independent implementation. The old sim was correct; only the segment's summary was wrong.

**2. Initial-rate vs closed form** ($B_1 = -\iota(1-\mu_{\bar 1})\rho/((n+1)\lVert\mathbf J\rVert^2)$ for OR; sign $+$ with Jacobian factor $\mu_{\bar 1}$ for AND; $n_{\text{init}} = 10$; $2 \times 10^6$ draws per cell; symmetric $\Delta$-grid at $\theta_C = 0.5$ so $\rho = \Delta^2/4$):

| root | $\rho$ | observed | predicted | err |
|---|---|---|---|---|
| OR | 0.0400 | $-3.62 \times 10^{-3}$ | $-3.64 \times 10^{-3}$ | 0.4% |
| OR | 0.0900 | $-8.16 \times 10^{-3}$ | $-8.18 \times 10^{-3}$ | 0.3% |
| OR | 0.1600 | $-1.451 \times 10^{-2}$ | $-1.455 \times 10^{-2}$ | 0.3% |
| OR | 0.2025 | $-1.837 \times 10^{-2}$ | $-1.841 \times 10^{-2}$ | 0.2% |
| OR | 0.2401 | $-2.183 \times 10^{-2}$ | $-2.183 \times 10^{-2}$ | 0.0% |
| AND | 0.0400 | $+3.66 \times 10^{-3}$ | $+3.64 \times 10^{-3}$ | 0.7% |
| AND | 0.1600 | $+1.452 \times 10^{-2}$ | $+1.455 \times 10^{-2}$ | 0.2% |
| AND | 0.2401 | $+2.182 \times 10^{-2}$ | $+2.183 \times 10^{-2}$ | 0.0% |
| OR | 0.0500 | $-4.82 \times 10^{-3}$ | $-4.85 \times 10^{-3}$ | 0.6% (asymmetric edges) |
| AND | 0.0500 | $+3.95 \times 10^{-3}$ | $+3.93 \times 10^{-3}$ | 0.6% (asymmetric edges) |

All $\lt 1\%$. **AND-root opposite-sign/matching-magnitude confirmed by simulation** (previously derivation-only).

**3. Nulls.** Degenerate L1' ($\Delta = 0 \Rightarrow \rho = 0$): observed rate $\sim 10^{-5}$ (noise floor) for both roots. L0-matched control: drift $+3 \times 10^{-4}$ over 5000 cycles — no false positive.

**4. Drift shape (honesty note carried into the segment).** Scenario-A drift checkpoints (OR): $-0.317$ @500, $-0.346$ @1000, $-0.371$ @2000, $-0.400$ @5000. Growth is log-order (a linear ratio would be $2.0$ per doubling; observed $1.09$; frozen-state $\log$ prediction $1.17$) but decelerates *faster* than the frozen-state $\sum_t 1/(n{+}t{+}1)$ sum — the bias-induced $\mathbf p(t)$ trajectory effect the original spike's §7.3 already noted. The segment's old "logarithmic cumulative drift matches" was too strong; the restated block says log-order + decelerating, with the transient's closed form left open (as the segment's Epistemic Status already stated).

## Preserved script

The original's loss (`/tmp`) is why this one rides in the spike. Runs in ~40s with numpy.

```python
import numpy as np

def sigmoid(x): return 1.0/(1.0+np.exp(-x))
def logit(p): return np.log(p/(1.0-p))

def world_params(theta_C, pC, pnC):
    pC, pnC = np.array(pC, float), np.array(pnC, float)
    mu = theta_C*pC + (1-theta_C)*pnC
    rho = theta_C*(1-theta_C)*(pC[0]-pnC[0])*(pC[1]-pnC[1])
    return mu, rho

def draw(rng, size, theta_C, pC, pnC, L1prime, mu):
    if L1prime:
        c = rng.random(size) < theta_C
        y1 = rng.random(size) < np.where(c, pC[0], pnC[0])
        y2 = rng.random(size) < np.where(c, pC[1], pnC[1])
    else:
        y1 = rng.random(size) < mu[0]; y2 = rng.random(size) < mu[1]
    return y1.astype(float), y2.astype(float)

def initial_rate(rng, root, theta_C, pC, pnC, n_init=10, N=2_000_000):
    mu, rho = world_params(theta_C, pC, pnC)
    p1, p2 = mu
    y1, y2 = draw(rng, N, theta_C, pC, pnC, True, mu)
    if root == "OR":
        y = 1-(1-y1)*(1-y2); P = 1-(1-p1)*(1-p2); J1, J2 = 1-p2, 1-p1
    else:
        y = y1*y2;           P = p1*p2;           J1, J2 = p2, p1
    r = y - P
    Jn2 = J1*J1 + J2*J2
    obs = (1.0/(n_init+1)) * J1 * r.mean() / Jn2
    pred = (-(1-p2) if root == "OR" else +p2) * rho/((n_init+1)*Jn2)
    return obs, pred, rho

def trajectory(rng, root, theta_C, pC, pnC, L1prime=True, trials=400, cycles=5000, n_init=10):
    mu, rho = world_params(theta_C, pC, pnC)
    lam1 = np.full(trials, logit(mu[0])); lam2 = np.full(trials, logit(mu[1]))
    n1 = n2 = n_init
    checkpoints = {}
    for t in range(cycles):
        y1, y2 = draw(rng, trials, theta_C, pC, pnC, L1prime, mu)
        p1, p2 = sigmoid(lam1), sigmoid(lam2)
        if root == "OR":
            y = 1-(1-y1)*(1-y2); P = 1-(1-p1)*(1-p2); J1, J2 = 1-p2, 1-p1
        else:
            y = y1*y2;           P = p1*p2;           J1, J2 = p2, p1
        r = y - P
        Jn2 = J1*J1 + J2*J2
        lam1 += (1.0/(n1+1))*J1*r/Jn2; lam2 += (1.0/(n2+1))*J2*r/Jn2
        n1 += 1; n2 += 1
        if t+1 in (500, 1000, 2000, 5000):
            checkpoints[t+1] = (lam1.mean()-logit(mu[0]), lam2.mean()-logit(mu[1]))
    return checkpoints, rho

rng = np.random.default_rng(20260716)
for root in ("OR", "AND"):
    for Delta in (0.4, 0.6, 0.8, 0.9, 0.98):
        pC = (0.5+Delta/2,)*2; pnC = (0.5-Delta/2,)*2
        print(root, initial_rate(rng, root, 0.5, pC, pnC))
    print(root, initial_rate(rng, root, 0.5, (0.8,0.6), (0.3,0.2)), "(asym)")
    print(root, "null:", initial_rate(rng, root, 0.5, (0.5,0.5), (0.5,0.5)))
    print(root, "scenA:", trajectory(rng, root, 0.4, (0.9,0.9), (0.1,0.1)))
print("L0 ctrl:", trajectory(rng, "OR", 0.4, (0.9,0.9), (0.1,0.1), L1prime=False))
```

## Process guard (for future landings)

When summarizing a simulation record into a segment's Empirical-claim block, transcribe the record's parameters — don't paraphrase from memory. The confabulated block here survived three months of sweeps because it was *plausible*: right trial counts, wrong everything else. The tell that caught it: the claimed $\rho$ grid exceeded the parameterization's feasible maximum.
