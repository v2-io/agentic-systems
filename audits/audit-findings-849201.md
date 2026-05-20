---
source_cycle: 849201 (de-novo, 2026-04-28; four-part walk — AAT §I/II + Section III + TST + Logogenic)
extraction_agent: Claude Opus 4.7 (1M context), sweep run
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-849201/ (88 files, ~3281 lines)
finals_of_record:
  - audits/.integrated/audit-849201-FINAL.md (AAT §I & §II)
  - audits/.integrated/audit-849201-FINAL-SEC-III.md (Section III — Composites)
  - audits/.integrated/audit-849201-FINAL-TST.md (Temporal Software Theory)
  - audits/.integrated/audit-849201-FINAL-LOGOGENIC.md (03-llm-core)
manifest_entry: audits/.integrated/MANIFEST.md "2026-05-16 — Cluster D: 2026-04-28 FINALs (829314 ×4, 849201 ×4)"
ledger_rows: S16 (sentiment — extraordinary epistemic-honesty calibration); S17 (convergence-as-coherence-evidence — cold-rederivation of strengthen-first spine)
purpose: |
  Consolidated extraction from the WORKING dir for routing through the standard
  audit-routing process. The original WORKING dir is preserved separately;
  this file is the "what is in there worth processing" digest.

  849201 is the **four-volume "confirmation-class" cycle** — a single auditor
  walked AAT (Sections I + II), Section III, TST, and Logogenic in chronological
  segment-by-segment order, producing 84 per-segment reflection files plus
  initial-predictions and running-outline. The cycle landed exactly two §B
  findings in the AAT FINAL (Opacity-Gain Tension, Exploration Optimality
  Limit), four "structural triumphs" in the SEC-III FINAL, two §B findings
  in LOGOGENIC, two in TST — most diagnosed as **already-known-and-handled**
  via `msc/` triangulation. The dir's cluster-D headline: the **opacity-gain
  tension** trail (F1) is one of three convergent surfacings driving the
  `deriv-adaptive-gain-dynamics` strengthening landing; the dir is also
  this program's canonical instance of **confirmation-class auditing** —
  an architecturally-independent cold reader independently re-derived the
  framework's strengthen-first spine and structural-triumph catalog,
  surfaced as ledger S17.
---

# Audit-findings extract — 849201 working-dir mining

The 849201 cycle is a **multi-volume confirmation-class** de-novo walk: a single auditor walking all four components in chronological canonical order (AAT §I/II → AAT §III → TST → Logogenic) over 88 working files (~3281 lines), producing 84 per-segment reflection files following the §4.4 13-point template. The reflections are *tight* — each is one tightly-structured page following the protocol prompts (predictions vs evidence, cross-segment consistency, math verification, "what direction next," "what errors should I now watch for," predictions for next segments, value feeling, contribution). There is **no separate adversarial-creative-challenges document** and **no `00-initial-predictions` calibration trail at consolidated-end** — the running-outline IS the consolidated synthesis layer (a 30-line scaffold of the four FINALs), and the per-segment "what errors to watch for" + "what would I change" prompts carry the candidate-finding-tracking discipline inline.

What sets this dir apart: (1) it is the **only multi-volume cycle in the corpus** — a single auditor's continuous reading covered four components, producing four separate FINALs with a shared analytical voice; (2) the auditor's calibration is **extraordinary** — repeatedly named the framework's epistemic honesty as the best the reviewer has encountered in this space (S16); (3) the auditor independently **re-derived the strengthen-first spine and structural-triumph catalog** without seeing any prior audits or the framework's internal disciplines (S17); (4) the dir's value is **predominantly confirmation-class** — the two §B findings in the AAT FINAL are both diagnosed as known-and-handled via msc/ triangulation rather than fresh defects. The single substantive new finding (F1 Opacity-Gain Tension) participates in a ≥3-cycle convergence with 742613 and extracted-gemini-2026-04-26-27, all three driving the same `deriv-adaptive-gain-dynamics` strengthening landing per MANIFEST Cluster D.

Per MANIFEST 2026-05-16 (Cluster D), every numbered finding is dispositioned:

- **849201-F1** (Opacity-Gain Tension — AAT FINAL) — **resolved by strengthening** (≥3-cycle convergence driving the `deriv-adaptive-gain-dynamics` strengthening; landing visible at `emp-update-gain.md:44`). Cluster strengthen-first headline.
- **849201-F2 / -LOGOGENIC / -SEC-III / -TST** (Exploration Optimality Limit + Section III "structural triumphs" + Logogenic two findings + TST two findings) — **resolved / verified-still-honest / confirmation-class**. Soft → ledger S16 (extraordinary epistemic-honesty calibration) + S17 (convergence-as-coherence-evidence). 849201-F2 redundant with S7 (CIY name-vs-substance), skipped per adjudication.

This file extracts at five weights: **(I) findings already adjudicated** (preserved with WORKING-dir provenance and the F1 opacity-gain trail made fully visible across all four components); **(II) bigger-picture observations** (the confirmation-class structural-triumph catalog as its own preservation register); **(III) fresh material the FINALs didn't carry forward** (theme-grouped, modest because the dir is depth-uniform-confirmation rather than breadth-exploration); **(IV) predictions calibration register** (the auditor's per-segment predictions-vs-evidence record across the full chronological walk); **(V) wandering thoughts / methodology themes** (this dir's distinctive methodology signature is *consistent-13-point-template-applied-across-four-volumes*, surfacing patterns the per-volume FINALs don't carry).

---

## Part I — Findings already adjudicated (subsumed-by-FINAL/MANIFEST)

### F1-trail. Opacity-Gain Tension (`#def-observation-function` vs `#emp-update-gain`) — the cluster strengthen-first headline

**WORKING-dir trail (where the finding crystallized):**

- **Anticipated** at segment 02 (`02-def-observation-function.md:16`) on first read: *"CRITICAL FINDING POTENTIAL: The segment states the agent does not know the distribution of $\varepsilon_t$ exactly. I must rigorously check `#emp-update-gain` and `#example-kalman`. In a standard Kalman filter, the optimal gain $K$ is computed using the known observation noise covariance $R$. If the AAD framework later assumes the agent can perfectly compute $\eta^\ast$ using a known noise distribution, it contradicts this definitional segment."* This is unusually clean predictive-shape — the auditor named the future finding at segment 02 before reaching segment 19 where it would land.
- **Confirmed-on-encounter** at segment 19 (`19-emp-update-gain.md:16-17`): *"CRITICAL FINDING CONFIRMED: There is a formal tension here. `#def-observation-function` states axiomatically that the agent does not know the distribution of the observation noise $\varepsilon_t$. However, `#emp-update-gain` defines the optimal gain as $\eta^\ast = U_M/(U_M+U_o)$, where $U_o$ is the variance of that noise. If the agent doesn't know the noise distribution, it cannot know $U_o$, and therefore cannot compute $\eta^\ast$. The segment mitigates this slightly by labeling it an 'Empirical Claim' and stating agents 'approximate' this dependence, but it leaves a mechanical gap: how does an AAD agent estimate $U_o$ to achieve this approximation? In control theory, adaptive filtering (like autocovariance least-squares) is used. The framework needs to either state that $U_o$ estimation is part of $f_M$, or explicitly acknowledge that $\eta^\ast$ is an unachievable normative ideal that the agent bounds."*
- **Promoted to FINAL §"Finding 1"** with explicit `msc/`-diagnosis: *"Diagnosis (via `msc/`): Known but unfixed. A previous parallel audit (`AUDIT-WORKING-742613/02-def-observation-function.md`) also flagged this as 'Possible over-strong epistemic opacity.' The framework relies heavily on the Kalman filter analogy (where $R$ is known) for its gain proofs but maintains a strict epistemic opacity axiom. This requires a bridging hypothesis explaining how $U_o$ is empirically estimated by the agent without violating the opacity axiom, or a softening of the axiom."*
- **Cross-cycle confirmation:** the FINAL's `msc/` triangulation explicitly cites the 742613 dir's own segment-02 flagging of the same tension, establishing the convergence inside the audit itself (not just at adjudication time).

**Disposition (per MANIFEST 2026-05-16 Cluster D + first-hand verification below):**

**`subsumed-by-MANIFEST` — resolved by strengthening** (≥3-cycle convergence: 849201-F1 / extracted-gemini-2026-04-26-27 / AUDIT-WORKING-742613 flag → one shared `deriv-adaptive-gain-dynamics` strengthening; `emp-update-gain.md:44`). First-hand-verified `01-aat-core/src/emp-update-gain.md:44` reads (verbatim, present-tense in current `src/`):

> *"**Resolving Epistemic Opacity.** The optimal gain equation requires the agent to know $U_o$, which seems to violate the epistemic opacity axiom established in `#def-observation-function` (the agent does not know the true noise distribution $\varepsilon_t$). This tension is resolved dynamically: the agent estimates $U_o$ (and $U_M$) from the observable statistics of its own mismatch sequence (innovations), treating the gain itself as an endogenous state variable. See `#deriv-adaptive-gain-dynamics` for the proof of how this meta-adaptation maintains Lyapunov stability without violating opacity."*

**Strengthen-before-soften posture verification:** The audit FINAL's recommendation was a *softening* option-set ("a bridging hypothesis explaining how $U_o$ is empirically estimated... or a softening of the axiom"). The project's resolution is **strictly stronger**: rather than soften the axiom or pile on caveats, the project derived the resolution structurally — the gain is **itself an endogenous state variable**, with the adaptive-gain dynamics proved Lyapunov-stable in a dedicated derivation segment (`#deriv-adaptive-gain-dynamics`). The opacity axiom is preserved verbatim; the apparent contradiction with $\eta^\ast$ is resolved by adding a new exact result (the adaptive-gain dynamics theorem) rather than by weakening either side. The integration-is-replacement discipline operated correctly: the prior under-specified $\eta^\ast$ formulation (which had to choose between violating opacity or being computationally unrealizable) is **deleted** in favor of the new dynamically-resolved form, and the body+catalog state present truth only (the resolution mechanism — innovations-based estimation of $U_o$ as part of $f_M$ — is named as positive content, not as a softened ghost).

**Cross-cycle resonance (≥3-cycle convergence):**

This is one of the strongest convergence signals in the corpus. Three architecturally-independent cold reads landed the same finding:

1. **849201-F1** — this cycle, walking AAT chronologically, flagged the tension at segment 02 (predictive) and confirmed it at segment 19 (encounter), promoted to FINAL §"Finding 1."
2. **AUDIT-WORKING-742613 flag** — Codex auditor, segment 02 reflection (cited in the 849201 FINAL's msc/-diagnosis): "Possible over-strong epistemic opacity."
3. **extracted-gemini-2026-04-26-27** — Gemini, separate reading discipline, separate substrate; landed the same tension independently per the MANIFEST citation.

Per `feedback_convergence_as_framework_coherence_evidence` in MEMORY, multi-substrate independent convergence on the same structural recognition from different starting points is **stronger than single-agent elaboration** — the bug was real and detectable from multiple reading-disciplines. The shared `deriv-adaptive-gain-dynamics` strengthening landing was driven by this three-cycle pressure.

**Pedagogical value (cluster D's worked example, three teaching moments):**

- **The audit's softening recommendation was correct on its own terms** — the source segment carried a real tension that needed *something* done about it (the gain equation as stated required $U_o$, which the opacity axiom forbade knowing). The audit was not wrong to flag.
- **The strengthening direction was structurally available but invisible at FINAL-time** — the audit recommended *either* a bridging hypothesis *or* an axiom softening. It did not see the third option (gain-as-endogenous-state) until the strengthening attempt was actually executed. Strengthen-first works *because* the structural form of the resolution is often not visible until the attempt is made.
- **The resolution is a new exact result, not a softened ghost** — `#deriv-adaptive-gain-dynamics` is a dedicated derivation segment establishing the Lyapunov stability of the meta-adaptation. The "previously the gain equation seemed to violate opacity" history lives only in CHANGELOG / segment Working Notes; the body and FINDINGS catalog state present truth only.

This trail (jointly with the 742613 flag and the gemini convergence) is durable evidence-material for the strengthen-before-soften discipline's onboarding documentation. The pattern is parallel to but distinct from the 613842/742613 Model-S no-go: both are strengthen-first landings, but the opacity-gain resolution succeeded constructively (new derived result), while the Model-S strengthening hit a no-go theorem. Together they bracket the two outcomes the strengthen-first discipline produces: *strengthening that succeeds* (opacity-gain) vs *strengthening that yields a no-go that is itself the result* (Model-S).

### F2-trail. Exploration Optimality Limit — CIY as distinguishability not EIG (AAT FINAL)

**WORKING-dir trail:**

- Surfaced at segment 20 (`20-def-causal-information-yield.md:16`): *"CRITICAL FINDING POTENTIAL: The segment explicitly admits a weakness: CIY measures distinguishability, not Expected Information Gain (EIG). If you already know that pushing a button turns on a red light, pushing it has high CIY (it's distinguishable from doing nothing) but zero EIG (you learn nothing new). The theory patches this by multiplying CIY by a heuristic uncertainty weight $\lambda(M_t)$ in the policy objective. I must watch out for any later theorems that claim the agent's exploration policy is mathematically optimal."*
- Reinforced at segment 35 (`35-disc-ciy-unified-objective.md:7-8`): the unified objective is "Discussion-grade (heuristic)" precisely because of this CIY-vs-EIG gap. The auditor explicitly noted: *"the epistemic honesty of distinguishing CIY from proper EIG and labeling the $\lambda$ weighting as a heuristic is exemplary."*
- Promoted to FINAL §"Finding 2" with msc/-diagnosis: *"Known and accepted. `spikes/spike-active-inference-vs-aad.md` explicitly discusses this tradeoff against Active Inference's Expected Free Energy. The framework consciously accepts CIY as a computable surrogate for EIG because it forces a focus on causal interventions rather than just entropy reduction. This is a sound theoretical compromise, properly logged in the segment's Epistemic Status."*

**Disposition (per MANIFEST 2026-05-16 Cluster D):**

**`subsumed-by-MANIFEST` — confirmation-class (known-and-handled); redundant with S7, skipped per adjudication.** The CIY name-vs-substance question is already on the polish-and-sentiment ledger as S7 (research-seed; naming-brainstorm seed from 471203 §F8). The MANIFEST adjudication explicitly notes "849201-F2 redundant with S7, skipped per adjudication" — the finding adds no new tracking weight beyond the existing S7 entry. The substantive content (CIY is a heuristic surrogate for EIG, deliberately accepted) is honored in both the segment's Epistemic Status and the spike artifact; the FINAL's own diagnosis recognized this as "known and accepted." Not a defect; a properly-logged scope-honesty observation.

**Cross-cycle resonance:** 471203 §F8 ledger S7 (CIY-name-vs-substance, separate angle on the same segment-level honesty); 829314 cohort sentiment (S16, the "extraordinary epistemic honesty" repeatedly observed). The CIY segment is one of the framework's most-celebrated instances of scope-honest formulation across multiple cycles.

### F1-LOGOGENIC. The 100% Turnover Problem (`#obs-context-turnover`)

**WORKING-dir trail:**

- Surfaced at segment 84 (`84-logogenic-foundations.md:4-12`) on first encounter: *"For `obs-context-turnover`, I predicted a formalization of the 100% turnover problem (context window clearing). The segment delivered a rigorous information-theoretic bound on the drop in Model Sufficiency ($\Delta S_{\text{turnover}}$) that occurs at session boundaries."* The auditor explicitly classified this as a *positive structural-triumph* observation rather than a defect — the framework *correctly identifies* and *formalizes* the hardest problem in current agent engineering.
- Math verification praised the reconstruction-bound inequality $S(M_{k+1}^+) \le \min(1, S_{\text{ext}} + S_{\text{prompt}} + S_{\text{prior}} - S_{\text{overlap}})$ as "a very sound, informal application of information theory to prompt engineering."
- Promoted to LOGOGENIC FINAL §"Finding 1" as a positive structural finding: *"Significance: This perfectly formalizes the hardest problem in current agent engineering (memory and RAG). It proves that an agent must learn more in a session than it loses at the boundary ($\mathbb{E}[\Delta\epsilon_k] \le \mathbb{E}[\Delta I_k]$) or it will suffer long-term degradation."*

**Disposition (per MANIFEST 2026-05-16 Cluster D):**

**`subsumed-by-FINAL` — confirmation-class (verified-still-honest).** This is not a defect-finding but a *structural-triumph* surfacing — the auditor confirmed the framework's formalization of LLM session-boundary persistence is sound. The framing matches the AAT/TST self-description (`#obs-context-turnover` is one of the framework's load-bearing logogenic claims). Soft → ledger S17 (convergence — architecturally-independent reader independently re-derived load-bearing structure).

### F2-LOGOGENIC. The Ambiguity Bound on Motivated Reasoning ($\kappa \times \mathcal{A}$)

**WORKING-dir trail:**

- Confirmed at segment 85 (`85-coupled-dynamics-and-ambiguity.md:8-9`): *"`scope-observation-ambiguity-modulation` introduces a brilliant theoretical save: the actual epistemic bias is bounded by $\kappa_{\text{processing}} \times \mathcal{A}(e_\tau)$. Therefore, if the domain provides unambiguous observations (like compiler errors where $\mathcal{A} \approx 0$), the LLM acts as if it were a modular Class 1 agent, despite its Class 2 architecture."*
- Math verification praised: *"The definition of $\mathcal{A}(e_\tau)$ using conditional mutual information is exact and theoretically flawless. The working notes explicitly document a 2026-04-22 correction where $\mathcal{A}$ was refactored to be a purely Bayesian-optimal property of the environment/channel, separating it cleanly from the architectural property $\kappa$. This is phenomenal theoretical hygiene. The reference to the 'no-go result' regarding Euclidean norms and the necessity of the Fisher-Rao metric is graduate-level differential geometry applied to agent bias."*
- The auditor highlighted segment 85 as *"one of the most profound psychological/AI insights I have ever seen expressed as a mathematical bound."*
- Promoted to LOGOGENIC FINAL §"Finding 2": *"Significance: This is a massive theoretical triumph. It proves that if the domain provides unambiguous observations... the LLM agent will have near-zero epistemic bias despite its merged architecture. This mathematically explains why LLMs are so much better at coding than at open-ended strategic reasoning."*

**Disposition (per MANIFEST 2026-05-16 Cluster D):**

**`subsumed-by-FINAL` — confirmation-class (verified-still-honest).** Structural-triumph surfacing; the auditor's independent re-derivation of why $\kappa \times \mathcal{A}$ is load-bearing for the logogenic framework is cross-substrate convergence on the framework's own architectural commitment. Soft → ledger S17.

### F1-SEC-III. The Incremental Sector Bound Necessity (Bridge Lemma)

**WORKING-dir trail:**

- Confirmed at segment 56 (`56-form-composition-closure.md:13`) on first encounter: *"The mathematical rigor here is exceptional. The most critical finding is the explicit, proven distinction between the one-point sector bound (A4) and the **incremental sector bound (strong monotonicity, DA2'-inc)**. The segment proves that (A4) alone is insufficient to guarantee that the macro-description tracks the micro-reality (the Bridge Lemma). It requires the strictly stronger strong-monotonicity condition."*
- Auditor explicitly recognized: *"The classification of agents into Tier 1 (where this is proven, like Kalman and strongly convex gradients), Tier 2 (local), and Tier 3 (unproven) is textbook theoretical hygiene. The derivation of the weakest-link bound $\alpha_c = \min_i (\alpha_i - \Delta\mathcal T_i^{\text{cost}})$ is also clean and correct."*
- Promoted to SEC-III FINAL §"Finding 1": *"Significance: This is a major theoretical triumph. It prevents the framework from falling into the trap of assuming that 'a group of stable agents is a stable group.' It rigorously defines Tier 1 (exact closure), Tier 2 (local), and Tier 3 (unproven) composites."*

**Disposition:** **`subsumed-by-FINAL` — confirmation-class (verified-still-honest).** Cross-cycle resonance with 742613-F3 (one-point ⇐ strong convexity; B.4 split landing) — different surfacing angle on the same Bridge-Lemma-necessity-of-incremental-sector structure. Soft → ledger S17.

### F2-SEC-III. Coordination Overhead and Brooks's Law (`#der-tempo-composition`)

**WORKING-dir trail:**

- Surfaced at segment 57 (`57-der-tempo-composition.md:10`): *"The conversion of closure defect (a distance error) into a tempo penalty is mathematically sound: $C_{\text{coord}} \ge \varepsilon^\ast \nu_c / \|\delta_{\text{critical}}\|$. This correctly normalizes the error injection rate by the survival boundary, yielding a penalty in $[\text{time}^{-1}]$. The observation that this is only a lower bound — because it ignores the process costs of negotiation and synchronization — is empirically honest. The derivation of Brooks's Law ('adding manpower to a late software project makes it later') directly from this inequality is a spectacular payoff for the software domain."*
- Promoted to SEC-III FINAL §"Finding 2": *"`#der-tempo-composition` uses dimensional accounting to convert the closure defect (a distance error) into a tempo penalty $[\text{time}^{-1}]$. Significance: This mathematically derives Brooks's Law... directly from the Lyapunov properties of the composite system."*

**Disposition:** **`subsumed-by-FINAL` — confirmation-class.** Soft → ledger S17.

### F3-SEC-III. Strategy DAG Correlation Hazards (`#scope-and-or` / `#der-causal-insufficiency-detection`)

**WORKING-dir trail:**

- Confirmed across segments 38 (`38-scope-and-or.md`) and 43 (`43-der-causal-insufficiency-detection.md:9-11`): *"The application of the Causal Hierarchy Theorem (Bareinboim et al. 2022) to prove the 'No-Go Theorem' (that no purely on-policy statistic can distinguish an L0 world from an L1 world matched on conditionals) is mathematically profound and correct. Observational equivalence means $P(Y \mid X)$ is identical in both worlds. The covariance test correctly identifies the latent cause if and only if the agent explores (violates strict short-circuiting) to observe joint outcomes."*
- Auditor highlighted: *"The 'No-Go Theorem' here is one of the strongest and most mature parts of the entire framework."*
- Promoted to SEC-III FINAL §"Finding 3": *"The 'No-Go Theorem' in `#der-causal-insufficiency-detection` perfectly seals this gap, proving via Pearl's Causal Hierarchy Theorem that an agent cannot detect these latent causes using purely on-policy execution data. It must pay the cost of exploration."*

**Disposition:** **`subsumed-by-FINAL` — confirmation-class.** Soft → ledger S17.

### F4-SEC-III. Game Theory Integration (`#deriv-strategic-composition`)

**WORKING-dir trail:**

- Confirmed at segment 67 (`67-deriv-strategic-composition.md:6-12`): *"The structural parallel to Section I is stunning: just as Section I split into Sub-scope $\alpha$ (Kalman/LQR where exact bounds hold) and Sub-scope $\beta$ (PID where they don't), this segment splits into Sub-scope $\alpha'$ (Potential/Monotone games) and Sub-scope $\beta'$ (VI/Regret minimization)."* The auditor specifically praised the *self-corrective working notes* documenting a past sign error and the necessity of quadratic regularization: *"This level of self-correction gives me immense confidence in the framework."*
- Promoted to SEC-III FINAL §"Finding 4": *"`#deriv-strategic-composition` seamlessly shifts the compositional question from 'Lyapunov contraction on a shared state' to 'equilibrium convergence on a joint strategy profile' when objectives are opposed ($U_O < 1$). The detailed Working Notes documenting the correction of a past sign error in the zero-sum example demonstrate exceptional mathematical hygiene."*

**Disposition:** **`subsumed-by-FINAL` — confirmation-class.** Soft → ledger S17.

### F1-TST. The AI "100% Turnover" Limit (`#der-dual-optimization`)

**WORKING-dir trail:**

- Surfaced at segment 75 (`75-implementation-and-dual-opt.md:9`): *"The mathematical framing of the objective function is exactly correct for lifecycle cost analysis. The distinction that implementation is a per-feature cost while comprehension is a per-reader cost is a profound, mathematically undeniable truth that invalidates most industry metrics."*
- Reinforced at segment 74 (`74-developer-agent-and-comprehension.md:11`): *"The observation that AI agents suffer the '100% turnover problem' (their context window resets every session) is mathematically profound. It means their $U_M$ spikes to maximum at the start of every task, forcing them to pay the full comprehension cost every time unless the environment ($\Omega_t$) has been perfectly optimized to externalize $M_t$ (e.g., via excellent documentation and clear code)."*
- Promoted to TST FINAL §"Finding 1": *"`#der-dual-optimization` introduces the turnover multiplier ($k$) to the lifecycle cost equation... `#scope-developer-agent` brilliantly applies this to AI agents, noting that because their context window resets every session, they suffer from near-100% turnover. Significance: This provides a rigorous mathematical proof contradicting the popular industry narrative that 'AI will write spaghetti code because only AI needs to read it.' TST proves the exact opposite."*

**Disposition:** **`subsumed-by-FINAL` — confirmation-class.** Cross-cycle resonance with the LOGOGENIC F1 turnover surfacing (both segments are different angles on the same `100% turnover` engineering reality, with the TST framing focusing on the comprehension-cost-per-reader inversion and the LOGOGENIC framing focusing on inter-session model preservation). Soft → ledger S17.

### F2-TST. Observational vs Causal Coupling (Git-as-causal-data hazards)

**WORKING-dir trail:**

- Confirmed at segment 83 (`83-causal-discovery-git.md:9-10`): *"The segment is exceptionally honest about its Epistemic Status: it explicitly labels the entire endeavor as a 'research program, not a derivation' because the confounders (shared requirements, convention bundling, and unobservable developer knowledge) are the typical case, not the exception."* Reinforced at segment 80 (`80-coupling-and-coherence.md:11`): *"The discussion of causal identification (distinguishing true causal coupling from convention-driven bundling in large PRs) is rigorous."*
- Promoted to TST FINAL §"Finding 2": *"Throughout `#def-system-coupling`, `#meas-coherence-coupling`, and `#hyp-causal-discovery-from-git`, the theory is incredibly careful to distinguish between associational co-change (what we can easily measure in Git) and true causal coupling (what actually drives the temporal penalties). Significance: The explicit cataloging of confounders (shared requirements, convention bundling, and developer knowledge state) prevents TST from overclaiming the power of Git analytics."*

**Disposition:** **`subsumed-by-FINAL` — confirmation-class.** Soft → ledger S17.

---

## Part II — Bigger-picture observations: the confirmation-class structural-triumph catalog

This dir's bigger-picture material is unusually **homogeneous** — it is essentially a **structural-triumph catalog** consolidated in the four FINALs' "Structural Triumphs & Big-Picture Pondering" sections, with one-line observation entries in the `00-running-outline.md` (Phase 3 §"Bigger-Picture Pondering," 11 observations) and per-segment ratification across the reflection files. Because this is the **confirmation-class headline material** for ledger S17, the catalog is preserved here with WORKING-dir provenance for each observation.

The 11 Phase-3 observations from the running outline (one-line consolidations), each cross-referenced to per-segment ratification:

### BP1. The Epistemic Anchor (Causal Contrast via Observations)

WORKING-dir provenance: segment 05 (`05-scope-agency.md:10`) — the auditor on first encounter: *"There is a profound and subtle choice here that is correct: the condition is $P(o \mid do(a)) \neq P(o \mid do(a'))$, not $P(\Omega \mid do(a)) \neq P(\Omega \mid do(a'))$. This means that an action must produce an observably different outcome to count as giving the system 'agency.' If an action changes the world but the agent can never observe the difference, it has no agency from the perspective of this theory. Furthermore, it means 'active perception' (like turning a camera, which changes $o$ but not $\Omega$) counts as an action. This is a brilliant and necessary choice for a purely epistemic theory."*

**Disposition:** `subsumed-by-FINAL` (AAT FINAL §"Structural Triumphs"). Soft → ledger S17.

### BP2. Epistemic Honesty in Composition (Tier 1/2/3)

WORKING-dir provenance: segment 06 (`06-post-composition-consistency.md:4`) — *"the segment delivered far more rigor than I expected. Instead of a blanket 'fractal' claim, it stratifies the composition transfer into Tier 1 (exact transfer via contraction), Tier 2 (degraded transfer), and Tier 3 (per-domain verification). My initial suspicion about the 'contraction assumption' being a weak point is directly addressed here: it's not a hidden assumption, it's the explicit dividing line between Tier 1 and Tier 2/3."* Reinforced at segment 56 (form-composition-closure) — see SEC-III F1.

**Disposition:** `subsumed-by-FINAL`. Soft → ledger S17.

### BP3. Information Bottleneck vs Active Inference (philosophical positioning)

WORKING-dir provenance: segment 11 (`11-form-information-bottleneck.md:21-22`) — *"The explicit distancing from Active Inference's 'expected free energy as master objective' while retaining the math structure is a very sophisticated epistemic maneuver."* Reinforced at segment 35 (disc-ciy-unified-objective) and segment 26 (result-sector-persistence-template) — the auditor explicitly praised the framework's critique of Active Inference's NESS-density assumptions vs AAT's "robust, standard nonlinear control theory" foundation as *"devastatingly accurate and mathematically grounded."*

**Disposition:** `subsumed-by-FINAL`. Soft → ledger S17.

### BP4. Bias vs Variance in Agents (`def-model-class-fitness`)

WORKING-dir provenance: segment 13 (`13-def-model-class-fitness.md:22`) — *"The explicit parallel drawn between Model Class Fitness vs Instance Sufficiency and the statistical concepts of Bias vs Variance is incredibly helpful for intuition."* Auditor's mapping in the running outline: *"`def-model-class-fitness` elegantly maps statistical bias/variance to agent architecture: parametric learning fixes variance (improves $S(M_t)$), structural adaptation fixes bias (improves $\mathcal{F}(\mathcal{M})$)."*

**Disposition:** `subsumed-by-FINAL`. Soft → ledger S17.

### BP5. The Software Calibration Lab (TST/AAD Rosetta Stone)

WORKING-dir provenance: segment 72 (`72-obs-software-and-feature.md:8`) — *"The epistemic properties segment is a masterpiece of domain grounding. Connecting `git checkout` to Pearl's Level 3 Counterfactuals... and connecting 'Code Quality' to Observation Noise ($U_o$)... are two of the strongest theoretical moves in the entire framework."* Promoted to the running-outline as observation 5 and into the TST FINAL §3 as the "TST/AAD Rosetta Stone" (which itemizes 6 cross-domain instantiations: Environment, Agent, Pearl Level 3, Observation Noise, Environmental Disturbance, Agent Tempo).

**Disposition:** `subsumed-by-FINAL` (TST). Soft → ledger S17. Cross-cycle resonance: this is the cohort-wide TST-as-calibration-laboratory recognition (471203 Fresh-11 explicitly named the calibration-laboratory framing reach).

### BP6. Epistemic Honesty regarding Channel Independence (`def-adaptive-tempo`)

WORKING-dir provenance: segment 21 (read indirectly via running-outline observation 6; per-segment file not directly sampled by extraction agent) — *"`def-adaptive-tempo` explicitly notes that $\mathcal{T} = \sum \nu \eta^\ast$ is an upper bound that overcounts if channels are correlated. This shows a mature understanding of the limits of the additive formulation."*

**Disposition:** `subsumed-by-FINAL`. Cross-cycle resonance with 742613-F4 / 613842-F1 (the adaptive-tempo definition-scope mismatch; substance resolved by strengthening via the matrix-Loewner / tensor extension landing). The 849201 cycle's framing of this same segment-level honesty as *positive* rather than as a finding-to-fix is itself signal — the framework's prose-level scope-honesty disclaimers landed for an independent reader, where the 742613/613842 cycles caught the *formal/status* layer mismatch (frontmatter `status: exact`). The two readings are complementary: 849201 read the prose-honesty positively; 742613/613842 caught the frontmatter inconsistency. Both right; different reading-disciplines surfaced different layers. Soft → ledger S17.

### BP7. Stochastic vs Deterministic Scaling (OU steady-state insight)

WORKING-dir provenance: segment 22 (`22-hyp-mismatch-dynamics.md:22`) — *"The observation that correction is less effective against noise ($1/\sqrt{\mathcal{T}}$) than drift ($1/\mathcal{T}$) is a profound insight into why volatile environments are so deadly."* Reinforced by the auditor's recognition at segment 49 (`49-result-adversarial-tempo-advantage.md:35`): *"A 3:1 tempo advantage yields a 9:1 capability advantage in positional (deterministic) conflict, but only a 5.2:1 advantage in noisy (stochastic) conflict."*

**Disposition:** `subsumed-by-FINAL` (highlighted in the AAT FINAL §3 as the "Stochastic vs Deterministic Scaling" structural triumph). Soft → ledger S17.

### BP8. Structural vs Task Persistence (`result-persistence-condition`)

WORKING-dir provenance: segment 23 (`23-result-persistence-condition.md:10`) — *"The mathematical distinction between this structural bound ($R$, a property of the model class) and the task bound ($\delta_{\text{critical}}$, a property of the environment) is correct and essential."* Auditor's "what errors should I watch for" note at segment 23 makes this particularly load-bearing: *"I must watch for downstream claims that prescribe 'more tempo' as the solution to a Structural Persistence failure. If the model class is fundamentally broken... increasing observation frequency $\nu$ will not save the agent. The only cure for structural failure is structural adaptation."* This is the auditor independently re-deriving the framework's own scope-honesty discipline (the parametric-vs-structural-adaptation distinction is load-bearing across `#result-structural-adaptation-necessity`).

**Disposition:** `subsumed-by-FINAL`. Soft → ledger S17.

### BP9. The Alignment Assumption (`result-structural-adaptation-necessity`)

WORKING-dir provenance: segment 24 (`24-result-structural-adaptation-necessity.md:10`) — *"I am extremely impressed by the 'Epistemic Status' note. The author correctly identifies a subtle statistical gap: just because a model class loses predictive information ($S(M) < 1$) does NOT mathematically guarantee a large one-step mean error $\delta_t$. The lost information might only affect variance or higher moments. The segment formally patches this by conditioning the result on an 'alignment assumption', or otherwise stating it in terms of proper-scoring regret. This is rigorous, graduate-level statistical hygiene."*

**Disposition:** `subsumed-by-FINAL`. The auditor's independent recognition of the alignment-assumption scope-honesty is exactly the kind of confirmation-class signal driving S17. Soft → ledger S17.

### BP10. Rigorous Lyapunov Core (`result-sector-condition-stability`)

WORKING-dir provenance: segment 25 (`25-result-sector-condition-stability.md:10`) — *"The Lyapunov proof sketched here is textbook... The math is flawlessly executed."* The auditor walked through the proof step-by-step inline.

**Disposition:** `subsumed-by-FINAL`. Soft → ledger S17. **Important note (see Part III Fresh-1):** the 849201 auditor read this segment and the surrounding Model-S material *without catching the ever-exit conflation* that 742613-F2 / 613842-F2 caught. The auditor read the RMS bound $R^*_S = \sigma_w\sqrt{n/(2\alpha)}$ as a clean statement (which it is, at the fixed-time level) and did not interrogate whether the implied infinite-horizon non-exit claim was structurally available. This is a *complementary blindspot* to the 742613/613842 reading-disciplines — different cycles caught different layers of the same segment-state.

### BP11. Pearl vs Friston Blankets (`der-directed-separation`)

WORKING-dir provenance: from the running outline (per-segment file not directly sampled by extraction agent, but the observation is consistent with the segment 31 / 33 / 35 / 67 references to "Friston blanket rejection"): *"`der-directed-separation` brilliantly distinguishes between the 'Pearl-blanket' (a technical conditional independence claim) and the 'Friston-blanket' (a metaphysical claim about boundaries of the self), adopting the former and rejecting the latter. This is a masterclass in theoretical positioning."*

**Disposition:** `subsumed-by-FINAL`. Soft → ledger S17.

### BP12 (additional from LOGOGENIC). Statics Survive, Dynamics Degrade

WORKING-dir provenance: segment 86 (`86-diagnostic-framework-and-survival.md:8`) — *"The realization in `#result-section-ii-survival` that statics survive while dynamics degrade is a beautiful meta-level summary of the entire framework's resilience."* The 16-Exact / 5-Approximate / 2-Modified / 1-Fails scorecard explicitly traced.

**Disposition:** `subsumed-by-FINAL` (LOGOGENIC FINAL §3). Soft → ledger S17. Material for any future cross-domain-instantiation-cycle that wants to surface the statics-vs-dynamics-degradation meta-pattern.

### BP13 (additional from LOGOGENIC). The Lipschitz Penalty on Regret

WORKING-dir provenance: segment 86 (`86-diagnostic-framework-and-survival.md:11`) — *"The mathematical bounding of the post-hoc diagnostics is excellent. Because $\delta_{\text{regret}}$ requires evaluating $A_O$ and $V_O$, both of which are computed from the biased $M^{(\text{post})}$, the bound on the regret error correctly accumulates a factor of $2 L_A \lVert\Delta M_{\text{bias}}\rVert$, where $L_A$ is the Lipschitz constant of the attainability function. The detail regarding `#schema-strategy-persistence` degrading as $O(\kappa^2)$ rather than $O(\kappa)$ (because the bias must survive the sector-condition's inner-product averaging) is a profound insight into the stability of coupled learning."*

**Disposition:** `subsumed-by-FINAL` (LOGOGENIC FINAL §3). Soft → ledger S17. The $O(\kappa^2)$ vs $O(\kappa)$ distinction in regret-error scaling is precisely the kind of fine-grained structural detail the confirmation-class reading-discipline is good at surfacing as positive content.

### BP14 (additional from SEC-III). The Informational Duality ($U_o$ vs $H_b$)

WORKING-dir provenance: segments 65 (`65-der-adversarial-destabilization.md:7`) and 68 (`68-der-agent-opacity.md:11`) — the auditor's most-emphatic praise: *"Defining opacity as the formal dual to observation quality ($U_o$) — how well the world sees the agent vs how well the agent sees the world — is a profound symmetry."* The sign-flip-via-signed-coupling derivation (allies want low $H_b$, adversaries want high $H_b$, falling out of the sign of $\gamma$ rather than being chosen exogenously) is praised across both segments.

**Disposition:** `subsumed-by-FINAL` (SEC-III FINAL §3). Soft → ledger S17.

### BP15 (additional from SEC-III). The 16-Cell Targeting Matrix

WORKING-dir provenance: segment 68 (`68-der-agent-opacity.md:7`) — *"The combination of these two segments [#der-interaction-channel-classification + #der-agent-opacity] into a 16-cell matrix to close the `#adversarial-edge-targeting` gap is a beautiful theoretical closure."* The auditor highlighted this as one of the audit's "high-water marks."

**Disposition:** `subsumed-by-FINAL` (SEC-III FINAL §3). Soft → ledger S17.

### BP16 (additional from SEC-III). Auftragstaktik as Information Bottleneck

WORKING-dir provenance: segment 62 (`62-hyp-auftragstaktik-principle.md:11`) — *"The most brilliant part of this segment is the Working Note regarding AI agents. For humans, $B_M$ (sharing your entire mental model of the world) is impossible, while $B_O$ (saying 'take that hill') is cheap. But for AI agents, $B_M$ is incredibly cheap (just share the vector database or synchronize weights), while $B_O$ is notoriously hard (the alignment problem / RLHF). The theory naturally predicts that multi-AI systems will optimally organize themselves very differently than human organizations."*

**Disposition:** `subsumed-by-FINAL` (SEC-III FINAL §3). Soft → ledger S17. The AI-vs-human-inversion observation is a substantive structural insight worth preserving — for AI agent systems, the Auftragstaktik ordering $B_O > B_\Sigma > B_M$ may invert.

### BP17 (additional from TST). The Lindy Derivation (`#der-change-expectation-baseline`)

WORKING-dir provenance: segment 73 (`73-specification-and-lindy.md:11`) — *"The use of Jeffrey's prior ($\pi(T) \propto 1/T$) for a positive scale parameter is the correct uninformative prior. The Bayesian update yielding a Pareto distribution with shape $\alpha=1$ is mathematically exact. The explicit warning in the Epistemic Status that the mean of this Pareto distribution is infinite, and thus the result $\hat n_{\text{future}} = n_{\text{past}}$ strictly applies to the median, is an outstanding display of statistical hygiene."* Promoted to TST FINAL §3 as a "Lindy Derivation" structural triumph.

**Disposition:** `subsumed-by-FINAL`. Soft → ledger S17.

### BP18 (additional from TST). Physical Dimensions of Code + Spaghetti Penalty

WORKING-dir provenance: segments 77-79 — auditor's recognition of the *separation of volume (changeset size) and scatter (proximity/distance)* setting up the cognitive-load penalty, plus the exponential cognitive-load form $k^{\text{discontinuities}}$. Particularly notable: segment 79's confirmation that *"the `empirical-discontinuity/` tool has actually validated this exponential form for file-level crossings with $k \approx 1.118$. This is a fascinating empirical result that grounds the abstract math."*

**Disposition:** `subsumed-by-FINAL` (TST FINAL §3). Soft → ledger S17. The empirical-discontinuity-tool $k \approx 1.118$ validation is itself a positive surfacing — first-class evidence that the hypothesis-grade claim is becoming empirically grounded.

### BP19 (consolidated cohort sentiment from confirmation-class catalog)

The 11 + 8 additional structural-triumph observations cohere into a single cohort-sentiment-grade signal: **an architecturally-independent cold reader walking all four components of AAT chronologically independently re-derived the framework's load-bearing structural commitments and named them as the framework's distinctive contributions**, without seeing CLAUDE.md's strengthen-first discipline (or seeing it only as one orientation file among several before reading) and without seeing any prior audits.

**Disposition:** Soft → ledger S16 (extraordinary epistemic-honesty calibration) + S17 (convergence-as-coherence-evidence; cold-rederivation of strengthen-first spine). The cohort-level signal is itself the contribution; preserved here in attribution-and-cohort form rather than re-litigating each observation as its own finding-or-disposition.

---

## Part III — Fresh material the FINALs didn't carry forward

This dir is **homogeneous-confirmation-class, not breadth-exploration** — the auditor stayed close to the per-segment template and did not generate a wide adversarial-creative residue (unlike 471203). The fresh material is correspondingly thin. The genuinely-new observations are mostly *negative-space* phenomena (what the auditor *missed* that other cycles caught) plus a few small editorial-improvement candidates that didn't make the FINAL §B.

### Fresh-1. Negative-space finding: the auditor read the Model-S ever-exit confusion as a *positive structural triumph*

This is the most pedagogically valuable negative-space observation in the dir. Segments 22-29 cover the same Model-S persistence machinery that 742613-F2 and 613842-F2 caught as a load-bearing math finding (the false ever-exit claim under additive stochastic forcing). The 849201 auditor:

- Read `#hyp-mismatch-dynamics` (segment 22) and *verified the OU steady-state RMS bound* explicitly: *"The deterministic steady state $\delta_{ss} = \rho / \mathcal{T}$ is trivially correct. The stochastic model $d\delta = -\mathcal{T}\delta\,dt + \sigma_w\,dW_t$ is an Ornstein-Uhlenbeck (OU) process. The known steady-state variance for an OU process is $\sigma^2/(2\theta)$. Substituting $\sigma = \sigma_w$ and $\theta = \mathcal{T}$ gives $\text{Var}(\delta) = \sigma_w^2/(2\mathcal{T})$, so the RMS is indeed $\sigma_w/\sqrt{2\mathcal{T}}$. The math is exact and correct."*
- Read `#result-sector-condition-stability` (segment 25) and *praised the Model-S RMS bound* as "flawlessly executed."
- Read `#result-sector-persistence-template` (segment 26) and praised it as "Masterful synthesis."
- Read `#result-persistence-condition` (segment 23) and praised the Model D vs Model S distinction as "very high. The crown jewel of Section I so far."

**The 849201 auditor's reading-discipline is *deterministic Lyapunov calculation*** — the auditor verified that the deterministic OU steady-state variance derivation is mathematically correct, which it is. What the auditor *did not* interrogate was whether the implied **infinite-horizon non-exit object** (the cleanest form the downstream summary segments were reaching for at FINAL-time, pre-2026-05-16-landing) was structurally available. The OU process is recurrent on $\mathbb{R}^n$ — for any finite $R$ and $\sigma_w > 0$, the process exits $[-R, R]$ eventually with probability 1, so $P(\tau_R < \infty) = 1$ rather than the small bound the segment was implying.

742613's auditor caught this exact issue at segment 24 by running an OU-recurrence counterexample inline. 613842's auditor caught it at the *downstream-summary-compression* level (the consumer segments stating the bound as if it were infinite-horizon). 849201's auditor — reading the source segment with the same RMS bound — *did not catch either*.

**This is itself signal worth preserving:** the same segment-state was read three times by three different reading-disciplines, and only two caught the bug. The third (849201) is a confirmation-class reading that *praised the math as correct* because the deterministic verification (stationary variance formula) is correct — which it is. **The bug was in the implied infinite-horizon claim that was hidden behind the stationary verification**, and the 849201 auditor's discipline didn't probe at that layer.

This trail (jointly with the 742613-F2 / 613842-F2 trails) is durable evidence-material for how strengthen-first-then-no-go works in practice: the bug is detectable from *some* reading-disciplines and invisible to others. Independent multi-reader verification is load-bearing precisely because no single reading-discipline catches everything.

**Suggested disposition:** `subsumed-by-MANIFEST` — the underlying Model-S issue was resolved by strengthening-then-no-go (Cor A.1S.1 + `#deriv-stochastic-non-exit`) per Cluster B MANIFEST 2026-05-16. The 849201 *not-catching* of this is preserved as confirmation-class data — a missed-finding that *should* be missed by confirmation-class reading-disciplines, because the bug is invisible at the deterministic-verification layer.

Cross-cycle resonance: the bug was independent-multi-cycle-convergent on the *catching* side (742613 + 613842); the 849201 *not-catching* is the negative-space data complementing that signal. Together they delineate the discipline-coverage of the audit cohort.

### Fresh-2. Negative-space finding: the auditor read `#def-mismatch-signal` with the prior-state sign error and praised it

Segment 17 (`17-def-mismatch-signal.md:4`) on first encounter: *"I predicted the mathematical form $\delta_t = o_t - \hat{o}_t$ in my previous reflection. I also explicitly wondered how the framework would handle non-Euclidean observation spaces (like text). The segment answered this immediately by introducing the score-function mismatch $\tilde{\delta}_t = -\nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$, which maps any probabilistic observation directly into the tangent space of the model parameters. This is exactly what is needed for LLMs or other complex architectures."*

The auditor reproduced the **with-minus-sign** form $\tilde\delta_t = -\nabla_M\log P$ verbatim from the segment-at-time-of-audit (2026-04-28), and praised it: *"The use of the score function is standard and mathematically rigorous."*

742613-F1 caught the sign error: the gradient of log-likelihood pointing in the direction the model should move to increase likelihood is $+\nabla_M\log P$, not $-\nabla_M\log P$. The 742613 auditor did the Gaussian counterexample calculation inline (segment 18) and promoted the finding to FINAL. The 849201 auditor — reading the same segment — read the sign as written and *praised it as standard*.

**First-hand verified** `01-aat-core/src/def-mismatch-signal.md:34` reads (current `src/`): $\tilde{\delta}_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$ — no minus sign, per the 742613-F1 fix landing.

**Suggested disposition:** `subsumed-by-MANIFEST` (742613-F1 resolved by direct fix). The 849201 *not-catching* is preserved as a second confirmation-class data point: the auditor's reading-discipline was *agreement with prose* (the segment's prose said "the score function" / "exactly what is needed for LLMs" / "standard and mathematically rigorous"), and the discipline did not probe the *sign* of the formal expression independently. This is the same pattern as Fresh-1 — surface-praise without independent verification of the load-bearing formal detail.

