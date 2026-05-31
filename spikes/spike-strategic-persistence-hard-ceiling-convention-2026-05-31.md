# Spike: Is the strategic-persistence hard ceiling $\rho_\Sigma \ge R_\Sigma/2$ a convention artifact?

**Date:** 2026-05-31
**Origin:** AUDIT-WORKING-526815, finding F72 (surfaced in the gold-lift sweep, recorded in `#schema-strategy-persistence` Working Notes §3 "Off-ramp flag (load-bearing)").
**Target segments:** `#schema-strategy-persistence` (the ceiling claim) and `#deriv-strategic-persistence-hard-ceiling` (its appendix, `status: exact`).
**Upstream re-derived:** `#deriv-edge-credence-dynamics` (Prop B.1, Common Setup), `#hyp-edge-update-via-gain`, `#deriv-edge-update-natural-parameter`.
**Verdict:** **(B), strengthened** — the ceiling is *convention-dependent*; the strengthening is to name the forgetting-ordering convention as an explicit premise, supply AAT's own argument for why that convention is canonical, and state precisely the weaker bound that survives under the alternative.
**Status:** DRAFTED — pending external-eye gate. No canon edits.

> Settled by re-derived mathematics per `doc/spike-routing.md` §0, not by what the segment or NOTATION asserts.

---

## 1. The challenge (F72), stated precisely

`#schema-strategy-persistence`'s hard ceiling is:

$$\text{for } \rho_\Sigma \ge R_\Sigma/2,\ \text{no } \lambda \in [0,1)\ \text{satisfies the forgetting prerequisite}\quad\Longleftrightarrow\quad \sup_{\lambda}\alpha_\Sigma^{\text{ss}}(\lambda) = \tfrac12.$$

This rests entirely on the steady-state sector parameter

$$\alpha_\Sigma^{\text{ss}} = \frac{1-\lambda}{2-\lambda},$$

derived in `#deriv-strategic-persistence-hard-ceiling` Prop C.1 by substituting the discounted-update steady-state effective sample size $n_{\text{eff}} = 1/(1-\lambda)$ into the single-step conjugate gain $\alpha_\Sigma = 1/(n+1)$ from `#deriv-edge-credence-dynamics` Prop B.1.

F72's claim: under a *plausible alternative update-ordering convention*, the steady-state gain is instead $\alpha_\Sigma^{\text{ss}} = 1-\lambda$, whose supremum over $\lambda$ is $1$, not $\tfrac12$ — so the nontrivial hard ceiling at $\rho_\Sigma = R_\Sigma/2$ **dissolves** (it recedes to the trivial persistence bound $\rho_\Sigma \lt R_\Sigma$, which holds for any sub-unit gain).

The challenge is exactly the "are you *sure* you can't just …?" convention-audit a competent reader raises against an `exact`-status no-go with its own appendix. **Worked against the actual edge-update dynamics, it holds.**

## 2. The constitutive structure: AAT's edge update and its gain

From `#deriv-edge-credence-dynamics` (Common Setup) and `#hyp-edge-update-via-gain` (Formal Expression), the canonical AAT edge update is the **Beta-Bernoulli conjugate** update on pseudo-counts $(\alpha_k, \beta_k)$, $n_k = \alpha_k + \beta_k$, point estimate $\hat p_k = \alpha_k/n_k$:

$$\text{observe } y_k:\quad \alpha_k \mapsto \alpha_k + y_k,\quad \beta_k \mapsto \beta_k + (1-y_k),\qquad \Delta\hat p_k = \frac{y_k - \hat p_k}{n_k+1},\qquad \eta_k = \frac{1}{n_k+1}.$$

The gain $\eta_k = 1/(n_k+1)$ *is* the sector parameter $\alpha_\Sigma$ (Prop B.1, tight). The "$+1$" is exact and load-bearing: it is the increment the new observation makes to the total count, and the Beta posterior mean after one observation has denominator $n_k+1$.

So the entire convention question reduces to one quantity: **under exponential forgetting, what is the steady-state value of $n$ that enters the gain $1/(n+1)$?**

