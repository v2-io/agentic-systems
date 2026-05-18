# Spike: The Leakage Locus — Goal Contamination Confined to the Identifiability Null Space

**Status.** Exploratory research spike. Math worked to the point where the core result is exact and closed-form; two propagations are sketch-grade and marked as such.
**Date.** 2026-05-18.
**Pressure Point.** The `#def-agent-spectrum` Working Note (2026-05-18) flagged a thread that the theory touches but does not state: the dangerous $G_t \to f_M$ coupling does not live "at the future boundary" — it concentrates in the inference about the *unobserved present* (the gap-filling about the unseen parts of the current world), because that is the only step in $f_M$ with a *free prior*. It also conjectured that directed separation as currently stated — the conditional independence $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, e_\tau)$ ( `#der-directed-separation`) — addresses the *processing of the event* but does **not** prevent a goal-shaped prior that the next observation cannot wash out.

This spike works the math. The question: does the intuition survive contact with the filtering formalism, and if so is there a derivation, a strengthening, a diagnostic, or a normative structure on the other side of it?

The short answer: yes to all four. The intuition is exactly right and falls out of the Kalman/Laplace structure in closed form; it sharpens into a precise *insufficiency* result for directed separation as stated (a strengthening, not a softening); it yields a principled target subspace for the existing $\hat\kappa_{\text{processing}}$ behavioral estimator; it surfaces two counter-intuitive findings (contamination is invisible to the agent's own uncertainty; humility increases susceptibility); and it re-derives the framework's central inequality shape in a new place.

---

## 1. Decomposing $f_M$ and locating the free prior

Work in the Bayes-filter view. The world carries a latent state $z_t \in \mathbb{R}^n$ (the true present, mostly unobserved). The observation is a lossy/noisy projection $o_t = h(z_t) + v_t$. The model state $M_t$ is (a sufficient statistic for) the belief $b_t(z) = P(z_t = z \mid \text{history})$. The goal-blind update $f_M$ factors into the two standard half-steps:

1. **Predict** (pushes the prior forward through dynamics):
   $$b_{\tau^-}(z') = \int P(z' \mid z, a_{\tau^-})\, b_{\text{prev}}(z)\, dz.$$
   This is the *predictive-future* content — the forward model. It is future-stamped and **purely epistemic** (this is the $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ of `#def-mismatch-signal`; a Kalman predict-step or a weather forecast carries zero goal content). The Working Note's "arrow-of-time is the separator" idea dies here, as recorded there.

2. **Correct** (conditions on the realized event):
   $$b_{\tau^+}(z) \;\propto\; P(e_\tau \mid z)\; b_{\tau^-}(z).$$

**Where is the free prior?** The likelihood $L(z) := P(e_\tau \mid z)$ constrains $z$ only along the directions it is sensitive to. Decompose the current latent state relative to the observation: the observation has a *Fisher information* $\mathcal I_\tau$ (defined below); along $\ker \mathcal I_\tau$ the likelihood is flat — the event says nothing about those components of the present world. On that subspace the posterior is whatever the prior $b_{\tau^-}$ says, untouched by the data. **$\ker\mathcal I_\tau$ is exactly "the unseen parts of the current world."** It is the only place in the correct-step where belief is not pinned by evidence — the free prior the Working Note pointed at, now named precisely as the *non-identified subspace of the current latent state given the realized event*.

This is the first connection: the leakage locus *is* an identifiability null space — the same structural object the `#disc-identifiability-floor` meta-segment (M1) is built around. The floor governs not only what can be *learned* but, as the rest of this spike shows, what can be *corrupted by goals*. Same structure, dual use.

---

## 2. The exact Gaussian result

Linear-Gaussian instantiation (the Laplace approximation of the general case; exact when the model is linear-Gaussian, which is the canonical Section-I tracker — Kalman, Beta-Bernoulli linearization).

Post-predict prior: $b_{\tau^-} = \mathcal N(\mu^-, P^-)$.
Observation: $o = Hz + v$, $v \sim \mathcal N(0, R)$, so $L(z) \propto \exp\!\big(-\tfrac12 (o-Hz)^\top R^{-1}(o-Hz)\big)$.
**Observation Fisher information** (the information the event carries about the current latent state):
$$\mathcal I_\tau \;=\; H^\top R^{-1} H \;\succeq\; 0, \qquad \ker\mathcal I_\tau = \ker H \;=\;\text{unobserved subspace of } z_\tau.$$

Honest (goal-blind) correct step — the information-form Kalman update:
$$p_0 = \mathcal N(\mu_0,\Lambda_0^{-1}), \qquad \Lambda_0 = (P^-)^{-1} + \mathcal I_\tau, \qquad \mu_0 = \Lambda_0^{-1}\big[(P^-)^{-1}\mu^- + H^\top R^{-1} o\big].$$

**Contamination model.** Let the goal enter as a smooth multiplicative tilt $c_G(z) = \exp(g^\top z)$ on the posterior, $g$ a goal-pull vector (first-order: $g = \nabla$ of a goal-desirability potential; $\lVert g\rVert$ measures coupling strength). Exponential tilting is the minimum-relative-entropy way to impose a mean-shift — the I-projection that changes belief as little as possible while leaning it goalward, i.e. the *least-detectable* motivated-reasoning move, which is the adversarially-relevant case. **Robustness note:** a goal-*tilted prior* $b_{\tau^-}\!\cdot e^{g^\top z}$ followed by an honest likelihood gives an identically tilted posterior (multiplication commutes), so the result below is invariant to whether the goal enters through the prior or through the likelihood reweighting — it does not matter *where* in the predict/correct chain the goal leaks, only *along what subspace*.

Contaminated posterior $p_G \propto p_0 \cdot c_G$. Completing the square:
$$\log p_G = -\tfrac12 (z-\mu_0)^\top \Lambda_0 (z-\mu_0) + g^\top z + \text{const} = -\tfrac12 z^\top\Lambda_0 z + (\Lambda_0\mu_0 + g)^\top z + \text{const}.$$
so $p_G = \mathcal N(\mu_G, \Lambda_0^{-1})$ with

$$\boxed{\;\Delta\mu \;:=\; \mu_G - \mu_0 \;=\; \Lambda_0^{-1} g \;=\; \big[(P^-)^{-1} + H^\top R^{-1} H\big]^{-1} g, \qquad \text{covariance } \Lambda_0^{-1}\ \textbf{unchanged}.\;}$$

*[Exact under linear-Gaussian model + smooth tilt. Tier: exact.]*

The belief displacement caused by goal contamination is the goal-pull filtered through the **total posterior precision**. Everything below is reading this one equation.

---

## 3. The Leakage Locus Lemma (exact)

Take any $w$ in the unobserved subspace, $Hw = 0$ (so $\mathcal I_\tau w = 0$). Then $w^\top \Lambda_0 = w^\top (P^-)^{-1} + w^\top \mathcal I_\tau = w^\top (P^-)^{-1}$. Hence:

> **Lemma (Data-invariance of null-space leakage).** Along the unobserved subspace $\ker\mathcal I_\tau$, the goal-induced displacement is mediated entirely by the *prior* covariance and is **independent of the observation model $(H,R)$ and of the realized observation $o$**. No amount of sensor precision on the observed dimensions reduces leakage in the unobserved subspace.

Conversely, decompose $g$ in the eigenbasis of $\mathcal I_\tau$ (clean form: isotropic prior $P^- = pI$, or any $P^-$ commuting with $\mathcal I_\tau$); eigenvalue $\lambda_i$ of $\mathcal I_\tau$ along $v_i$:
$$ (\Delta\mu)_i = \frac{g_i}{\,1/p + \lambda_i\,}\;\;\longrightarrow\;\; \begin{cases} p\, g_i & \lambda_i \to 0 \quad(\text{unidentified: pull passes, scaled by prior variance})\\[4pt] g_i/\lambda_i \to 0 & \lambda_i \to \infty \quad(\text{identified: data firewalls the pull}). \end{cases}$$

General (non-commuting) statement, exact in Loewner order: since $(P^-)^{-1} \succ 0$, $\Lambda_0 \succ \mathcal I_\tau$ and $\Lambda_0 \succ (P^-)^{-1}$, so the **leakage gain matrix** $K_G := \Lambda_0^{-1}$ satisfies
$$0 \;\prec\; K_G \;\prec\; P^-, \qquad\text{and}\qquad K_G\big\rvert_{\mathrm{range}\,\mathcal I_\tau} \preceq \mathcal I_\tau^{+}\ \text{(pseudo-inverse) in the commuting case}.$$

> **Result (Leakage Locus).** Goal contamination of a goal-blind-data filter can move belief *only* along the directions the realized event fails to identify, and the data stream cannot reduce it within that subspace (zero Fisher information there by construction). Its magnitude in the unidentified subspace equals the prior uncertainty there; in the identified subspace it is suppressed in proportion to the observation's identifying power.

*[Tier: exact for the linear-Gaussian + smooth-tilt model; **robust qualitative** for general smooth contamination — the confinement-to-$\ker\mathcal I_\tau$ and data-irreducibility-there arguments are information-geometric and survive nonlinearity, only the closed-form magnitude is model-specific.]*

This is the Working Note's intuition, derived. The leakage locus is $\ker\mathcal I_\tau$, the identifiability null space of the *current* latent state given *this* event.

*[Candidate landing: a new appendix segment (math-lives-in-segments — this must not reside only in the spike) cross-linked from `#der-directed-separation` and `#disc-identifiability-floor`; the Lemma is appendix-grade non-obvious.]*

---

## 4. Three surprises (the treasure)

**Surprise 1 — the contamination is invisible to the agent's own uncertainty.** The covariance is *unchanged*: $p_G$ and $p_0$ share $\Lambda_0^{-1}$. Only the mean moves. So an agent cannot detect this leakage by inspecting its own posterior spread — its calibration report is identical with and without the goal tilt. This is *why* the existing $\hat\kappa_{\text{processing}}$ behavioral estimator ( `#der-directed-separation`) is necessarily a *cross-goal-counterfactual mean comparison* (same event, two goal states, divergence of the epistemic content) rather than an uncertainty check — and the analysis hands that estimator a **principled target**: it should probe the *unidentified subspace* $\ker\mathcal I_\tau$, where all the signal is, not the full state. A diagnostic that watches the low-curvature subspace of the posterior precision $\Lambda_0$ catches exactly the directions goal-contamination can occupy. (This refines, with a target, the Hafez-IDT external-monitor pattern already discussed in `#der-directed-separation` Working Notes.)

**Surprise 2 — the humility paradox.** Leakage magnitude in an unidentified direction is the *prior variance* there ($\approx p\,g_i$). An agent that is *more uncertain* about the unseen present is *more* susceptible to motivated perception precisely where it is most blind — and (by Surprise 1) its reported uncertainty does not betray the contamination. This is the project's own epistemic disposition — *uncertainty is where wishfulness operates* — falling out as a derived consequence rather than an asserted value. Note the safe regime: an agent that holds an *honestly wide* posterior on $\ker\mathcal I_\tau$ **and acts robustly with respect to it** is fine; the danger is the agent whose goal silently sharpens the mean while the covariance (its self-reported humility) stays wide — confidently wrong in the dark, and unable to feel it.

**Surprise 3 — the guarantee gap is in the prior, not the processing.** Directed separation as stated, $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, e_\tau)$, conditions on $M_{\tau^-}$. But the leakage rides in through $M_{\tau^-}$ itself — a goal-shaped *predict-step prior* on $\ker\mathcal I_\tau$ — and the conditional independence is then *vacuously satisfied* while belief is fully contaminated: nothing about the processing of $e_\tau$ was goal-dependent; the data simply had nothing to say along the corrupted subspace. The scope condition's clause 2 ("no confirmation bias baked into $f_M$") polices the *processing*; it does not police a goal-laundered prior the event cannot correct. This is a real, localized gap in the guarantee — and it sharpens into §5.

