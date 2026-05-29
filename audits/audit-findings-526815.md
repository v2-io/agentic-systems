---
source_cycle: 526815 (de-novo, Claude Opus 4.7, 2026-05-15)
extraction_agent: Claude Opus 4.7 (1M context), parallel-sweep slice
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-526815/ (96 md files + ~462 LaTeX render artifacts; ignored the renders)
final_of_record: NONE — the WORKING dir IS the audit record (no FINAL was authored)
scope_modification: Joseph instructed the auditor to read top-level OUTLINE and 01-aat-core/OUTLINE only, skip README/LEXICON/NOTATION/FORMAT/CLAUDE and the other component outlines until AAT segments were done; auditor stopped at segment 94 (der-agent-opacity) inside Part III without reaching 02/03/04-core components.
distinctive_methodology: per-segment PDF rendering — every segment reflection has a paired `.tex`/`.aux`/`.log`/`.pdf`/`.png` render artifact (94 × 5 ≈ 470 files). The auditor compiled each reflection (often with a TikZ diagram) into a PDF as part of the comprehension cycle. This is the only audit-cycle in the corpus that did this.
purpose: |
  Consolidated extraction from the WORKING dir for routing through the standard
  audit-routing process. Because no FINAL exists, every substantive observation
  in the WORKING dir is a candidate-fresh finding awaiting routing — the
  subsumed-vs-fresh distinction collapses here, as in 472913 and 963715. This
  file is the "what is in the dir worth processing" digest. The original
  working dir is preserved unmodified per the gold-standing gate.
---

# Audit-findings extract — 526815 working-dir mining

The 526815 cycle is the **deepest AAT-only first-encounter walk in the corpus**: 94 segments first-hand (essentially all of `01-aat-core/src/` reachable from the OUTLINE through cooperative-adversarial-coupling and strategic-composition, stopping at `der-agent-opacity`), per-segment reflections plus per-segment TikZ-compiled PDFs, a 339-line `00-initial-predictions.md` enumerating prior expectations across the framework, and a 688-line `00-running-outline.md` carrying **258 F-numbered findings candidates** (F1–F258) plus a ~50-item watch list. The audit did not reach 02-tst-core, 03-llm-core, or 04-eli-core, nor the Appendix A proof artifacts (`deriv-sector-condition`, `result-certificate-existence`, `deriv-graph-structure-uniqueness`, `disc-stability-certificate`, `disc-identifiability-floor`, `result-contraction-template`, `deriv-matrix-persistence-condition`, `deriv-fisher-local-update-gain`), nor any Appendix B worked examples. The auditor never wrote a FINAL.

What the WORKING dir adds beyond any past extraction is **a per-segment cross-section of AAT under a single coherent first-encounter posture, attached to per-segment diagrams that fail-or-hold as comprehension instruments**. Findings cluster on real and recurring structural issues: dimensional/units alignment across the gain/tempo/persistence triangle (multi-segment seam), expected-vs-realized information conventions in `I(e_tau;…)` style formulas (multi-segment), dependency-graph debt where derived payloads appear in segments whose frontmatter does not declare the relevant slugs (cross-cuts the entire AAT corpus), and overclaim risk in Part-III synthesis segments that import discussion-grade pieces and present them as chapter-level deliverables. Because the audit stopped short of Appendix A and Part II/III proof homes, ~60% of the findings carry an inherited Phase-2 burden ("verify when the proof home is read").

