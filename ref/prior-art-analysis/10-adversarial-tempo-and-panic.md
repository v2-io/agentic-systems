# Prior-Art Analysis: Adversarial Tempo, the Effects Spiral, and the Four-Regime Interaction-Channel Classification

> [!note]
> **Refreshed 2026-05-21.** The previous version captured the OODA-style tempo and effects-spiral arguments well; the refresh integrates the Adversarial_tempo_and_panic novelty memo, adds the **four-regime recipient-side classification** from `#der-interaction-channel-classification` that the prompt's "Regimes: informative, magnitude shock, structural shock, ambient erosion" referred to, adds the **resource-bounded destabilization** extension that closes the effects spiral via a different channel, and surfaces the signed-coupling unification (cooperation and adversariality as the same coupling law with opposite signs).

**Target Claim:**
Adversarial interaction is the same coupling law as cooperation **with opposite signs on the coupling term**: cooperators reduce the recipient's effective disturbance, adversaries increase it. Building on this signed-coupling unification, AAT derives several theorem-grade results:

1. **Destabilization thresholds (Models D and S).** Under deterministic drift coupling (Model D), agent $A$ destabilizes $B$ when $\mathcal T_A > (\alpha_B R_B - \rho_{B,\text{base}}) / \gamma_A$ — *exact* from `#result-sector-persistence-template` (Prop A.1). Under stochastic noise coupling (Model S), the threshold becomes $\mathcal T_A > (R_B \sqrt{2 \alpha_B} - \sigma_{B,\text{base}}) / \gamma_A$ — the same template applied with Model S's $R^\ast_S = \sigma \sqrt{n/(2 \alpha)}$ steady state. Both are *exact* under their respective coupling assumptions.

2. **Superlinear adversarial tempo advantage (`#result-adversarial-tempo-advantage`, `#result-adversarial-exponent-regimes`).** Under Model D, the adversarial mismatch ratio scales as **$\mathcal T_A^2 / \mathcal T_B^2$** (exponent $b = 2$). Under Model S, it scales as **$\mathcal T_A^{3/2} / \mathcal T_B^{3/2}$** (exponent $b = 3/2$). This is the structural origin of the superlinear "OODA advantage" claim — not a separate derivation, but the propagation of the template's $1/\alpha$ vs. $1/\sqrt{\alpha}$ disturbance-model split through the destabilization-negation step.

3. **Effects spiral as joint-Jacobian eigenvalue condition.** When $B$ is driven past its stability boundary and $B$'s degrading model causes $B$'s actions to become erratic in a way that increases $A$'s coupling effectiveness $\gamma_A(\lVert \delta_B \rVert)$, the disturbance grows superlinearly, $\dot V_B > 0$ and increasing. The closed-form condition is $\max_{\pi^\ast} \mathrm{Re}(\lambda_{\max}(\nabla F(\pi^\ast))) > 0$, where $F$ is the joint best-response field (per `#deriv-strategic-composition` §Discussion). The asymmetric formulation in `#der-adversarial-destabilization` is *discussion-grade*; the symmetric coupled formulation in `#deriv-strategic-composition` makes the eigenvalue condition derivation-grade.

4. **Resource-bounded destabilization (`#der-resource-bounded-destabilization`).** A hard-budget agent self-depletes to **certain finite-time destabilization** against even a *constant*-effectiveness adversary. With no replenishment ($r_{\mathcal B} = 0$), the budget $\mathcal B_t$ strictly decreases as correction runs, so $\alpha_B(\mathcal B_t)$ is a time-varying, monotonically-decaying sector parameter. Even an agent that would persist forever at full budget destabilizes once fuel drains the correction rate below threshold. This closes the effects spiral via a *different channel*: it makes the open coupling term $\gamma_A(\lVert \delta_B \rVert)$ unnecessary by making the spiral come from the agent's own correction-rate decay.