## 3. The forgetting recurrence has a real ordering ambiguity

The forgetting mechanism is introduced (segment §"Forgetting as Prerequisite", appendix Prop C.1 setup) to stabilize the otherwise-decaying gain. Three update rules are in play; the gain they produce differs, and the difference is genuine (numerically confirmed, `sim-forgetting-conventions.py`).

### Convention SEG — discount the prior pool, then add the current observation at full weight

This is the form the appendix states (Prop C.1):

$$\alpha_k \mapsto \lambda\,\alpha_k + y_k,\qquad \beta_k \mapsto \lambda\,\beta_k + (1-y_k)\quad\Longrightarrow\quad n \mapsto \lambda n + 1.$$

Fixed point $n_{\text{eff}} = 1/(1-\lambda)$. Gain:

$$\alpha_\Sigma^{\text{ss}} = \frac{1}{n_{\text{eff}}+1} = \frac{1}{1/(1-\lambda)+1} = \frac{1-\lambda}{2-\lambda}.\qquad\boxed{\sup_\lambda = \tfrac12\ \text{as}\ \lambda\to 0^+}$$

**Weight structure:** the current observation enters with weight $1$ (undiscounted); the observation $k$ steps ago carries weight $\lambda^k$. Total effective mass $= \sum_{k\ge 0}\lambda^k = 1/(1-\lambda)$, *including the current observation at full weight*.

### Convention ALT1 — add the current observation, then discount the whole pool

$$\alpha_k \mapsto \lambda(\alpha_k + y_k),\qquad \beta_k \mapsto \lambda(\beta_k + (1-y_k))\quad\Longrightarrow\quad n \mapsto \lambda(n+1).$$

Fixed point $n_{\text{eff}} = \lambda/(1-\lambda)$. Gain:

$$\alpha_\Sigma^{\text{ss}} = \frac{1}{n_{\text{eff}}+1} = \frac{1}{\lambda/(1-\lambda)+1} = \frac{1-\lambda}{(\lambda)+(1-\lambda)} = 1-\lambda.\qquad\boxed{\sup_\lambda = 1\ \text{as}\ \lambda\to 0^+}$$

**Weight structure:** the current observation is *also* discounted — it enters with weight $\lambda$; the observation $k$ steps ago carries weight $\lambda^{k+1}$. Total effective mass $= \lambda/(1-\lambda)$, *excluding* a full-weight current observation. This is the textbook RLS / discounted-least-squares forgetting-factor steady state and yields the classical EWMA gain $1-\lambda$.

### Convention EWMA — constant-gain estimate update (the other route to $1-\lambda$)

$$\hat p \mapsto \lambda\,\hat p + (1-\lambda)\,y\quad\Longrightarrow\quad \Delta\hat p = (1-\lambda)(y-\hat p),\qquad \alpha_\Sigma = 1-\lambda\ \text{(constant, from step 1)}.$$

This has no pseudo-count and no "$+1$"; the gain is constant in $\lambda$ and independent of experience.

## 4. Which convention does AAT actually commit to? (strengthen-first)

Per strengthen-first: before down-tiering, try to make the ceiling **robust** by showing AAT's dynamics uniquely commit to SEG. The attempt **partially succeeds** — strongly enough to make SEG canonical *within the schema's stated premise*, but not strongly enough to reduce the finding to landing (A).

### 4.1 The $\lambda\to 1$ (no-forgetting) reduction test

The discounted update must reduce to AAT's unforgotten conjugate update $\alpha_k \mathrel{+}= y_k$ when $\lambda = 1$ (no forgetting). Result (`sim-forgetting-conventions.py`):

| convention | $\lambda=1$ limit | reduces to AAT conjugate? | transient gain |
|---|---|---|---|
| **SEG** $(\alpha\mapsto\lambda\alpha+y)$ | $\alpha\mathrel{+}=y$ | **yes** | $1/(n+1)$, decays |
| **ALT1** $(\alpha\mapsto\lambda(\alpha+y))$ | $\alpha\mathrel{+}=y$ | **yes** | $1/(n+1)$, decays |
| **EWMA** $(\hat p\mapsto\lambda\hat p+(1-\lambda)y)$ | $\hat p\mapsto\hat p$ (no update) | **no** | constant $1-\lambda$ |

