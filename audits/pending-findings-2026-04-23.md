# Pending Findings — 2026-04-23 De Novo Audit Trio

Three independent de novo audits (Codex, Gemini, Opus) ran after the 2026-04-22/23 cascading strengthening cycle closed. This document consolidates the findings with cross-audit agreement marked, msc/ pointers preserved, and subsumption-by-proposal where applicable. Integration only — not an execution document.

**Read alongside.** `audits/pending-findings-2026-04-22.md` (F1–F21 from the prior audits); `msc/architectural-proposals-2026-04-22.md` (portfolio + post-2026-04-23 extensions SP-2 through SP-8 added in this integration).

## Trust-signal note

The three audits were run independently and share significant overlap in both findings and big-picture observations — Gemini's "invert the foundation" and Codex's "foreground AAD as bounded correction under decomposed disturbance" converge, and all three independently point at the same meta-theme: the framework's **epistemic architecture** (separability, identifiability floor, calibration-lab, scope-honesty) is the distinctive contribution, not the integration narrative. When three independent audits converge on a reframe, the reframe warrants serious consideration rather than case-by-case integration.

---

## Finding overlap map (consolidated)

| Audit | Finding | Consolidated ID | Overlap / independence |
|---|---|---|---|
| Codex 1 | README overclaims scope vs. Class 2 exact-theorem scope | **F22** | Overlaps with Opus C (stacked scope narrowings) and Gemini F4 (directed separation vs LLMs); surfaced at repo-entry level here |
| Codex 2 | "16/24 exact survival" headline overstates | **F23** | Standalone to Codex |
| Codex 3 | Strategy-edge semantics vs. identifiability machinery | **F24** | Overlaps with Opus F (DAG-forced framing) and Gemini F2 (causal sufficiency bottleneck) |
| Codex 4 | Coupled-diagnostic-framework runtime-recipe vs. analytical-reconstruction | **F25** | Standalone to Codex |
| Codex 5 | Section III composition-closure reads more closed than epistemic status supports | **F26** | Overlaps with Gemini F1 (bridge lemma tension) and Opus D (Tier 3 prevalence); Opus D is sharpest |
| Gemini 1 | Bridge lemma / macro-tracking tension | merged into **F26** | See F26 |
| Gemini 2 | Causal-sufficiency bottleneck | merged into **F24** | See F24 |
| Gemini 3 | Scalar tempo overcounting | **F27** | Standalone; already substantially caveated in segment (see below) |
| Gemini 4 | Directed separation excludes modern LLMs | merged into **F22** | Already-known scope narrowing |
| Opus A | $\rho_\Sigma$ unmeasurable threshold parameter | **F28** | Standalone to Opus; deepest substantive finding |
| Opus B | Update-rule heterogeneity integration debt in `#def-unity-dimensions` | **F29** | Standalone to Opus; pure integration debt |
| Opus C | Stacked scope narrowings (Class 1 + learning-agent) | **F30** | Strong scope-visibility finding; partial overlap with F22 |
| Opus D | Tier 3 prevalence in composition-closure | merged into **F26** | See F26 |
| Opus E | Orient cascade 4c signal-to-noise sensitivity | **F31** | Standalone to Opus; medium confidence |
| Opus F | `#def-strategy-dag` "DAG forced" framing vs. `#deriv-graph-structure-uniqueness` sufficiency-only | merged into **F24** | See F24 |

Net: **10 consolidated findings** from **15 raw audit findings** (cross-audit agreement on 5).

---

## F22 — Repo-entry scope framing outruns Section II's exact theorem scope

**Source:** Codex F1 + Gemini F4 (partial). **Confidence:** high (Codex), medium (Gemini on LLM scope exclusion).

**Problematic passages:**
- `README.md` line 10: "single coherent account..."
- `README.md` line 12: "from thermostats through military organizations"