5. **Four-regime recipient-side classification (`#der-interaction-channel-classification`).** The same scalar emitter signal $\gamma_A \mathcal T_A$ lands on $B$ as one of four qualitatively distinct event types, determined by three independent boundary conditions on $B$'s sector region, model-class capacity, and observability floor:
   - **Regime I (informative update)** — within sector, representable in model class, above observability floor. The good case.
   - **Regime II-a (magnitude shock)** — event magnitude exceeds the sector region. Repair: more bandwidth or tempo.
   - **Regime II-b (structural shock)** — within sector but information content exceeds the model class. Repair: structural adaptation (a different model class); more tempo does not help.
   - **Regime III (ambient erosion / cognitive DDoS)** — below the observability floor individually, but cognitive overhead accumulates. Repair: infrastructure-level filtering before signals reach the agent.

   *The emitter sees a scalar; the recipient sees a regime.* Events of identical scalar magnitude can sit in any of the four regimes with structurally different repairs. This recipient-side decomposition surfaces Regime-I-with-adversarial-content (sign-chosen misinformation injection on the log-odds signal) — an adversarial move the scalar emitter formulation cannot express.

6. **Opacity as the dual of observation quality** — modulates tempo advantage by changing the recipient's effective $U_{o,B}$ and therefore the coupling $\gamma_A$. The dual-quantity packaging in `#der-agent-opacity` ties stealth/concealment literature into the same machinery as observation quality.

---

## 1. State of the Field & Scientific Precedence

The literature has strong antecedents on each flank but lacks the unified signed-coupling closed-form package.

### Pillar 1: Boyd's OODA Loop and Synchronization Models
- **Boyd (1986, 1987)** — the OODA loop and "getting inside the opponent's loop" as the conceptual anchor for tempo-as-decisive-variable in military theory.
- **Brehmer (2005)** *The Dynamic OODA Loop* — translation to system dynamics.
- **Kalloniatis et al. (2012, 2020)** *On the Boyd-Kuramoto Model* — coupled Kuramoto oscillators modeling C2 synchronization; faster network disrupts target's synchrony.
- **Zup20, Ahe21** — synchronization and command models extending the same line.

### Pillar 2: Delayed-Information Differential Games and Communication-Constrained Control
- **Shinar & Glizer (1999, 2000, 2001, 2006)** — pursuit-evasion games with delayed information; the value of the delayed-information game is never zero; information delay strictly bounds game value against a faster opponent.
- **Tatikonda & Mitter (2004)** *Control under communication constraints* — IEEE TAC. Channel rate floors for stabilization.
- **Nair & Evans (2004)** *Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates*.
- **Sahai & Mitter (2006)** *Anytime Capacity for Stabilization* — necessity-and-sufficiency: for an unstable scalar plant, stabilization requires channel support that outruns the plant's exponential divergence. The threshold is set by the unstable growth rate — strong precedent for "adversarial or environmental tempo can outrun correction."
- **Khong et al. (2016)** *Information, Time, and Communication* — timing carries information, but delay makes timing information stale, producing phase transitions in stabilization rate.
- **Yu et al. (2020)** *Competitive control with delayed imperfect information* — delay drives worst-case performance losses exponentially in unstable systems.

### Pillar 3: Tracking Under Drift / Adaptive-Filter Nonlinear Scaling
- **Widrow & Stearns (1976, 1984)** — classical adaptive-filter literature; lag-noise tradeoff.
- **Guo (1994)** *Performance analysis of general tracking algorithms*.
- **Ljung (1990)** *System Identification: Theory for the User*.
- **Kuh, Petsche & Rivest (1997)** — proves upper bounds on generalization error under random drift, including a $\gamma^{2/3}$-type scaling for conservative trackers and linear-in-$\gamma$ scaling for nonconservative ones. The closest existing ancestry for nontrivial scaling exponents — not the same as AAT's $b=2$ / $b=3/2$ but the same general territory.