EWMA is *disqualified as "the discounted version of AAT's update"*: it does not reduce to the conjugate update and has no transient $1/(n+1)$ decay — it is a different estimator family (constant-gain). It falls outside the schema's premise (i) "Beta-Bernoulli edge dynamics." So the real contest is **SEG vs ALT1**, which differ only in whether the discount lands on $n$ or on $n+1$ at the increment step — i.e., *whether the current observation is discounted before or after it is incorporated.*

### 4.2 AAT's own coordinate commitment favors SEG

AAT's deepest commitment about the edge update is `#deriv-edge-update-natural-parameter`: edge credences live on the **log-odds coordinate**, on which independent Bernoulli evidence is *additive*,

$$\Lambda_{\text{post}} = \Lambda_{\text{prior}} + \ell(y),\qquad \ell(y) = \log\frac{P(y\mid H_1)}{P(y\mid H_0)},$$

where $\Lambda = \log(p/(1-p))$ is the accumulated log-odds, forced (up to positive affine) by the evidential-additivity axiom via Aczél's Cauchy-FE uniqueness theorem. The canonical *discounted* additive-evidence recursion in this coordinate is

$$\Lambda_{t+1} = \lambda\,\Lambda_t + \ell(y_{t+1}),$$

i.e. **discount accumulated log-evidence, admit the fresh log-likelihood-ratio at full weight.** Discounting $\ell(y_{t+1})$ itself (the ALT1 move) would assert that *the observation currently being processed arrives already partly forgotten* — there is no likelihood-ratio reading of that: $\ell(y)$ is the evidential content of *this* datum, defined independent of any forgetting mechanism. The full-weight-current / discounted-past structure is exactly SEG's weight structure (§3), and it gives $n_{\text{eff}} = 1/(1-\lambda)$.

**This is a real strengthening toward (A):** AAT's log-odds uniqueness theorem prefers SEG, the convention under which the ceiling holds. The strengthening does *not* fully close to (A) for two honest reasons:

1. **ALT1 is internally consistent and Bayesian-coherent on counts.** $\alpha\mapsto\lambda(\alpha+y)$ is a coherent discounted-Dirichlet/RLS update; it reduces correctly at $\lambda=1$; it is the standard form in much of the adaptive-control literature (the steady state $n_{\text{eff}} = \lambda/(1-\lambda)$ and gain $1-\lambda$ are textbook RLS-with-forgetting). One cannot call it *wrong* — only *not the coordinate-canonical choice for AAT*. The two coincide only at $\lambda=1$.
2. **The $(1-\lambda)/(2-\lambda)$ form itself comes from substituting $n_{\text{eff}}$ into the moment-parameter gain $1/(n+1)$** (appendix Prop C.1), not from the log-odds coordinate directly. The log-odds argument secures $n_{\text{eff}} = 1/(1-\lambda)$ (SEG), which *then* yields $(1-\lambda)/(2-\lambda)$ — so the canonicity argument supports the ceiling, but through the moment-parameter substitution the appendix already performs, and that substitution is what a skeptic targets.

### 4.3 The honest residue

Net: the ceiling is robust **within the premise "Beta-Bernoulli conjugate dynamics + discount-the-prior-pool (SEG) forgetting,"** and AAT's own additive-log-evidence axiom supplies a principled reason that premise is canonical. It is **not** robust against (a) the add-then-discount count timing (ALT1) — internally consistent, reduces correctly, textbook — nor (b) a constant-gain EWMA estimator (outside the conjugate premise). The forgetting-ordering convention is therefore a **genuine, currently-unstated premise** of the hard ceiling, not a derived consequence of AAT's prior commitments.

## 5. What survives under each convention (the precise scoping)