**Strongest counter-passages:**
- `01-aad-core/OUTLINE.md:7` — "Section II's exact results apply to Class 1 (modular) agents"
- `#der-directed-separation:97` — "This is a genuine scope restriction, not a footnote"

**Status:** still real. The caveat is present at OUTLINE and segment level, but the repo-entry framing reads broader than the exact theorem surface defended for merged, goal-conditioned agents. A reader lands at README and builds a wider expectation than the theory's exact results support.

**Subsumed by:** Partially by O-BP8 (scope lattice naming) if pursued; also by the proposed Phase C framing pass. The repo-entry fix is editorial (README.md) and distinct from the OUTLINE-level fix.

**Repair direction:** Update README.md to surface the Class 1 architectural scope and the learning-agent-scope narrowing (see F30) at the entry point; the wider "thermostats through military organizations" framing should be re-scoped to "the framework of adaptive-systems Section I, with Section II's exact results applying to Class 1 modular agents in the learning sub-scope." Codex's recommended reframe ("AAD as theory of bounded correction under decomposed disturbance") is the cleanest positive form; composes with O-BP1 / O-BP10.

---

## F23 — "16/24 exact survival" headline compresses distinctions the segment itself names

**Source:** Codex F2. **Confidence:** high.

**Problematic passages:**
- `03-logogenic-agents/src/result-section-ii-survival.md:37` — "Of Section II's 24 results, 16 survive exactly..."
- Same segment line 47 — "SURVIVES EXACTLY (16)" table

**Strongest counter-passages** (same segment):
- Line 53 — `#def-value-object` marked "Partial"
- Line 117 — approximate bounds are only order-of-magnitude
- Line 127 — "statement-level" rather than operational applicability

**Status:** still real. The segment's body correctly qualifies each claim, but the leading ratio compresses definitional carryover, partial carryover, and instrumentation dependence into one reassuring number. The headline does work the body contradicts.

**Subsumed by:** Partially by C-BP1 (three-layer epistemic separation — defined / causally valid / operationally extractable) which would force the "16" to be resolved into per-layer counts.

**Repair direction:** Replace the single ratio with per-layer breakdown: "of 24 results, N survive at the definitional layer, M at the causally-valid layer, P at the operationally-extractable layer." The msc/ spike `spikes/spike-coupled-survival-analysis.md:69` already frames this — "what survives exactly is mostly the coordinate/definitional layer" — and `spikes/spike-coupled-survival-analysis.md:528` notes the promoted set is a "minimal skeleton, not a complete theory." Integration debt rather than open research.

---

## F24 — Strategy-edge semantics not harmonized with identifiability machinery; DAG-forced framing slightly overclaims

**Source:** Codex F3 + Opus F + Gemini F2 (partial). **Confidence:** high (Codex, Opus); high (Gemini on causal sufficiency bottleneck).

**Problematic passages:**
- `#def-strategy-dag:48` — edge definition
- `#def-strategy-dag:163` — "Pearl's do-calculus therefore applies directly"
- `#def-strategy-dag` elsewhere — "The graph structure is derived..."

**Strongest counter-passages:**
- `#scope-edge-update-causal-validity:16` — scopes update by regime and identification strength
- `#scope-edge-update-causal-validity:91` — warns of claiming interventional semantics from associational evidence
- `#deriv-graph-structure-uniqueness` opening — "sufficient only (the desiderata guarantee DAG+Markov, but no one has shown a non-DAG structure cannot satisfy them)"
- `#deriv-graph-structure-uniqueness` — "For agent-constructed strategies, causal sufficiency is a **modeling ideal, not a typical condition**..."

**Status:** still real across three audits. Three distinct aspects:
1. `#def-strategy-dag` speaks of do-calculus applying directly; identifiability regime A/B/C softens this elsewhere. The "direct" language outpaces the regime structure.
2. `#def-strategy-dag`'s "graph structure is derived" reads stronger than `#deriv-graph-structure-uniqueness` actually proves (sufficiency, not necessity).
3. Gemini's deeper point: causal sufficiency is the dominant failure mode, and the CMC-based Markov derivation relies on it. L1-augmentation is the named repair but the base DAG structure is fragile to unknown environmental variables.