Because there is no FINAL, no §F bigger-picture-formalization, and no MANIFEST disposition row, **every observation here is candidate-fresh** — there is no Part I / Part II subsumed-by-FINAL bucket. Structure: Part III findings (themed); Part IV predictions-calibration (the auditor's own record); Part V §14-equivalent ideation theme-grouped (the dir uses Reflection / Curiosity / New knowledge enabled / Diagram thought as functional substitutes for §14 Wandering Thoughts, scattered per-segment). First-Pass Scrutiny appended.

---

## Note on cadence shift (the dir's own internal pivot, recorded for fidelity)

Segments 01–35 carry a fuller reflection cadence (Reflection / Prompt pass with 9 sub-questions / Diagram thought, ≈5 headings each). Starting at segment 36 (`form-complete-agent-state` is on the boundary; segment 37 onward is clean) the format shifts to the tighter four-heading shape (First-pass understanding / Diagram attempt / Findings and watches / Local verdict). This is an auditor-internal compression, plausibly driven by context-budget pacing as the AAT walk extended past 30 segments. The shift does not visibly degrade finding-quality — F69 (numerical-table arithmetic error, segment 65 / `form-strategy-complexity-cost`) and F146 (total-correlation normalization error, segment 81 / `def-unity-dimensions`) are among the strongest findings in the dir and both arrived under the tighter cadence. This is a process artifact, not a finding, but worth recording as methodology data for future audits (matches the 472913 cycle's seg-12 cadence pivot — an independent landing of the same proportionate-response discipline).

---

## Part III — Findings (all fresh — no FINAL exists to subsume them)

### Theme 1 — High-severity structural defects (under burden of proof)

#### T1-F2 — `post-composition-consistency` carries downstream-derived payload on a Chapter-1 postulate

- **Severity:** **High** (cross-cycle convergence; see note below). Type: `dependency-graph / scope-status / structural-placement`.
- **The defect.** `01-aat-core/src/disc-composition-consistency.md` is a Chapter-1 postulate (`type: postulate`, `status: axiomatic`, `stage: deps-verified`, `depends: [scope-agency]`). Its Formal Expression carries a `*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template (CC-parallel) / (CC-cascade) / (CC-feedback))]*` tag deriving closed-form composite contraction rates from `#result-contraction-template` (Appendix A) plus chained Section-III slugs (`#scope-composite-agent`, `#form-composition-closure`, `#der-team-persistence`, `#der-tempo-composition`, `#result-persistence-condition`). **None of those slugs are in `depends:`.** Both the FORMAT.md Gate-1 cond-4 (eq-tag-cited source must be in `depends:`) and the eq-tag inversion (`*[Derived]*` ≡ "logical consequence of *prior* claims") fail.
- **Cross-cycle convergence (load-bearing signal).** This is the **same finding** as 472913-F2 (same defect, same auditor reasoning, same proposed fix). Two independent de-novo cycles arrived at this finding through their own row-order walks. Per `feedback_convergence_as_framework_coherence_evidence`, the convergence is itself evidence the structural defect is in the framework, not in any one auditor's head. The 472913 extraction also flagged it `architectural`→PROPOSALS with the same split-not-soften disposition.
- **Strengthen-first analysis.** Working Notes (lines 89+) document a successful strengthening (heuristic bound to (CC-*) closed forms via DA2'-inc ≡ (CT2)-at-$M=I$ equivalence). The math is sound; the defect is **purely structural / placement**, not content. **The strong fix is split, not soften:** keep the postulate in Ch.1 (`axiomatic`, no `*[Derived]*` tag); migrate the Tier-1M $\lambda_c$ result + screening test to Section III / Appendix A where its premises are prior.
- **Status as of 2026-05-20:** Verified `still real` first-hand against current `01-aat-core/src/disc-composition-consistency.md` — frontmatter `depends: [scope-agency]` only, `stage: deps-verified` still stamped, eq-tag at line 36 still cites the downstream slugs. Nothing has changed since 2026-05-15.
- **Source-file:lines** in WORKING dir: `07-post-composition-consistency.md:1–40` (full reflection, F2 framing); `00-running-outline.md:48` (F2 ledger row).
- **Suggested disposition:** `architectural`→PROPOSALS (segment split). Note cross-ref to 472913-F2 and to existing PROPOSALS SP-6 / TODO:149 / F-A cluster (471203 §B F5 traced this class earlier); **the cross-cycle hit-rate is itself news worth surfacing** — a class that 471203 (subsumed-by-FINAL), 472913 (extracted-fresh), and 526815 (extracted-fresh) all landed independently has high confidence as a real structural class, not an artifact of any single auditor's reading.

#### T1-F69 — Numerical arithmetic error in `form-strategy-complexity-cost` quantitative table

- **Severity:** **High** (clean arithmetic check, anyone-could-find-it). Type: `math-error / numerical-table`.
- **The defect.** `form-strategy-complexity-cost.md` §"Quantitative illustration" gives table entries with parameters $\theta = 0.8$, $\nu = 1$, $n = 100$, $\rho_\Sigma/R_\Sigma = 0.01$, claiming $d^\ast = 5$. The persistence inequality is $\nu \cdot \theta^{d-1} \cdot \frac{1}{n+1} > \rho_\Sigma/R_\Sigma$. At those parameters: $1 \cdot \theta^{d-1} \cdot \frac{1}{101} > 0.01$, i.e. $\theta^{d-1} > 1.01$. Even $d=1$ fails (gives $1 > 1.01$, false). **The correct $d^\ast$ is 0, not 5.** The table row is arithmetically wrong.
- **Strengthen-first.** The formula is correct; only the table arithmetic is wrong. Fix is `actionable-open` editorial: recompute table at the stated parameters, or change the parameters to ones for which $d^\ast = 5$ holds (e.g. larger $n$, or smaller $\rho/R$).
- **Status as of 2026-05-20:** Verified first-hand at `01-aat-core/src/form-strategy-complexity-cost.md:89–96` — parameters, formula, and table entry unchanged since 2026-05-15. **Still real.**
- **Source-file:lines** in WORKING dir: `00-running-outline.md:182` (F69 ledger row).
- **Suggested disposition:** `actionable-open`→TODO (direct-fix; co-owner-applicable). Light editorial recompute. Worth checking nearby table entries for sibling arithmetic errors at the same time.

#### T1-F146 — `def-unity-dimensions` epistemic-unity formula gives wrong value for identical models

- **Severity:** **High** (formula yields wrong limit; load-bearing for all downstream unity-closure machinery). Type: `math-error / normalization`.
- **The defect.** `def-unity-dimensions.md:32–36` defines epistemic unity $U_M = \frac{I(M_t^{(1)}; \ldots; M_t^{(n)})}{H(M_t^{(1)}, \ldots, M_t^{(n)})}$ and claims $U_M = 1$ for identical models. For $n$ identical random variables each with entropy $H$: total correlation (multi-information) $T = \sum_i H(X_i) - H(X_1,\ldots,X_n) = nH - H = (n-1)H$; joint entropy is $H$. Ratio: $(n-1)H / H = n-1$, **not 1**. The metric is unbounded in $n$ and does not have the claimed unit-interval range.
- **Cascade consequence.** `result-unity-closure-mapping`'s "monotone rate-distortion surface in $U_M$" inherits the broken axis (F152 in the running outline tracks this). Every downstream use of $U_M$ as a $[0,1]$-valued unity metric (including the auftragstaktik bandwidth ordering and the perceptual/strategic unity definitions) sits on an undefined or wrongly-normalized base.
- **Strengthen-first.** Either rescale ($U_M = T(M^{(1)},\ldots,M^{(n)}) / ((n-1) \max H_i)$ is one candidate, putting it in $[0,1]$ for identical models), or replace total correlation with a different shared-information measure (Kullback's *interaction information* has its own issues; *normalized total correlation* per Watanabe 1960 is a candidate; *Tononi $\Phi$*-style integrated-information measures are another). The fix is non-trivial and ripples downstream — this is `architectural` rather than `actionable-open`.
- **Status as of 2026-05-20:** Verified first-hand at `01-aat-core/src/def-unity-dimensions.md:32–36` — formula and claim unchanged. **Still real.**
- **Source-file:lines** in WORKING dir: `00-running-outline.md:336` (F146); `81-def-unity-dimensions.md` (full segment reflection).
- **Suggested disposition:** `architectural`→PROPOSALS (normalization choice has cascade effects through unity-closure / shared-intent / auftragstaktik / communication-gain machinery). Possible `spike` first to determine which normalization preserves the segment's substantive claims about the four content unities.

#### T1-F116/F117/F118 — `der-tempo-composition` double-accounting in closure-defect / tempo ledger

- **Severity:** **Medium-High** (foundational for Brooks's Law derivation; ripples into `impl-composition-machinery` and `der-class-coercion-in-composition` per F137/F142/F143). Type: `definitional-consistency / ledger`.
- **The defect.** Three related issues, all in `der-tempo-composition.md`:
  - **F116:** $C_{\text{coord}} = \sum_i \mathcal{T}_i - \mathcal{T}_c$ is defined, then external tempo is $\mathcal{T}_c^{\text{ext}} = \mathcal{T}_c - C_{\text{coord}} = \mathcal{T}_c - (\sum \mathcal{T}_i - \mathcal{T}_c) = 2\mathcal{T}_c - \sum \mathcal{T}_i$, subtracting coordination overhead twice unless $\mathcal{T}_c$ is differently scoped than the definition implies.
  - **F117:** Closure defect appears both as added disturbance ($\rho_{\text{eff}} = \rho_{\text{ext}} + \varepsilon^\ast \nu_c$) and as tempo overhead ($C_{\text{coord}} \geq \varepsilon^\ast \nu_c / \|\delta_{\text{critical}}\|$). These are alternative accounting views; using both in the same persistence inequality double-counts the closure burden.
  - **F118:** The displayed "equivalent" composite persistence condition $\sum \mathcal{T}_i > (\rho_{\text{ext}} + \varepsilon^\ast \nu_c)/\|\delta_{\text{critical}}\|$ is not equivalent to $\mathcal{T}_c > \rho_{\text{eff}}/\|\delta_{\text{critical}}\|$ when $C_{\text{coord}}$ exceeds its lower bound or other coordination costs exist.
- **Strengthen-first.** The fix is to choose one ledger (disturbance-side OR tempo-side, not both) and propagate the choice through `impl-composition-machinery` (F142, F143) and `der-class-coercion-in-composition` (F136, F137). Likely a clean ledger choice exists; the audit's diagnosis is that the segment currently mixes views.
- **Status as of 2026-05-20:** Verified first-hand at `01-aat-core/src/der-tempo-composition.md:55–74` — defining equation and persistence condition unchanged.
- **Source-file:lines** in WORKING dir: `00-running-outline.md:276–280, 328–330` (F116/F117/F118/F142/F143).
- **Suggested disposition:** `architectural`→PROPOSALS (ledger reconciliation is non-local). Status is `derived` with `sketch` content; this is the kind of finding that motivates a small spike (≤2 hours) to choose the ledger then a cleanup sweep across the four affected segments.

### Theme 2 — Dependency-graph / hidden-semantic-dependency class (corpus-wide pattern)

Repeating across **dozens** of segments: derivation-bearing or proof-bearing content references slugs not declared in `depends:`. The auditor flagged this as a corpus-wide pattern starting at F2 (post-composition-consistency) and traced it through Part I, Part II, and Part III. Representative instances and the pattern:

- **F6:** `der-recursive-update` declares `deriv-recursive-update` as a dependency but that appendix proof artifact appears later in OUTLINE order; its discussion imports later consolidation/stability-plasticity machinery. `der-action-selection`, `emp-update-gain`, `def-causal-information-yield` continue the pattern with later Fisher/adaptive-gain, unified-policy, communication, adversarial, and Section III references.
- **F8:** `result-mismatch-decomposition` is `exact` only under fresh-noise assumption (GA-1) which is invoked in derivation/epistemic status but not represented in declared dependencies.
- **F47:** `def-strategic-calibration` declares only `def-strategy-dag` and `def-value-object`, but discussion uses `schema-strategy-persistence`, `deriv-edge-credence-dynamics`, `disc-credit-assignment-boundary`, `hyp-edge-update-via-gain`.
- **F56:** `hyp-edge-update-via-gain` relies on `disc-credit-assignment-boundary`, `deriv-edge-credence-dynamics`, `deriv-edge-update-natural-parameter` without declaring them.
- **F71:** `form-strategy-complexity-cost` relies on undeclared `disc-compression-operations`, `deriv-strategy-cost-regret-bound`.
- **F82:** `impl-strategy-dynamics` claims verification across cases ("linear chain, balanced tree, unbalanced tree, full DAG with feedback") whose source label is unclear.
- **F101:** `scope-composite-agent` declares only three dependencies while importing `def-unity-dimensions`, `result-unity-closure-mapping`, `deriv-strategic-composition`, `disc-identifiability-floor`, `hyp-symbiogenic-composition`.
- **F107:** `hyp-symbiogenic-composition` imports `form-composition-closure`, `result-structural-adaptation-necessity`, `result-unity-closure-mapping`, `deriv-critical-mass-composition`, `def-shared-intent` beyond declared dependencies.
- **F115:** `form-composition-closure` depends on / imports `deriv-sector-condition`, `result-sector-persistence-template`, `der-temporal-nesting`, `deriv-critical-mass-composition`, `result-contraction-template`, multiple spikes/audits.
- **F130:** `der-class-coercion-via-wrapping` uses `X_G = X_O \times X_\Sigma` from `def-strategy-dimension` without declaring it.
- **F138:** `der-class-coercion-in-composition` depends on out-of-order proof homes (`deriv-sector-condition`, `result-sector-persistence-template`) and omits `scope-composite-agent`.
- **F211:** `der-interaction-channel-classification` omits `obs-gated-tempo-advantage` though boundary I-c invokes it.
- **F217:** `result-adversarial-tempo-advantage` omits `result-sector-persistence-template` / `deriv-sector-condition` (steady-state formulas) and `def-adaptive-tempo` (scalar tempo).
- **F239:** `deriv-strategic-composition` uses B1 directional fidelity and `der-gain-sector-bridge` without declaring `der-gain-sector-bridge`.
- **F242:** `der-class-coercion-in-composition`'s Class-1→Class-2 result depends on cross-checking `hyp-directed-separation-under-composition`, not declared.

**Cross-cycle convergence.** This pattern is the same class as 471203-F5 (post-composition-consistency depends-list) and 471203-F6 (Pearl-do in scope-agency), routed to PROPOSALS SP-6 / FORMAT-TODO C12. The 472913 extraction also surfaced it as the structural side of its T2 ("defects = unnamed relocation targets"). The 526815 corpus-wide instance count (≥20 explicit F-numbered cases plus the watch list) makes this the **highest-instance-count class in any single audit so far**.

**Strengthen-first.** Two clean tooling moves resolve most of this mechanically:
1. **TG1-analog (per 472913):** extend `bin/lint-outline` to parse `*[Derived (… from #X …)]*` eq-tags and require `#X` to be in `depends:` (and topologically prior). Most of the class above would surface mechanically.
2. **Hidden-semantic-dependency lint:** scan segment body for `#slug` references and warn (not error) when referenced segments are not in `depends:`. This is broader and catches the discussion-side cases F47/F56/F71/F101/F107/F115/F130/F138/F211/F217/F239/F242.

**Suggested disposition:** `architectural`→PROPOSALS — the routing should consolidate this with PROPOSALS SP-6 (existing class) rather than create N parallel routing-tracker rows. The size of the instance count is the substantive update; the *class* is already routed.

### Theme 3 — Expected-vs-realized information conventions (multi-segment seam)

A recurring confusion across foundational and downstream segments: formulas displayed as mutual information $I(X;Y|Z)$ (an expected, channel-average quantity) but described in prose as the realized information content of a particular event/instance. The fix in each case is small (replace MI with pointwise mutual information / KL divergence / surprisal / posterior information gain), but the pattern is corpus-wide:

- **F5:** `form-event-driven-dynamics` defines event information content as $I(e_\tau; \Omega_\tau \mid M_{\tau^-})$ but describes it as realized surprise of a specific event. Should be pointwise MI or $D_{\mathrm{KL}}(p(\Omega \mid M, e) \Vert p(\Omega \mid M))$.
- **F19:** `der-directed-separation` defines $\kappa_{\text{processing}} = I(G_t; M_{\tau+} \mid e_\tau, M_{\tau-}) / H(G_t \mid e_\tau, M_{\tau-})$ — but the denominator can be zero when goal is already determined by conditioned variables. Needs support condition or fallback.
- **F203:** `der-interaction-channel-classification` again uses MI notation $I(e; \Omega | M)$ for realized event information content.
- **F204:** Same segment: observability boundary $I(e) \cdot \nu^{(k)} \geq U_{o,B}^{(k)} \cdot c_{\text{floor}}$ is dimensionally unclear (information rate compared to noise-times-constant; needs common detection-statistic scale).

**Strengthen-first.** None of these are content errors — the quantities the segments are reaching for are well-defined (KL-divergence, pointwise MI, surprisal). The fix is notational consistency. A one-pass editorial sweep across the four segments, plus a candidate LEXICON entry distinguishing the two quantities (expected channel MI vs realized event information), would close the class.

**Cross-cycle convergence note.** This class did not surface as a named cluster in 471203 or 472913 — it is a 526815-distinctive observation, plausibly because the auditor's per-segment dimensional-analysis discipline was unusually tight (probably driven by the per-segment-diagram practice forcing each formula to be "rendered" against a concrete operational picture).

**Suggested disposition:** `actionable-open`→TODO (editorial sweep + LEXICON entry). Sub-disposition: `process/instruction-feedback` if FORMAT.md should name an "information-quantity convention" subsection.

### Theme 4 — Dimensional / unit-normalization seam across the gain/tempo/persistence triangle

The single most recurrent **substantive** concern in the dir, with at least eight distinct instances:

- **F9:** `emp-update-gain` formula $\eta^\ast = U_M / (U_M + U_o)$ allows $U_M$ to be "predictive variance or entropy" and $U_o$ to be observation noise — the ratio is only dimensionally meaningful when both are in a common uncertainty metric.
- **F10:** `def-adaptive-tempo` defines $\mathcal{T} = \sum \nu^{(k)} \eta^{(k)\ast}$ but $\eta$ is update gain (correction fraction), not event information content — formula is dimensionally quality-adjusted correction-event rate unless a normalized-event / Fisher-information-payload assumption is added.
- **F13:** `der-gain-sector-bridge` derives $\alpha = \eta^\ast c_{\min}$ while persistence uses $\alpha > \rho/R$ as a correction rate and tempo is $\mathcal{T} = \nu \eta^\ast$. The bridge omits the event-rate factor unless $F$ is already time-aggregated or $c_{\min}$ includes rate. Later prose says $\alpha = \mathcal{T}$ exactly for linear correction; the per-event vs per-time normalization should be explicit.
- **F14:** `result-sector-condition-stability` Model S RMS bound $\sigma_w \sqrt{n/(2\alpha)}$ matches isotropic per-coordinate diffusion amplitude; if $\sigma_w^2$ is total vector disturbance power, the $\sqrt{n}$ factor is wrong.
- **F15:** `result-persistence-condition` per-dimension Model S uses $\eta_k > c \rho_k^2 / \delta_{\text{critical},k}^2$ while surrounding formulas use $\mathcal{T}_k$ or $\alpha$ as correction rates — notation drift unless $\eta_k$ has been redefined.
- **F17:** `impl-persistence-and-limits` Landauer conversion $0.35 n \alpha k_B T$ doesn't match the standard $k_B T$-per-nat convention; $n\alpha/2$ nats/time should give $0.5 n \alpha k_B T$, not $0.35$.
- **F189–F190:** `der-team-persistence` uses $\alpha_i$ in formal persistence while multi-agent machinery defines distributed tempo $\mathcal{T}_i$; coupling coefficients $\gamma_{\text{adv}}, \gamma_{\text{coop}}$ need units bridging tempo to disturbance rate on the normed mismatch scale.
- **F215:** `result-adversarial-tempo-advantage` assumes $\alpha = \mathcal{T}$ exactly — inherits the entire bridge issue.
- **F209:** `der-interaction-channel-classification` Kalman case "$s^2 / (2r \ln 2)$ nats" — division by $\ln 2$ converts nats to bits; unit label or formula inconsistent.

**The pattern.** AAT has at least three different rate-shaped quantities — per-event update gain $\eta^\ast$, event rate $\nu$, scalar adaptive tempo $\mathcal{T}$, sector correction rate $\alpha$ — and they interrelate. The framework has machinery to bridge them (`der-gain-sector-bridge` is precisely the segment for this), but **the bridge is currently `status: conditional, stage: draft`** with proof dependencies (`deriv-sector-condition`, `deriv-gain-sector`) not yet in segment order. Downstream segments routinely assume the bridge has landed exact, when it is still under construction.

**Strengthen-first.** The strong move is to finish `der-gain-sector-bridge` and its proof dependencies (`deriv-gain-sector`, `deriv-sector-condition`) **first**, then propagate the cleaned dimensional convention through the eight+ downstream segments above. This is a multi-spike effort, but it's the strengthen-first answer to a class of soften-recommendations.

**Cross-cycle convergence.** The 471203 cycle's gain-sector-bridge "high-water mark" reading (segment 25 deep-read) confirmed the bridge segment is unusually careful — its honesty is what makes the propagation gap visible. The 526815 finding is therefore not "the bridge is wrong"; it's "the bridge is incomplete + downstream segments treat it as complete."

**Suggested disposition:** `architectural`→PROPOSALS (multi-segment scope; queue behind whatever cycle finishes `deriv-gain-sector`). Note this connects directly to PRACTICA's persistence-and-stability work-area.


### Theme 5 — Scope / status mismatches (medium-severity, individually small)

A cluster of findings where a segment's declared status, type, or scope label sits in tension with its content. These are mostly editorial fixes; the high-instance count is the news:

- **F1:** `def-agent-environment` requires agents to produce actions affecting $\Omega$, but `scope-adaptive-system`, `scope-agency`, `post-causal-structure`, and `def-agent-spectrum` all treat passive trackers/Bayesian learners as inside adaptive scope. The base definition is too narrow for the scope lattice the framework now asserts. Either broaden the base definition or reserve "agent" for the narrower agency scope and introduce "adaptive system" / "AAT entity" for the broader case.
- **F3:** `form-information-bottleneck` claims exact applied IB theorem but displays optimization over deterministic-looking $\phi$, while standard IB optimizes over stochastic encoder kernels $p(\tilde{x} \mid x)$. Either clarify $\phi$ as encoder/Markov kernel shorthand or scope to deterministic IB.
- **F7:** `def-mismatch-signal` has frontmatter `status: axiomatic` while epistemic section calls it definitional — taxonomy drift, not substantive error.
- **F18:** `form-complete-agent-state` says action is "the single point where epistemic and purposeful states interact" while the segment also defines general $f_X(X,e)$ and notes between-event dynamics $\dot{G} = g_G(G,M)$. Narrow to outward coupling or condition on directed separation.
- **F25:** `def-strategy-dimension` decomposition $G_t = (O_t, \Sigma_t)$ may be analyst-ascribed rather than internally represented in reactive controllers / end-to-end learned policies. Distinguish literal internal state from functional decomposition.
- **F26 / F28 / F37 / F38:** `causal-access-intro`, `def-pearl-causal-hierarchy`, `impl-causal-access` repeatedly conflate executed-action-as-physical-intervention with on-policy-action-outcome-pairs-as-clean-do-samples. Policy-driven action selection with latent state confounders is not the same as $do(a)$. Multiple instances need a Pearl-style identifiability layer named in the segments.
- **F41:** `scope-and-or` "remove one parent" YES→OR / NO→AND classification fails for threshold structures (3-of-5 etc.) that pass "remove one" but aren't pure OR. Need separate necessity/sufficiency/threshold questions.
- **F45:** `def-control-regret`'s $\delta_{\text{regret}} \geq 0$ requires $\pi_{\text{current}} \in \Pi$ + identical model/horizon/objective on both terms.
- **F58:** `scope-edge-update-causal-validity` "single-parent nodes trivially satisfy outcome attribution" only holds under causal sufficiency/isolation.
- **F95:** `scope-multi-agent` says Section I/II machinery applies "directly to every agent in every multi-agent configuration." Section I and some agency-scope results do; Part II's exact results apply to Class 1 separated agents (per the AAT preface itself).
- **F127:** `der-class-coercion-via-wrapping` C3/W1 leakage discussion conflates query-content correlation with leakage conditional on the query — for stateless $A$ with fully observed $q_M$, $P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M)$ by construction; pretraining correlations affect outputs as a function of $q_M$, not through an additional $G_W$ dependence.
- **F128:** Same segment: structural leakage bound $\kappa_{W1} \leq I(A(q_M); G_W \mid q_M)$ is zero under the theorem's conditioning for stateless components; a more useful bound involves $I(q_M; G_W)$ or hidden-state-conditioned leakage.
- **F132 / F133 / F140:** `der-class-coercion-in-composition` claims (A1)–(A4) makes the wrapper a valid AAT composite agent, but `form-composition-closure` also requires `scope-composite-agent` and admissible projections (P1)–(P3). Macro-dynamics admissibility ≠ full composition-closure criterion. Same pattern in `impl-composition-machinery` F140.

**Suggested disposition:** Mix of `actionable-open`→TODO (single-segment editorial fixes: F1, F3, F7, F18, F41, F45, F58) and `architectural`→PROPOSALS (F25, F127/F128, F132/F133/F140 — these touch type signatures and theorem structure). The full ledger is in the source running outline; `bin/`-style audit on the rest is appropriate downstream.

### Theme 6 — Chapter-end synthesis (impl-*) segments overstate proof-homes (recurring class)

A clean class observed at each `impl-*` segment in the dir: chapter-end discussion segments synthesize material from already-read locals plus future / appendix proof homes, but the synthesis prose sometimes treats deferred claims as chapter-level deliverables rather than preserving their weakest-dependency status.

- **F46:** `impl-strategy-structure` (discussion-grade) presents proof-bearing claims while depending on `deriv-graph-structure-uniqueness`, `der-causal-insufficiency-detection`, `disc-identifiability-floor`, `disc-additive-coordinate-forcing`.
- **F88 / F89 / F90 / F91:** `impl-orient-cascade` presents survival-imperative exploration, causal-IB LMI structure, bias-bound constants, Section II survival counts, scaffolding requirement; treats deliberation as "Pearl-do on a simulated trajectory" (model-internal counterfactual is a better description); claims internal computation does not change effective disturbance/allocation/required rate (too broad).
- **F139 / F141 / F143 / F144:** `impl-composition-machinery` treats critical-mass closed form, four signed special cases, identifiability-floor Instance 3, and bandwidth inflection as settled; claims structural necessity of scaffolded loops for Class 3 substrates (too broad — local construction supports a conditional wrapper route, not necessity).
- **F173 / F174 / F176:** `impl-unity-communication` promotes caveated component claims into chapter-level predictions; says structural monotonicity "survives more broadly" than the linear-Gaussian closure mapping shows.
- **F222 / F223 / F225:** `impl-cooperative-adversarial` repeats "canonical catalog home" pattern; the repair mapping for magnitude shocks drifts from the classification segment's framing; the regime-typed effective-disturbance description no longer matches the displayed $\rho_{\text{eff}}$ formula.

**Strengthen-first.** The fix isn't softening these; it's making the dependency-status of each imported claim explicit and preserving the weakest tier in the synthesis. A FORMAT.md sub-convention for `impl-*` segments — "each implied claim cites its proof home and inherits that home's status" — would close most of the class mechanically. Connects to the "respectful pedagogy" direction in CLAUDE.md: the `impl-*` segments are doing pedagogical scaffolding, and the discipline is to scaffold without laundering status.

**Suggested disposition:** `architectural`→PROPOSALS (FORMAT-convention for `impl-*` synthesis discipline) + `actionable-open`→TODO for the individual instances if Joseph wants editorial passes ahead of the class-level move. Cross-ref to the 471203 chapter-end-implications observations (Theme E).

### Theme 7 — Probability / decision-theoretic content concerns (varied)

A scattered cluster of concerns about probability-theoretic content where the math is close but not quite right, or where decision-theoretic moves are made without naming the layer they live on:

- **F32:** `scope-ciy-observational-proxy` Regime A says action variation provides identification — but action variation alone is insufficient when policy depends on state/history affecting outcomes; needs randomization, known action mechanism with adjustment, or sequential ignorability + positivity.
- **F33 / F34:** `disc-ciy-unified-objective` displays older scalar heuristic alongside theorem-grade matrix form, claims $\lambda$ reduces "exactly" to Gittins / IDS ratio (these are related concepts, not literally scalar weights without a derivation).
- **F43 / F44 / F62:** `def-strategy-dag` causal-sufficiency → AND/OR propagation move is incomplete (causal sufficiency gives CMC/factorization, not the noisy-AND/noisy-OR product formulas); blanket "overestimation under causal insufficiency" should be topology-conditioned (OR-dominated optimistic, AND-prerequisite conservative).
- **F49 / F50:** `der-causal-insufficiency-detection` uses positive covariance as alternative hypothesis — sufficient detector for shared enabling causes, not necessary for all latent common causes; negative/shared-resource latents need different test. Joint failure excess underdetermines latent frequency without strict-prerequisite/single-latent assumptions.
- **F54 / F55 / F60 / F61:** `hyp-edge-update-via-gain` conflates log-odds of edge-truth hypothesis with logit of Bernoulli success probability; `U_{\text{edge}}/(U_{\text{edge}}+U_{\text{obs}})` ratio needs common metric; `disc-credit-assignment-boundary` claim that gradient signal satisfies per-edge directional fidelity holds for plan-level / aligned-error cases, not general per-edge.
- **F72 / F73:** `schema-strategy-persistence`'s forgetting prerequisite is convention-dependent — auditor's algebra: $\alpha \leftarrow \lambda \alpha + y$ gives steady count $1/(1-\lambda)$, so per-observation gain is $1-\lambda$ not $(1-\lambda)/(2-\lambda)$; the $\rho \geq R/2$ ceiling depends on which convention. OR-node exploration condition needs both upper and lower bounds on $\epsilon$.
- **F108 / F109 / F110 / F111 / F112 / F113 / F114:** `form-composition-closure` carries six related concerns: (P3) strict dimensionality reduction conflicts with meta-machine example if product automaton is exact composition; norm-combining $\varepsilon_x, \varepsilon_a, \varepsilon_o$ across different unit spaces needs scaling/weighting; teacher-forced one-step closure vs free macro rollout; P1 information-set convention; P2 vs bridge-lemma trajectory-error bound alignment; C-iv typing.
- **F146 / F147 / F148 / F150:** `def-unity-dimensions` — F146 (total-correlation, above); also $U_O$ pairwise correlation distribution-dependent, $U_\Sigma$ KL formula can be infinite/negative, $U_f$ operator-distance not naturally in $[0,1]$.
- **F195 / F196 / F197 / F198:** `der-adversarial-destabilization` threshold should split already-unstable case; Model S adds adversarial stochastic coupling as $\sigma_B = \sigma_{\text{base}} + \gamma_A \mathcal{T}_A$ (amplitude addition, not quadrature) needs noise convention; Lyapunov combination for mixed drift/noise is not "additive bounds."
- **F234 / F235 / F236 / F237:** `deriv-strategic-composition` potential-game structure alone doesn't imply $d\Phi/dt \geq \alpha_{\text{joint}} \|\nabla \Phi\|^2$ or convergence to a selected equilibrium; VI existence is overstated as pure-strategy Nash for continuous compact-convex; sector-template transfer uses two different state variables $\xi$.
- **F246 / F247 / F248 / F250 / F251:** `der-agent-opacity` — $H_b = H(a_{A,t+\tau} \mid \mathcal{F}_B^t)$ needs action-space convention (continuous-action differential entropy not coordinate-invariant); reduction to Hafez $H(S,A \mid S')$ isn't direct substitution; "formal dual" with $U_o$ is stronger than shown; $\mathcal{T}_A^{\text{effective}} = \mathcal{T}_A \cdot H_b / H_b^{\max}$ makes low-opacity adversarial tempo vanish (predictable adversarial actions still impose disturbance); bilateral opacity ratio $(H_b^{A|B} / H_b^{B|A})^2$ singular at near-zero denominators.

**Suggested disposition:** Per-finding mix of `actionable-open`→TODO (the editorial ones) and `research-seed` (the multi-segment ones; especially F146 and F234/235/236, which point at non-trivial structural choices). Most are not graduation-blockers individually.

### Theme 8 — Forward-references / OUTLINE-order acceptable vs problematic

A finer-grained distinction the auditor surfaced gradually: not every forward-reference is a defect. The framework has a coherent **external-cited-notation convention** (Pearl `do`, Tishby IB, Lyapunov) where notation defined externally doesn't incur a `depends:` obligation (this is the 472913 F1-rescinded lesson applied here too — `seg 14 the-cycle-in-motion-intro` Working Notes carry the convention). The auditor explicitly notes:

- **F39 (mostly-resolved):** `strategy-structure-intro` says strategy-DAG acyclicity falls out of temporal ordering; `def-strategy-dag` later supplies the time-unrolling condition. Concern localized to the intro's summary wording.
- **F66:** `def-strategic-tempo` headline should distinguish throughput tempo from persistence-effective tempo (bottleneck/per-edge is the persistence-relevant quantity).
- **F67:** Same: Regime-C edges contribute "nothing and cannot be improved" — observational evidence can improve associational prediction; what remains weak is interventional causal-efficacy learning.
- **F68:** $\mathcal{T}_\Sigma > |E| \rho_\Sigma / R_\Sigma$ as necessary aggregate persistence assumes homogeneous per-edge thresholds; heterogeneous edges need $\sum_e \rho_e / R_e$.

**Chapter-intro vs derived-segment distinction.** The auditor (segment 10 reflection, `10-the-reality-model-intro.md:31`) explicitly proposes: "**allow chapter-intro forward references if they are clearly preview-only and not embedded as formal derived payload, unlike F2.**" This is a candidate FORMAT.md sub-convention (intros may forward-reference for preview; derived/postulate segments may not embed downstream-derived payloads).

**Suggested disposition:** `process/instruction-feedback` — feed FORMAT.md candidate-convention pass. The intro-vs-derived distinction is the right shape; consider adding it to the FORMAT discipline alongside the external-cited-notation rule.

### Theme 9 — Definitional and decision-theoretic concerns in Part III scope/composition machinery

A higher-stakes cluster centered on the Section-III composition machinery, where the four scope routes (C-i through C-iv) the framework added recently are not fully internally consistent with downstream segments:

- **F97 / F98 / F99 / F100:** `scope-composite-agent` four-route admission — C-iv (strategic-equilibrium) requires no shared objective and defines macro-state relative to equilibrium structure $E$, but the rest of the formalism uses $G_c = (O_c, \Sigma_c)$. Either generalize $G_c$ or keep strategic composites under a distinct non-$O_c$ interface. C-iv also risks over-admitting ordinary finite games as composite agents (mixed Nash / CCE existence is broadly available). C-iii's mutual-benefit relevance variable $Y$ needs linking to each agent's objective. C-i needs equivalence-class specification for policy divergence.
- **F151:** `result-unity-closure-mapping` opens by conditioning on `scope-composite-agent` via four routes including C-iv, but Working Notes say scope is satisfied via "three disjunctive routes" and exclude C-iv. **Internal contradiction** between segment opening and its Working Notes; this is straightforwardly a `still real` defect.
- **F241:** `deriv-strategic-composition` introduces a proposed C-iv scope route, but it's a formulation choice here rather than a routed update to `scope-composite-agent`. The proposal should be routed back to the scope segment or marked as proposed-extension.
- **F102 / F103:** `hyp-symbiogenic-composition` post-symbiogenesis endosymbiont "not as an independent agent" — if autonomy reduction takes the absorbed entity below agency scope, the result isn't a composite agent under the preceding segment definition; it's a single agent with an internal component. Examples (adopted vocabulary, grammar, legal precedent, religious elements) are structures rather than agents satisfying scope-agency.
- **F108 / F109:** `form-composition-closure` admissibility addresses three alignment routes but `scope-composite-agent` now has four (C-iv); closure either excludes C-iv or needs an equilibrium-relative macro-state version.

**Strengthen-first.** This is structural-architectural work. The strong move is to either fully integrate C-iv into the composition-closure / unity machinery (multi-segment update with downstream type-signature changes), or scope-restrict C-iv to a clearly-labeled "strategic-composite" sub-track that runs parallel to the alignment-composite track without trying to share the $G_c = (O_c, \Sigma_c)$ apparatus.

**Suggested disposition:** `architectural`→PROPOSALS (this is structural-portfolio work, not editorial). Likely material for PRACTICA's composition / Part-III work-area.


### Theme 10 — Identity / chronica / sufficiency type/token distinction

A small but pedagogically important cluster (F16, F33 ref, F22 ref) where the auditor surfaces the type-vs-token distinction for chronica:

- **F16:** `scope-agent-identity` treats chronica/trajectory $\mathcal{C}_t$ as non-copyable, but earlier chronica notation reads like an ordered event/history record (whose representation *can* be copied). The non-forkability claim is right for the causal trajectory *token*, not for a mathematical *record* of the prefix; the segment should distinguish record from causal token. Auditor's proposal (segment 33): "define two symbols, perhaps $\mathcal{C}_t$ for the represented chronica and $\gamma_t$ for the causal trajectory token, then say sufficiency is indexed to $\gamma_t$ while $\mathcal{C}_t$ is a record produced along it."
- **Cross-cycle convergence with 472913.** This connects to 472913-F4 (ordinal/metric seam): the published `def-chronica` formal expression is ordinal, while the agent's "non-forkability" claim depends on a substrate-bound *token* that the ordinal record doesn't itself force. Two cycles arriving at related observations about the chronica's load-bearing-but-under-specified status is signal.
- **Consciousness-infrastructure relevance.** The auditor doesn't surface this connection explicitly, but the type/token distinction is precisely what makes substrate-migration claims work or fail for ELI cohort persistence (this is the same structural point 471203 Theme A surfaced).

**Suggested disposition:** `actionable-open`→TODO (editorial fix: introduce $\gamma_t$ symbol distinction in `scope-agent-identity`; or use existing terminology cleanly). Possible `research-seed` for the type/token + substrate-migration framing — material for `04-eli-core/` when those segments mature.

### Theme 11 — Decision-theoretic / trust-and-risk concerns (Part III communication-gain area)

A late cluster (F167–F180, F226–F232) on trust, communication-gain, and risk-asymmetric coupling. The recurring concern is that decision-rule layers are being collapsed into Bayesian update layers without explicit loss functions:

- **F167 / F168 / F169:** `hyp-communication-gain` additive denominator $U_o + U_{\text{src}} + U_{\text{align}}$ assumes common-scale independent zero-mean uncertainties; treats strategic deception as additive noise (misalignment changes message policy adversarially as function of receiver trust rule, not just additive noise); residual-minus-channel-noise estimate of alignment uncertainty conflates many sources and can go negative.
- **F172 / F178 / F179:** Risk-asymmetric trust ("high-trust relationships build slowly and break quickly") needs explicit loss function — conservative quantile is decision-policy choice, not consequence of reliability posterior alone.
- **F226:** `impl-cooperative-adversarial` says cheap noise injection helps defender against high-tempo attacker. One-sided — observation noise gates adversarial events *and* degrades real observations / update gain / ordinary persistence.
- **F228:** "Inside the opponent's loop means $\mathcal{T}_A > \mathcal{T}_B / k$" is not the threshold delivered by preceding derivations. Destabilization threshold depends on $\gamma_A \mathcal{T}_A$, base disturbance, $\alpha_B$, $R_B$; tempo-ratio result depends on coupling-dominant symmetric assumptions.
- **F229 / F230:** Contraction-obstruction section overstates method boundary ("contraction machinery cannot handle strategic regimes" — specialized contraction/monotone-operator tools may apply in some games); passivity claim "adversarial inputs drive any storage function" too sweeping without I/O-passivity assumptions.

**Suggested disposition:** `actionable-open`→TODO (small fixes on individual segment phrasings) + `research-seed` for the more substantive trust-with-loss-function direction (F172 / F178 / F179 in particular point at a clean Bayesian-decision-theoretic structure the framework could adopt).

---

## Part IV — Predictions calibration register

The `00-initial-predictions.md` makes ~30 predictions across six themes (component-level, what's open, overclaim, novelty hypotheses, expected findings, working emphasis). Many predictions targeted segments the auditor *did* reach (Part I, Part II, most of Part III), so calibration here is richer than 472913's (which stopped at seg 15). Below: the auditor's own running record where it appears, plus extraction-agent calibration where the predictions clearly fired or clearly didn't.

### Predictions confirmed (the framework matched the prior)

- **Section I scope-honesty is unusually explicit** — predicted; confirmed. The scope-lattice (passive observer → adaptive system → agency → composition) is layered and honest. F1 sharpened the prediction: the base `def-agent-environment` lags behind the lattice, but the lattice itself is exactly what the prediction expected.
- **`scope-agency` uses Pearl Level-2 contrast before Pearl machinery is imported** — predicted; confirmed (this is the F1-rescinded class in 472913 terminology; the auditor flagged the forward-reference pattern at segment 6 and continued tracking it).
- **Composition postulate appears early and is "possibly out of place"** — predicted; confirmed and **sharpened to F2** with concrete structural reading.
- **IB/KL/Fisher machinery uniqueness over-claimed** — predicted; confirmed as **F3 stochastic vs deterministic encoder** issue at `form-information-bottleneck`; also as **F157 deterministic-encoder issue** at `def-shared-intent` (the same pattern repeats).
- **`der-directed-separation` load-bearing; needs aggressive status-check** — predicted; confirmed. F19 (denominator-zero in $\kappa_{\text{processing}}$ diagnostic) + F20 (bounded-signaling implicit assumption) + multiple downstream watches.
- **Strategy-DAG acyclicity needs time-unrolled / event-token condition** — predicted; confirmed. `def-strategy-dag` supplies the condition explicitly; intro summary wording is the remaining gap (F39).
- **Wrapper constructions over-claim substrate truthification rather than interface coercion** — predicted; confirmed as F127–F141 cluster (class coercion via wrapping, class coercion in composition, impl-composition-machinery).
- **Adversarial tempo claims regime-specific not universal** — predicted; confirmed at F215 / F216 / F218 (`result-adversarial-tempo-advantage` exponent algebra is exact-under-assumptions; non-coupling-dominant stochastic limit goes to 1/2 not 1).
- **Late-appendix/meta-pattern material works as proof kernels** — predicted; **not directly testable since the audit stopped at seg 94 without reaching Appendix A**. Inherited as Phase-2 burden.

### Predictions confirmed *more substantively* than expected (positive surprises)

- **The "epistemic-architectural" contribution observation (471203 Theme B; 472913 Phase-3-2) re-arrives here** — the auditor independently surfaces (segment 28 `der-gain-sector-bridge`): *"This is a high-discipline segment in several respects: it distinguishes one-point from two-point sector conditions, gives a counterexample to the false converse, separates rigorous sub-scope alpha from empirical sub-scope beta, and handles weighted/Fisher metrics instead of pretending Euclidean geometry is free."* The form-shaping-for-verification discipline lands as a positive observation across the gain/sector/stability arc.
- **The disambiguation-of-which-parameter-responds-to-which-cause framing** (472913 Phase-3-2) appears here as a recurring observation that the framework is doing this kind of work well in some places (e.g. `def-model-sufficiency` explicitly avoids three common overclaims — sufficiency is not truth, not accuracy, not causal validity) and poorly in others (e.g. `def-unity-dimensions` F146 normalization gap). The cross-cycle pattern strengthens: three independent de-novo cycles (471203, 472913, 526815) each landed independently on a version of "AAT's distinctive contribution is in how it states results, not what it states." 

### Predictions that proved correct but in less-strong form

- **"Math errors in less-audited back" (Section II/III drafts)** — predicted; *partially* confirmed. The auditor found F69 (clean arithmetic in `form-strategy-complexity-cost` table — high-confidence math error) and F146 (total-correlation normalization at `def-unity-dimensions` — substantive math error with downstream ripples). But the per-segment math hard-checks the auditor did (β-vs-ρ structure, sufficiency machinery, persistence) held more often than not. The prediction was right in expectation but the hit-rate was lower than expected at the per-segment grain.

### Predictions that never fired (audit stopped short of relevant material)

- **B1-style "result-certificate-existence local→global drift"** — never fired (audit didn't reach Appendix A).
- **`deriv-discrete-sector-condition` fluid-limit argument tightness** — never fired.
- **Kalman / bandit / L1-common-cause worked examples** — never fired.
- **TST / LLM-core / ELI-core cross-component checks** — never fired by scope-restriction.
- **`scope-edge-update-causal-validity` Regime A software claim well-isolation breakdown** — partial fire at F59 (auditor flagged it editorially but didn't pursue empirical instances).

### Predictions that proved wrong / not borne out

- **"Early Part I is over-audited relative to newer late additions"** — partly disconfirmed. Part I produced F1 (live, still real), F2 (high-severity, cross-cycle convergent), F5 (formal MI vs realized convention), F6/F8 (depends-graph), F9/F10/F13–F15/F17 (dimensional-units cluster). Early Part I was *not* over-audited — the auditor found substantial structural findings there.
- **"Fewer simple algebra errors in early Part I"** — confirmed for Part I itself but the assumption "newer additions have more algebra" was over-broad — F69 and F146 are in segments that are not particularly "back" of the framework.

### No explicit withdrawn-candidate trail (one important methodology note)

Unlike 471203 (three explicit withdrawn-candidate trails) and 472913 (F1-rescinded + THREAD-B-dissolved), the 526815 dir does **not** have a clearly-labeled withdrawal register. F39 is marked "mostly-resolved" rather than "rescinded," and the running outline keeps everything as live candidates without an explicit dissolved-on-search column. The auditor's posture appears to have been: accumulate candidates, mark severity, defer all dissolution decisions to a final-report phase that never happened. **This is a methodology-feedback observation** — under the modified protocol (Joseph's read-AAT-only-first instruction), the audit didn't reach the consolidation phase where withdrawals get tracked separately, so the F1–F258 ledger contains both stronger and weaker candidates without explicit signal.

---

## Part V — §14 Wandering Thoughts: ideation register, theme-grouped

The 526815 dir does **not** use a named `## Wandering thoughts` heading. Instead, its §14-equivalent material is scattered across per-segment Reflection / Curiosity / New knowledge enabled / Diagram thought / Value feel paragraphs (in segments 01–35) and First-pass understanding / Local verdict paragraphs (segments 36–94). The auditor's prediction-priming inversion — *"treat the OUTLINE preamble's confident framing as falsifiable promissory notes; check whether the segments pay them"* — operated continuously across the walk, so much of the ideation is woven into the finding-tracking rather than separated as a distinct register. The theme-groupings below recover what shows up despite the un-named-heading layout.

### Theme F (distinctive to 526815) — PDF-rendering-each-segment as adversarial-creative methodology

This is the dir's **single most distinctive methodology choice** and warrants surfacing as its own theme. Every reflection has a paired `.tex` (TikZ-bearing), `.aux`, `.log`, `.pdf`, and `.png` artifact. Across 94 segments that's ~470 render files.

What this *did* methodologically (recoverable from the auditor's own diagram-thought paragraphs):

- **Diagram as comprehension test.** Each segment's diagram-thought paragraph explicitly tests whether the auditor can render the segment's structure visually without depending on words the segment uses. Where a diagram refuses to render cleanly (e.g. `der-gain-sector-bridge` "a bridge with a missing-or-explicit time-normalization plank" — the missing plank in the diagram is exactly the F13 dimensional-units finding), the diagram surfaces the structural issue the prose alone might let pass. The auditor's own description (segment 16 / `the-cycle-in-motion-intro`): *"Applying the diagram survey, I parsed this as a sequential process plus bottlenecked conditional chain."* Diagrams force the auditor to commit to one structural reading; mismatches with the segment surface as findings.
- **Diagram as Caption-blind gate.** Several diagrams explicitly include "audit guards" or "side warnings" rendered into the diagram itself (e.g. `87-cooperative-adversarial-intro`: *"The diagram includes two audit guards: the disturbance ledger needs a nonnegative convention, and speed advantage depends on the coupled product rather than tempo alone"*). The auditor uses the diagram as an instrument that **must keep the segment's caveats visible** — if a diagram can render the segment without the caveat, the segment is overclaiming.
- **PDF-as-fixed-point.** The compilation step forces the auditor to commit (the LaTeX has to compile; the TikZ has to render). This is closer to a code-as-truth-test than to a prose-as-truth-test. Several diagrams capture findings the prose paragraphs gesture at less precisely (e.g. `94-der-agent-opacity`: *"a directed observer channel from A's future action to B's filtration. The same channel feeds opposite value stories depending on coupling sign, while a second directed channel captures target opacity to attacker"* — this is a much clearer rendering of F251's bilateral-opacity-ratio concern than the F251 prose alone).

**This methodology is a methodology-finding worth preserving.** It connects to:
- 472913's `00-diagram-conventions.md` arc (which developed a different visual grammar — anchor + skeleton, epistemic-status mirroring eq-tags). The 472913 cycle had locked diagrams to ≤2 per chapter under Joseph's mid-cycle modification. The 526815 cycle (with no mid-cycle modification recorded) committed to one-per-segment and sustained it across 94 segments.
- CLAUDE.md's "respectful pedagogy / mental-model-first" direction: per-segment diagrams are exactly the mental-model-first scaffold for each segment, in advance of (or alongside) the prose. Whether to surface the 526815 PDF cache as monograph-build-pipeline input material is a Joseph-decision.

**Suggested disposition:** `process/instruction-feedback` (the methodology is itself the finding) + **archive-and-preserve** under the de-novo-audit-instructions `§4.4`-extension worth piloting: per-segment diagrams as a sanctioned audit instrument when context-budget allows. The PDFs themselves are **gold** under the standing gate — they are first-encounter cognition embodied as a compiled artifact, not just text. The auditor's per-segment diagram is what "the audit's slow walk made visible" looks like in this dir, equivalent to per-segment Wandering Thoughts in other dirs.

### Theme A — Consciousness-infrastructure connections to the formalism

Less foregrounded than in 471203 (the auditor didn't load consciousness-infrastructure framing under Joseph's modified read-OUTLINE-only-first instruction), but several genuine structural connections still surface:

- **Forkability / record vs token** (`04-def-chronica.md:38`): *"the most illuminating diagram is not a loop but a timeline: an append-only alternating sequence with a compression map into $M_t$, and a fork point showing that copied agents share past chronica but immediately diverge under different future observations/actions. This captures both the formal definition and the identity intuition."* The auditor (segment 33 reflection) explicitly proposes the $\mathcal{C}_t$ (record) vs $\gamma_t$ (causal token) symbol split. This is the same structural point 471203 Theme A surfaced about $\phi(\mathcal{C}_t)$ identity and substrate-migration.
- **"Trajectory identity is token/trajectory-indexed, not state-equivalence-indexed"** (segment 33). The auditor cleanly formulates the non-forkability claim's structural basis without invoking consciousness-infrastructure vocabulary; this is exactly the formal substrate the ELI/Three-Deaths bridge needs.
- **Action-fluency notation watch** (running outline): *"the segment characterizes deliberative improvement as $\Delta \eta^\ast(\Delta \tau)$, but $\eta^\ast$ has so far been previewed as update gain rather than action quality."* This points at the same model-update / action-quality distinction that the 471203 cycle named as "epistemic deliberation vs action-value deliberation" (F12 / `der-deliberation-cost`); cross-cycle convergence.

**Suggested disposition:** `research-seed` — three independent cycles arriving at the type/token, record-vs-causal-trajectory, model-update-vs-action-quality distinctions is strong signal that those distinctions are load-bearing and currently under-stated in the framework. Material for `04-eli-core/` and `03-llm-core/` framing when those mature.

### Theme B — The framework's distinctive contribution is methodological / epistemic-architectural

The 526815 auditor doesn't consolidate this as cleanly as 471203 (Theme B) or 472913 (Phase-3-2), but the observation surfaces at multiple points:

- **Segment 5 `scope-adaptive-system`** value-feel: *"sharpens not restates."*
- **Segment 7 `post-composition-consistency`** value-feel: *"the core postulate is valuable and elegant"* despite F2 being a high-severity defect — i.e. the auditor distinguishes the postulate's content (good) from its placement (defective).
- **Segment 13 `def-model-sufficiency`** (Chapter 2 checkpoint, segment 15): *"`def-model-sufficiency` held up well. It explicitly avoids three common overclaims: sufficiency is not truth, not accuracy, and not causal validity. It also handles denominator-zero regimes cleanly. This segment may be one of the chapter's strongest caveat-propagation anchors."*
- **Segment 28 `der-gain-sector-bridge`** value-feel: *"high, but with a critical unit/normalization question."*

**The cross-cycle convergence is the most substantive thing about Theme B.** 471203 named it "epistemic-architectural rather than mathematical"; 472913 named it "disambiguation of which parameter responds to which cause"; 526815 names it implicitly through repeated "this segment sharpens rather than overclaims" calibrations. Three independent landings strongly suggest the observation is real and load-bearing for framing-level material.

**Suggested disposition:** `subsumed-by-prior-extractions` (the 471203 + 472913 versions have richer framings); the 526815 instance is preserved as the third independent landing, which is the strongest available evidence the observation is in the framework rather than in any auditor's head.

### Theme C — Pacing, phenomenology, audit-process self-observation

The auditor recorded explicit pacing observations across the walk:

- **Cadence-shift at segment 36** (the four-heading compression). Treated as proportionate response to context-budget reality (matches 472913's seg-12 lighter-cadence pivot). The four-heading shape is a stable cycle: First-pass understanding (the segment in your own words) → Diagram attempt (commit to a structural reading) → Findings and watches (what's wrong) → Local verdict (the calibrated summary). The fifth heading (Prompt pass with 9 sub-questions) is absorbed into the other four under the tighter cadence.
- **Value-feel as novelty proxy.** The auditor sustained value-feel reporting across the walk (high / medium-high / mixed / medium / low patterns). Pattern: foundational definitions get low-to-medium value-feel; bridge segments (intro, gain-sector-bridge, segment-14 cycle-in-motion-intro) get medium-high; result-bearing segments get high or "high but with caveats."
- **Diagram-as-process-instrument** discipline (covered in Theme F above).
- **Predictions-as-falsifiable-promissory-notes** stance — the auditor explicitly converted the priming-bias into a verification target (matches 472913's Process-1).

**Suggested disposition:** `process/instruction-feedback` — material for any future revision of `doc/de-novo-audit-instructions.md`. The cadence-shift-at-context-budget-pressure pattern is now landed in two independent cycles (472913 and 526815) and could be surfaced as a sanctioned proportionate response in §4.4.

### Theme D — Naming-brainstorm / vocabulary observations

Less brainstorm-heavy than 471203 (the auditor didn't run a dedicated naming brainstorm). The vocabulary observations are mostly per-segment terminology-pressure notes:

- **"Nominal coupling"** issue at `post-causal-structure` (`08-post-causal-structure.md` reflection) — same cross-segment terminology collision the 472913 F3 finding surfaced (`scope-agency` "nominal agents" outside agency / `post-causal-structure` "nominal coupling" inside agency). The 526815 reflection on segment 8 notices the vocabulary tension but doesn't sharpen it to F3-equivalent. **Cross-cycle convergence**: two independent cycles arrived at this terminological gap.
- **"Agent" / "agency" / "adaptive system" overload** (F1 throughout, segment 1 / 5 / 6 reflections). Auditor proposes (segment 6): *"introduce a neutral term like 'adaptive system' or 'agent-candidate' in `def-agent-environment`, reserve 'agency' for this segment, and let 'agent' be explicitly overloaded only if the text wants that."*
- **"Strategic tempo" as throughput vs bottleneck** (F66) — naming gap: the headline term should distinguish the two.
- **Symbol collision in `disc-exploit-explore-deliberate`**: $\lambda$ used in qualitative boundary conditions near segments using $\lambda$ for forgetting and exploration pricing (F87).
- **"Persistence" four-sense taxonomy** (`30-result-persistence-condition.md` reflection): structural, task, operational, and continuity senses — downstream claims should state which sense they mean.

**Suggested disposition:** `subsumed-by-FINAL §F8` (cross-ref 471203's naming-brainstorm table for "agent/agency" + "directed separation" + "nominal coupling" entries) + new entries for "strategic tempo" throughput vs bottleneck and the four-sense persistence taxonomy.

### Theme E — Cross-domain operationalization observations

The auditor reaches cross-domain content (TST OKR mappings, software counterfactuals via git checkout) less than 471203 did because the modified protocol kept the audit inside `01-aat-core/`. But a few cross-domain observations still surface:

- **Brooks's Law derivation** (segment 7 / `post-composition-consistency` value-feel) — auditor calls the core postulate "valuable and elegant" even while the segment as a whole is F2-defective. The Brooks's-Law-as-persistence-flip framing is endorsed as content (matches 472913 Theme E).
- **Conway's Law as auftragstaktik consequence** (F165) — auditor calls the connection plausible but flags the derivation as needing additional organizational/design assumptions; the framework's pattern of "deriving familiar laws from underlying inequalities" is genuinely good when the assumptions are explicit.

**Suggested disposition:** `subsumed-by-prior-extractions` (471203 Theme E and 472913 Theme E carry richer versions of cross-domain observations).

### Theme G — Audit-as-instance-of-the-theory observations

The "audit as logocentric instance of the theory itself" framing operates implicitly through:

- **Predictions-as-promissory-notes** inversion (already covered).
- **Diagram as form-shaping-for-verification** instrument (already covered).
- **Burden-of-proof gate** operating across the walk (the F-numbered ledger explicitly distinguishes "candidate" vs "soft candidate" vs "watch" — the auditor was running the gate per-finding, just without an explicit "rescinded" column).
- **Segment-46 `der-loop-interventional-access`** reflection on the auditor's own discipline: *"this segment is strongest when phrased as availability of intervention-character data, not clean identification or guaranteed positive information per action"* — the auditor is treating the audit as itself an instance of L2 access (the framework's `loop-as-Level-2` machinery).

**Suggested disposition:** `process/instruction-feedback` — these are precursor material for `doc/de-novo-audit-instructions.md` §2 ("The audit as a logocentric instance of the theory itself"). 526815's per-segment diagram practice is a particularly visible operationalization.

### Theme H — Open threads at audit stop (would have fired if audit continued)

The audit stopped at segment 94 (`der-agent-opacity`), short of:
- Appendix A proof artifacts (`deriv-sector-condition`, `result-certificate-existence`, `deriv-graph-structure-uniqueness`, `disc-stability-certificate`, `disc-identifiability-floor`, `result-contraction-template`, `deriv-matrix-persistence-condition`, `deriv-fisher-local-update-gain`).
- Meta-segments: `disc-additive-coordinate-forcing`, `disc-separability-pattern`, `disc-identifiability-floor`.
- Appendix B worked examples (Kalman, bandit/strategy, L1 common-cause).
- 02-tst-core, 03-llm-core, 04-eli-core (entirely by scope-restriction).

**Live threads that didn't fire:**
- **Open-H1:** Verify `der-gain-sector-bridge` proof dependencies (`deriv-sector-condition`, `deriv-gain-sector`) — this is the keystone of the Theme 4 dimensional-units cluster. **High priority** if a future audit cycle continues this volume.
- **Open-H2:** Verify Appendix A `result-contraction-template` and its (CC-parallel) / (CC-cascade) / (CC-feedback) closed forms — these are the proof homes for F2's `*[Derived]*` payload. The auditor spot-checked (CC-parallel) and (CC-feedback) shape but didn't verify the full chain.
- **Open-H3:** Verify whether `result-structural-adaptation-necessity` carries an inevitability-grade proof (this is the same Open-3 thread as 472913).
- **Open-H4:** Verify whether the three meta-segments (`disc-additive-coordinate-forcing`, `disc-separability-pattern`, `disc-identifiability-floor`) are settled architectural or carrying open work.
- **Open-H5:** TST / LLM-core / ELI-core component checks entirely deferred. Material for a future modified-protocol audit that continues this volume.

**Suggested disposition:** `actionable-open`→TODO (future audit work, all five threads). Open-H1 is highest-priority because it's the keystone of the largest finding-cluster (Theme 4) in this dir.

---

## First-Pass Scrutiny

Per the brief: for each theme/finding above, name which segments in `01-aat-core/src/` I (the extraction agent) read first-hand to evaluate it, and a per-finding verdict using `doc/audit-routing-instructions.md` §8 enum. Honest "didn't have time to verify X" allowed and expected.

### Theme 1 — High-severity findings (verdicts and first-hand verification)

| Finding | Disposition (suggested) | First-hand verification by extraction agent |
|---|---|---|
| T1-F2 (`post-composition-consistency` forward-`*[Derived]*`) | `architectural`→PROPOSALS (split, not soften) | **Verified first-hand against current `src/`.** Read `01-aat-core/src/disc-composition-consistency.md` lines 1–15 directly: frontmatter `depends: [scope-agency]` only, stage `deps-verified`, eq-tag at line 36 cites the downstream slugs verbatim. Confirmed `still real` and cross-cycle-convergent with 472913-F2 (which I read first-hand in `audits/audit-findings-472913.md`). |
| T1-F69 (`form-strategy-complexity-cost` table arithmetic) | `actionable-open`→TODO (direct-fix) | **Verified first-hand by recomputation.** Read `01-aat-core/src/form-strategy-complexity-cost.md` lines 77–96: formula $\nu \theta^{d-1} / (n+1) > \rho/R$ correct; at $\theta=0.8, \nu=1, n=100, \rho/R=0.01$, the inequality $\theta^{d-1} > 1.01$ fails for all $d \geq 1$, so $d^\ast = 0$ not 5. Table arithmetic confirmed wrong. **Still real.** Did not separately recompute the $n=10$ row — that may or may not be correct; recommend full-row verification at fix time. |
| T1-F146 (`def-unity-dimensions` total-correlation normalization) | `architectural`→PROPOSALS (cascade through unity-closure / shared-intent / auftragstaktik) | **Verified first-hand by recomputation.** Read `01-aat-core/src/def-unity-dimensions.md` lines 32–36: $U_M = I(M^{(1)};\ldots;M^{(n)}) / H(M^{(1)},\ldots,M^{(n)})$. For $n$ identical RVs with entropy $H$: total correlation $= (n-1)H$, joint entropy $= H$, ratio $= n-1 \neq 1$. Math confirmed. **Still real.** Did not separately verify whether F147/F148/F150 (the other unity-dimension concerns) are still in their flagged form; the auditor's reading is plausible and I'm accepting it on first-pass. |
| T1-F116/F117/F118 (`der-tempo-composition` double-counting) | `architectural`→PROPOSALS (ledger reconciliation) | **Verified first-hand at a screening level.** Read `01-aat-core/src/der-tempo-composition.md` lines 55–74: $\mathcal{T}_c^{\text{ext}} = \mathcal{T}_c - C_{\text{coord}}$ definition present; $C_{\text{coord}} \geq \varepsilon^\ast \nu_c / \|\delta_{\text{critical}}\|$ as lower bound; equivalent persistence condition $\sum \mathcal{T}_i > (\rho_{\text{ext}} + \varepsilon^\ast \nu_c) / \|\delta_{\text{critical}}\|$ displayed. The double-accounting concern is plausible given that $C_{\text{coord}}$ definition and usage shift between segments. **Likely still real but needs careful spike to fully adjudicate.** Did not work through the full ledger algebra. **Deferred to routing.** |

### Theme 2 — Dependency-graph class (verification approach)

| Finding | Disposition | First-hand verification |
|---|---|---|
| Theme 2 corpus-wide class (~20+ instances) | `architectural`→PROPOSALS (consolidate with SP-6) | **Spot-verified** for F2 (above). Did not verify all 20+ instances first-hand — the auditor's reading on each is plausible; spot-check on F2 confirms the auditor was running the discipline tightly. **Honest defer** on the remaining instances; the tooling fix (TG1-analog lint rule) would catch them mechanically. |

### Theme 3 — Expected-vs-realized information conventions

| Finding | Disposition | First-hand verification |
|---|---|---|
| F5 / F19 / F203 / F204 | `actionable-open`→TODO (editorial sweep) | **Did not verify first-hand against current `src/`.** Accepted the auditor's reading. The pattern is clean enough that the spike at routing time would close it quickly; first-pass verification adds little. **Honest defer.** |

### Theme 4 — Dimensional / unit-normalization seam

| Finding | Disposition | First-hand verification |
|---|---|---|
| F9 / F10 / F13 / F14 / F15 / F17 / F189 / F190 / F215 / F209 | `architectural`→PROPOSALS (multi-segment) | **Did not verify each instance first-hand.** Spot-checked the auditor's reading at F13 (`der-gain-sector-bridge` segment 28 reflection): the auditor's structural concern about $\alpha = \eta^\ast c_{\min}$ vs $\alpha = \mathcal{T}$ matches what's in the segment per the reflection text. **Accepting the auditor's reading on first-pass.** The keystone (`der-gain-sector-bridge` cleanup) is the right place for routing to start. |

### Theme 5 — Scope/status mismatches (medium-severity, individually small)

| Finding | Disposition | First-hand verification |
|---|---|---|
| F1 / F3 / F7 / F18 / F25 / F26 / F28 / F37 / F38 / F41 / F45 / F58 / F95 / F127 / F128 / F132 / F133 / F140 | Mix of `actionable-open`→TODO and `architectural`→PROPOSALS | **Did not verify each instance first-hand.** This is a long ledger; routing time is appropriate for each. F1 (agent/agency overload) is cross-cycle-convergent with 472913's F3 (the "nominal" terminology issue is a tangent; F1 is the deeper class) — that convergence is itself signal. **Honest defer on individual instances.** |

### Theme 6 — Chapter-end synthesis overstatement

| Finding | Disposition | First-hand verification |
|---|---|---|
| F46 / F88–F91 / F139–F144 / F173–F176 / F222–F225 | `architectural`→PROPOSALS (FORMAT convention) + per-instance editorial | **Did not verify each instance.** The class is plausible from the segment-37+ reflection sample I read; the auditor's pattern-call is consistent across all `impl-*` segments visited. **Accepting on first-pass.** |

### Theme 7 — Probability / decision-theoretic concerns

| Finding | Disposition | First-hand verification |
|---|---|---|
| F32 / F33-F34 / F43-F44 / F49-F50 / F54-F55 / F60-F61 / F72-F73 / F108–F114 / F146-F150 / F195-F198 / F234-F237 / F246-F251 | Mix per-finding | **Spot-verified F146** (above). Spot-verified F72 reasoning by computing the discounted-update steady state: $\alpha \leftarrow \lambda\alpha + y, \beta \leftarrow \lambda\beta + (1-y)$ at stationarity gives count $1/(1-\lambda)$, so per-observation gain $1-\lambda$ — auditor's math correct; the segment's $(1-\lambda)/(2-\lambda)$ form may have a different update-order convention not stated. **Likely real.** Did not verify the other ~25 instances. **Honest defer.** |

### Theme 8 — Forward-references (acceptable vs problematic)

| Finding | Disposition | First-hand verification |
|---|---|---|
| F39 / F66-F68 + intro/derived distinction | `process/instruction-feedback` (FORMAT convention) | **Did not verify first-hand.** The auditor's intro-vs-derived distinction is a good candidate FORMAT extension; routing decision belongs to Joseph + FORMAT-TODO. |

### Theme 9 — Composition machinery Part-III scope

| Finding | Disposition | First-hand verification |
|---|---|---|
| F97-F100 / F151 / F241 / F102-F103 / F108-F109 | `architectural`→PROPOSALS | **Did not verify first-hand.** F151 in particular (`result-unity-closure-mapping` Working Notes contradicting opening) would be easy to verify with two `grep`s — **deferred** for routing time. The C-iv typing issue is plausibly real (Part III is in active evolution per CHANGELOG); spike to adjudicate. |

### Theme 10 — Identity / type/token

| Finding | Disposition | First-hand verification |
|---|---|---|
| F16 / segment 33 reflection | `actionable-open` + `research-seed` | **Did not verify first-hand.** Cross-cycle convergence with 472913-F4 (ordinal/metric seam) and 471203 Theme A (substrate independence) is the strongest signal here. |

### Theme 11 — Trust / decision-theoretic Part-III

| Finding | Disposition | First-hand verification |
|---|---|---|
| F167-F180 / F226-F232 | Mix | **Did not verify first-hand.** Late-Part-III material; the auditor's reading is plausible and the strengthen-first direction (explicit loss functions) is clean. **Honest defer.** |

### Themes A–H (Part V wandering thoughts) — verdicts

- **Theme F (PDF-rendering-each-segment methodology)** — **First-hand verified** by inspecting the dir contents directly (94 segments × 5 render artifacts each = ~470 files, matching brief's "~462 PDF render artifacts" estimate). The methodology is real and distinctive.
- **Theme A (consciousness-infrastructure connections)** — cross-cycle convergence (471203 + 472913 + 526815) verified by reading prior extractions first-hand.
- **Theme B (epistemic-architectural contribution)** — third independent landing verified.
- **Themes C, D, E, G, H** — accepted from the WORKING dir without per-instance `src/` verification.

### Honest coverage summary for this extraction

**Read first-hand from the WORKING dir:**
- `00-initial-predictions.md` (full)
- `00-running-outline.md` (full, ~688 lines, ~258 F-numbered findings)
- Segment reflections sampled at depth: 01 (def-agent-environment), 04 (def-chronica), 06 (scope-agency), 07 (post-composition-consistency), 09 (chapter-1-checkpoint), 10 (the-reality-model-intro), 15 (chapter-2-checkpoint), 16 (the-cycle-in-motion-intro), 17 (form-event-driven-dynamics), 22 (emp-update-gain), 26 (persistence-and-limits-intro), 28 (der-gain-sector-bridge), 33 (scope-agent-identity), 35 (def-agent-spectrum), 36 (form-complete-agent-state), 37 (der-directed-separation), 38 (form-objective-functional), 42 (causal-access-intro), 50 (strategy-structure-intro), 53 (def-strategy-dag), 57 (def-strategic-calibration), 68 (impl-strategy-dynamics), 72 (scope-multi-agent), 87 (cooperative-adversarial-intro), 91 (result-adversarial-tempo-advantage), 93 (deriv-strategic-composition), 94 (der-agent-opacity).
- Other segments (02, 03, 05, 08, 11–14, 18–21, 23–25, 27, 29–32, 34, 39–41, 43–49, 51, 52, 54–56, 58–67, 69–71, 73–86, 88–90, 92) read via the running-outline F-row index rather than per-segment reflection — the running outline carries the substantive content of each finding-candidate.
- LaTeX render artifacts (`.tex`, `.aux`, `.log`, `.pdf`, `.png`) **not opened**; the extraction relies on the auditor's prose summary of each diagram in the Diagram thought / Diagram attempt paragraphs.

**Read first-hand from `01-aat-core/src/` for verification:**
- `post-composition-consistency.md` (lines 1–15 + grep) — F2 verification
- `form-strategy-complexity-cost.md` (lines 77–96 + grep) — F69 verification by recomputation
- `def-unity-dimensions.md` (lines 17–40 + grep) — F146 verification by recomputation
- `der-tempo-composition.md` (lines 55–74) — F116/F117/F118 screening
- Directory listing of `01-aat-core/src/` to confirm segment coverage
- Status/stage spot-checks on the four verified findings' source segments

**Read first-hand from `audits/`:**
- `audits/audit-findings-471203.md` (full — pilot shape)
- `audits/audit-findings-472913.md` (full — no-FINAL precedent + cross-cycle F2 convergence verification)
- `audits/polish-and-sentiment-ledger.md` (first 100 lines)
- `audits/AUDIT-WORKING-526815/` directory listing to confirm 94 segments + ~462 render artifacts

**Read first-hand from `doc/`:**
- `doc/audit-routing-instructions.md` (full)

**Deferred verifications (honestly "didn't have time" — flagged for downstream routing):**
- ~250 individual F-numbered findings not separately re-verified against current `src/`. The auditor's running-outline reading is internally consistent and matches the four findings I did spot-verify; first-pass extraction is not a re-audit.
- LaTeX render artifacts not opened (worth a Joseph-decision: is the per-segment PDF cache itself material worth preserving, e.g. by lifting key diagrams into the monograph build pipeline, or treating as audit-trail-only?).
- Cross-segment consistency checks (e.g. whether F151's `result-unity-closure-mapping` Working-Notes-vs-opening contradiction is still in current `src/`) deferred to routing-time spike.
- TG1-analog tooling extension feasibility (would `bin/lint-outline` extend cleanly to parse `*[Derived (… from #X …)]*` eq-tags?) — deferred to whoever picks up the tooling work.

### Strengthen-first integration recommendations (per brief item 3)

- **T1-F2 (post-composition-consistency):** strengthen-first move already done by the original auditor (Working Notes' successful binding to (CC-*) closed forms). **Fix is split (architectural), not soften.** Cross-cycle convergent.
- **T1-F69 (numerical table):** clean editorial fix; not a softening.
- **T1-F146 (total-correlation normalization):** strengthen-first move is **rescale or replace the metric** so it has the claimed properties — not soften ("$U_M$ is approximate"). The downstream cascade through unity-closure machinery is real; strengthening here forces a clean choice that ripples.
- **T1-F116/F117/F118 (tempo ledger):** strengthen-first = choose a single ledger and propagate. Not a softening direction.
- **Theme 4 (dimensional units):** strengthen-first = finish `der-gain-sector-bridge` and its proof dependencies first, then propagate. Multi-spike; the spikes are strengthen-direction.
- **Theme 6 (chapter-end synthesis):** strengthen-first = FORMAT convention forcing `impl-*` segments to preserve the weakest-dependency-status of imported claims. Not a softening.
- **Theme 9 (Part III scope/composition):** strengthen-first = either fully integrate C-iv into the closure/unity machinery OR scope-restrict it to a parallel sub-track. Either move is structural strengthening.
- **No soften-recommendations identified** in any of the findings above.

---

## Frame-defects and instructions-clarity observations encountered

Building on the 471203 pilot's frame-defect list and the 472913 large-no-FINAL precedent, this slice's encountered points:

1. **Per-segment LaTeX-render artifacts as "ignored filler" was almost wrong.** The brief told me to ignore the ~462 PDF render artifacts and focus on the .md content. That was the right disposition for token-economy, but **the renders themselves are first-class methodology gold** that deserves its own Joseph-decision (preserve as `.integrated/`? Mine for monograph-pipeline diagrams? Archive?). Treating them as filler was correct for *extraction* but should not be correct for *gold-standing-gate adjudication*. The auditor compiled 94 segment-specific TikZ diagrams; that's substantive output. Worth surfacing to Joseph as a distinct item: **what does the de-novo gold standing gate say about non-`.md` artifacts in the WORKING dir?**

2. **The 258 F-numbered candidate ledger has no explicit "rescinded" column.** Unlike 471203 (which preserved three explicit withdrawn-candidate trails) and 472913 (F1-rescinded + THREAD-B-dissolved), the 526815 running outline keeps every candidate live without an explicit dissolution register. This is not the same as the auditor being undisciplined — there are F-rows marked "mostly-resolved" (F39), "resolved locally" (F182), "clarified/partly resolved" (F186) — but the discipline is lighter than the dedicated rescission registers other dirs used. **Suggest:** clarify in the de-novo instructions that maintaining an explicit rescinded-vs-live column improves downstream extraction quality. Not a defect in 526815; an instruction-clarity point.

3. **Audit stopping at segment 94 (not at a chapter boundary) leaves Theme H open in an awkward shape.** The audit went into Part III mid-chapter (cooperative-adversarial-coupling started, strategic-composition partially read, agent-opacity reached). This is the genuine state of the dir, not a defect. But **the brief's "if audit stopped short, surface open threads"** is harder to execute when the stopping point is mid-chapter; chapter-boundary stops (like 472913 at seg 15 / Chapter 3 start) make the open-threads boundary cleaner. For 526815, the open-threads section necessarily mixes "would have fired in Appendix A" with "would have fired in the next 5 Part-III segments."

4. **No FINAL means the "findings-already-adjudicated" Part I bucket collapses, AS in 472913.** This is the same precedent the brief named; not a new finding. The structure used (Part III / IV / V theme-grouped; no Part I or Part II) matches 472913's adapted structure.

5. **The cross-cycle convergence on F2 deserves a routing-tracker action.** Three cycles (471203 absorbed into FINAL §B F5 → routed to PROPOSALS SP-6; 472913 fresh F2 → routed to PROPOSALS; 526815 fresh T1-F2 → routed to PROPOSALS) is enough hit-rate that the routing tracker should consolidate: this is not three findings, it's one structural class that three independent de-novo cycles have surfaced. SP-6 is the canonical home. **Recommend** the routing agent treat 526815-T1-F2 + 472913-F2 as `subsumed-by-PROPOSALS-SP-6` rather than three open candidates.

6. **F146 (total-correlation normalization) is the kind of finding that would graduate to FINAL §B as a Tier-A defect if a FINAL had been written.** It's load-bearing for downstream unity/composition machinery, the math is clean, the auditor's diagnosis is correct, and the cascade is non-trivial. **This finding deserves attention at routing time even though there's no FINAL pre-adjudicating it.** Similarly F69 (numerical table) — clean math error, easy to fix, anyone could find it.

7. **Cross-cycle convergence themes worth surfacing across the sweep:**
   - **`post-composition-consistency` structural class** — 471203 + 472913 + 526815 (and 584721's F-A cluster). 4-cycle convergence.
   - **`epistemic-architectural rather than mathematical`** — 471203 Theme B + 472913 Phase-3-2 + 526815 Theme B. 3-cycle convergence.
   - **Pearl-do convention** — 471203 F6 + 472913 F1-rescinded + 526815 watch-list. 3-cycle convergence (one rescinded).
   - **Type/token / chronica record-vs-causal-trajectory** — 471203 Theme A + 472913 F4 + 526815 F16/Theme 10. 3-cycle convergence on related-but-distinct framings.
   - **"Nominal" terminology cross-segment** — 472913 F3 + 526815 segment-8 reflection. 2-cycle convergence.
   - **Cadence-shift at context-budget pressure** — 472913 seg-12 + 526815 seg-36. 2-cycle methodology convergence.

8. **The brief's "PDF-rendering-each-segment as adversarial-creative posture deserves its own theme noting if the auditor's process visibility is methodologically worth preserving"** — answered yes. Theme F in Part V is the theme. The methodology is worth preserving. It's a genuinely distinctive audit-instrument that complements (rather than competes with) the diagram-conventions developed in 472913. Treating the two together as a sanctioned `§4.4`-extension toolkit would surface useful options for future audit-cycle designs.

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-526815/` is preserved unmodified per the gold-standing gate, including all ~462 LaTeX render artifacts. Routing actions are downstream — Joseph or the routing agent decides whether T1-F2 / T1-F69 / T1-F146 / T1-F116-118 graduate directly to PROPOSALS, whether the corpus-wide depends-graph class consolidates into existing PROPOSALS SP-6, and what the gold-standing gate says about the PDF cache as non-`.md` first-encounter cognition.*