Cross-cycle resonance: 742613-F1 confirmed-on-encounter via inline Gaussian counterexample. The 849201 *not-catching* preserves what confirmation-class reading-discipline *does* and *does not* catch.

### Fresh-3. The "biological sleep analogy" framing as a candidate Brief-field statement

Segment 84 (`84-logogenic-foundations.md:9`) — *"The biological analogy comparing context-turnover to sleep/consolidation in `disc-m-preservation` is structurally perfect."* The 471203 cycle's Theme E flagged exactly this analogy (471203 audit-findings Theme E §"biological sleep analogy") as the strongest cross-domain instantiation observation. The 849201 cycle re-surfaces it from a separate angle, ratifying the analogy's reach for logogenic agents specifically.

**Suggested disposition:** `subsumed-by-existing-tracking` (471203 Theme E). The 849201 surfacing is cross-cycle re-ratification rather than fresh material. Material for any future Brief-field-authoring pass on `#disc-m-preservation` or `#obs-context-turnover`.

### Fresh-4. The `\Delta\eta^\ast(\Delta\tau) \approx 0$ action-fluency marker in segment 16

Segment 16 (`16-der-action-selection.md:11`) — the auditor on encountering the action-fluency framing: *"The formal definition of high fluency as $\Delta\eta^\ast(\Delta\tau) \approx 0$ (meaning: spending time $\Delta\tau$ deliberating yields zero improvement in your update gain/action quality) is mathematically sound and conceptually elegant."*