**msc/ integration target:** `spikes/spike-edge-semantics-resolution.md:62` proposes the cleaner "causal efficacy credence" framing. This is the integration target per Codex's explicit recommendation.

**Subsumed by:** No single proposal. The three-part resolution requires: (a) soften `#def-strategy-dag`'s do-calculus and DAG-forced language to match `#deriv-graph-structure-uniqueness`'s sufficiency-only + `#scope-edge-update-causal-validity`'s regime structure; (b) adopt the "causal efficacy credence" framing from the edge-semantics-resolution spike; (c) foreground causal sufficiency as a scope condition (adjacent to Correlation Hierarchy).

**Repair direction:** Editorial + promotion-from-spike. Medium effort; no new theory required.

---

## F25 — `#result-coupled-diagnostic-framework` slides from "defined" to "computable"

**Source:** Codex F4. **Confidence:** high.

**Problematic passages:**
- `03-logogenic-agents/src/result-coupled-diagnostic-framework.md:18` — "the diagnostic quantities ... can be computed after each coupled update"
- Same segment line 40 — "From $X^{(post)}$, compute"

**Strongest counter-passages:**
- `03-logogenic-agents/src/def-coupled-update-dynamics.md:66` — M/G split is "post-hoc and analytical"
- `#result-section-ii-survival:127` — 16/24 exact survival explicitly disclaims "operational extractability"
- `02-tst-core/src/obs-software-epistemic-properties.md:124` — instrumentation-boundary doctrine

**Status:** still real. The segment reads as a runtime recipe for quantities the rest of the repo treats as analytically reconstructed and instrumentation-dependent.

**Subsumed by:** C-BP1 (three-layer epistemic separation) directly. The three-layer convention would force per-quantity tagging as (defined / causally-valid / operationally-extractable), surfacing the layer-collapse.

**msc/ integration targets** (Codex notes):
- `ref/agentic-tft/agentic-tft-evaluation-framework.md:78, 112` — explicit tracking protocols
- `ref/agentic-tft/agentic-tft-cognitive-loop-spec.md:125` — context-assembly protocol
- `ref/agentic-tft/agentic-tft-review-response.md:73` — missing failure-mode-to-metric mapping admitted

**Repair direction:** The segment needs to adopt the instrumentation-boundary doctrine from `#obs-software-epistemic-properties`. Rewrite the "compute $X^{(post)}$" passages to distinguish analytical reconstruction from runtime computation, with instrumentation-boundary framing. 60–90 min if C-BP1 is not yet landed; 30–60 min if C-BP1 is landed first.

---

## F26 — Section III composition-closure reads more closed than its epistemic status supports; Tier 3 prevalence not characterized

**Source:** Codex F5 + Gemini F1 + Opus D. **Confidence:** medium (Codex, Gemini); medium-high (Opus, the sharpest).

**Problematic passages:**
- `#form-composition-closure:203` — "the same macro-level persistence/tempo machinery applies"
- `#form-composition-closure:215` — "Together they close the loop"

**Strongest counter-passages** (same segment):
- Line 187 — admissibility, norms, $K_c$, projection computability remain open
- Line 189 — bridge lemma conditional on DA2'a-inc (strictly stronger than (A4))
- Epistemic Status — Tier 3 "must be verified per-domain"
- `#der-tempo-composition:30` — core result marked as sketch with dependency gap

