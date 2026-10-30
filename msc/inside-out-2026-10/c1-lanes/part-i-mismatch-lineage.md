*KR C.1 — "Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier." Items A7 and A10 of `owner-review/integrator-items.md`. Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself."*

# Part I: the two mismatch objects, and the persistence lineage (A7, A10)

The landing is commit `da38d358` on branch `worktree-agent-ad30707049b34ab9d`. Its body lists every file and paragraph touched. The checks are recorded in `reviews/part-i-mismatch-lineage-integration.md` (taken into vsect), and four open questions in `questions/`. This file is for the verifier who comes next: what was found, what landed, what was declined, and how to check it without trusting me.

## What A7 turned out to be

The reviewer's item was a naming defect: `#def-mismatch-signal` defines the observed residual $\delta_t = o_t - \hat o_t$ (the innovation), while the persistence results contain the estimation error. Re-running it from the page confirmed the conflation and found that it hid a term.

The dynamics $\dot\delta = -F(\delta) + w$ have a state that a correction contains. The innovation has no such dynamics; for an optimal filter it is white. The state is the estimation error $\bar\delta = \bar o - \hat o$ ($= He$ in a state-space model). The update, however, is driven by the innovation, $\bar\delta$ plus channel noise. So every correction feeds a share of the channel noise back into the estimation error. The disturbance on the contained state is environmental change *plus* gain-injected noise, and the gain-injected part grows with the correction rate.

For linear correction at rate $\alpha$ under Model S, with environmental diffusion $\sigma_{\text{env}}$ and channel-noise intensity $\sigma_\nu$,

$$\mathbb E\lVert\bar\delta\rVert^2_{ss} = \frac{n(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)}{2\alpha}$$

This is U-shaped in $\alpha$. Its minimum is at the Kalman–Bucy gain $\sigma_{\text{env}}/\sigma_\nu$, where the lag and noise contributions are equal, and its value there is $n\sigma_{\text{env}}\sigma_\nu$. Canon had read $\sigma_w$ as environmental only. That gives $n\sigma_{\text{env}}^2/(2\alpha)$, which is monotone in $\alpha$ and half the true value at the optimum. Under Model D with channel noise bounded by $\bar\nu$, the bound is $R^\ast = \rho_{\text{env}}/\alpha + \bar\nu$: a floor that no gain removes.

Consequence: `#result-persistence-condition`'s "faster adaptation improves persistence" was false for tempo raised by gain on fixed observations past the optimum. It is true for tempo raised by event rate or better observations. The segment now states this as "Two levers in $\mathcal T$". The propositions of `#deriv-sector-condition` stand as written, since they are exact for any disturbance meeting their hypotheses. What changed is the reading of $\rho$ and $\sigma_w$, and of the $1/\alpha$ and $1/\sqrt\alpha$ scalings: those describe the lag term alone. `#emp-update-gain` already said a gain set too high fits the noise, so the contradiction was inside the persistence layer, not between it and the gain principle.