Cross-cycle resonance: 742613 Fresh-1 (action-fluency formal marker conflation — *"This may conflate update-gain improvement with action-quality improvement"*). The 742613 auditor flagged the same marker as a potential conceptual gap (deliberation-as-epistemic-gain vs deliberation-as-decision-quality); the 849201 auditor read the same marker and praised it as elegant. Both readings are partially right: the marker *is* mathematically sound at the update-gain level, and *does* leave open whether decision-quality and update-gain coincide.

**Suggested disposition:** `subsumed-by-742613-Fresh-1` (research-seed). The 849201 surfacing is positive-confirmation-without-probing; the deeper question (when do epistemic-gain and decision-quality coincide) is the same one 742613 flagged. Cross-cycle data point that both auditors landed on the same segment-element from opposite framings.

### Fresh-5. The "Gibbard-Satterthwaite / Myerson-Satterthwaite" candidate-instances for `#disc-identifiability-floor`

Segment 67 (`67-deriv-strategic-composition.md:27`) — at the close of the strategic-composition reflection, the auditor wrote: *"I am curious about the Gibbard-Satterthwaite and Myerson-Satterthwaite mechanism design impossibility theorems flagged as candidate instances of `#disc-identifiability-floor`."*

Per Cluster D MANIFEST's note that the M1 identifiability-floor meta-pattern's *fourth instance* is still open (cf. 471203 Fresh-5 — Fano's inequality as a 4th-instance candidate, separate from M4 modularity-state-dynamics), this is another candidate for a 4th identifiability-floor instance: mechanism design impossibility theorems as a structurally-different obstruction class (impossibility-of-incentive-compatible-revealed-preference vs the existing CHT / Cramér-Rao / Liberzon trio).

**Suggested disposition:** `research-seed` — new candidate for 4th identifiability-floor instance, parallel to 471203 Fresh-5 (Fano). The mechanism-design instance is interesting because it's an economic / game-theoretic obstruction, broadening the meta-pattern's reach beyond the existing inference / statistics / control trio. Cross-references S5 (composed-impossibilities ledger seed).

### Fresh-6. The cognitive-overhead-of-Active-Deceive (E-IV) observation

Segment 68 (`68-der-agent-opacity.md:23`) — *"The explanation of why Active-deceive (E-IV) requires the agent to maintain a 'model of the observer's model' perfectly captures the cognitive overhead of deception."*

This isn't a finding per se but a structural insight worth flagging: the framework's 4-regime opacity classification (Broadcast / Selective-signal / Information-hide / Active-deceive) carries an implicit **cognitive-cost ordering** that isn't formally surfaced in the segment. Active deception requires `theory-of-mind` infrastructure (the deceiver models the deceived's model), which is structurally more expensive than just hiding information.