---

## 5. Strengthening directed separation (a no-go-flavored sufficiency result)

Per strengthen-before-soften: the move here is **not** "directed separation is weaker than claimed, soften it." It is "the stated condition is insufficient; here is the precise *additional* premise that makes the goal–belief independence it wants actually hold." That is a strengthening — it makes the guarantee true under a named, checkable condition rather than approximately-true under an unstated one.

> **Proposition (Insufficiency + the missing premise).** The conditional independence $M_{\tau^+}\perp G_t \mid (M_{\tau^-}, e_\tau)$ does **not** imply goal–belief independence $M_{\tau^+}\perp G_t$. Counter-model: $f_M$ goal-blind in its event-processing, but $M_{\tau^-}$ carries a $G_t$-dependent component supported on $\ker\mathcal I_\tau$; then $M_{\tau^+}$ inherits it (Lemma §3, data-invariance) while the stated conditional independence holds. **Sufficient condition:** additionally require the prior on the unidentified subspace to be goal-blind —
> $$\Pi_{\ker\mathcal I_\tau}\, M_{\tau^-} \;\perp\; G_t,$$
> where $\Pi_{\ker\mathcal I_\tau}$ is the projector onto the current unidentified subspace. Under the stated condition **plus** this, $M_{\tau^+}\perp G_t$ on the correct-step (proof: identified subspace pinned by data via the Lemma's converse → independent of prior hence of $G_t$; unidentified subspace independent of $G_t$ by the added premise; direct sum).

*[Tier: the insufficiency (counter-model) is exact. The sufficiency direction is exact for the linear-Gaussian correct-step; the recursive/temporal closure — that a goal-blind prior stays goal-blind under the predict step — is **not** free and is exactly what §6 is about. Conditional on §6.]*

*[Candidate landing: a third clause on `#der-directed-separation`'s Scope Condition — "(3) the agent's prior on the currently-unidentified subspace $\ker\mathcal I_\tau$ is goal-blind" — plus an Epistemic-Status note that clauses 1–2 govern processing and clause 3 governs the laundered-prior channel. This also refines the wrapping construction: a strict-W₁ wrapper that commits goal-blind belief-update *queries* still does not, by that commitment alone, firewall a goal-shaped *prior* on $\ker\mathcal I$. W₁ should additionally type-commit the predict-step prior on the unidentified subspace, not only the query. That is an actionable, structural sharpening of `#der-class-coercion-via-wrapping`, not a behavioral one.]*

---

## 6. Temporal propagation — the central inequality, again, in a new place

Does a transient goal-tilt self-correct? Only if the dynamics carry the corrupted subspace back into the sensor's view. Continuous-time sketch: the corrupted component on $\ker\mathcal I_\tau$ is rotated by the flow $F$ each predict step; if the system is *observable* (every latent direction eventually projects onto the sensor — the observability Gramian $\mathcal W = \int_0^{T} e^{F^\top s} \mathcal I\, e^{F s}\, ds \succ 0$), an *injected-once* tilt is exposed and washed out with a half-life set by $\mathcal W$'s spectrum. But a *persistent* goal (a stable objective re-applies $g$ every step) sustains a steady-state bias. Linearizing the bias dynamics $\dot{\Delta\mu} = -A_{\text{obs}}\,\Delta\mu + B\, g$ (correction rate $A_{\text{obs}}$ set by observability-weighted Fisher accumulation; drive $B g$ the per-step re-injection) gives an ultimate bound

$$\Delta\mu_\infty \;\approx\; \mathcal W^{-1}\, g \quad\text{(goal-pull rate over observability-corrective rate).}$$

Compare the persistence ultimate bound $R^\ast = \rho/\alpha$ ( `#result-persistence-condition`): **same form.** Roles: $\rho \to$ goal-pull re-injection rate; $\alpha \to$ observability-weighted correction rate; and the *unobservable* subspace ($\mathcal W$ singular) is the $\alpha_{\text{eff}} = 0$ case — unbounded susceptibility, the exact structural-failure analog of `#result-structural-adaptation-necessity`. A persistent objective whose pull outruns the observability refresh holds a permanent, data-uncorrectable belief bias confined to the slow-observability subspace.

This is the framework's central inequality recurring in a third place (epistemic mismatch; adversarial tempo; now goal–belief bias). Per the project's convergence-as-coherence principle, the *recurrence of the same threshold/ultimate-bound shape* under independent derivation is itself evidence the pattern is structural, not an artifact of one model.

*[Tier: **sketch / robust-qualitative.** The $\mathcal W^{-1}g$ form is heuristic — a full result needs the sector-Lyapunov machinery applied to the bias ODE, parallel to `#result-sector-condition-stability`. Flagged as the natural follow-on; do not promote the steady-state constant without that derivation. The structural parallel (same inequality shape, observable↔persistent / unobservable↔structural-failure) is the robust-qualitative claim and is the load-bearing part.]*

---

## 7. Normative / design structure

The Leakage Locus has a constructive dual: the antidote to motivated-reasoning leakage is *not* "try harder to be goal-blind in processing" (Surprise 3 shows that is insufficient). It is one of two structural moves on $\ker\mathcal I_\tau$:

- **Defer on the unidentified.** Make the chosen action robust/minimax over $\ker\mathcal I_\tau$ — decide in a way that is insensitive to the subspace the goal can corrupt. (The agent acts on what it has earned epistemically and explicitly refuses to let the dark drive the decision.)
- **Probe the unidentified.** Actively shrink $\ker\mathcal I_\tau$ before acting — i.e. choose actions that raise the Fisher information along the currently-unidentified directions. This is *exactly* the Causal Information Yield framework ( `#def-causal-information-yield`), repurposed: CIY appears in Section I as an adaptation accelerant; here it is a **goal-contamination defense**. Targeted active testing is the structural cure for motivated reasoning, because it converts free-prior directions into data-pinned directions, where the Lemma's converse firewalls the goal pull.

This is a normative bridge between two existing parts of the theory (directed separation ↔ CIY) that the current text does not draw: *the discipline of seeking disconfirming evidence is, formally, the act of moving belief out of the goal-corruptible subspace.* The project's truth-honoring disposition is here a derivable control law, not only a value.

*[Candidate landing: Discussion paragraph in the new appendix segment, and a cross-reference added to `#def-causal-information-yield` ("CIY as goal-contamination defense — see [appendix]"). Possibly a `normative` segment if the act-on-identified / probe-the-unidentified dichotomy strengthens into a stated design principle.]*

---

## 8. Nonparametric bound (conjecture)

Beyond Gaussian: a Bernstein–von Mises argument suggests, asymptotically in data, that the posterior on $\mathrm{range}\,\mathcal I_\tau$ concentrates on a deterministic function of the data (prior-washed), so all goal dependence of $M_{\tau^+}$ flows through the prior on $\ker\mathcal I_\tau$:
$$I(G_t; M_{\tau^+}) \;\lesssim\; I\big(G_t;\ \Pi_{\ker\mathcal I_\tau} M_{\tau^-}\big).$$
This would bound the existing $\kappa_{\text{processing}}$ diagnostic by an *identifiability quantity* — the fraction of posterior entropy living in the unidentified subspace — connecting this thread quantitatively to the established operationalization.

*[Tier: **conjecture / heuristic.** BvM regularity (smooth finite-dim parametric, prior positive at truth) is exactly what fails for the interesting Class-3 cases (high-dim, non-regular). State the asymptotic intuition; do not assert the inequality. Open question, §9.]*

---

## 9. Status ledger

| Result | Tier | Lands where (candidate) |
|---|---|---|
| §2 Belief displacement $\Delta\mu = \Lambda_0^{-1}g$, covariance invariant | **exact** (lin-Gauss + smooth tilt) | new appendix |
| §3 Leakage Locus Lemma (data-invariance on $\ker\mathcal I_\tau$; Loewner sandwich) | **exact** (model) / **robust-qual** (general) | new appendix; xref `#disc-identifiability-floor` |
| §4 S1 invisibility-to-own-covariance; S2 humility paradox; S3 prior-not-processing gap | **exact** (corollaries of §2–3) | appendix Discussion; sharpen `#der-directed-separation` |
| §5 Insufficiency counter-model | **exact** | `#der-directed-separation` Scope Condition clause 3 |
| §5 Sufficiency (correct-step) | **exact** (correct-step); conditional on §6 for temporal closure | same |
| §6 $\Delta\mu_\infty \approx \mathcal W^{-1}g$ steady-state | **sketch / robust-qual** | follow-on spike (needs sector-Lyapunov) |
| §6 central-inequality structural parallel | **robust-qual** | appendix Discussion; convergence note |
| §7 act-on-identified / probe-the-unidentified; CIY-as-defense | **robust-qual** (structural) | `#def-causal-information-yield` xref; possible `normative` segment |
| §8 MI bound by $\ker\mathcal I$ prior entropy | **conjecture** | open |

**Open questions / next moves.**
1. Close §6 properly with the sector-Lyapunov machinery (parallel to `#result-sector-condition-stability`); confirm the observable↔persistent / unobservable↔structural-failure mapping is exact, not just shaped-the-same.
2. §8: is there a non-asymptotic (finite-information) version that survives the Class-3 non-regular regime? Likely needs an $f$-divergence/strong-data-processing argument rather than BvM.
3. Reconcile with `spike-strategic-self-coupling.md` and the M4 pattern: this looks like a *mechanism-level* account of strategic self-coupling (the middle M4 operation) — the Leakage Locus would say strategic self-coupling necessarily routes through $\ker\mathcal I$. Worth checking whether that spike already has a compatible or competing mechanism; flagged for the author, not resolved here.
4. Reconcile the Lemma with the existing `#disc-identifiability-floor` instances (the floor spike series, incl. `spike-identifiability-floor-instance4-resolution-2026-05-18.md`): is "goal-corruptible subspace" a *new instance* of the floor, or a re-description of an existing one? Author call — do not fold silently.

**Documented dead-end (guardrail for future agents).** "Arrow-of-time / future-timestamp as the $M_t$–$O_t$ separator" does not work — the predict-step forward prediction $\hat o_t$ is future-stamped and purely epistemic (§1). Do not re-attempt; the real separator is evidence-conditioned vs. preference/intervention-conditioned, and the *spatial* (subspace) localization, not the *temporal* one, is what carries the weight.

**Provenance.** Originating intuition: Joseph, 2026-05-18, `#def-agent-spectrum` Working Note thread ("the danger is in the assumptions about the unseen parts of the current world"). This spike is the reasoning trail; the exact math (§2–5) is owed a segment per math-lives-in-segments and must not remain spike-only once vetted.