### Pillar 4: Self-Reinforcing Degradation / Overload / Effects Spiral Ancestry
- **Hancock & Warm (1989)** *A dynamic model of stress and sustained attention* — performance under stress as a compensatory process with limited energetic reserve.
- **Hockey (1997)** *Compensatory control in the regulation of human performance under stress and high workload*.
- **Hubbard, Kott & Martin (2016)** *Inducing and Mitigating a Self-Reinforcing Degradation in Decision-making Teams* — direct precedent. Decision teams with nonlinear workload-accuracy curve and positive-feedback loop: errors create more requests, which create more errors, eventually producing abrupt collapse. Soft-threshold workload-accuracy map with cascading regime. The strongest direct ancestor for a thresholded self-reinforcing degradation story.
- **Wallace (2020, 2021, 2023)** *How AI founders on adversarial landscapes of fog and friction* — asymptotic limit theorems formalizing "punctuated failure" and system collapse under adversarial conditions.

### Pillar 5: Adversarial Coupling, Stealth, and Detectability in Cyber-Physical Systems
- **Mo & Sinopoli (2010)** — false data injection attacks; conditions under which an adversary can destabilize by exploiting feedback loops.
- **Bai et al. (2017)** *Data-Injection Attacks in Stochastic Control Systems: Detectability and Performance Tradeoffs* — KL-based stealth definitions; detectability-performance tradeoff.
- **Sui et al. (2020)** *The vulnerability of cyber-physical system under stealthy attacks* — stealthy and strictly stealthy attacks via output-nulling / zero-dynamics structure can drive estimation bias unbounded.
- **Huang et al. (2021)** — pursuit-evasion with strategic information acquisition and concealment.
- **Khazraei et al. (2022)** *Stealthy attacks on perception-based control systems* — attack success depends on estimation quality, stealth constraints, defender's perceptual extraction capacity. The faster the open-loop plant diverges, the more vulnerable the closed-loop is.

---

## 2. Key Anchor Papers Identified

1. **Sahai, A. & Mitter, S. (2006).** *The Necessity and Sufficiency of Anytime Capacity for Stabilization.* IEEE TIT 52:3369.
   *Significance:* The cleanest necessity-and-sufficiency theorem: stabilization requires channel support that outruns the plant's exponential divergence. Strong precedent for "adversarial/environmental tempo can outrun correction."
2. **Hubbard, P., Kott, A. & Martin, M. (2016).** *Inducing and Mitigating a Self-Reinforcing Degradation in Decision-making Teams.*
   *Significance:* The strongest direct ancestor for thresholded self-reinforcing degradation (workload-accuracy cascade with soft threshold).
3. **Wallace, R. (2020).** *How AI founders on adversarial landscapes of fog and friction.*
   *Significance:* Asymptotic limit theorems formalizing punctuated failure under adversarial conditions; cousin to AAT's phase-transition-at-reserve-boundary.
4. **Kalloniatis, A. et al. (2012, 2020).** *On the Boyd-Kuramoto Model.*
   *Significance:* Rigorous mathematical formalization of Boyd's OODA via coupled oscillators; modeling phase disruption from an agile adversary.
5. **Shinar, J. & Glizer, V. Y. (1999, 2000).** Pursuit-evasion games with delayed information.
   *Significance:* Information delay strictly bounds game value; foundational for "tempo deficit" mathematics.
6. **Kuh, A., Petsche, T. & Rivest, R. (1997).** Upper bounds on generalization error under random drift.
   *Significance:* The closest existing nontrivial-exponent result ($\gamma^{2/3}$ for conservative trackers); structurally adjacent to AAT's $b=2$ / $b=3/2$.
7. **Khazraei et al. (2022).** *Stealthy attacks on perception-based control systems.*
   *Significance:* The cleanest formal statement linking estimation quality and attack vulnerability — adjacent to AAT's opacity-as-dual-of-observation-quality framing.
8. **Bai et al. (2017).** *Data-Injection Attacks in Stochastic Control Systems: Detectability and Performance Tradeoffs.*
   *Significance:* KL-based stealth definitions; detectability-performance tradeoff; nearest existing formal opacity-style result.