| convention | $n_{\text{eff}}$ | $\alpha_\Sigma^{\text{ss}}$ | $\sup_\lambda \alpha_\Sigma^{\text{ss}}$ | persistence reachable for | hard ceiling |
|---|---|---|---|---|---|
| **SEG** (discount prior, add current full-weight) | $1/(1-\lambda)$ | $\dfrac{1-\lambda}{2-\lambda}$ | $\tfrac12$ | $\rho_\Sigma \lt R_\Sigma/2$ | **at $\rho_\Sigma = R_\Sigma/2$ (holds)** |
| **ALT1** (add current, then discount pool) | $\lambda/(1-\lambda)$ | $1-\lambda$ | $1$ | $\rho_\Sigma \lt R_\Sigma$ | **dissolves** to the trivial bound $\rho_\Sigma \lt R_\Sigma$ |
| **EWMA** (constant-gain estimate) | — | $1-\lambda$ | $1$ | $\rho_\Sigma \lt R_\Sigma$ | dissolves (and outside conjugate premise) |

The CS-norm reading: this is **not** a weakening. A no-go theorem *with an explicit premise that names the convention under which it bites, plus the exact weaker bound that survives under the complement*, is strictly more useful and more honest than an unqualified "exact" no-go whose validity silently depends on an unstated ordering choice. The convention-scoped ceiling is a first-class result (`CLAUDE.md` "scope precision is valuable, not a weakness").

## 6. Proposed integration (DRAFTED — for the external-eye gate; no canon edits made)

### 6.1 `#deriv-strategic-persistence-hard-ceiling` (the appendix)

**(a) Add a named premise to the setup**, before Prop C.1, with the FORMAT `*[Definition]*`/`*[Assumption]*` tag:

> *[Assumption (full-weight-current forgetting convention)]*
> The discounted Beta-Bernoulli recurrence discounts the *prior accumulated* pseudo-counts and admits the *current* observation at full weight: $n \mapsto \lambda n + 1$, giving effective sample size $n_{\text{eff}} = 1/(1-\lambda)$ (current observation included at weight $1$; observation $k$ steps ago at weight $\lambda^k$). This is the convention forced by AAT's additive-log-evidence coordinate (`#deriv-edge-update-natural-parameter`): in log-odds the canonical discounted recursion is $\Lambda_{t+1} = \lambda\,\Lambda_t + \ell(y_{t+1})$ (writing $\Lambda$ for the accumulated log-odds) — accumulated log-evidence is discounted; the fresh log-likelihood-ratio $\ell(y_{t+1})$, being the evidential content of the datum currently processed, enters undiscounted. The alternative *add-then-discount* count timing $n \mapsto \lambda(n+1)$ (discounting the current observation too, the textbook RLS-with-forgetting steady state) gives $n_{\text{eff}} = \lambda/(1-\lambda)$ and $\alpha_\Sigma^{\text{ss}} = 1-\lambda$; under that timing the supremum gain is $1$ and the hard ceiling recedes to the trivial bound $\rho_\Sigma \lt R_\Sigma$. The ceiling at $\tfrac12$ is therefore a consequence of the full-weight-current convention.

**(b) Adjust Prop C.2's statement and Discussion** to carry the convention as an explicit hypothesis ("under the full-weight-current forgetting convention of the setup, …"), and add a Discussion paragraph stating the ALT1 alternative and the surviving bound — present truth, not history:

> **Convention dependence of the $\tfrac12$ cap.** The cap value is set by the forgetting-ordering convention. Under the full-weight-current convention (forced by `#deriv-edge-update-natural-parameter`), $\sup_\lambda \alpha_\Sigma^{\text{ss}} = \tfrac12$ and the reachable region is $\rho_\Sigma \lt R_\Sigma/2$. Under the add-then-discount convention, $\sup_\lambda \alpha_\Sigma^{\text{ss}} = 1$ and the reachable region widens to the trivial $\rho_\Sigma \lt R_\Sigma$. The two coincide only at $\lambda = 1$ (no forgetting), where both reduce to AAT's conjugate update. The nontrivial cap is the full-weight-current instance; AAT commits to that convention via its additive-log-evidence coordinate.

