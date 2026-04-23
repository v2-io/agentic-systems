# Spike: G-BP1 Logit / Natural-Parameter Reparameterization — Scoping and Strengthen-First

**Date:** 2026-04-22
**Trigger:** Joseph asked for a scoping spike + strengthen-first attempt on architectural proposal G-BP1 (see `msc/architectural-proposals-2026-04-22.md` §G-BP1), combined with deciding what to do about Gemini Finding 2 (the unbounded-gradient mechanical break in `#credit-assignment-boundary`; see `msc/pending-findings-2026-04-22.md` §Finding 2).
**Posture:** Strengthen first, attempt the improbable, characterize scope honestly.

---

## 1. The question

Can log-odds / natural-parameter reparameterization for edge credences in AAD's strategy DAG be derived as *uniquely forced* by an AAD-internal principle — as opposed to canonical-on-convergent-grounds or merely useful for fixing the Finding 2 mechanical break?

Five candidate paths (Paths A–D for strengthening attempts, Path E for honest failure). The target outcome is one of:
- **A**: a uniqueness theorem is available (analog to the reverse-KL uniqueness result under the chain-rule additivity axiom),
- **B**: canonical-not-unique, on several convergent grounds that together select log-odds without forcing it,
- **C**: no principle selects log-odds over other parameterizations; the choice is purely operational.

Parallel secondary question: what scope in `01-aad-core/src/` is touched by G-BP1, and is that scope narrow enough to execute partially, or wide enough to require a full portfolio commitment first?

---

## 2. Deliverable 1 — Scope characterization

For each segment identified in the G-BP1 proposal, the scope assessment below reflects reading the current text.

### `#strategy-dag` — edge/leaf credence representation

**Change under G-BP1.** The primary change is a representational note: `p_{ij}` is the *probability-space* presentation of edge credence; the *update-space* presentation is the log-odds `λ_{ij} = log(p_{ij}/(1-p_{ij}))`. The AND/OR propagation formulas remain in probability space because multiplicative combination is the Beta-Bernoulli-consistent rule.