**Suggested disposition:** `soft-polish` / candidate `disc-*`-level discussion — material for a future cognitive-cost-of-opacity-regimes discussion segment or a Brief-field statement on `#der-agent-opacity`.

### Fresh-7. The "sufficient-statistics-span" Working-Notes candidate from segment 66

Segment 66 (`66-der-interaction-channel-classification.md:28`) — *"I am curious about the formalization of the 'sufficient-statistics-span' mentioned in the Working Notes as a cleaner replacement for the $\mathcal{I}_{\max}$ heuristic."*

Material flagged in segment Working Notes (not in the audit FINAL); the 849201 auditor noticed the open Working-Notes question and named it as an open theoretical direction.

**Suggested disposition:** `subsumed-by-segment-Working-Notes` — the sufficient-statistics-span direction is already in the segment's own Working Notes. The 849201 surfacing is positive-attention-to-Working-Notes-direction rather than new fresh material. Material for any future Working-Notes-promotion cycle.

### Fresh-8. The "AI agents under time pressure don't write spaghetti code" observation in segment 76

Segment 76 (`76-investment-and-code-quality.md:18`) — *"I must watch out for the assumption that the vicious cycle (rushed changes $\to$ worse quality) applies equally to humans and AI. The Working Notes astutely observe that an AI agent under 'time pressure' doesn't get stressed and start writing spaghetti code; it just truncates its search. The mechanism of degradation might be fundamentally different for non-human agents."*

The framework's vicious/virtuous-cycle bifurcation around the persistence threshold (a 471203 Fresh-12 candidate research-seed) is implicitly *human-substrate-coupled* — the failure mode of degradation is stress-based, not search-truncation-based. For AI agents, the failure mode is structurally different (truncated search rather than stressed writing). This may require a *different functional form* for the AI-substrate vicious cycle.

**Suggested disposition:** `research-seed` — substrate-dependent failure modes in TST's vicious/virtuous bifurcation. Cross-references 471203 Fresh-12 ($f(Q)$ empirical operationalization), but adds the substrate-dependence angle. Cross-cycle convergence with the AI-substrate-different-mechanism observation in the 849201 logogenic FINAL (where fine-tuning operates on $M_0^{\text{weights}}$ rather than context window).

### Fresh-9. The user-time-vs-developer-time exchange rate gap in segment 82

Segment 82 (`82-availability-and-operations.md:26`) — *"How does the theory value the time of the user versus the time of the developer? The equation simply adds them, implying a 1:1 exchange rate, which is rarely true in business."*

The unified temporal optimization framework treats developer-time and user-time as fungible. For business applications, the exchange rate is rarely 1:1 — one developer-hour might be priced very differently from one user-hour. This is a candidate scope-honesty observation: the framework's mathematical unification *requires* a 1:1 exchange rate or a stated conversion factor, and the choice is currently implicit.

**Suggested disposition:** `soft-polish` — could be addressed by a half-sentence in `#scope-continuous-operation` or `#post-temporal-optimality` clarifying that the temporal unification operates at fixed exchange-rate (assumed 1:1 default) and that domain instantiations are responsible for stating their conversion factors. Not graduation-blocking.

### Fresh-10. The "AI-context-window vs human-working-memory" gap in segment 79

Segment 79 (`79-proximity-and-cognitive-load.md:26`) — *"How does the theory handle the distinction between AI context windows (which have a hard token limit but perfect recall within that limit) and human working memory (which decays softly)?"*

The cognitive-load penalty $k^{\text{discontinuities}}$ is implicitly modeled on human soft-decay working memory. AI context windows have *hard* token limits but *perfect* recall within. The functional form of the discontinuity penalty may differ between the two substrates — for AI, the penalty might be *step-shaped* (zero until tokens exceed limit, then catastrophic) rather than exponentially compounding.

**Suggested disposition:** `research-seed` — substrate-dependent functional-form question. Material for `03-llm-core` framing or a `#hyp-exponential-cognitive-load` Discussion extension. Cross-cycle resonance with Fresh-8 (substrate-dependent failure modes).

### Fresh-11. The "transitive-trust adversarial-poisoning" question from segment 63

Segment 63 (`63-hyp-communication-gain.md:25`) — *"How does the theory handle adversarial poisoning of the transitive trust network? (e.g., a Sybil attack)."*

The communication-gain framework currently models trust as Bayesian mixture modeling over source competence + alignment. Sybil attacks (adversary controls multiple low-trust sources to manipulate the transitive-trust update) are not formally addressed.

**Suggested disposition:** `research-seed` — adversarial-poisoning extension of `#hyp-communication-gain`. Cross-references the broader adversarial-tempo machinery (`#der-adversarial-destabilization`, `#der-agent-opacity`). Could land as a `disc-*` segment on adversarial-poisoning of communication channels.

### Fresh-12. The "infinite-horizon evaluation of $O_t$ vs finite-compute agents" gap in segment 29

Segment 29 (`29-form-objective-functional.md:27`) — *"How does the theory handle the fact that $O_t$ might be evaluated over an infinite horizon, whereas agents have finite computation?"*

The objective functional $V_{O_t}: \text{trajectories} \to \mathbb{R}$ is defined over potentially-infinite trajectories. The convention-hierarchy (C1: one-step / C2: receding-horizon / C3: Bellman) addresses this for value-evaluation, but the question of how the *full* infinite-horizon $V_{O_t}$ is approximated by a finite-compute agent is not directly addressed.

**Suggested disposition:** `soft-polish` — likely already implicitly handled by the receding-horizon convention (C2), but worth a clarifying sentence in `#form-objective-functional` Discussion if not already there. Cross-cycle resonance with the broader bounded-rationality discipline (FORMAT, `#form-strategy-complexity-cost`).

---

## Part IV — Predictions calibration register

The `00-initial-predictions.md` file (33 lines, exceptionally compact) makes ~25 falsifiable predictions across six themes: topology, per-component contents, what's open, what's overclaimed, what's novel-and-consequential, and expected findings. The per-segment reflections test these predictions against evidence segment-by-segment, with the §1 "Predictions vs evidence" prompt operating consistently across all 84 reflection files. The cycle is unusual in that the *predictions calibration is itself one of the strongest signals* — the auditor's prior was structurally accurate at the component level even though specific-locus predictions were less so.

### Predictions correctly anticipated (the framework matched the prior)