This is where A7 and A10 meet. The lag/noise trade-off is Widrow, McCool, Larimore & Johnson 1976. I read the paper at the primary (C. R. Johnson's Cornell copy, now registered in relata). Its abstract says gradient noise is "proportional to the speed of adaptation", lag is "inversely proportional", and the sum is minimized "by choosing the speed of adaptation to make equal the two contributions". That is the balance point $\alpha^2\sigma_\nu^2 = \sigma_{\text{env}}^2$ above.

## The knock-on: `#deriv-persistence-cost`

The main theorem evaluated a rate-distortion function $\sigma^2/(4D)$ at $D = \sigma^2/(2\alpha)$, the environment-only Model S error. It then said the Kalman–Bucy filter "saturates" the bound, because KB's information rate is $K/2$. But KB's actual error is $\sigma^2/K$, twice that $D$, so the comparison was between two different distortions. Separately, the displayed algebra produced $\alpha/2$ where it asserted $n\alpha/2$: the lead's `todo-algebra-typo-…-2e58`, which a 2026-05-30 Working Note had marked "RESOLVED".

What I could verify, and what landed:

- The non-causal RDF of OU at high resolution is $2\sigma^2/(\pi^2 D)$. I computed it numerically by reverse water-filling; it matches Berger 1970's Wiener-process value. It is not $\sigma^2/(4D)$. I did not read Ihara 1993 Thm 4.6.4, which the segment cited for $\sigma^2/(4D)$, so I can't say what that theorem states. Its citation was removed with the derivation it supported.
- The bound that binds an acting agent is the sequential (causal) RDF. For a scalar Gauss–Markov source it is $\tfrac12\log(a^2 + W/D)$ (Tanaka, Kim, Parrilo & Mitter 2017, eq. (28), read on ar5iv), attained by a linear-Gaussian sensor with a Kalman filter. Its continuous-time limit is $\sigma^2/(2D) - \lambda$.
- By Duncan's theorem, KB's information rate is $P/(2\sigma_o^2)$. The steady-state Riccati equation makes that equal to $\sigma^2/(2P) - \lambda$ exactly, for every $\lambda$. So KB meets the causal bound with equality at its own error, at rate $K/2$ per component.

So the segment's headline values survive as exact statements for the Kalman-optimal agent: rate $n\alpha/2$, channel floor $C \geq \mathcal T/2$ per dimension, Landauer $\tfrac12 n\alpha k_BT$. The general statement is now in the error held: $\dot R \geq n(\sigma^2/(2D) - \lambda)$. For a gain other than $K$, the price follows from the error that gain achieves and is not $n\alpha/2$. One caveat on how strong this is: the continuous-time bound is the term-by-term $\Delta \to 0$ limit of the exact discrete result, not a limit theorem. The exact KB match and the numerical convergence are the support, and the Epistemic Status says so.

Working Notes and restatements were brought into line. One audit-gold bullet, "environmental volatility cancels out of the cost", was false and was deleted, along with the same sentence in `#impl-persistence-and-limits`. A more volatile signal needs more information for the same error.

## What A10 landed

`#result-persistence-condition` had claimed novelty, "with no direct anticipation known", for the structural / task-adequacy split. It now credits the split in the body as robust control's stability-versus-performance distinction (Skogestad & Postlethwaite 2005; Zhou, Doyle & Glover 1996). It credits the linear operational form as LMS tracking (Widrow et al. 1976; Guo & Ljung 1995, fields checked on Crossref), and calls the adaptive reserve a disturbance stability margin. The Novelty Claim is now claim synthesis, and what it keeps as ASF's is stated: the threshold with a validity region $R$, which the linear tracking literature lacks; its uniform use across agent classes with the derived/posited sub-scope line; class-level tightness (A.1N); the Model S containment dichotomy; and the information-rate price. The new "Two levers" statement is not claimed as novel either, because it is Widrow's trade-off. Its use inside the persistence condition is a correction, not a contribution.

I count this as a precision fix and not a soften. The parts kept are stated and stand on their own derivations. The one result that changed tier is the corrected information-rate theorem, which stayed exact where it is exact.

## Names

Through `bin/term`: a new entry `estimation-error` (standard name, notation $\bar\delta$, alias "tracking error"); `mismatch` gains the alias "innovation" and a `do_not_confuse`; the `persistence-cost` gloss is restated; decision events are recorded and LEXICON re-rendered. In the segments, "mismatch" stays the ASF name for the innovation. Each persistence-family Setup now states that its $\delta$ denotes the estimation error.

## Declined or left open, and why

- **Symbol sweep** (`question:persistence-family-delta-symbol`). The persistence family still writes $\bar\delta$ as $\delta$, declared at each Setup. Changing the symbol touches about 160 files and other integrators' work.
- **Downstream Model S results** (`question:model-s-total-disturbance-downstream`). Per-dimension, matrix-Loewner, discrete, and especially the adversarial 3/2 exponent were not re-derived under the corrected disturbance. The adversarial exponent looks like the most exposed: it rests on $1/\sqrt{\mathcal T}$ at fixed $\sigma_w$.
- **`#example-kalman` Structural Adaptation section** (`question:example-kalman-structural-adaptation-model-d`). It still applies a Model D ratio to a stochastic system. I kept to the sections I named to the lead because the A.1 integrator is editing that file.
- **Robust-control book citations** (`question:robust-control-lineage-primary-check`). Cited from recall as standard texts, not read.
- **The `todo-algebra-typo-…-2e58` item** is not in this branch's ledger; it was imported after the branch point. `da38d358` resolves it. Please `vsect recheck` it as `landed` at merge.

## What a checker who didn't write this should verify

1. Read `#def-mismatch-signal` and the Setup of `#deriv-sector-condition`. Is it true that the dynamics' state is $\bar\delta$ and that the disturbance includes $-\alpha\nu$? Derive Kalman–Bucy's error SDE yourself.
2. Re-run `kb_check.py` below, or derive $(\sigma^2 + k^2 o^2)/(2k)$ from the OU stationary variance. Then check that "Two levers in $\mathcal T$" says only what that supports, and that nothing in the corrected segments still reads $\sigma_w$ as environment-only.
3. Check the sequential-RDF step in `#deriv-persistence-cost` against Tanaka et al. 2017 eq. (28), and the Duncan/Riccati identity. Re-run `srdf_kb_check.py`. The step most worth doubting is whether the discrete per-step sequential RDF divided by $\Delta$ is the right object for a continuous-time information rate. I believe it is (directed information rate), but I took the limit formally.
4. Re-run `example_kalman_numbers.py` against the new Lyapunov Bounds section of `#example-kalman`.
5. Read the A10 Findings block against the Widrow primary (relata `widrow-1976-stationary`). Ask whether the kept ASF parts are each true and each actually ASF's.
6. Look for places I missed that restate "faster correction always helps", the $1/\sqrt\alpha$ law as a property of the whole error, or "Kalman–Bucy saturates" in the old form. I grepped Part I and the term entries, but not Parts II–IV or the README partials beyond what `bin/refresh-all` regenerated.

## Scripts

Each runs with `python3 -I` and needs numpy (and scipy for the last).

### `kb_check.py`

```python
import numpy as np
rng = np.random.default_rng(1)
# scalar continuous time: dx = s dW (random walk), dy = x dt + o dV ; filter dxh = k (dy - xh dt)
s, o = 1.0, 0.5
dt = 1e-3
N = 400_000
M = 200  # parallel paths

def run(k):
    x = np.zeros(M); xh = np.zeros(M); acc = 0.0; cnt = 0
    innov_acc = 0.0
    for i in range(N):
        dW = rng.normal(0, np.sqrt(dt), M); dV = rng.normal(0, np.sqrt(dt), M)
        dy = x * dt + o * dV
        xh += k * (dy - xh * dt)
        x += s * dW
        if i > N // 10:
            acc += np.mean((x - xh) ** 2); cnt += 1
    return acc / cnt

kopt = s / o
for k in [0.5 * kopt, kopt, 2 * kopt, 4 * kopt]:
    mse = run(k)
    print(f"k={k:.2f} sim MSE={mse:.4f}  total-disturbance (s^2+k^2 o^2)/(2k)={(s*s+k*k*o*o)/(2*k):.4f}  env-only s^2/(2k)={s*s/(2*k):.4f}")
print("Kalman-Bucy P = s*o =", s * o)
```

### `srdf_kb_check.py`

```python
"""Check: Kalman-Bucy's information-supply rate (Duncan: P/(2 so^2)) equals the
continuous-time limit of the scalar Gauss-Markov sequential RDF
(Tanaka-Kim-Parrilo-Mitter 2017 eq. 28: 0.5*log(a^2 + W/D) per step) at D = P.
Signal dx = -lam x dt + s dW; observation dy = x dt + so dV."""
import numpy as np

for lam, s, so in [(0.0, 1.0, 0.5), (0.3, 1.0, 0.5), (1.0, 2.0, 0.3)]:
    # steady-state Riccati: s^2 - 2 lam P - P^2/so^2 = 0
    P = so**2 * (-lam + np.sqrt(lam**2 + s**2 / so**2))
    K = P / so**2
    duncan = P / (2 * so**2)
    cont = s**2 / (2 * P) - lam
    out = []
    for dt in [1e-2, 1e-3, 1e-4]:
        a = np.exp(-lam * dt)
        W = s**2 * dt if lam == 0 else s**2 * (1 - np.exp(-2 * lam * dt)) / (2 * lam)
        out.append(0.5 * np.log(a**2 + W / P) / dt)
    print(f"lam={lam} s={s} so={so}: P={P:.5f} K={K:.4f}  Duncan rate={duncan:.5f}  s^2/(2P)-lam={cont:.5f}  "
          f"discrete SRDF/dt (dt=1e-2,1e-3,1e-4)={[round(x,5) for x in out]}  K/2={K/2:.5f}")
```

### `example_kalman_numbers.py`

```python
"""Exact steady-state numbers for #example-kalman (scalar random walk q=0.25, r_H=1, r_L=9),
and the lag/noise trade-off of a fixed gain K: prior-error variance V(K) = (q + K^2 r)/(1-(1-K)^2).
Monte Carlo check of V(K) included."""
import numpy as np
from math import erf, sqrt
q = 0.25
for name, r in [("H", 1.0), ("L", 9.0)]:
    Pm = (q + np.sqrt(q * q + 4 * q * r)) / 2
    K = Pm / (Pm + r)
    P = K * r
    print(f"mode {name}: P^-={Pm:.4f} K_ss={K:.4f} P={P:.4f} rms(e+)={np.sqrt(P):.3f} rms(e-)={np.sqrt(Pm):.3f} rms(innov)={np.sqrt(Pm+r):.3f}")
r = 1.0
rng = np.random.default_rng(0)
for K in [0.15, 0.3904, 0.81]:
    V = (q + K * K * r) / (1 - (1 - K) ** 2)
    x = 0.0; xh = 0.0; acc = [];
    N = 400000
    v = rng.normal(0, sqrt(q), N); n = rng.normal(0, sqrt(r), N)
    for t in range(N):
        x += v[t]               # prior: x_t, xh is prior estimate
        e_prior = x - xh
        if t > 1000: acc.append(e_prior * e_prior)
        y = x + n[t]
        xh += K * (y - xh)
    print(f"K={K}: V(K) formula={V:.4f}  MC={np.mean(acc):.4f}")
sd = np.sqrt((q + np.sqrt(q * q + 4 * q * 1.0)) / 2)
z = 1.4 / sd
print("P(|e-|>1.4) =", 1 - erf(z / sqrt(2)))
```

### `rdf_check.py`

```python
"""Non-causal (Kolmogorov reverse water-filling) RDF of a scalar OU process,
dx = -lam x dt + s dW, spectrum S(f) = s^2 / (lam^2 + (2 pi f)^2), f in Hz.
Rate in nats/s: R = int_{S>th} 0.5 ln(S/th) df ; D = int min(th, S) df.
Compare R*D/s^2 against the segment's 1/4 and the closed form 2/pi^2 (high resolution),
and the sequential (causal) Gauss-Markov value 1/2 (R_c = s^2/(2D) - lam)."""
import numpy as np
from scipy import integrate, optimize

s, lam = 1.0, 0.01

def S(f):
    return s**2 / (lam**2 + (2*np.pi*f)**2)

def RD(th):
    # band where S > th: |f| < fc
    val = s**2/th - lam**2
    if val <= 0:
        return 0.0, s**2/(2*lam)
    fc = np.sqrt(val)/(2*np.pi)
    R = 2*integrate.quad(lambda f: 0.5*np.log(S(f)/th), 0, fc, limit=200)[0]
    D = 2*(th*fc + integrate.quad(S, fc, np.inf, limit=200)[0])
    return R, D

for th in [1e-2, 1e-3, 1e-4, 1e-5]:
    R, D = RD(th)
    print(f"th={th:g}  D={D:.5f}  R={R:.4f} nats/s  R*D/s^2={R*D/s**2:.4f}   (2/pi^2={2/np.pi**2:.4f}; segment 1/4; causal 1/2)")
```