**Scope.** Minor touch. One paragraph added (interface convention), no derivation redo. The Correlation Hierarchy (L0/L1/L1'/L2) is parameterization-agnostic. Prop B.6 three-way gating and Prop B.7 five-way gating are stated in terms of Beta-Bernoulli gains `1/(n+1)`, which is exactly the moment-parameter presentation; the log-odds presentation gives the same gains but via different surface algebra.

### `#edge-update-via-gain` — update rule in natural parameters

**Change under G-BP1.** The update rule restates as: "The update rule operates additively in log-odds; the probability-space form `p_{ij}^{\text{new}} = p_{ij} + η · (signal − p_{ij})` is the projected image of the log-odds gradient step." The Beta-Bernoulli gain `1/(n+1)` is the moment-parameter presentation of the natural-parameter update.

**Scope.** Minor touch. Beta-Bernoulli content unchanged; add a parallel log-odds statement and a cross-ref to the new appendix (§4 of this spike, landed as `#edge-update-natural-parameter`).

### `#credit-assignment-boundary` — signal function in ℝ (this is where Finding 2 lives)

**Change under G-BP1.** This is the segment where Finding 2's mechanical break lives. The default signal function:

```
signal_k(o_t) = p_k + ι_k · J_k · (y_G − P̂_Σ) / ‖J‖²
```

can produce unbounded signals when `‖J‖² → 0`, pushing `p_k` outside `[0, 1]`. Under G-BP1, the update lives in log-odds space where the same correction term produces a bounded update:

```
λ_k^{new} = λ_k + η · ι_k · J_k · (y_G − P̂_Σ) / ‖J‖²
```

The domain is `ℝ`, so no clipping is needed even when `‖J‖² → 0` (the update magnitude grows, but it cannot escape the domain). Converting back via `p_k = σ(λ_k)` gives a bounded probability.

**Scope.** Substantive touch. The mechanical fix to Finding 2 is a log-odds presentation of the same signal function, which is cleaner than "restore normalization constant + clip" because it eliminates the `[0,1]` escape by construction rather than by bookkeeping.

### `#strategic-dynamics-derivation` — Props B.1–B.7 restatement

**Change under G-BP1.** The propositions use expected-value sector-condition analysis on `δ_k = p̂_k − θ_k`. Under log-odds reparameterization, `δ^λ_k = λ̂_k − λ_k^\ast`. The expected-correction algebra is isomorphic:

- In probability space: `E[Δp̂_k] = −δ_k / (n_k + 1)` — linear in `δ`, `α_Σ = 1/(n+1)` tight.
- In log-odds space: `E[Δλ̂_k] ≈ −p(1-p) · δ^λ_k` near truth — linear in `δ^λ` with `α^λ = p(1-p) · η`.

The log-odds version is less algebraically tight near Bernoulli boundaries (where `p(1-p) → 0`), but the sector parameter remains positive globally. In probability space the sector parameter is also positive globally (by direct Beta-Bernoulli algebra); this is a well-known consequence of Beta being the conjugate prior — Beta-Bernoulli is an exponential family whose natural parameter is log-odds and whose canonical sector structure is identical in either coordinate (§5.6 of `msc/spike-gain-sector-bridge-nonlinear.md`).

**Scope.** No re-derivation required for Props B.1–B.7. The sector parameters are invariant-on-Beta-Bernoulli: the probability-space statement and the log-odds-space statement both derive from the same underlying Fisher-information argument, and the moment-parameter algebra `E[Δp̂] = −δ/(n+1)` is cleaner for pedagogy. **Conclusion: Props B.1–B.7 stay in probability-space form; the segment gains a short note that the derivation is Fisher-equivalent to a natural-parameter-space analysis.**

Prop B.5d (gradient-based attribution) is already the probability-space image of a log-odds gradient update; no change.

The O-BP14 derivation-audit table row for B.5d can stay as-is; the underlying derivation is parameterization-agnostic.

### `#agent-model` — possible extension if $M_t$ parameters are treated similarly

**Change under G-BP1.** Discussion-level parallel. If `M_t` holds Bernoulli / categorical parameters, the same log-odds / softmax-natural-parameter reparameterization applies. For Gaussian `M_t` (Kalman), natural parameters are already linear in the mean, so no reparameterization is needed.

**Scope.** No edit required. The segment is formulation-level; the natural-parameter move is orthogonal to the formulation.

### `#worked-example-kalman` — Kalman tracking

**Change under G-BP1.** None. Kalman works in Gaussian natural parameters already (mean and precision are linear in natural parameters of the Gaussian exponential family). Log-odds is Bernoulli-specific.

**Scope.** No edit.

### `#worked-example-bandit` — Beta-Bernoulli bandit

**Change under G-BP1.** The bandit worked example already uses Beta-Bernoulli in moment parameters. Could add a parallel log-odds presentation. Low value — the moment-parameter form is more familiar to RL readers.

**Scope.** Optional parallel note. Not required for G-BP1 execution.

### `#worked-example-strategy` — strategy DAG bandit

**Change under G-BP1.** Same as `#worked-example-bandit`. The strategy-level machinery is already stated in moment parameters; log-odds adds nothing to the pedagogy.

**Scope.** No edit required.

### `#worked-example-L1` — L1 augmented DAG

**Change under G-BP1.** No edit — worked example is parameterization-agnostic.

**Scope.** No edit.

### Hidden interactions

**A2' $\alpha$/$\beta$ sub-scope partition** (`msc/spike-a2-prime-strengthening.md`). Log-odds reparameterization does **not** shift agents between sub-scopes. In probability space, Beta-Bernoulli is already in sub-scope $\alpha$ (B1 holds by Bayesian coherence). In log-odds space, Beta-Bernoulli is in sub-scope $\alpha$ because it is an exponential family in its natural parameter with `Fisher = p(1-p) > 0` globally in the interior. The same agent class occupies sub-scope $\alpha$ in both parameterizations; the sector parameter differs by a factor of `p(1-p) / 1` (i.e., log-odds is locally "tighter" at `p ≈ 1/2` and "looser" at the boundaries). **No partition shift.**

**Prop B.7 five-way gating** (componentwise conditional-branch update requirement). Prop B.7 splits the DAG into conditional sub-DAGs `P_Σ(G | C)` and `P_Σ(G | ¬C)`. Under log-odds reparameterization, each conditional credence `p_{j|C}`, `p_{j|¬C}` becomes `λ_{j|C}`, `λ_{j|¬C}`. Componentwise updates remain componentwise (each conditional is updated on trials where that conditional is active). The Cramér-Rao refutation under unobservable `C` is an observational-channel argument, not a parameterization argument, and still holds. **No conflict.**

**B1 directional fidelity preservation.** In log-odds space, `F(δ^λ) = η · p(1-p) · δ^λ` (near truth). Since `p(1-p) > 0` on the interior `(0,1)`, directional fidelity holds globally in `ℝ`. In probability space, `F(δ) = δ/(n+1)` also globally satisfies directional fidelity. **Both parameterizations preserve B1.**

### Scope summary

| Segment | Scope |
|---|---|
| `#strategy-dag` | Minor touch (one paragraph) |
| `#edge-update-via-gain` | Minor touch (parallel log-odds statement) |
| `#credit-assignment-boundary` | **Substantive**: Finding 2 fix via log-odds signal function |
| `#strategic-dynamics-derivation` | **No edit required** (Fisher-equivalent; moment-parameter form is cleaner) |
| `#agent-model` | No edit |
| `#worked-example-*` (4 examples) | No edit required |

**Scope verdict: NARROW.** The substantive work is localized to `#credit-assignment-boundary`. All other segments either need a one-paragraph parallel presentation or no change. The log-odds appendix segment (§4 below) lands the strengthening theorem and interface convention; the existing Props B.1–B.7 derivations do not require restatement because the sector-parameter content is invariant to the choice of Beta-Bernoulli coordinate.

---

## 3. Deliverable 2 — Strengthening attempt

### Path A — Exponential family canonical

**Claim to test.** Beta-Bernoulli is an exponential family; its canonical / natural parameter is log-odds. If AAD internally requires "updates live in the exponential-family natural-parameter space," then log-odds is forced.

**Check.** AAD does **not** internally require this principle. `#edge-update-via-gain` states the Beta-Bernoulli update in moment parameters; it does not cite an exponential-family-canonicalness axiom. Adding such a principle would be a new commitment.

**Convergent evidence.** Path A supplies one convergent motivation: exponential-family natural parameters are the coordinate in which log-likelihood is globally convex (the log-partition function `A(λ) = log(1 + e^λ)` is strictly convex in `λ`) and in which the information geometry uses the e-connection as its canonical flat connection (Amari 1985, 1998). In the probability-space / moment-parameter coordinate, the same log-likelihood has singular curvature at `p ∈ {0, 1}`, which is the mechanism by which the Finding 2 mechanical break arises.

**Verdict.** Path A gives a *convergent* argument, not a uniqueness theorem. Log-odds is canonical within the exponential-family lineage, but AAD is not committed to exponential-family naturalness as a load-bearing axiom.

### Path B — Additive-decomposition parallel to reverse-KL (strengthening succeeds)

**Claim to test.** The reverse-KL uniqueness theorem in `#strategy-cost-regret-bound` §6.1 was forced by the chain-rule additivity axiom — the divergence-level analog of `#chain-confidence-decay`'s additive log-confidence decomposition along causal chains. A parallel axiom at the update level: *independent evidence updates credence additively*. Is there a theorem forcing log-odds as the unique parameterization on which Bayesian independent evidence accumulates additively?

**Setup.** Let `ψ : (0, 1) → ℝ` be a smooth, strictly monotone reparameterization of Bernoulli credence `p`. Consider a sequence of independent Bernoulli observations `y_1, …, y_n` from a channel with likelihood `P(y | H_1) / P(y | H_0)`. Suppose the posterior update takes the form:

```
ψ(p_post) = ψ(p_prior) + g(y)
```

for some function `g : {0, 1} → ℝ` *independent* of `p_prior` and of observation history.

**Theorem (evidential-additivity uniqueness of log-odds).** The functional equation above admits solutions if and only if `ψ(p) = c · log(p / (1 − p)) + d` for some constants `c > 0`, `d ∈ ℝ`, and `g(y) = c · ℓ(y)` where `ℓ(y) = log[P(y | H_1) / P(y | H_0)]` is the log-likelihood ratio.

**Proof.** By Bayes' theorem applied to binary hypotheses:

```
p_post / (1 − p_post) = [p_prior / (1 − p_prior)] · [P(y | H_1) / P(y | H_0)]
```

Taking logarithm of both sides:

```
h(p_post) = h(p_prior) + ℓ(y), where h(p) := log(p / (1 − p))
```

Thus `h` satisfies the additive update identity with `g(y) = ℓ(y)`.

For any other monotone `ψ` to satisfy `ψ(p_post) − ψ(p_prior) = g(y)` for all `p_prior ∈ (0, 1)` and all `y ∈ {0, 1}` with `g` independent of `p_prior`, the difference `ψ(p_post) − ψ(p_prior)` must depend only on the Bayesian mapping `p_prior ↦ p_post` (which is fully determined by `y` through the likelihood ratio). Under the Bayesian mapping, `h(p_post) − h(p_prior) = ℓ(y)` holds as an identity. If `ψ satisfies the additive form` too, then

```
ψ(p_post) − ψ(p_prior) = g(y) = G(ℓ(y))
```

for some function `G`. Changing variables via `λ = h(p)`, let `Ψ(λ) := ψ(σ(λ))` (where `σ` is the sigmoid); then `Ψ(λ + ℓ) − Ψ(λ) = G(ℓ)` for all `λ ∈ ℝ` and all `ℓ ∈ ℝ` (extending to continuous evidence). By the Cauchy functional equation with continuity, `Ψ(λ) = c · λ + d` for some `c ≠ 0`, `d`. Monotonicity of `ψ` forces `c > 0`. Thus `ψ(p) = c · h(p) + d`. □

**AAD-internal motivation for the evidential-additivity axiom.** Three layers of additive decomposition are now load-bearing in AAD:

1. **Chain level** ( #chain-confidence-decay): confidence along causal chains decomposes additively in log-scale: `log P(chain) = Σ log P(E_i | E_{<i})`.
2. **Divergence level** ( #strategy-cost-regret-bound §6.1): mismatch between `π^\ast` and `Q_{Σ_t}` decomposes additively across the DAG's causal layers along the optimal trajectory (chain-rule additivity of reverse-KL).
3. **Update level** (this spike): evidence accumulation along the same causal structure decomposes additively on the log-odds scale — log-likelihood ratios add for independent evidence.

The three are structurally the same move. Picking log-odds for edge credences is the update-level instance of the chain-level and divergence-level principles AAD has already committed to.

**Verdict.** Path B yields a genuine uniqueness theorem — within the stated axiom scope. The axiom ("independent evidence updates credence additively in some fixed coordinate") is AAD-internally motivated as the update-level analog of `#chain-confidence-decay`. Without the axiom, the uniqueness claim weakens to canonical-not-unique. With the axiom, log-odds is forced.

**Scope of the axiom.** The evidential-additivity axiom applies to agent classes that treat evidence as independent likelihood evidence — the Bayesian-coherent subclass of AAD. Non-Bayesian agents (PID controllers, rule-based systems) do not invoke likelihood ratios and are out of scope for the axiom. This matches the sub-scope $\alpha$ / sub-scope $\beta$ partition of `#gain-sector-bridge` / `msc/spike-a2-prime-strengthening.md`: the uniqueness applies within sub-scope $\alpha$ (where B1 is already derived from Bayesian coherence).

### Path C — Fisher / natural gradient

**Claim to test.** Natural gradient descent on a Fisher-information manifold picks the natural-parameter coordinate. If AAD commits to natural gradient, log-odds is forced (for Bernoulli edges).

**Check.** AAD does not currently commit to natural gradient. G-BP3 (Fisher unification, separate proposal) would add this commitment. Path C therefore requires G-BP3 first.

**Verdict.** Path C is valid but conditional on G-BP3. Within the current axiom set, it is not standalone.

### Path D — Sector-condition preservation

**Claim to test.** Does log-odds reparameterization preserve or enable directional fidelity more robustly than probability-space parameterization?

**Check.** In log-odds `λ = log(p / (1 − p))`, the Bernoulli log-likelihood gradient is `n(p̄ − p(λ))` where `p̄` is the sample mean. The Hessian is `−n · p(1 − p) < 0` (log-likelihood concave), equivalently `+n · p(1 − p) > 0` for the negative-log-likelihood. Since `p(1 − p) ∈ (0, 1/4]` on `(0, 1)`, this is strictly positive interior — giving globally strong convexity of `−ℓ` on the log-odds interior. In probability space, the Fisher information in `p` is `n / [p(1 − p)]`, which blows up at boundaries and is well-behaved only on the interior.

**Operational consequence.** Gradient updates in log-odds cannot escape the representable domain (`ℝ` is unbounded); gradient updates in probability space can escape `[0, 1]` when the update magnitude exceeds `min(p, 1 − p)`. This is exactly Finding 2's mechanical break.

**Verdict.** Path D gives an operational selection argument — log-odds is the parameterization on which the continuous-gradient update is well-defined globally. This is not a uniqueness theorem; it is a well-posedness argument. Other parameterizations exist on which gradient updates are also well-defined (e.g., `arcsin(2p − 1)` also maps to an unbounded domain), but log-odds is the unique one that is *simultaneously* well-posed, exponential-family-canonical (Path A), and evidential-additivity-forced (Path B).

### Path E — Honest failure / outcome B

If none of Paths A–D gave a principled uniqueness result, the honest outcome would be: "log-odds is canonical-not-unique, on four convergent grounds (exponential family, Fisher/natural-gradient, sector-condition domain-well-posedness, and evidence accumulation)." Each is a selection criterion; none alone is a uniqueness theorem.

### Outcome declaration

**Outcome A (uniqueness found) — under the evidential-additivity axiom.** Path B's theorem is tight: on the axiom "independent Bernoulli evidence updates credence additively in some fixed coordinate," log-odds is the unique choice up to positive affine transformation. The axiom is AAD-internally motivated as the update-level analog of `#chain-confidence-decay`'s chain-level additive log-confidence decomposition and `#strategy-cost-regret-bound` §6.1's divergence-level chain-rule additivity. Without the axiom, the selection weakens to Outcome B.

**Outcome B (canonical-not-unique) — outside the axiom.** Paths A, C, D supply three additional convergent grounds: exponential-family naturalness, Fisher/natural-gradient canonicity, and domain-well-posedness of the continuous gradient. Each is a selection criterion; together they strongly recommend log-odds, but none alone forces it.

**Recommendation.** Land Path B's theorem in an appendix segment with the evidential-additivity axiom explicitly named. The resulting epistemic status is *Derived (conditional on evidential-additivity axiom)* — the same shape as the reverse-KL uniqueness result in `#strategy-cost-regret-bound` §6.1.

---

## 4. Deliverable 3 — Action recommendation

**Given scope is narrow (§2) + strengthening yields a real theorem (§3, Path B), the recommended action is:**

### 4.1 Land the strengthening theorem as a new appendix segment

New segment `01-aad-core/src/edge-update-natural-parameter.md` carries the Path B theorem, the evidential-additivity axiom statement, and the three-layer-of-additivity parallel (chain / divergence / update). Status: *Derived (conditional on evidential-additivity axiom)*, mirroring the reverse-KL uniqueness result.

### 4.2 Apply the Finding 2 local fix in `#credit-assignment-boundary` using log-odds presentation

The default signal function is restated in log-odds. The probability-space surface form stays as the projected image for readability. Normalization and clipping are no longer needed because the update lives in `ℝ`.

### 4.3 Add interface notes

- `#strategy-dag`: one paragraph noting `λ_{ij} = log(p_{ij}/(1-p_{ij}))` as the natural-parameter presentation, with pointer to the new appendix.
- `#edge-update-via-gain`: parallel log-odds statement of the update rule alongside the moment-parameter form.
- `#strategic-dynamics-derivation`: a single line noting that Props B.1–B.7 are Fisher-equivalent in either parameterization.

### 4.4 What is NOT recommended

- Full restatement of Props B.1–B.7 in log-odds. The moment-parameter form is pedagogically cleaner and algebraically tight for Beta-Bernoulli. Restating in log-odds would complicate the exposition without changing the content.
- Reworking `#worked-example-*` segments. The worked examples are parameterization-agnostic at the level they operate.
- Executing the full G-BP1 architectural sweep. The scoping shows it is narrow; full execution would be motivated by G-BP3 (Fisher unification) as the natural companion, not by Finding 2.

### 4.5 Cascading findings for adjacent segments

- **F2 resolved.** Finding 2 closes with the log-odds local fix — not by "restore normalization + clip" but by the cleaner move of parameterizing in the domain where the mechanical break cannot occur.
- **A2' $\alpha$/$\beta$ partition unchanged** (§2 interactions). Log-odds does not shift any agent between sub-scopes.
- **Prop B.7 five-way gating unaffected** (§2 interactions). The conditional-branch componentwise structure and Cramér-Rao refutation are parameterization-agnostic.
- **Prop B.5d gradient attribution** — the probability-space image of the log-odds gradient update, already correctly derived. No change.
- **`#discussion-identifiability-floor`** is unaffected. The no-go results are information-theoretic, not parameterization-dependent.

---

## 5. Summary

| Question | Answer |
|---|---|
| Is G-BP1's scope narrow enough to execute partially? | Yes — substantive work localized to `#credit-assignment-boundary`. |
| Is there an AAD-internal uniqueness principle for log-odds? | Yes — evidential-additivity axiom (Path B). Parallel to reverse-KL §6.1 chain-rule axiom. |
| Does Finding 2's local fix require clipping / normalization? | No — log-odds presentation eliminates the mechanical break by construction. |
| Does log-odds reparameterization shift A2' $\alpha$/$\beta$ sub-scope membership? | No. Same agent class occupies sub-scope $\alpha$ in both parameterizations. |
| Does it interact with Prop B.7 five-way gating or the Cramér-Rao refutation? | No. Both are parameterization-agnostic. |
| Outcome tier | A (uniqueness-under-axiom) for Path B; B (canonical-not-unique) without the axiom. The axiom is AAD-internally motivated as the update-level analog of #chain-confidence-decay. |

The framework stands complete without `msc/`: the strengthening lands in `#edge-update-natural-parameter` (new appendix), the fix lands in `#credit-assignment-boundary`, and the interface notes land in `#strategy-dag` and `#edge-update-via-gain`.