**Status:** multi-layered.
- **Layer 1 (Codex framing concern):** Summary sentences overstate closure relative to open items the segment itself names. Editorial.
- **Layer 2 (Gemini bridge lemma tension):** Macro-admissibility (A1)–(A4) do not imply bridge lemma holds; that requires strictly stronger DA2'a-inc. Admitted in Epistemic Status but the admissibility framing doesn't surface this.
- **Layer 3 (Opus Tier 3 prevalence):** Weakest-link bound implies composites with any rule-based / non-convex / non-Bayesian component fall in Tier 3. Most practical composites are Tier 3 (most human teams, most multi-LLM systems, most hybrid architectures). The bridge lemma's central transferability result is unavailable in exactly the regime where composition is empirically most interesting. Not characterized in the segment.

**Subsumed by:** No single proposal. Opus's Big Picture §5 recommends a **consolidation pass** trading apparent generality for substantial simplification — scope the bridge lemma machinery explicitly to linear-Gaussian and exponential-family cases where it actually delivers; state the general claim as "composite agents are AAD agents iff their effective dynamics admit an AAD-shaped reduction" at a more honest generality. This is proposed as **SP-6** in the architectural proposals doc.

**Repair direction:** Adopt SP-6 consolidation if pursued; otherwise add a "Tier 3 prevalence" subsection to `#form-composition-closure` Epistemic Status + `#der-team-persistence` that honestly frames the practical availability of the transferability result. 30–60 min for editorial; multi-session for SP-6 consolidation.

---

## F27 — Scalar tempo overcounting already caveated but foundational

**Source:** Gemini F3. **Confidence:** high.

**Problematic passage:** `01-aad-core/src/def-adaptive-tempo.md` — additive formula $\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$.

**Strongest counter-passages** (same segment):
- Discussion — "additive formula assumes informationally independent channels... When channels are correlated... the additive formula *overcounts* effective tempo"
- Per-dimension: "scalar tempo overestimates by 72%" (empirically confirmed)

**Status:** **already adequately caveated** but Gemini's observation that this is the foundational metric and the empirical 72% overestimate is load-bearing. Not counted as a new finding (rejection rationale: Opus-style rejection applies here — already scope-honest). Kept in the consolidated list for visibility only.

**Subsumed by:** O-BP3 (continuous-parameter tiering — would handle scalar → per-dimension → tensor as continuous parameter) or by promoting `#disc-approximation-tiering`'s "Scalar vs. per-dimension tempo" candidate tiering.

---

## F28 — $\rho_\Sigma$ is an unmeasurable threshold parameter on which a trajectory guarantee depends

**Source:** Opus A. **Confidence:** high (gap is real); medium (substantive flaw vs. honest open question).

**Problematic passage:** `#schema-strategy-persistence:53-62` — forgetting prerequisite `$\lambda < 1 - \rho_\Sigma / R_\Sigma$` stated as "prerequisite of the schema's trajectory guarantee, not a tunable heuristic."

**Strongest counter-passage** (same segment, Discussion §3): "$\rho_\Sigma$... **Still open** as a formalized quantity — currently a domain parameter, analogous to how $\rho$ for epistemic disturbance is a domain parameter in `#result-persistence-condition`."

**Status:** real gap, sharper than the segment admits. The asymmetry with epistemic $\rho$ is not symmetric: epistemic $\rho$ is at least *observable through the same channel that produces $\delta_t$* (agent sees model errors and can infer disturbance rate). The strategic analogue would require observing how often the agent's *causal links* become invalid — but the agent's evidence about edge truth comes through the very edge updates that are being calibrated by $\lambda$. **This is closer to a circularity than a parameter-estimation problem.** The trajectory guarantee is not yet operational.

**msc/ context:** `spikes/spike-strategy-dynamics-gaps.md:195-225` and `spikes/spike-strategy-tempo-cost.md:392` both describe $\rho_\Sigma$ identically ("qualitatively different sources" with no estimator). **No msc material addresses how an agent could measure $\rho_\Sigma$ from its own data.** This is a genuinely unaddressed question, not an integration debt.