---

## 3. Conclusion on Novelty & Overlap

The literature has rich antecedents for tempo-as-decisive, delayed-information games, self-reinforcing degradation, stealth/detectability tradeoffs, and OODA-style synchronization. AAT does not invent any of these.

**Where AAT actually contributes:**

1. **Closed-form superlinear scaling exponents (theorem-grade math; the strongest math novelty on this row).** AAT proves the adversarial mismatch ratio scales as $\mathcal T_A^2 / \mathcal T_B^2$ under deterministic drift (Model D) and $\mathcal T_A^{3/2} / \mathcal T_B^{3/2}$ under stochastic noise (Model S) — explicit closed-form exponent regimes. The structural origin is the template's $1/\alpha$ vs $1/\sqrt{\alpha}$ disturbance-model split propagated through the destabilization-negation step. The closest existing ancestry (Kuh-Petsche-Rivest 1997's $\gamma^{2/3}$ scaling for conservative trackers) is in the same territory but a different exponent. This elevates the OODA loop from strategic heuristic to quantitative law with named exponents. Nash-style: new theorem-grade result using established sector-condition machinery.

2. **Signed-coupling unification (architectural-synthetic novelty).** The disturbance decomposition in `#der-adversarial-destabilization` uses **the same mathematical template with opposite signs on the coupling term** for cooperation and adversariality: allies reduce effective disturbance or improve update tempo; adversaries increase effective disturbance through coupling terms proportional to their tempo. This is stronger than "interactions can help or hurt" — it lets one derive common persistence conditions, common reserve logic, and common tempo accounting for cooperative and adversarial cases. The synchronization literature (Kalloniatis et al., Zup20, Ahe21) has neighboring ideas but does not work out the signed-coupling move across tempo, reserve, and destabilization.