**(c) `status:` reconsideration (gate decision, not asserted here).** Prop C.1's algebra stays `exact` *given the convention*. The Finding's framing should make explicit that "exact" is exact-under-the-named-convention. Whether the segment `status:` should move from `exact` to `conditional` (it already lists conditions; the convention is a fourth) is a gate call — the cleanest reading is that the convention joins the existing "(i)–(iii) named conditions" list and the segment stays `exact` *under stated conditions*, since `exact` in AAT already means "validated under stated assumptions." Recommendation: keep `exact`, add the convention to the condition list, do **not** down-tier (down-tiering an algebraically-exact result for surfacing one more premise would be the category error `CLAUDE.md` "integration is replacement" warns against).

### 6.2 `#schema-strategy-persistence` (the schema)

- In §"Forgetting as Prerequisite" and the Epistemic Status, attach the convention to the $n_{\text{eff}} = 1/(1-\lambda)$ step and the ceiling claim (one clause: "under the full-weight-current forgetting convention — `#deriv-edge-update-natural-parameter`; see `#deriv-strategic-persistence-hard-ceiling` setup").
- The Findings "Brief"/"Impact" mention of the $\tfrac12$ ceiling should carry the same one-clause scope so the auto-extracted `FINDINGS.md` catalog states present truth (convention-scoped), not an unqualified universal.
- Working Notes §3 off-ramp flag (F72) can be marked resolved with a pointer to this spike and the verdict (B).

### 6.3 No new segment needed

The convention statement folds into the existing appendix setup; no separate segment. (Contrast the sibling F127/F128 spike, which needed a new no-go segment — here the no-go already exists and only needs its premise named.)

## 7. Confidence and unresolved

- **Confidence the ceiling is convention-dependent (verdict B): high.** The two count recursions $n\mapsto\lambda n+1$ and $n\mapsto\lambda(n+1)$ are elementary, both reduce to AAT's conjugate update at $\lambda=1$, and give $\sup_\lambda$ of $\tfrac12$ vs $1$ respectively (re-derived by hand and numerically). This is not a subtlety that resolves on closer reading; it is a real modeling choice.
- **Confidence SEG is AAT-canonical (the strengthening toward A): moderate-high.** The additive-log-evidence argument (discount accumulated evidence, admit fresh $\ell(y)$ at full weight) is principled and ties to `#deriv-edge-update-natural-parameter`, an existing AAT commitment. It is an argument from the natural coordinate, not a forced identity; a reviewer could still prefer the RLS timing on different grounds. Hence (B)-strengthened rather than (A).
- **Unresolved / candidate follow-ups:**
  1. **A stochastic-noise interaction.** The segment's Working Notes already flag $\rho_\Sigma/\sqrt{\mathcal T_\Sigma}$ vs $\rho_\Sigma/\mathcal T_\Sigma$ for the stochastic case. Whether the convention choice interacts with the stochastic ultimate-bound (Prop B.1's $O(1/\sqrt n)$ floor) under forgetting is not worked here.
  2. **NeurIPS Paper 2 $\mathcal A_{\text{decay}}$ lift.** The appendix cross-references the gain-decay-class theorem. That class-level result should be checked for the same convention sensitivity — does the bidirectional-threshold claim for finite-gain mechanisms assume full-weight-current? (Likely yes, since constant-step / sliding-window mechanisms are closer to ALT1/EWMA; flagged for the Paper-2 owner.)
  3. **Is there a convention-free invariant?** The product $n_{\text{eff}}\cdot(\text{current-obs weight})$ or the half-life $\log 2/\log(1/\lambda)$ might give a convention-robust restatement of "how much memory" — a possible strengthening that states the persistence threshold in a quantity invariant to the timing choice. Not attempted; candidate for a future pass.

## Appendix: simulation

`sim-forgetting-conventions.py` (this dir) reproduces, to steady state: SEG $\to (1-\lambda)/(2-\lambda)$, ALT1 $\to 1-\lambda$, EWMA $\to 1-\lambda$; the $\lambda=1$ reduction test; and the weight-structure decomposition (full-weight vs discounted current observation).