**Subsumed by:** None. Candidate for a dedicated spike or an honest scope-narrowing of the trajectory guarantee to "conditional on domain-supplied $\rho_\Sigma$." The strengthen-first attempt would try to derive $\rho_\Sigma$ from observable quantities (e.g., rate of edge-credence-credence drift after accounting for update dynamics); the softening fallback labels the trajectory guarantee as "operational under external $\rho_\Sigma$ specification."

**Repair direction:** Strengthen-first spike. Honest outcome-B fallback if strengthening fails: explicit scope-narrowing of the trajectory guarantee.

---

## F29 — Update-rule heterogeneity integration debt in `#def-unity-dimensions`

**Source:** Opus B. **Confidence:** high.

**Problematic passage:** `#def-unity-dimensions` opening — "The quality of a composite agent's composition... decomposes along four substantially independent *quality* dimensions..."

**Strongest counter-passage:** `#result-unity-closure-mapping` — "Update heterogeneity is not captured by any of the four unity dimensions as defined in `#def-unity-dimensions`... This is an independent dimension of the closure-defect rate-distortion surface." And `#def-unity-dimensions` Working Notes: "Update-rule heterogeneity is a missing axis... Option (C) is the current working position... Formal resolution open."

**Status:** real, pure integration debt. The Working Note documents the gap and names the chosen resolution (Option C: two-axis structure, unity × homogeneity). But the *Formal Expression* of `#def-unity-dimensions` still names four dimensions as "the" decomposition. A reader who consults `#def-unity-dimensions` first sees a four-axis claim that the theory has internally rejected.

**msc/ integration target:** `spikes/spike-unity-closure-mapping.md` §"Two-axis structure" derives the closed form $\varepsilon_x^2 = (\Delta K/2)^2[S_- - C_{+-}^2/S_+]$ explicitly. Integration not yet done.

**Subsumed by:** None. Pure integration debt. 45–90 min editorial work updating `#def-unity-dimensions` Formal Expression to two-axis form with $\Delta K$ as explicit second axis; cross-ref to `#result-unity-closure-mapping` and the spike.

**Repair direction:** Mechanical integration — next session should land this.

---

## F30 — Stacked scope narrowings for Section II exact results; only Class 1 at OUTLINE level

**Source:** Opus C. **Confidence:** high.

**Problematic passage:** `01-aad-core/OUTLINE.md` Section II preamble — "**Section II's exact results apply to Class 1 (modular) agents**... **This is the most significant scope restriction in the theory**."

**Strongest counter-passage:** `#der-causal-hierarchy-requirement` Scope Narrowing — "We restrict attention to **learning purposeful agents**... Pre-compiled agents are within agency scope (they have objectives and act on them) but outside learning-agent scope... **All remaining Section II results operate within learning-agent scope** unless explicitly noted otherwise."

**Status:** real and architecturally consequential. Section II exact results require Class 1 ∩ learning-agent, but only Class 1 is foregrounded at OUTLINE level. Kalman+LQR is *in* Class 1 but *out* of learning-agent scope — a reader designing a control system would reasonably believe Section II covers Kalman+LQR and be wrong by the theory's own internal logic. The canonical example of Class 1 is also a canonical example of pre-compiled-not-learning.

**Subsumed by:** O-BP8 (explicit scope lattice naming) closes this directly. Phase C of the recommended sequence.

**Repair direction:** Amend OUTLINE preamble to mention learning-agent narrowing alongside Class 1. 20–40 min standalone; cleaner if done as part of O-BP8 scope-lattice pass.

---

## F31 — Orient cascade 4c's signal-to-noise sensitivity not surfaced where step is prescribed

**Source:** Opus E. **Confidence:** medium.

**Problematic passage:** `#der-orient-cascade` step 4c — "**(4c) Causal-sufficiency check (L0→L1 escalation).** If persistent $\delta_s \approx 0$ coincides with persistent negative plan-outcome residuals... the diagnostic is pairwise sibling covariance under an augmented test..."

