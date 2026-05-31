# Spike: Value-Object Convention Monotonicity + $Q_O$ Causal Validity — strengthen-first verdict

**Date:** 2026-05-30
**Type:** strengthen-first / challenged-`exact`-claim
**Segment under challenge:** `01-aat-core/src/def-value-object.md` (`status: exact`, `stage: deps-verified`)
**Trigger:** A deeply-mathematical de-novo auditor (AUDIT-WORKING-526815) raised two distinct objections to the segment's `exact` status, both recorded in the segment's `## Working Notes` "Follow-up items" and in the raw note `audits/AUDIT-WORKING-526815/.integrated/40-def-value-object.md`:

1. **Front 1 — the C2 (receding-horizon) monotonicity rung.** The claimed ordering $A_O^{(1)} \leq A_O^{\text{RH}}$ (one-step $\leq$ receding-horizon) can fail: a myopic replanner over a shorter window $N_r \lt N_h$ can pick actions locally optimal over $N_r$ but worse over the full evaluated horizon $N_h$ than continuing $\pi_{\text{current}}$.
2. **Front 2 — the causal-validity claim.** Establishing the $do(\cdot)$-validity of $Q_O$ may require $M_t$ to *identify the action-transition causal structure*, not merely predictive sufficiency ( #def-model-sufficiency) plus directed separation ( #der-directed-separation).

**Disposition:** This spike modifies no canon — no `*/src/*.md` body edits, no `status:` change. It draws the math to its conclusion and drafts the proposed per-segment integration *inside this document* for the external-eye review gate. The two reproducibility scripts (`sim-rh-counterexample.py`, `sim-rh-strengthening.py`) accompany this verdict and are independently runnable.

---

## 0. Verdict at a glance

| Front | Landing | One-line |
|---|---|---|
| **Front 1 (C2 monotonicity rung)** | **(C) no-go on the rung as stated, wrapped in (B) a strengthened scoped theorem** | The left rung $A_O^{(1)} \leq A_O^{\text{RH}}$ is **false in general** for $N_r \lt N_h$ (explicit deterministic counterexample, numerically confirmed). It holds **exactly** under any one of three named, structurally-checkable consistency conditions (RH-1)/(RH-2)/(RH-3), each restoring it as a sharper scoped result. The **right rung $A_O^{\text{RH}} \leq A_O^{\text{B}}$ is and remains exact, unconditionally.** |
| **Front 2 ($Q_O$ causal validity)** | **(B) strengthening / scope-sharpening; consistent with the 2026-05-30 transportability spike** | The auditor is right: predictive sufficiency + directed separation give the interventional *query* and sever current-action and continuation confounding, but **identifying** $P(o \mid do(a), M_t)$ additionally needs (C1) positivity, (C2) sequential ignorability / no-unmodeled-confounder, (C3) known/identified action-transition mechanism. These are the *same* (C1)–(C3) the sibling spike lifted into `#der-loop-interventional-access`; `def-value-object` is one segment upstream and must gate consistently. The fix is to lift the identification conditions from the implicit "interventional interpretation correct but estimate may be biased" sentence into a first-class gating statement. |

**The headline framing (per `CLAUDE.md` *Math-novelty recognition* and *scope precision is valuable — the CS norm*):** neither front is a deflation of the segment. Front 1 produces a no-go theorem *plus* a three-condition characterization of exactly when the rung holds — a CS-grade scoped result (named hypotheses + explicit no-go for the complement) that is *stronger and more useful* than the unconditional claim it replaces. Front 2 lifts the segment to consistency with already-landed sibling machinery and makes the identification gate first-class instead of buried.

---

## Front 1 — the C2 receding-horizon monotonicity rung

### 1.1 What the segment claims and where the bug is

The segment's `### Monotonicity` block states, for fixed $M_t$, fixed policy class $\Pi$, fixed evaluated horizon $N_h$ (the explicit static-evaluation form):

$$A_O^{(1)}(M_t;\, \Pi, N_h) \;\leq\; A_O^{\text{RH}}(M_t;\, \Pi, N_r, N_h) \;\leq\; A_O^{\text{B}}(M_t;\, \Pi, N_h).$$

Its derivation reads (paraphrased): C1 freezes continuation at $\pi_{\text{current}}$; C2 re-optimizes periodically, so "$\pi_{\text{RH}} \succeq \pi_{\text{current}}$ at each future step, because C2 optimizes where C1 holds fixed"; C3 is globally optimal; a weakly-better continuation yields a weakly-higher value, so the chain follows.

**The right rung is sound.** $\pi^\ast = \arg\sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$ maximizes the full-horizon objective over $\Pi$ by definition, so *any* continuation drawn from $\Pi$ — including the receding-horizon continuation $\pi_{\text{RH}}$ — satisfies $V_O(M_t, \pi_{\text{RH}}; N_h) \leq V_O(M_t, \pi^\ast; N_h)$. Taking the supremum over the first action preserves this. The right rung is exact and needs no condition. (This is the "supremum over a larger set" argument, which is the part of the derivation that is correct.)

**The left rung contains the bug.** The load-bearing step "$\pi_{\text{RH}} \succeq \pi_{\text{current}}$ at each future step, because C2 optimizes" is *false as a statement about the full-horizon objective $V_O(\cdot; N_h)$*. C2 with a replanning window $N_r \lt N_h$ optimizes a **different, truncated objective** — the sum of stage values over the next $N_r$ steps (with whatever terminal treatment the window carries), not the full $N_h$-horizon objective on which $A_O$ is scored. "Optimizes" is true *of the truncated objective*; it does not deliver "$\succeq \pi_{\text{current}}$ on the full objective." The two coincide only under added structure. This is exactly the well-known fact in receding-horizon / model-predictive control that **a short-horizon MPC controller without a terminal cost or terminal constraint is not guaranteed to be monotone — or even stabilizing — and can be outperformed by a fixed baseline** (Rawlings, Mayne & Diehl, *Model Predictive Control: Theory, Computation, and Design*, 2nd ed., 2017, Ch. 2 on terminal-cost/terminal-set ingredients for stability; Grüne & Pannek, *Nonlinear Model Predictive Control*, 2nd ed., 2017, Ch. 6 on stability without terminal constraints and the role of the prediction horizon; Bertsekas, *Dynamic Programming and Optimal Control*, Vol. I, on limited-lookahead policies and rollout).

### 1.2 The counterexample (no-go on the rung as stated)

A deterministic finite-horizon MDP suffices. Evaluate continuations from a post-first-action state $x$, with full evaluated horizon $N_h = 2$ continuation steps and replanning window $N_r = 1$. Stage rewards are on transitions; $V_O$ is their sum over the evaluated horizon.

- At $x$, two admissible actions:
  - $g$ ("greedy"): immediate value $+1$, transitions to a dead state $D$ (value $0$ thereafter).
  - $p$ ("patient"): immediate value $0$, transitions to a high-value state $H$.
- At $H$: value $+10$ per step. At $D$: value $0$.
- $\pi_{\text{current}} =$ "patient at $x$" ($p$).

Then:

- **C1 (frozen $\pi_{\text{current}}$):** $0$ (step 1, via $p$) $+ 10$ (step 2, at $H$) $= 10$. So $A_O^{(1)} = 10$.
- **C2 ($N_r = 1$ replanning):** the one-step lookahead at $x$ prefers $g$ ($+1 \gt 0$), lands in $D$, collects $0$ at step 2. Full-horizon value $= 1 + 0 = 1$. So $A_O^{\text{RH}} = 1$.
- **C3 (Bellman over $N_h = 2$):** picks $p$, value $10$. So $A_O^{\text{B}} = 10$.

Hence $A_O^{(1)} = 10 \;\gt\; A_O^{\text{RH}} = 1$: **the left rung is violated.** The right rung ($1 \leq 10$) holds, as proved. Numerically confirmed in `sim-rh-counterexample.py`, which also confirms the control case $N_r = N_h$ restores the rung (then $A_O^{\text{RH}} = A_O^{\text{B}} = 10$). This is the classic "myopic trap": the short window optimizes a truncated objective whose order is *inverted* relative to the full objective ($+1$ now beats $+0$ now in the window, but $+0$ now $\to +10$ later beats $+1$ now $\to 0$ later on the full horizon).

The no-go is exact and non-pathological: it is a two-state, two-action, two-step instance, precisely the situation the segment's C2 row ("captures multi-step recovery: a goal that appears unattainable under frozen continuation may be reachable with replanning") is reaching for — and it shows the reaching cuts *both* ways unless the replanning objective is consistent with the evaluated objective.

### 1.3 The strengthening: exact conditions under which the left rung holds

The failure is *entirely* objective-mismatch. The left rung holds **exactly** when C2's per-step selection is an *order-consistent surrogate* for the full-horizon objective — i.e., for every reachable state, the action C2 commits has full-$N_h$-horizon value at least that of the action $\pi_{\text{current}}$ would take. Three named, structurally-checkable sufficient conditions force this; each is exact, and (RH-3) is the general one of which the others are instances.

**(RH-1) Horizon alignment: $N_r \geq N_h$.** The replanning window covers the whole evaluated horizon, so C2's per-step optimization *is* full-horizon optimization from each reached state. By Bellman's principle of optimality the receding-horizon continuation then equals the optimal continuation, giving $A_O^{\text{RH}} = A_O^{\text{B}} \geq A_O^{(1)}$. Exact. (Honest about its own degeneracy: when $N_r \geq N_h$, C2 collapses into C3 on the evaluated horizon — the rung holds because the distinction between C2 and C3 disappears. Useful as a boundary marker, not as the operative condition for genuine $N_r \lt N_h$ replanning.)

**(RH-2) Value-compared (improvement-checked) replanning — the operative one.** C2 commits the replanned action only if its full-horizon value is at least the value of continuing $\pi_{\text{current}}$; otherwise it keeps $\pi_{\text{current}}$. Formally, at each reachable state $s$ with $k$ steps remaining,

$$\pi_{\text{RH}}(s) \;:=\; \arg\max_{a \in \{a_{\text{replan}}(s),\; \pi_{\text{current}}(s)\}} \Big[\, r(s, a) + V_O\big(s'(s,a),\, \pi_{\text{current}};\, k-1\big) \,\Big],$$

i.e., each candidate first action is scored by *rollout under the base policy $\pi_{\text{current}}$* over the remaining full horizon. By construction $\pi_{\text{RH}}$ weakly dominates $\pi_{\text{current}}$ pointwise on the full objective, so $A_O^{(1)} \leq A_O^{\text{RH}}$. Exact. This is precisely **rollout / one-step policy improvement with base policy $\pi_{\text{current}}$** (Bertsekas, *Rollout, Policy Iteration, and Distributed Reinforcement Learning*, 2020; *DP & OC* Vol. I), whose defining guarantee is that rollout never underperforms its base policy. It is the natural AAT reading of C2-for-strategy-revision, since the cascade's purpose is *improvement over the current strategy* ( #der-orient-cascade step 4), and it makes the monotonicity a *consequence of the improvement guard* rather than an unconditional property of replanning.

**(RH-3) Terminal-cost / cost-to-go consistency — the general condition.** Equip the $N_r$-step replanning objective with a terminal value function $V_f$ at the truncation boundary satisfying both
$$V_f(s) \;\leq\; \max_{a} \big[\, r(s,a) + V_f(s') \,\big] \quad \text{(a control-Lyapunov / value-underestimator decrease inequality)},$$
$$V_f(s) \;\leq\; V_O\big(s,\, \pi_{\text{current}};\, \text{remaining horizon}\big) \quad \text{(the terminal cost lower-bounds the baseline tail)}.$$
The first inequality is the standard MPC ingredient that makes the truncated-with-terminal-cost optimization a valid surrogate for the full-horizon objective (a terminal cost that is a control-Lyapunov function makes the finite-horizon receding-horizon value monotone and bounds the closed-loop cost by the unconstrained optimum — Rawlings-Mayne-Diehl Ch. 2; Grüne-Pannek Ch. 5). The second ensures the surrogate never *undervalues the baseline tail*, so the replanner never trades the baseline away for a truncation artifact. Together they force order-consistency, giving $A_O^{(1)} \leq A_O^{\text{RH}}$. Exact. (RH-1) is the special case $V_f \equiv$ optimal tail with $N_r = N_h$; the value-function-on-the-baseline reading of (RH-2) is the special case $V_f = V_O(\cdot, \pi_{\text{current}}; \cdot)$.

**Unifying statement (the scoped theorem that replaces the unconditional rung):**

> **Convention-monotonicity (corrected).** For fixed $M_t$, $\Pi$, $N_h$, the right rung $A_O^{\text{RH}} \leq A_O^{\text{B}}$ holds unconditionally. The left rung $A_O^{(1)} \leq A_O^{\text{RH}}$ holds **iff** the receding-horizon replanning objective is an *order-consistent surrogate* for the full-horizon objective — for every reachable state, the action C2 selects has full-$N_h$-horizon value at least that of $\pi_{\text{current}}$'s action. Conditions (RH-1) $N_r \geq N_h$, (RH-2) value-compared/rollout guard, and (RH-3) a baseline-lower-bounding control-Lyapunov terminal cost each force order-consistency and are therefore each sufficient. Absent any such condition, the left rung is false (counterexample §1.2): unguarded short-horizon replanning can underperform the frozen current policy.

Both strengthening conditions are numerically confirmed on the §1.2 counterexample in `sim-rh-strengthening.py`: the naive $N_r = 1$ replanner gives value $1$ (rung fails), while both the (RH-2) value-compared guard and the (RH-3) baseline-lower-bounding terminal cost give value $10$ (rung restored).

### 1.4 What does *not* change

- **The right rung stays exact.** No condition needed.
- **The C1-default and the diagnostic direction are untouched.** C1 remains the most conservative diagnostic; the *capability-limit-vs-locally-stuck* reading is unaffected.
- **The corollary orderings ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$) inherit the same gate.** $\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$ and the reversed regret ordering hold to the same extent as the underlying $A_O$ ordering: the $\delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$ half (equivalently the regret half) is conditional on (RH-1/2/3); the $\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}}$ half is unconditional. `#def-satisfaction-gap` and `#def-control-regret` both recite the full three-term monotonicity and so inherit the correction (see §3.2).
- **`#der-orient-cascade` step 5c** ("convention escalation C1 $\to$ C2 $\to$ C3 may reveal recovery paths") is *consistent with* the corrected result — escalating to C2 reveals recovery paths *when C2 is run with a consistent (guarded/terminal-cost/aligned) objective*, which is the natural deployment reading; the cascade text says "evaluating under C2 ... may show $\delta_{\text{sat}}^{\text{RH}} \leq 0$", and "may" is already correct. A one-clause pointer that this presumes order-consistent replanning is the only ripple (see §3.3).

---

## Front 2 — the causal-validity claim for $Q_O$

### 2.1 What the segment claims

The segment's `**Causal validity of the value object**` paragraph argues that two mechanisms make $Q_O$ depend on $M_t$ alone as a state variable: (1) the $do$-operator severs current-action confounding ($G_t$'s influence on action choice is irrelevant because the action is intervened on); (2) the continuation policy is a fixed parameter, not a $G_t$-derived quantity. It then states: "The remaining requirement: $M_t$ must support the interventional query $P(o \mid do(a), M_t)$. Under directed separation ... this holds because $M_t$ updates independently of $G_t$ ..." and, in the Epistemic Status, calls the causal-validity claim "*conditional* on directed separation," with the closing sentence: "When $S(M_t) = 1$ and directed separation holds, $Q_O$ is causally valid. When $S(M_t) \lt 1$ or directed separation fails, the interventional interpretation is correct but the conditional estimate may be biased."

### 2.2 Why the auditor is right, and exactly how far

The auditor's contention — "$do(a)$ defines an interventional *query*, but *estimating/identifying* it requires $M_t$ to contain/identify the relevant action-transition causal structure; observational predictive sufficiency plus goal-blind processing do not by themselves guarantee valid interventional expectations" — is correct, and it is the **same structural fact** the 2026-05-30 transportability spike (`spike-causal-access-transportability-2026-05-30.md`) established from the primary sources one segment downstream at `#der-loop-interventional-access`. There is no need to re-litigate the imported machinery; the job here is to make `def-value-object` gate *consistently* with that already-drafted integration.

The precise decomposition (reading CHT Defs 4–5 as the sibling spike did):

- **What mechanisms (1) and (2) genuinely buy.** Severing current-action confounding via $do$ and fixing $\pi_{\text{cont}}$ as a parameter make $Q_O$ a *well-defined interventional query* whose value depends on $M_t$ (the model) and the fixed parameters $O_t, \pi_{\text{cont}}, N_h$ — *not* on $G_t$ through action selection or continuation. This part of the argument is **correct and survives intact.** It is a statement about the *query's well-definedness and $G_t$-independence*, and directed separation is exactly what it needs.
- **What it does not buy.** $G_t$-independence of the query is *not* the same as *identifiability of the interventional expectation from $M_t$*. The interventional distribution is, by CHT Def 5, defined over the model's exogenous distribution; computing $\mathbb{E}[V_{O_t}(\tau) \mid M_t, do(a), \ldots]$ correctly requires that $M_t$ encode (or identify) the **action-transition causal mechanism** $P(o \mid do(a))$, not merely an associational predictor $P(o \mid a)$ that is a sufficient statistic for *observed* futures. Predictive sufficiency ( #def-model-sufficiency, $S(M_t) = 1$) is a Level-1 property — the segment *already says this* ("predictive sufficiency is a Level 1 (associational) property") — and `#def-model-sufficiency` itself flags that the causal validity "requires an additional condition: that $M_t$ satisfies the backdoor criterion with respect to the agent's actions (see #def-value-object)." So `def-model-sufficiency` already *forwards the obligation to this segment*, and this segment currently discharges it only in the soft "estimate may be biased" sentence.

The honest condition set, named (matching the sibling spike's (C1)–(C3) so the chapter gates consistently):

- **(C1) Positivity / overlap:** every action $a$ under consideration has support under the data-generating process the model was estimated from (else the interventional expectation is not estimable from $M_t$ regardless of structure).
- **(C2) Sequential ignorability / no unmodeled confounder:** no unmodeled common cause affects both the outcome and the agent's epistemic processing / action selection through paths not captured in $M_t$ — i.e., the backdoor condition `#def-model-sufficiency` already names. Directed separation is what *delivers* (C2) on the *epistemic-processing* side (goal-blind $f_M$ blocks the $G_t \to f_M \to M^+$ confounding path); it does **not** by itself deliver (C2) on the *environment* side (latent environment confounders bypassing $M_t$).
- **(C3) Known / identified action-transition mechanism:** $M_t$ must encode $P(o \mid do(a))$, not merely $P(o \mid a)$ — the action-transition structure is in the model (this is `#def-action-transition`, already a `def-model-sufficiency` dependency), either by construction (the agent's model class represents it) or by identification from interventional data ( #der-loop-interventional-access supplies the channel under its own (C1)–(C3)).

The corrected reading: **directed separation is necessary but not sufficient for causal validity.** It secures the *query side* ($Q_O$ is a $G_t$-independent interventional query) and the *epistemic-processing* leg of unconfoundedness; full causal validity of the *estimate* additionally requires (C1)–(C3) on the model–environment relationship. This is a strict sharpening: it correctly localizes what directed separation does and does not do, and it connects the segment to the loop-interventional-access result that *supplies* the identification channel.

### 2.3 Why this is (B), not a deflation

The segment's frontmatter `status: exact` is, per its own Epistemic Status, scoped: the *definitions* of $V_O, Q_O$ are exact (uncontested — they are conditional expectations), and the *causal-validity argument* is already labeled "conditional on directed separation." The correction does not down-tier the definitions; it (i) replaces "conditional on directed separation" with the more precise "conditional on directed separation **and** the identification conditions (C1)–(C3)," and (ii) lifts the soft "estimate may be biased" sentence into a first-class gating statement. The interventional *interpretation* remains correct unconditionally (that is what mechanisms (1)+(2) prove); what gets gated is *identifiability of the estimate*. This is the same move the sibling spike made at `#der-loop-interventional-access` (Option A: "availability of the channel is exact; identification is explicitly gated"), and the two should land with identical condition-naming.

---

## 3. Proposed per-segment integration (drafted, not applied)

All drafts below are for the external-eye gate. No canon is edited by this spike. Math-lives-in-segments: the Front-1 counterexample and the three-condition characterization are non-obvious (the "are you *sure* replanning can't underperform?" kind) and warrant landing in the segment body (the corrected Monotonicity block) plus, optionally, a short demonstration appendix carrying the counterexample.

### 3.1 `def-value-object.md` — Front 1 (the Monotonicity block)

**Replace** the unconditional left rung and its buggy derivation step with the corrected scoped theorem. Concretely:

- The displayed chain stays $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$ but is **annotated**: the right inequality unconditional; the left inequality gated on order-consistency of the replanning objective (RH-1/2/3).
- **Fix the derivation.** Delete the sentence "By construction, $\pi_{\text{RH}} \succeq \pi_{\text{current}}$ at each future step, because C2 optimizes where C1 holds fixed" — it is the false step (C2 optimizes the *truncated* objective). Replace with: the right rung from "supremum over the full set" (correct as written); the left rung from the order-consistency condition, with (RH-1)/(RH-2)/(RH-3) as the named sufficient conditions.
- **Add the counterexample** as a short demonstration (body or a `#deriv-convention-monotonicity` appendix segment per math-lives-in-segments): the two-state $+1$-vs-$+10$ myopic trap showing the unguarded $N_r \lt N_h$ rung is false, so the conditions are not ceremony.
- **The C2 row in the Convention Hierarchy** gains a half-sentence: receding-horizon replanning captures multi-step recovery *and* is monotone over the frozen baseline only when the replanning objective is order-consistent (window covers the horizon, or a value-compared guard / control-Lyapunov terminal cost is used); unguarded short-horizon replanning can underperform $\pi_{\text{current}}$.

**Drafted corrected Monotonicity statement** (segment voice, present-truth):

> For fixed $M_t$, horizon $N_h$, and policy class $\Pi$:
> $$A_O^{(1)}(M_t;\, \Pi, N_h) \;\leq\; A_O^{\text{RH}}(M_t;\, \Pi, N_r, N_h) \;\leq\; A_O^{\text{B}}(M_t;\, \Pi, N_h),$$
> where the **right inequality holds unconditionally** ($\pi^\ast$ maximizes $V_O(M_t, \cdot; N_h)$ over $\Pi$, so any continuation in $\Pi$ — including $\pi_{\text{RH}}$ — has value at most $A_O^{\text{B}}$, and the supremum over the first action preserves this), and the **left inequality holds exactly when the receding-horizon replanning objective is an order-consistent surrogate for the full-horizon objective** — for every reachable state, the action C2 selects has full-$N_h$-horizon value at least that of $\pi_{\text{current}}$. Three structurally-checkable conditions each force order-consistency: **(RH-1)** the replanning window covers the horizon ($N_r \geq N_h$); **(RH-2)** value-compared replanning — commit the replanned action only when its rollout value under base policy $\pi_{\text{current}}$ is at least that of continuing $\pi_{\text{current}}$ (one-step policy improvement, which never underperforms its base policy); **(RH-3)** the $N_r$-step replanning objective carries a terminal cost $V_f$ that lower-bounds the baseline tail and satisfies the control-Lyapunov decrease inequality. Absent any such condition the left inequality can fail: a myopic replanner over $N_r \lt N_h$ can grab a near-term value and forfeit a larger horizon value the frozen current policy would have collected (demonstration: appendix / below).

**Epistemic Status edit (layer 3).** Currently "The monotonicity result ... is a direct consequence of 'better continuation policy yields higher expected value' — the ordering is forced by the definition of optimality." That justification is *only* valid for the right rung. Rewrite to: the right rung is exact and unconditional; the left rung is exact *under* the order-consistency condition (RH-1/2/3) and false in general without it (the C2 replanning objective is a truncated surrogate); the corollary $\delta$-orderings inherit the same split. This makes layer 3 honest about which half is unconditional.

### 3.2 `def-satisfaction-gap.md` and `def-control-regret.md` — inherited correction (both `status: exact`)

Both recite the full three-term monotonicity ($\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$ in `def-satisfaction-gap`; $\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$ in `def-control-regret`). Each should gain a one-clause gate: the $\text{B} \leq \text{RH}$ / $\text{RH}$-side half is unconditional; the $\text{RH} \leq (1)$ / $(1)$-side half is conditional on the order-consistency of C2's replanning objective ( #def-value-object). No `status:` change — these segments' `exact` is for the *definitions* ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$ as differences), and the convention-monotonicity they *cite* is now correctly gated at its source. The "Convention dependence and the hierarchy" paragraph in `def-satisfaction-gap` Epistemic Status is the natural place for the clause.

### 3.3 `der-orient-cascade.md` — one-clause pointer (`status: conditional`)

Step 5c and the "Convention hierarchy and diagnostic power" block say convention escalation to C2 "may show $\delta_{\text{sat}}^{\text{RH}} \leq 0$" — the hedged "may" is already correct. Add a half-sentence that C2's recovery-path-revealing and its monotone-improvement-over-C1 reading both presume the replanning objective is order-consistent (guarded / terminal-cost / window-covering); unguarded short-horizon replanning is not guaranteed to dominate the frozen baseline. No `status:` change; the cascade ordering is untouched (it never depended on the left rung).

### 3.4 `def-value-object.md` — Front 2 (the Causal-validity paragraph + Epistemic Status layer 2)

**Lift the identification conditions into the Formal-Expression causal-validity paragraph.** Keep mechanisms (1) and (2) verbatim (they correctly establish the $G_t$-independent interventional *query*). Replace the single soft sentence "When $S(M_t) = 1$ and directed separation holds, $Q_O$ is causally valid. When $S(M_t) \lt 1$ or directed separation fails, the interventional interpretation is correct but the conditional estimate may be biased" with a first-class gate:

> The interventional *interpretation* of $Q_O$ holds whenever mechanisms (1) and (2) do — it is a $G_t$-independent interventional query. The *identifiability of the interventional expectation from $M_t$* is a separate, stronger requirement: (C1) **positivity** (each evaluated action has support under the model's data-generating process); (C2) **no unmodeled confounder** (the backdoor condition of #def-model-sufficiency — directed separation delivers this on the epistemic-processing leg by making $f_M$ goal-blind, but it does not by itself rule out latent environment confounders bypassing $M_t$); (C3) **identified action-transition mechanism** ($M_t$ encodes $P(o \mid do(a))$ via #def-action-transition, not merely the associational predictor $P(o \mid a)$ — supplied by construction or identified from interventional data per #der-loop-interventional-access). Directed separation is necessary but not sufficient: it secures the query and the epistemic-processing leg of unconfoundedness; full causal validity of the estimate additionally requires (C1)–(C3). When all hold, $Q_O$ is causally valid; when (C1)–(C3) fail, the interventional interpretation remains correct but the estimate may be biased.

**Epistemic Status layer 2 edit.** Replace "*conditional* on directed separation" with "*conditional* on directed separation **and** the identification conditions (C1)–(C3)" and note that directed separation alone secures the query and the epistemic-processing leg, not the full identification. This matches `#der-loop-interventional-access`'s Option-A gated form (per the 2026-05-30 transportability spike) and discharges the obligation `#def-model-sufficiency` already forwards here.

**Consistency reconciliation note (for the gate).** This Front-2 fix and the sibling transportability spike's `#der-loop-interventional-access` fix name the same (C1)–(C3); they should be reviewed together so the chapter gates causal validity with one consistent condition set across `#def-model-sufficiency` (forwards the obligation) $\to$ `#def-value-object` (this segment, query + identification gate) $\to$ `#der-causal-hierarchy-requirement` (Level-2 access needed) $\to$ `#der-loop-interventional-access` (the channel that supplies identification). No re-derivation of the imported Pearl/CHT machinery is needed; both spikes rely on the same primary-source reading already verified in the transportability spike §1.

### 3.5 `def-value-object.md` — `status:` and `depends:` (reserved for the external-eye gate)

- **`status:` decision (reserved for Joseph / the external eye).** Two coherent options, mirroring the sibling spike's Option-A/Option-B structure:
  - **Option A (recommended — keep `status: exact`, rewrite the bodies):** the *definitions* are exact; the *right rung* is exact; the *left rung* is exact *under the named (RH-1/2/3) condition*; the *causal-validity query* is exact and the *identification* is exact under (C1)–(C3). Every exact-labeled claim is then defensible *as rewritten*, with the conditions first-class in the body. This is the strengthen-first landing: a scoped theorem + a no-go for the complement, not a down-tier.
  - **Option B:** split the segment-level status, or carry the convention-monotonicity and causal-validity as `conditional`-tagged sub-claims while the definitions stay `exact`. Heavier; only if the external eye prefers the segment to wear the conditionality in its frontmatter rather than in clearly-gated body statements.
  - I recommend **Option A**: the corrected claims are all genuinely exact *under their named conditions* (CS-norm scoped theorems), and the no-go is itself an exact result; nothing here is merely heuristic or discussion-grade. The `exact` frontmatter is honest *provided the body carries the conditions* — which is the whole point of the rewrite.
- **`depends:`** unchanged for Front 1. For Front 2, no new dependency is forced ( #def-action-transition and #def-model-sufficiency are already in the chain via #def-model-sufficiency; #der-loop-interventional-access is a downstream supplier, cited not depended-on). If the external eye lands the counterexample as a new `#deriv-convention-monotonicity` appendix, that appendix `depends:` on `def-value-object`.

---

## 4. Confidence and escalation

- **Front 1 — left rung false in general; right rung exact; rung holds under (RH-1/2/3):** **high confidence.** The counterexample is elementary, deterministic, and numerically confirmed (`sim-rh-counterexample.py`); the strengthening conditions are standard receding-horizon/rollout/MPC-terminal-cost results, two of them numerically confirmed to restore the rung on the same instance (`sim-rh-strengthening.py`). The bug in the segment's derivation step is identified precisely (C2 optimizes the truncated objective, so "optimizes $\Rightarrow$ $\succeq \pi_{\text{current}}$ on the full objective" is a non-sequitur).
- **Front 2 — directed separation necessary not sufficient; identification needs (C1)–(C3):** **high confidence on the diagnosis** (it is the same fact the 2026-05-30 transportability spike established from primary CHT sources one segment downstream, and `#def-model-sufficiency` already forwards the backdoor obligation here). **Medium confidence on the exact phrasing of the gate** — the (C1)/(C2)/(C3) split should be reconciled verbatim with the sibling spike's draft so the chapter is internally consistent; that reconciliation is a gate-time activity.
- **`status:` (Option A vs B) and any tier transition:** **reserved for the external-eye gate**, per the spike brief. I recommend Option A on both fronts.

**Surprises / unresolved:**

- The two fronts land at *different* completion-states but compose cleanly: Front 1 is a (C) no-go-on-the-rung wrapped in (B) a scoped strengthening; Front 2 is a (B) scope-sharpening. Neither touches the *definitions*' exactness or the C1-default diagnostic logic.
- **Coherence with the sibling spike is the main gate-time obligation.** `spike-causal-access-transportability-2026-05-30.md` and this spike both gate causal validity with (C1)–(C3) at adjacent segments (`#der-loop-interventional-access` and `#def-value-object`). They were drafted independently from the same auditor (526815) and the same primary sources; they should be landed in one consistent pass. I did **not** re-derive the Pearl/CHT/transportability machinery — that was verified directly from `ref/bareinboim-2022-pearl-hierarchy.pdf` / `ref/r443.pdf` in the sibling spike, and Front 2 here relies on that reading rather than re-opening it (appropriate: imported machinery AAT cites, not AAT-internal math).
- I did **not** locate a dedicated MPC/receding-horizon textbook in `ref/` (no Rawlings-Mayne-Diehl / Grüne-Pannek / Bertsekas PDF). The Front-1 strengthening conditions are standard and self-contained as derived here; if any of (RH-1/2/3) lands in canon as a cited result, the external citation should be added via `relata` at gate time (the math does not depend on the citation — it is elementary DP).

---

## Working Notes

- Sources read directly this cycle: `01-aat-core/src/def-value-object.md` (full); its dependencies `der-directed-separation.md`, `def-model-sufficiency.md`, `form-objective-functional.md`, `der-causal-hierarchy-requirement.md`, `def-pearl-causal-hierarchy.md`, `der-orient-cascade.md`, `def-satisfaction-gap.md`, `def-control-regret.md`; the sibling spike `spikes/spike-causal-access-transportability-2026-05-30.md`; the challenge note `audits/AUDIT-WORKING-526815/.integrated/40-def-value-object.md`.
- Reproducibility: `sim-rh-counterexample.py` (the no-go counterexample + the $N_r = N_h$ control) and `sim-rh-strengthening.py` (the RH-2 and RH-3 strengthenings restoring the rung) accompany this verdict. Python per the community-facing-reproducibility script convention.
- **Documented dead-end (so a future agent does not re-attempt it):** there is no way to recover the unconditional left rung $A_O^{(1)} \leq A_O^{\text{RH}}$ for genuine $N_r \lt N_h$ replanning without an order-consistency condition — the failure is structural (objective-mismatch between the truncated replanning objective and the evaluated full-horizon objective), and the two-state counterexample is minimal. Do not re-derive the rung as unconditional; the strengthening *is* the (RH-1/2/3) characterization.
- This spike proposes no canon edits and changes no `status:`. The drafted §3 integration is for the external-eye review gate. Reserved-for-Joseph / external-eye: the Option-A-vs-B `status:` choice (both fronts), and reconciling the Front-2 (C1)–(C3) phrasing verbatim with the sibling transportability spike's `#der-loop-interventional-access` draft.
- Status of this spike: **complete; Front 1 = (C)-no-go-in-(B)-strengthening; Front 2 = (B)-scope-sharpening; awaiting external-eye review of the §3 integration.**