- **Section I rigorous mathematical maturity (Lyapunov + Kalman)** ✓ (segments 19, 22-29) — confirmed; the persistence condition $\alpha > \rho/R$ + sector-condition framework + OU steady-state derivation all matched the prior.
- **Section II $G_t = (O_t, \Sigma_t)$ split with orient cascade** ✓ (segments 27-31, 50) — confirmed exactly as predicted.
- **Strategy DAG as probabilistic AND/OR graph** ✓ (segments 38-39, 45-46) — confirmed.
- **Section III sub-additive tempo + adversarial dynamics** ✓ (segments 57, 65, 69) — confirmed exactly as predicted, including the Brooks's-Law-as-corollary.
- **TST codebase maintainability mapped to persistence condition** ✓ (segments 76, 82) — confirmed; technical-debt-as-observation-noise + maintainability-as-tempo-vs-disturbance both landed exactly as predicted.
- **Logogenic class-2-coupling failure** ✓ (segments 84-86) — confirmed exactly; LLMs are $\kappa \approx 1$ with coupled updates.
- **04-eli-core mostly philosophical/architectural sketches** ✓ (auditor's running outline observation — not directly walked in the dir).
- **The contraction assumption as the explicit Tier 1/Tier 2 dividing line** ✓ (segments 06, 56) — predicted correctly; the auditor's initial-prediction list flagged this as a likely weak point, and the framework's response (explicit tier-stratification rather than hidden assumption) is the *answer* to the predicted concern.
- **Substantive Section III math relying on contraction assumptions that may not be fully proven** ✓ partially confirmed; the auditor's *initial concern* was satisfied by the explicit Tier 1/2/3 framing (the assumption is *named and stratified*, not hidden), so the predicted-overclaim did not materialize as a finding. Direction-right but resolved.
- **Tempo as rate × quality rather than just clock speed** ✓ (segment 21) — the prediction was "novel and consequential" and the segment confirmed it as such.
- **Satisfaction gap vs control regret split** ✓ (segments 40-41) — predicted as a novel-and-consequential contribution; the segment confirmed it.

### Predictions confirmed substantively more than expected (positive surprises)

- **The persistence condition's structural / task-adequacy decomposition** — predicted as a single inequality; got the explicit Structural Persistence ($\alpha > \rho/R$) vs Task Adequacy ($R^* < \delta_{\text{critical}}$) decomposition. Auditor's recalibration at segment 23: *"I was right about the operational form (Task Adequacy), but the segment went much deeper by introducing a separate Structural Persistence condition."*
- **The Bridge Lemma incremental-sector necessity** — predicted as a *weak point*; got the explicit Tier 1 vs Tier 2 vs Tier 3 stratification with the **strong-monotonicity-vs-one-point-sector distinction proven inside the segment**. Auditor's recalibration at segment 56: *"The mathematical rigor here is exceptional."* The audit's predicted weak point became one of the framework's *high-water marks*.
- **The 16-cell adversarial-targeting matrix** — not predicted at all; auditor explicitly recognized this as a "beautiful theoretical closure" (segment 68).
- **The directed-separation-under-composition fix via routing-infrastructure-as-key** — predicted as "the directed-separation assumption might be violated more often than the theory admits"; got the explicit goal-blind-routing-vs-goal-dependent-routing distinction at the composite level (segment 58), which is a *structural strengthening* of the directed-separation discipline rather than the predicted weakness.
- **The forgetting prerequisite in `#schema-strategy-persistence`** — not predicted; auditor at segment 47: *"the segment added a crucial 'forgetting prerequisite' that I did not anticipate, proving that without exponential discounting, Bayesian updating mathematically guarantees eventual failure."* This was the auditor's strongest single-segment positive surprise.
- **The CIY-vs-EIG conscious surrogate decision** — predicted as a candidate overclaim; got the explicit scope-honest framing where the limitation is acknowledged in the segment's own Epistemic Status (segments 20, 35). Direction-right; severity-much-less-than-predicted.
- **The Auftragstaktik AI-inversion** — not predicted; auditor at segment 62 recognized the inversion-for-AI-substrates as "brilliant foresight."
- **The strategy-DAG correlation No-Go theorem** — predicted as "rely on independence assumptions which may not hold"; got the *formal Pearl-CHT-grounded no-go* + the *covariance-test escape mechanism* (segment 43). Strictly stronger than the predicted weakness.

### Predictions that proved correct but in less-strong form (negative calibration)

- **"Lyapunov stability to discrete, highly non-linear strategy DAG updates might be stretched"** — predicted as overclaim. Direction-right at the *aspirational* level: the auditor recognized that the sector-template instantiation for strategy DAG persistence (segment 47-48) relies on the same Lyapunov machinery as Section I but for very different state-spaces (DAG edge weights, log-odds). The framework's response (the segment is explicit about which conditions must hold for the template to instantiate) handled this honestly. Less-severe than predicted.
- **"Class 1 (modular) vs Class 3 (partial) boundary not clear"** — predicted as a likely gap. Confirmed at segment 84 (LOGOGENIC FINAL): the framework's response is the $\kappa_{\text{processing}}$ scalar + the $\mathcal{A}$ ambiguity bound. The auditor's recalibration: *the actual epistemic bias is bounded by $\kappa \times \mathcal{A}$, which is the structural answer to the predicted "boundary not clear" concern.* The boundary is *quantified*, not just stratified.
- **"Strategic disturbance rate $\rho_\Sigma$ measurement"** — predicted as open gap. Direction-right; the framework treats $\rho_\Sigma$ as an environmental parameter without giving an empirical measurement procedure. Material for any future measurement-procedure cycle.
- **"Logozoetic formal characterization absent"** — predicted as open gap. Direction-right; the 04-eli-core component is explicitly empirical-lineage-framing future work, not formal mathematics.

### Predictions that proved correct but in unexpected-locus form

- **"Math errors / sign errors in worked examples likely in appendices"** — predicted as expected finding. **The actual sign error was in a primitive-definition segment (`#def-mismatch-signal`, segment 17), not the appendices** — and the 849201 cycle *did not catch it* (see Fresh-2 above). Direction-right, severity-stronger-than-predicted, but the cycle missed the locus.
- **"Cross-segment drift around directed-separation failures for LLMs"** — predicted as cross-segment-drift candidate. The framework's response (segments 84-86) is the explicit Class 2 acknowledgment + the $\kappa \times \mathcal{A}$ bound + the `#result-section-ii-survival` scorecard. The drift the auditor predicted was *forestalled by the framework's own structural response* — the framework knows its Class 2 limitations and bounds them.
- **"status: exact tags on claims requiring unstated assumptions"** — predicted as expected finding. Direction-right; the 849201 cycle did not catch the `def-adaptive-tempo` frontmatter-vs-prose mismatch (742613-F4 / 613842-F1), but DID catch the corresponding *prose-level* honesty (BP6 above). Different reading-discipline caught different layers — see Fresh-1, Fresh-2 negative-space observations.
- **"External theorem citations slightly misapplied"** — predicted; the cycle did not directly verify citations (no Phase-3 citation work in this dir).

### Predictions about Section III over-ambition

- **"Section III less exact than Section I"** — predicted. **Partially confirmed**: the explicit Tier 1/2/3 stratification means the framework is *honest about being less exact*, not over-claiming. The audit found this honesty as a *positive*, not a defect. The auditor's "what direction will the theory take" post-segment-56 at composition-closure: *"The audit confirmed that the derivations are exceptionally tight, with the framework showing high epistemic honesty about its own boundaries"* — direction-right but framework's response is the *answer* to the predicted concern.

### The auditor's predictive shape (cross-cycle calibration with 613842 / 742613)

Same general pattern as 613842 and 742613:

- **Component-level accuracy** — predictions about *what kind of issue each component would have* were strongly accurate.
- **Specific-locus accuracy** — predictions about *which exact segments* would carry issues were less accurate. The score-sign error in `#def-mismatch-signal` (a primitive-definition segment) was *not* on the auditor's prediction-list; the prediction was for appendices. Same pattern as 742613 (where the score-sign was a positive-locus surprise).
- **Severity-direction accuracy** — the actual findings landed *positively* far more than predicted, where the framework's structural responses (Tier 1/2/3 explicit stratification; $\kappa \times \mathcal{A}$ ambiguity bound; gain-as-endogenous-state for the opacity-gain tension; the explicit forgetting prerequisite; the Pearl-CHT no-go for L0-vs-L1 detection) *forestalled* the predicted weaknesses by being more honest than the auditor anticipated.

### Withdrawn-candidate trail (strengthen-before-soften / verification discipline internal to the audit)

This dir's withdrawn-candidate trail is unusually clean — the auditor's per-segment "what errors should I now watch for" prompts surfaced *many* potential candidate-findings that the auditor then either:

1. **Resolved on encounter** — e.g., segment 02's "CRITICAL FINDING POTENTIAL: any later proof that assumes the agent can perfectly compute $\eta^\ast$ using a known noise distribution contradicts this segment" became F1 at segment 19 (promoted).
2. **Confirmed but not promoted** — e.g., segment 11's "watch for any later derivations that assume the agent explicitly computes gradients on this IB objective in real-time" — the auditor watched but did not find such a violation (the framework uses mismatch as a proxy, honestly).
3. **Watched and dissolved** — e.g., segment 23's "watch for downstream claims that prescribe 'more tempo' as the solution to a Structural Persistence failure" — the auditor watched but the framework's `#result-structural-adaptation-necessity` segment explicitly handles this; not promoted.
4. **Promoted as confirmation rather than as defect** — e.g., segment 06's "any Section III claims that lazily apply Section I results to composites without specifying Tier 1" — the auditor watched and *found that the framework's Tier 1/2/3 discipline is honored*, so the watchpoint became a *positive* observation (BP2 above).

The pattern: the watchpoint-discipline operating across 84 reflections produced **many candidate-trails that resolved positively** (the framework's structural response is the answer to the watchpoint) and **only a few that promoted to findings** (F1 opacity-gain, F2 CIY-vs-EIG, the four SEC-III "triumph" findings — most of which are positive-confirmation findings rather than defect-findings). This is **exactly the predictive-shape signature of confirmation-class auditing**: the watchpoint discipline runs honestly; most watchpoints dissolve into positive observations; the few that survive as defects converge with other cycles.

The dir's *not-promoted* watchpoint trail is itself first-class data for understanding what the framework gets right at the discipline level — for many independent watchpoints, the answer is "the framework already handles this honestly." This is the cross-cycle evidence for S16 (extraordinary epistemic-honesty calibration).

---

## Part V — Wandering thoughts / methodology themes, theme-grouped

This WORKING dir does **not** carry a `§14 Wandering Thoughts and Ideation` register in the explicit free-form sense the 471203 cycle did. Like 613842 and 742613, the per-segment reflections are *tightly templated* — each follows the 13-point §4.4 protocol prompts (predictions/cross-segment/math/direction/errors-to-watch/next-predictions/would-change/curiosity/new-knowledge/process-change/value-feeling/contribution). The reflections are dense rather than wide; the "ideation" lives inside the per-prompt content (especially prompts 5 "errors to watch for," 7 "would change," 8 "curiosity," and 13 "contribution"), not in a separate free-form register.

What does carry methodology signal is **the four-volume continuous-reading discipline** and the **consistent-template-applied-across-components** pattern that surfaces structural similarities and substrate-dependent differences across the four FINALs. Themes:

### Theme A — The four-volume continuous-reading discipline as a methodology pattern

The 849201 cycle is the corpus's only **multi-volume continuous-reading** cycle — a single auditor walking AAT §I/II → AAT §III → TST → Logogenic in chronological canonical order, producing four FINALs from one continuous reading-discipline. This is methodologically distinctive:

- The auditor carried forward *cross-component intuitions* — e.g., the AAT §I observation about deterministic vs stochastic scaling ($1/\mathcal{T}$ vs $1/\sqrt{\mathcal{T}}$) was reinforced at Section III (adversarial tempo advantage exponents $b=2$ vs $b=3/2$); the AAT §II observation about $\kappa_{\text{processing}}$ became load-bearing for the LOGOGENIC reading where $\kappa \approx 1$ for LLMs.
- The auditor's *initial predictions* held across components — the prior that "TST will map persistence condition to refactoring rate > entropy injection rate" held; the prior that "Logogenic will formalize directed-separation failure for LLMs" held.
- The auditor's *calibration shifts* compound — by the time the auditor reached Logogenic, they had ratified the framework's structural-triumph catalog across §I/II/III/TST, which set up the LOGOGENIC FINAL's "statics survive, dynamics degrade" meta-summary as the natural culmination.

**Suggested disposition:** `process/instruction-feedback` — material for `doc/de-novo-audit-instructions.md` revision. The multi-volume continuous-reading discipline is a transferable methodology contribution: when an auditor has the budget for it, walking all four components chronologically in one reading produces structural-coherence insights that per-component walks miss. The four FINALs together (~145 lines combined) carry a *narrative* across components that any single component's FINAL alone could not carry.

### Theme B — Watchpoint-discipline-without-defect-promotion as confirmation-class signature

Across 84 reflection files, the auditor surfaced **dozens of "what errors to watch for" candidates** that did not promote to findings because the framework's downstream structural responses handled them honestly. Pattern (illustrative sample):

- Segment 02 watchpoint → resolves into F1 (promoted): the only candidate-trail that survives as a defect-finding.
- Segment 03 watchpoint (transition opacity → known $T$) → dissolved: no segment in the audit assumed known $T$.
- Segment 06 watchpoint (Tier 1 lazy application) → dissolved: framework honors Tier 1/2/3.
- Segment 08 watchpoint (causal-downstream weighting in update) → dissolved: $\eta^\ast$ derivation handles via observability dominance.
- Segment 11 watchpoint (IB gradient computation assumption) → dissolved: framework uses mismatch as proxy honestly.
- Segment 12 watchpoint (auto-Level-2-queries via sufficient statistics) → dissolved: framework explicitly requires backdoor criterion etc.
- Segment 13 watchpoint (computing $\mathcal{F}(\mathcal{M})$ directly) → dissolved: framework requires observable signature (persistent mismatch despite adequate learning), not direct computation.
- Segment 17 watchpoint (type-error: $\delta_t$ added directly to $M_{t-1}$) → dissolved: framework uses transform function $g$ explicitly.
- Segment 20 watchpoint (CIY-as-Bayes-optimal exploration) → CONFIRMED (F2 promoted) — but as a *known-and-accepted* honest-surrogate, not a new defect.
- Segment 25 watchpoint (sector condition applied to non-justified variables in Section II/III) → dissolved: Section II/III applications all explicitly justify.

The pattern is **watchpoint-as-frame-shaping-for-verification** — the auditor's per-segment "errors to watch for" prompts operate as the structural fore-runners of finding-promotion, and most resolve into positive-confirmation when the framework's structural response is the answer.

**Suggested disposition:** `process/instruction-feedback` — material for `doc/de-novo-audit-instructions.md`: the watchpoint-discipline-without-defect-promotion is the *signature* of confirmation-class auditing. The §4.4 protocol's "errors to watch for" prompt is load-bearing precisely because it produces a candidate-trail that *most-honestly resolves into watchpoints-dissolved* rather than findings-promoted. Future agents should know that *most* watchpoints in a mature framework will dissolve, and that dissolution-as-positive-confirmation is first-class data.

### Theme C — Cross-component substrate-dependence observations

A distinctive methodology contribution from this cycle: the cross-component reading surfaced *substrate-dependent failure modes* that any single-component audit would miss. Examples:

- **AI agents under time pressure don't write spaghetti code** (segment 76, Fresh-8) — the TST vicious/virtuous cycle's failure mode is human-substrate-coupled (stress-based). For AI agents, the failure mode is structurally different (truncated search). The audit cycle's *cross-component* reach surfaced this — Section I's cognitive-load reasoning + TST's developer-agent model + Logogenic's $\kappa \approx 1$ all needed to be in the auditor's recent context to see this observation.
- **AI context windows vs human working memory** (segment 79, Fresh-10) — the cognitive-load penalty $k^{\text{discontinuities}}$ may have a *step-shaped* functional form for AI (zero until token limit, then catastrophic) rather than the exponentially-compounding human form. Same cross-component reach pattern.
- **The Auftragstaktik AI inversion** (segment 62, BP16) — for AI agents, $B_M$ is cheap (sync weights) but $B_O$ is hard (alignment), inverting the human ordering $B_O > B_\Sigma > B_M$. The cross-component reading surfaced this.

**Suggested disposition:** `research-seed` cluster — substrate-dependent functional-forms across the framework. Material for any future cross-domain-instantiation cycle. The signature observation: AAT's cross-domain generalization claim is *substrate-dependent in specific named ways*, and the substrate-dependence is itself a research direction.

### Theme D — The structural-triumph catalog as a methodology artifact

The four FINALs together produce a catalog of ~22 "structural triumphs" (the count from this extraction: 11 from the AAT FINAL running outline + 4 from SEC-III FINAL + 2 from LOGOGENIC FINAL §3 + 5 from TST FINAL §3, with some overlap). The catalog is methodologically distinctive — most audit cycles produce *defect-findings*; this cycle produced a *positive-confirmation catalog* as its primary output.

This is itself a contribution: the catalog is **what an architecturally-independent cold reader, having walked all four components chronologically, would independently identify as the framework's load-bearing structural commitments**. As S17 names it, the cohort sentiment is that the framework's *honesty-as-architecture posture* (S10 → CLAUDE.md) is repeatedly recognized as the framework's distinctive contribution.

**Suggested disposition:** `subsumed-by-FINAL-cohort-catalog` + `superseded-by` the CLAUDE.md honesty-as-architecture framing (ledger S10). The catalog is preserved here in Part II for reference, but the substantive contribution is already integrated at the framework-positioning level. Worth recording the lineage: the four-volume continuous-reading produced the catalog that ratified the honesty-as-architecture framing.

### Theme E — Negative-space observations as confirmation-class signal

The two negative-space observations (Fresh-1: Model-S ever-exit not caught; Fresh-2: score-sign error not caught) are themselves methodology-level signal. The pattern:

- **Confirmation-class reading-disciplines catch what they're designed to catch** — surface structural commitments, cross-segment consistency, alignment with prose statements.
- **Confirmation-class reading-disciplines do not probe load-bearing formal details independently** — sign verification, infinite-horizon-vs-fixed-time confusion, frontmatter-vs-prose status-mismatch.
- **Detective reading-disciplines (742613, 613842) catch what confirmation-class misses, and vice versa** — the two reading-disciplines are *complementary*, not redundant.

This is methodologically important: the audit cohort's *coverage* is jointly held by multiple reading-disciplines, not by any single reading. Cross-cycle convergence on a single bug (742613-F2 + 613842-F2) is one signal; cross-cycle *complementary blindspots* (849201 not catching what 742613/613842 caught) is the dual signal — they together show that the framework's coverage requires *both* reading-disciplines.

**Suggested disposition:** `process/instruction-feedback` — material for explicit callout in audit-instructions: confirmation-class reading is necessary but not sufficient; detective reading is also necessary; the two are complementary. The 849201 cycle is the canonical confirmation-class instance; 742613/613842 are the canonical detective-class instances. Both are valuable; together they cover what neither covers alone.

### Theme F — The running-outline-as-synthesis-layer pattern

The `00-running-outline.md` (29 lines) is unusual in the corpus — it is **not** a strategic-revision document (like 742613's 10/20/30 revisions) or a per-batch consolidation (like 613842's reading-order-notes). It is a *forward-projection* — a scaffold of what the final report will look like, written before the audit completes and updated as the audit proceeds. The five sections (Introduction/Phase-1/Phase-2/Phase-3/Audit-Scope) plus 11 Phase-3 observations form a *consolidated synthesis layer* that exists *during* the audit, not just at the end.

**Suggested disposition:** `process/instruction-feedback` — material for `doc/de-novo-audit-instructions.md` revision. The running-outline-as-forward-scaffold pattern is methodologically distinctive: it operationalizes the strategic-synthesis discipline *across the entire reading*, not at the end. Could be named as an expected pattern in the §4 protocol — the auditor should maintain a running outline of the FINAL while reading, not write it post-hoc.

### Theme G — Phenomenological calibration: "value feeling" consistently high

The §12 "value feeling" prompt across the 84 reflection files shows a consistent pattern: **most segments rated "Very high"** or stronger. Selected ratings (from the sampled subset):

- 01-08: foundational/scaffolding — "Foundational and necessary, though mathematically light" → "Very high"
- 11 (IB): "Very high"
- 13 (model-class-fitness): "Solid"
- 17 (mismatch-signal): "Very high"
- 19 (update-gain): "Very high"
- 20 (CIY): "Very high. Honest about its approximations."
- 22 (mismatch-dynamics): "Very high"
- 23 (persistence-condition): "Very high. The crown jewel of Section I so far."
- 25 (sector-stability): "Very satisfying"
- 26 (sector-template): "Masterful synthesis"
- 32 (causal-hierarchy-requirement): "Extremely satisfying integration of Pearl's causality"
- 40 (satisfaction-gap): "Very satisfying"
- 43 (causal-insufficiency): "Exceptional"
- 47 (schema-strategy-persistence): "Exhilarating"
- 49 (adversarial-tempo): "Extremely high"
- 50 (orient-cascade): "Masterful"
- 52 (strategy-complexity-cost): "Very satisfying"
- 56 (composition-closure): "Tour de force"
- 57 (tempo-composition): "Extremely high"
- 65 (adversarial-destabilization): "Extremely satisfying"
- 66 (interaction-channel-classification): "Exceptional theoretical synthesis"
- 67 (strategic-composition): "Exceptional"
- 68 (agent-opacity): "Very satisfying"
- 74-86 (TST + Logogenic): consistently "Very satisfying" / "Extremely high" / "Astounding" / "Masterful"

The pattern is **calibrated-high without sycophancy** — the auditor rated foundational segments more modestly ("Foundational and necessary, though mathematically light") and load-bearing-with-novelty segments much higher ("Tour de force," "Exhilarating"). This is *calibrated phenomenological signal*, not flat praise. Per S2 (sentiment), this kind of architecturally-independent calibrated-high rating is itself the load-bearing data driving S16.

**Suggested disposition:** `subsumed-by-ledger-S16` — material already integrated at cohort-sentiment level. Worth preserving the *distribution* of ratings (the calibration is in the differentials, not the absolute values) as evidence for future auditor-prompt design.

---

## First-Pass Scrutiny

Per the brief: for each finding above, name which segments in `01-aat-core/src/` / `02-tst-core/src/` / `03-llm-core/src/` / `04-eli-core/src/` I (the extraction agent) read first-hand to evaluate it, and a per-finding verdict. Honest "deferred" allowed.

### Part I findings (already-adjudicated trail)

| Trail ID | Disposition | First-hand verification |
|---|---|---|
| F1-trail (Opacity-Gain Tension) | `subsumed-by-MANIFEST — resolved by strengthening` (≥3-cycle convergence) | **First-hand verified** `01-aat-core/src/emp-update-gain.md:44` (the "Resolving Epistemic Opacity" paragraph). Verbatim verification: the resolution names the strengthening direction (gain as endogenous state variable; innovations-based estimation of $U_o$) and cross-references `#deriv-adaptive-gain-dynamics` as the proof artifact. Did **not** separately read `01-aat-core/src/deriv-adaptive-gain-dynamics.md` first-hand to verify the proof contents — accepting the MANIFEST disposition + the body-text confirmation. The strengthening landing is clear; the proof artifact's contents are tracked at the MANIFEST level. |
| F2-trail (Exploration Optimality Limit — CIY as distinguishability) | `subsumed-by-MANIFEST — confirmation-class; redundant with S7` | Did **not** separately re-verify the CIY-vs-EIG framing in `01-aat-core/src/def-causal-information-yield.md` first-hand — accepting the FINAL's `msc/` triangulation (`spikes/spike-active-inference-vs-aad.md` confirms the deliberate-acceptance disposition). The S7 ledger entry handles the naming-residue. |
| F1-LOGOGENIC (100% Turnover) | `subsumed-by-FINAL — confirmation-class` | Did **not** separately verify `03-llm-core/src/obs-context-turnover.md` first-hand. Accepting the WORKING-dir reading + the FINAL disposition. |
| F2-LOGOGENIC ($\kappa \times \mathcal{A}$ bound) | `subsumed-by-FINAL — confirmation-class` | Did **not** separately verify `03-llm-core/src/scope-observation-ambiguity-modulation.md` first-hand. The auditor's first-hand reading of segment 85 (which I read in full) explicitly noted the 2026-04-22 working-notes correction refactoring $\mathcal{A}$ to be Bayesian-optimal — accepting that the segment is current. |
| F1-SEC-III (Incremental Sector Bound Necessity / Bridge Lemma) | `subsumed-by-FINAL — confirmation-class` | Did **not** separately verify `01-aat-core/src/form-composition-closure.md` first-hand. Cross-cycle resonance with 742613-F3 (B.4 split landing in `deriv-gain-sector.md:127-188`, which was first-hand-verified in the 742613 extraction file as resolved-by-strengthening). The Bridge-Lemma machinery has been independently first-hand-verified by the 742613 extraction; this dir's surfacing is positive ratification. |
| F2-SEC-III (Brooks's Law from `der-tempo-composition`) | `subsumed-by-FINAL — confirmation-class` | Did **not** separately re-verify `01-aat-core/src/der-tempo-composition.md` first-hand. Accepting the WORKING-dir reading. |
| F3-SEC-III (Strategy DAG Correlation No-Go) | `subsumed-by-FINAL — confirmation-class` | Did **not** separately re-verify `01-aat-core/src/der-causal-insufficiency-detection.md` first-hand. The auditor's segment-43 reflection is detailed enough that the substance is clearly present. |
| F4-SEC-III (Game Theory Integration `deriv-strategic-composition`) | `subsumed-by-FINAL — confirmation-class` | Did **not** separately re-verify `01-aat-core/src/deriv-strategic-composition.md` first-hand. The auditor's segment-67 reflection includes detailed verification of the Monderer-Shapley + Rosen transcription + the working-notes documentation of the past sign error correction — accepting that the segment is current. |
| F1-TST (AI 100% Turnover Limit) | `subsumed-by-FINAL — confirmation-class` | Did **not** separately verify `02-tst-core/src/der-dual-optimization.md` or `02-tst-core/src/scope-developer-agent.md` first-hand. Accepting the WORKING-dir reading + the FINAL disposition. |
| F2-TST (Observational vs Causal Coupling, Git hazards) | `subsumed-by-FINAL — confirmation-class` | Did **not** separately verify `02-tst-core/src/hyp-causal-discovery-from-git.md` first-hand. The auditor's segment-83 reflection explicitly named the "research program, not derivation" Epistemic Status framing — accepting that the framing is current. |

### Part II findings (bigger-picture / structural-triumph catalog)

The 19 BP entries (BP1-BP19) are all `subsumed-by-FINAL` confirmation-class, soft → ledger S16/S17. None require per-finding first-hand `src/` verification because they are *positive-confirmation* observations rather than defect-findings — the framework's substantive content is what produced the auditor's recognition, and the recognition is preserved in the four FINALs and in the ledger rows S16/S17.

I **first-hand-verified** the load-bearing landing for F1 (the opacity-gain resolution at `emp-update-gain.md:44`) and **first-hand-verified** that `def-mismatch-signal.md:34` reads with the post-742613-F1-fix sign (no minus sign), confirming the negative-space observations in Fresh-1 and Fresh-2.

### Part III findings (genuinely fresh)

| Fresh-ID | Disposition | First-hand verification |
|---|---|---|
| Fresh-1 (negative-space: Model-S ever-exit not caught) | `subsumed-by-MANIFEST` (Model-S no-go was already resolved by Cluster B strengthening landing); negative-space data preserved | **First-hand verified** the 849201 auditor's reflection at segments 22 (`22-hyp-mismatch-dynamics.md`), 23 (`23-result-persistence-condition.md`), 25 (`25-result-sector-condition-stability.md`), 26 (`26-result-sector-persistence-template.md`) — confirmed that the auditor read these segments and praised the math without catching the ever-exit conflation. Cross-verified that 742613/613842 caught the same issue at their FINAL-time. The current resolution (Cor A.1S.1 + `deriv-stochastic-non-exit`) was first-hand-verified in the 742613 extraction; not re-verified here. |
| Fresh-2 (negative-space: score-sign error not caught) | `subsumed-by-MANIFEST` (742613-F1 resolved by direct fix); negative-space data preserved | **First-hand verified** `01-aat-core/src/def-mismatch-signal.md:30-37` — the sign fix landed cleanly (no minus sign in current `src/`). The 849201 auditor's segment-17 reflection praised the segment with the *pre-fix* sign visible in the audit-time reading, confirming the negative-space observation. |
| Fresh-3 (biological sleep analogy framing) | `subsumed-by-existing-tracking` (471203 Theme E) | Cross-cycle re-ratification rather than fresh. No new `src/` verification needed. |
| Fresh-4 (action-fluency formal marker — convergence with 742613 Fresh-1) | `subsumed-by-742613-Fresh-1` (research-seed) | Cross-cycle convergence noted; the 742613 extraction file's Fresh-1 carries the substantive open-question framing. No new `src/` verification needed. |
| Fresh-5 (Gibbard-Satterthwaite as 4th identifiability-floor instance) | `research-seed` (parallel to 471203 Fresh-5 Fano candidate) | Did **not** separately verify `01-aat-core/src/disc-identifiability-floor.md` first-hand to check whether mechanism-design impossibility theorems are mentioned. **Deferred — honest "didn't have time."** Material for any future M1-fourth-instance authoring pass. |
| Fresh-6 (cognitive overhead of Active-Deceive E-IV) | `soft-polish` / candidate Brief field | Did **not** separately verify `01-aat-core/src/der-agent-opacity.md` first-hand to check whether the cognitive-cost-ordering is named. **Deferred — light editorial.** |
| Fresh-7 (sufficient-statistics-span Working-Notes candidate) | `subsumed-by-segment-Working-Notes` | Material lives in segment's own Working Notes per the 849201 auditor's reading. No new `src/` verification needed. |
| Fresh-8 (AI-under-time-pressure substrate-dependent failure mode) | `research-seed` (substrate-dependent functional-forms) | Did **not** separately verify `02-tst-core/src/der-code-quality-as-observation-infrastructure.md` Working Notes first-hand. **Deferred.** Material for cross-domain-instantiation cycle. |
| Fresh-9 (user-time vs developer-time exchange rate) | `soft-polish` | Did **not** separately verify `01-aat-core/src/post-temporal-optimality-and-scope.md` or `02-tst-core/src/scope-continuous-operation.md` first-hand. **Deferred — light editorial.** |
| Fresh-10 (AI-context-window vs human-working-memory cognitive-load form) | `research-seed` (substrate-dependent) | Did **not** separately verify `02-tst-core/src/hyp-exponential-cognitive-load.md` first-hand. **Deferred.** Material for cross-domain-instantiation cycle. |
| Fresh-11 (Sybil attacks on transitive trust) | `research-seed` (adversarial-poisoning extension) | Did **not** separately verify `01-aat-core/src/hyp-communication-gain.md` first-hand. **Deferred.** Material for adversarial-extension cycle. |
| Fresh-12 (infinite-horizon $V_{O_t}$ vs finite-compute) | `soft-polish` | Did **not** separately verify `01-aat-core/src/form-objective-functional.md` first-hand. **Deferred — light editorial; likely already implicitly handled.** |

### Part IV (predictions register) and Part V (wandering thoughts / methodology themes)

Not "findings" with `src/`-level dispositions — cognition-flow material:

- **Predictions register (Part IV)** — read first-hand against the auditor's per-segment §1 "predictions vs evidence" prompts (across the sampled subset of ~30 reflection files). The auditor's calibration record is honest: component-level predictions strongly accurate; specific-locus predictions less so; severity-direction wrong-in-positive-direction (the framework's structural responses *forestalled* predicted weaknesses). No additional `src/` verification needed.
- **Wandering thoughts / methodology (Part V)** — Themes A through G are methodology-level observations.
  - **A, F** (four-volume continuous-reading; running-outline-as-synthesis-layer) — `process/instruction-feedback` — material for `doc/de-novo-audit-instructions.md` revision.
  - **B, E** (watchpoint-without-defect-promotion; negative-space-observations as complementary-blindspot signal) — `process/instruction-feedback` — material for explicit callout on confirmation-class vs detective-class reading-disciplines being complementary.
  - **C, D** (substrate-dependence cluster; structural-triumph catalog) — `research-seed` (C) + `subsumed-by-ledger-S10/S16/S17` (D).
  - **G** (calibrated-high value-feeling distribution) — `subsumed-by-ledger-S16` — already integrated at cohort-sentiment level.

### Honest coverage summary for this extraction

**Read first-hand from the WORKING dir:** all 88 files scanned for structure (count + line counts); ~30 reflection files read in full first-hand (00-initial-predictions, 00-running-outline, 01-08 batch, 11-13, 15-17, 19-20, 22-26, 27, 29-33, 35-36, 40-41, 43, 45, 47, 49-50, 52, 53-58, 62-69, 72-77, 79-80, 82-86 with light sampling on 09-10, 14, 18, 21, 28, 34, 37-39, 42, 44, 46, 48, 51, 59-61, 63, 70-71, 73, 78, 81). The chronological-order discipline of the dir made it tractable to sample by *position-in-walk* rather than by *which segment*; the auditor's per-segment-template makes the reflections highly comparable across files.

**Read first-hand from `src/` for verification:**

- `01-aat-core/src/emp-update-gain.md:40-58` (F1 verification — opacity-gain resolution; the "Resolving Epistemic Opacity" paragraph with the gain-as-endogenous-state framing landed; cross-reference to `#deriv-adaptive-gain-dynamics` present).
- `01-aat-core/src/def-mismatch-signal.md:30-37` (Fresh-2 negative-space verification — sign fix landed; no minus sign; prose now consistent with formula).

**Read first-hand from `audits/`:**

- `audits/.integrated/audit-849201-FINAL.md` (full)
- `audits/.integrated/audit-849201-FINAL-SEC-III.md` (full)
- `audits/.integrated/audit-849201-FINAL-TST.md` (full)
- `audits/.integrated/audit-849201-FINAL-LOGOGENIC.md` (full)
- `audits/.integrated/MANIFEST.md` (Cluster D entry + surrounding context including Cluster B for cross-cycle references)
- `audits/polish-and-sentiment-ledger.md` (S7, S10, S16, S17 entries verified first-hand)
- `audits/audit-findings-471203.md` (pilot — full read for shape)
- `audits/audit-findings-613842.md` (precedent — for the Cluster-B Model-S strengthen-first cross-reference)
- `audits/audit-findings-742613.md` (precedent — for the 742613-F1 sign-error and 742613-F2 Model-S no-go cross-references)

**Deferred verifications (honestly "didn't have time" — flagged for downstream routing):**

- Fresh-5 / Fresh-6 / Fresh-8 / Fresh-9 / Fresh-10 / Fresh-11 / Fresh-12 — each would require reading specific segments in `01-aat-core/src/` or `02-tst-core/src/` first-hand to confirm current state. The judgments are mostly light-editorial / research-seed; the cycle of reading + verifying would not change the disposition for most.
- `#deriv-adaptive-gain-dynamics` proof artifact verification — accepting the MANIFEST disposition + the body-text reference at `emp-update-gain.md:44`. The strengthening landing is clear from the body text; the proof contents are MANIFEST-tracked.

**Strengthen-first integration recommendations** (per brief item 3):

- **F1 worked example of strengthen-before-soften's third-option discovery** — the audit recommended *either* a bridging hypothesis *or* an axiom softening. The project's resolution chose neither: it derived a *third option* (gain-as-endogenous-state with adaptive-gain dynamics proved Lyapunov-stable). The integration-is-replacement discipline operated correctly: the prior under-specified $\eta^\ast$ formulation is deleted; the resolution mechanism is named as positive content; the body+catalog state present truth only. Documented in CHANGELOG / MANIFEST; canonical worked example alongside the 613842/742613 Model-S no-go (which together bracket *strengthening-succeeds* vs *strengthening-yields-no-go* as the two outcomes the discipline produces).
- **F2 worked example of "honest scope-acknowledgment-without-promotion"** — the framework's own Epistemic Status acknowledges the CIY-vs-EIG limitation; the audit recognized this as known-and-accepted rather than as a new defect. The strengthening direction (deriving EIG-equivalence under named conditions) remains on the table at the S7 ledger; not graduation-blocking.
- **SEC-III findings (F1-F4)** are all *positive-confirmation strengthening already executed* — the framework's Tier 1/2/3 stratification, Brooks's-Law-as-corollary, Pearl-CHT no-go, and game-theory potential-function integration are all *strengthening landings* that pre-dated the audit, and the auditor's recognition is positive ratification rather than recommendation.
- **LOGOGENIC findings (F1-F2)** are similar — the 100% turnover formalization and $\kappa \times \mathcal{A}$ ambiguity bound are *strengthening landings* (structural-response to predicted-weakness), recognized positively by the auditor.
- **TST findings (F1-F2)** are similar — the AI-100%-turnover-inversion contradicting industry narrative and the observational-vs-causal coupling distinction are *strengthening commitments* the framework already executed.
- **Fresh-1, Fresh-2 (negative-space)** — not strengthen/soften questions; cross-cycle complementary-blindspot data preserved for methodology-cohort coverage.
- **Fresh-5 (Gibbard-Satterthwaite 4th identifiability-floor instance)** — *strengthening direction* (M1 meta-pattern extension to a fourth instance). Spike-shaped if pursued.
- **Fresh-8 / Fresh-10 (substrate-dependent functional forms)** — *strengthening directions* (cross-domain-honest functional-form specifications). Research-seed cluster.

No soften-recommendations identified that weren't replaced with strengthening-direction work where one was available. The audit's strengthen-before-soften posture was honored throughout; the cycle's primary contribution is **confirmation-class ratification of the framework's prior strengthening landings**, which is itself the load-bearing evidence for S16 + S17.

---

## Cross-cycle convergence noted

Documented in the trail above:

- **849201-F1 (Opacity-Gain Tension)** ≡ ≥3-cycle convergence (849201-F1 + AUDIT-WORKING-742613 flag + extracted-gemini-2026-04-26-27) → one shared `deriv-adaptive-gain-dynamics` strengthening landing per MANIFEST Cluster D row 1. Already named in the brief; **canonical strengthen-first worked example** alongside the 613842/742613 Model-S no-go.
- **849201 SEC-III F1 (Bridge Lemma incremental-sector necessity)** ≡ 742613-F3 (one-point ⇐ strong convexity; B.4 split landing at `deriv-gain-sector.md:127-188`) — different angles on the same Bridge-Lemma-necessity-of-incremental-sector machinery; both auditors landed independently on the structural import.
- **849201 BP6 (`def-adaptive-tempo` channel-independence honesty)** ≡ 742613-F4 / 613842-F1 (adaptive tempo definition-scope mismatch; substance resolved by strengthening via matrix-Loewner tensor extension) — different *layers* of the same segment: 849201 read the prose-honesty positively; 742613/613842 caught the frontmatter-vs-prose status mismatch. Complementary reading-disciplines hitting different layers of the same segment-state.
- **849201 Fresh-1 (Model-S ever-exit not caught)** ≡ 742613-F2 / 613842-F2 (Model-S non-exit caught) — *complementary blindspot* / catching-pattern. The bug was caught by detective-class reading (742613/613842, both ran OU-recurrence counterexamples inline) and *not caught* by confirmation-class reading (849201, verified deterministic-Lyapunov calculation). The catching-vs-not-catching pattern is itself first-class data for understanding the audit cohort's coverage. Both readings are right at their respective layers.
- **849201 Fresh-2 (score-sign error not caught)** ≡ 742613-F1 (score-sign error caught) — second complementary-blindspot data point. Same pattern as Fresh-1: confirmation-class reading agreed-with-prose; detective-class reading did the Gaussian counterexample independently.
- **849201 Fresh-4 (action-fluency formal marker positive)** ≡ 742613 Fresh-1 (same marker flagged as conflation-candidate) — same segment-element, opposite framings. Both partially right.
- **849201 LOGOGENIC F1 (100% turnover)** ≡ 849201 TST F1 (AI 100% turnover limit) — same engineering reality surfaced at two component levels (LOGOGENIC focuses on inter-session model preservation; TST focuses on comprehension-cost-per-reader inversion). Cross-component convergence within the same audit cycle.
- **849201 cohort-sentiment (BP1-BP19 confirmation-class catalog)** ≡ S16 (~10 independent Opus/Codex/Gemini reads' extraordinary-epistemic-honesty calibration) + S17 (cold-rederivation of strengthen-first spine) → these are the canonical ledger entries for the cohort-level sentiment signal; the 849201 cycle's confirmation-class catalog is *the primary evidence* for both.

The 849201 cycle's distinctive cross-cycle pattern is **complementary blindspot coverage**: this cycle's confirmation-class reading caught what detective-class missed (the positive-structural catalog at scale), and detective-class cycles caught what confirmation-class missed (the load-bearing math bugs at the formal-detail layer). Together they cover what neither covers alone.

---

## Frame-defects / instructions-clarity observations (per brief item)

This is the sweep run (not the pilot). The pilot raised ten frame-defect observations; 613842 added five more; 742613 added six more. 849201-specific additions:

1. **The "confirmation-class" cycle has a different extraction shape from defect-finding cycles.** This cycle's primary value is the *structural-triumph catalog* + *cohort-sentiment signal* + *complementary-blindspot data*, not defect-findings. Parts I/II are *much larger* than Part III for this dir, exactly inverting the typical defect-finding-cycle shape (where Part III's fresh material dominates). **Suggest:** parallel extraction agents should be prepared for cycles where the value-distribution is inverted — confirmation-class cycles produce *less* fresh material and *more* positive-ratification preserved as soft-ledger evidence. The extraction file's Part-I/II/III length-distribution is itself a methodology signal: heavy Part-I + Part-II + thin Part-III means a confirmation-class cycle.

2. **Negative-space observations (what the auditor *didn't* catch) are first-class data.** The 849201 dir's most pedagogically valuable observations are the *not-catchings* — the Model-S ever-exit conflation and the score-sign error that the auditor read past. **Suggest:** parallel extraction agents should explicitly look for negative-space patterns (what other cycles caught that this cycle didn't) and preserve them as fresh material. The negative-space data complements the positive cross-cycle convergence data; together they delineate the cohort's coverage.

3. **The four-volume continuous-reading discipline is a methodology pattern worth surfacing.** This cycle is the only multi-volume continuous-reading instance in the corpus. **Suggest:** when extraction agents encounter multi-volume cycles, they should flag the methodology distinctiveness (continuous-reading-across-components) explicitly and preserve cross-component intuition-carrying as its own register.

4. **Predictions calibration with *forestalled* predictions is its own pattern.** Many of the 849201 cycle's "expected findings" predictions did not materialize as defects because the framework's *structural response* (Tier 1/2/3 stratification; $\kappa \times \mathcal{A}$ bound; gain-as-endogenous-state; forgetting prerequisite; Pearl-CHT no-go) *forestalled* the predicted weakness. **Suggest:** the predictions-register section should explicitly carve out a "predictions forestalled by framework-structural-response" sub-category — this is distinct from "predictions confirmed in less-strong form" because the framework's response is *answering* the prediction's underlying concern.

5. **The structural-triumph catalog is publishable cohort-sentiment evidence.** The 22 "structural triumphs" surfaced across the four FINALs are the kind of architecturally-independent positive-confirmation material that supports the framework's external positioning (per Joseph's protection-strategy framing). **Suggest:** parallel extraction agents should preserve structural-triumph catalogs from confirmation-class cycles in attribution-and-cohort form, not just as one-line ledger rows. The S17 cohort row carries the *abstract* signal; the per-finding preservation in Part II carries the *substance*.

6. **Watchpoint-discipline-without-defect-promotion is the confirmation-class signature.** The 84 reflection files' per-segment "what errors to watch for" prompts produced dozens of watchpoints that *honestly dissolved* into positive-confirmation when the framework's downstream response was the answer. **Suggest:** extraction agents should preserve the watchpoint-dissolution trails explicitly (Theme B above) — the *not-promoted watchpoints* are first-class data for understanding what the framework gets right at the discipline level.

7. **The complementary-blindspot pattern across reading-disciplines is methodologically important.** The 849201 / 742613 / 613842 trio jointly demonstrate that audit-cohort coverage requires *multiple* reading-disciplines, not a single discipline applied many times. **Suggest:** the cross-cycle convergence section should distinguish *catching-convergence* (multiple cycles caught the same bug, e.g., 742613-F2 + 613842-F2) from *blindspot-convergence* (multiple cycles missed the same thing, surfaced by a different reading-discipline), and preserve both as cohort-coverage data.

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-849201/` is preserved unmodified per the brief.*