3. **The four-regime recipient-side classification (architectural novelty; the memo's "highest novelty candidate" for this row).** Most multi-agent frameworks treat coupling as a scalar coefficient — the emitter-side view. `#der-interaction-channel-classification` names what that scalar hides: events of identical magnitude can sit in any of the four regimes (informative update / magnitude shock / structural shock / ambient erosion) with structurally different repairs. The Regime II-b (structural shock) case is especially load-bearing — more tempo does not help; the repair is *structural adaptation*, a different model class (per `#result-structural-adaptation-necessity`). The Regime III (ambient erosion) case is the framework's structural reason that DDoS-of-low-priority-alerts is a real attack rather than just inconvenience. The four-way decomposition is not found as an articulated framework in the search literature.

4. **Effects-spiral as joint-Jacobian eigenvalue condition + resource-bounded destabilization (two theorem-grade paths).** Path A: `#deriv-strategic-composition` §Discussion gives the symmetric formulation $\max \mathrm{Re}(\lambda_{\max}(\nabla F)) > 0$ on the joint best-response field. Path B: `#der-resource-bounded-destabilization` *closes* the effects spiral by a different channel — the agent's own correction rate, not the adversary's coupling. The hard-budget agent ($r_{\mathcal B} = 0$) self-depletes to **certain finite-time destabilization** against even a *constant*-effectiveness adversary; the static persistence inequality holding at $t=0$ does not prevent this. This is a substantive new result: degradation does not only worsen performance, it changes the coupling environment so that the adversary's future tempo becomes more effective (Path A) or the agent's own correction rate drains below threshold (Path B).

5. **Opacity-as-dual-of-observation-quality + tempo advantage (architectural novelty).** `#der-agent-opacity` treats opacity as the dual of observation quality and lets it modulate tempo advantage. The neighboring stealth literature (Huang et al., Bai et al., Sui et al., Khazraei et al.) gives strong adjacent ideas but does not package opacity as a *dual quantity* tied to the same disturbance-and-tempo machinery as observation-side constructs.

6. **Regime-I-with-adversarial-content (architectural novelty).** A sign-chosen misinformation injection on the log-odds signal — exploiting $B$'s openness to informative updates — is an adversarial move that the scalar emitter formulation cannot express. Surfaced by the recipient-side decomposition.

**AAT-native methodological inventions on this row:**
- The signed-coupling decomposition unifying cooperation and adversariality.
- The closed-form $b = 2$ / $b = 3/2$ exponent regimes (Model D / Model S).
- The four-regime recipient-side classification with three independent boundary conditions (sector / model-class / observability).
- The opacity-as-dual-of-observation-quality packaging.
- The resource-bounded destabilization closure of the effects spiral via correction-rate decay.
- The composite persistence condition partitioning effective disturbance into external + closure-defect + adversarial-coupling components.

**Where AAT does *not* claim novelty:**
- The OODA loop (Boyd 1986).
- Delayed-information differential games (Shinar-Glizer).
- Channel-rate floors for stabilization (Sahai-Mitter, Nair-Evans, Tatikonda-Mitter).
- Nontrivial scaling under drift (Kuh-Petsche-Rivest, Widrow-Stearns).
- Self-reinforcing degradation as cascade (Hubbard-Kott-Martin, Hancock-Warm, Hockey).
- Stealth/detectability tradeoffs in CPS (Bai et al., Sui et al., Khazraei et al.).
- The signed-coupling idea in isolation (the synchronization literature has neighbors).

**Epistemic status of the load-bearing segments.**
- `#der-adversarial-destabilization` is `status: conditional` — Model D and Model S thresholds are *exact* under their coupling assumptions; the asymmetric coupling-treatment treats $\mathcal T_A$ as exogenous. The effects-spiral *corollary* in this segment is `discussion-grade` (the $\gamma_A(\lVert \delta_B \rVert)$ functional form is not formalized).
- `#deriv-strategic-composition` is `status: conditional` — the joint-Jacobian eigenvalue condition for the spiral is derivation-grade in the symmetric formulation (sub-scope $\alpha'$).
- `#der-resource-bounded-destabilization` is `status: conditional` on (A-cost), (A-gate) of `#form-resource-budget`; the hard-regime $r_{\mathcal B} = 0$ certain-finite-time-destabilization result is *derived*.
- `#der-interaction-channel-classification` is `status: conditional` — the four-regime classification is derivation-grade under stated boundary conditions.
- `#result-adversarial-tempo-advantage` and `#result-adversarial-exponent-regimes` give the closed-form exponent regimes; the simulation results corroborate the analytical scaling.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **High.** The $b = 2$ / $b = 3/2$ exponent derivations (closed-form, Nash-style); the destabilization thresholds (Models D and S, exact under coupling assumptions); the resource-bounded certain-finite-time-destabilization theorem; the joint-Jacobian eigenvalue condition for the effects spiral; the four-regime classification with three independent boundary conditions. Multiple substantive theorem-grade derivations.
- *Arch Novelty:* **High.** Signed-coupling unification, four-regime recipient-side classification, opacity-as-dual, resource-bounded closure of the effects spiral.
- *Synth Novelty:* **High.** Unifies delayed-information games, communication-constrained control, tracking-under-drift, self-reinforcing degradation, and stealth-detectability tradeoffs into one signed-coupling persistence framework.
- *Appl Novelty:* **Some.** Direct relevance to LLM-agent adversarial robustness (Regime III cognitive DDoS, Regime II-b structural shock requiring class change). Military / cyber-physical security applications.
- *Impact:* **High.** Per the meta-summary's Part 2 — proving that tempo advantage translates to *squared* mismatch advantage under drift and $3/2$ under noise "elevates the OODA loop from a strategic heuristic to a quantitative law of physics." The signed-coupling and four-regime moves give multi-agent adversarial-robustness work a cleaner vocabulary. The resource-bounded destabilization theorem is a structural alignment-relevant result: hard-budget agents are vulnerable to constant-effectiveness adversaries regardless of static persistence margins.