**Strongest counter-passage:** `#der-causal-insufficiency-detection` Epistemic Status — "Its sensitivity depends on how cleanly the agent can separate sibling-covariance signal from edge-credence noise at convergence; in adversarial or fast-drifting environments the test's effective sample size shrinks."

**Status:** real, half-caveated. `#der-causal-insufficiency-detection` honestly flags the signal-to-noise issue. But the cascade cites step 4c as the *unique broadly-available* diagnostic (backed by the no-go theorem). A reader following the cascade reaches a step whose practical effectiveness is treated as a secondary detail in a sister segment. The combination — "step 4c is the unique escape; step 4c is least powerful where you need it most (adversarial, fast-drifting)" — is not surfaced in the cascade.

**Subsumed by:** No single proposal. Fix is editorial: add a one-paragraph practical-sensitivity note to `#der-orient-cascade` step 4c.

**Repair direction:** 30 min editorial addition to `#der-orient-cascade`; no new theory needed.

**msc/ context:** No msc material addresses the practical sensitivity bounds. An alternative structural repair path — promote a sensitivity-bound analysis to `#der-causal-insufficiency-detection` — is a research question, not integration debt.

---

## Findings rejected by Opus (retained here for transparency)

Opus applied the same rigorous standard used in the previous audits and rejected the following candidate findings because the repo already adequately caveats them. Listed here so that future audits do not re-raise resolved concerns:

- Pinsker bound looseness vs. linear-KL form trade-off — `#deriv-strategy-cost-regret-bound` §7 self-aware
- Channel independence in scalar tempo — `#disc-independence-audit` item 6 + `#result-per-dimension-persistence`
- $G_t = (O_t, \Sigma_t)$ "definitional but load-bearing" — `#def-strategy-dimension` Discussion reframes
- Causal sufficiency as dominant failure — covered in `#def-strategy-dag` Correlation Hierarchy + `#der-causal-insufficiency-detection` + `#disc-identifiability-floor` + `#disc-independence-audit`
- $V_{\max} \lt \infty$ assumption — `#deriv-strategy-cost-regret-bound` §8 + `#form-strategy-complexity-cost` Epistemic Status
- L1' unobservable-common-cause identifiability-blocked — refuted (not "open"); `#def-strategy-dag` + `#disc-identifiability-floor` Instance 2 give Cramér-Rao
- $K_c$ timescale ratio in composition-closure — acknowledged; 2026-04-22 repair made $K_c$ explicit
- Section III's `--GAP--` rows — flagged in OUTLINE, not concealed
- Logogenic agents out of formal scope of `#scope-agent-identity` — explicit in segment Discussion
- Pre-compiled controllers (PID, LQR) outside learning-agent scope — acknowledged (F30 sharpens what *isn't* adequate)

Also rejected (by Codex):
- Recursive-update uniqueness overclaims — `#der-recursive-update` and `#deriv-recursive-update` both already caveat partly-definitional nature

---

## Meta-observation: the rejection set is doing load-bearing work

Across three audits, ~25% of candidate findings were explicitly rejected because the repo's existing scope-honesty discipline already covers them. This ratio is the inverse of the previous audit cycles' rejection rate and is itself evidence that the strengthen-first + scope-honesty-as-load-bearing posture is working: as the repo accumulates honest caveats, audit findings increasingly reduce to integration debts (F23, F25, F29), foregrounding questions (F22, F26, F30, F31), or genuinely novel gaps (F24's causal-sufficiency dominance, F28's $\rho_\Sigma$ circularity).

The findings that *do* survive are substantively different in character from prior cycles' findings: they are less about local segment bugs and more about **global framing decisions** (how to present a body of self-aware content without over- or under-claiming at the entry point). The appropriate repair cadence shifts correspondingly — less "spike and strengthen per finding" and more "consolidation pass across the scope-honesty apparatus."
