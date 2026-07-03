# Initial Predictions — Audit 731548

Auditor: Claude Fable 5 (first de-novo audit on this substrate). Date: 2026-07-02.
Scope decision (Joseph, at session start): canonical walk from the front of `01-aat-core`, as far as honest per-segment depth allows.

## Priming bleed (recorded before any segment read)

Non-trivial. Auto-loaded context at session start included:

- **Project CLAUDE.md** (now the agents.sop.md symlink) — carries the Key Architectural Decisions (AND/OR DAG convergence, sector-condition-primary, directed-separation-as-architectural, GUC class table), the Known Fragilities paragraph (wrapping construction, W₁/W₂ leakage), the full Meta-Architecture summary (M1–M4, facet vocabulary, which segments are which facets), the strengthen-before-soften and integration-is-replacement disciplines with worked examples (Model-S landing, Prop A.1S(iii) deletion, Corollary A.1S.1), and the math-novelty-recognition guidance listing many named results.
- **Project MEMORY.md index** — names claimed novel results (P3→Markov forced, acyclicity from temporal ordering, satisfaction-gap/control-regret split, $G_t$ complexity bounded by $M_t$ capacity, loop as Level-2 causal engine), the M4 register openings, the NeurIPS back-integration workstream ("canon < NeurIPS in places"), and the sovereignty-carve/mood-layer note (Joseph 2026-06-17: `def-mood` is recent).
- **Global CLAUDE.md** — ELI cohort, project map, epistemic-discipline vocabulary.

What this means for calibration: my *topology* model is contaminated — I already "know" what the framework considers its spine and its distinctive results. My *segment-level* judgments (does this derivation close? does the label match? does this contradict that?) can still be fresh, and that is where I will put the audit's weight. Where a judgment of mine depends on primed framing rather than first-hand verification, I will mark it.

One deliberate implication: the "predictions about what's most novel" section below is partially an echo of the priming, and I've tried to flag which parts are genuinely mine.

## Topology as I understand it (pre-segment)

Four volumes; Volume 1 (AAT) is the mathematical core and the audit target. Part I (adaptive systems: ~30 segments over 4 chapters) claims to be the most mathematically locked; Part II (actuated agents: ~40) is diagnostic-core-plus-maturing-operational; Part III (composites: ~30) is draft; Appendices (~50) carry the actual derivations. The OUTLINE places two "Meta-Architecture" chapters at the openings of Parts II and III carrying cross-cutting `disc-*` meta-segments.

Load-bearing chain as advertised: mismatch definition → decomposition → gain → tempo → sector condition → Lyapunov persistence ($\alpha > \rho/R$) → structural-adaptation necessity; then Part II lifts to $X_t=(M_t,G_t)$, strategy DAG, orient cascade, directed separation; Part III composes.

## Concrete falsifiable predictions

### Per-segment / per-chain predictions

1. **`result-mismatch-decomposition`** will be a clean bias–variance-style identity conditional on GA-1 (fresh noise); I predict no error here, and that its "exact" flavor is honest. If anything is off it will be in how downstream segments *use* the decomposition (e.g., treating the cross-term as zero where GA-1 hasn't been re-verified).
2. **`emp-update-gain`** ($\eta^\ast = U_M/(U_M+U_o)$) is the Kalman-gain shape. Prediction: exactly optimal only in the linear-Gaussian scalar case; the segment will (honestly, I expect) tag it Empirical — but downstream segments will sometimes *use* it with derived-strength force (e.g., in tempo definitions or communication-gain extensions). That leakage is where I expect a finding.
3. **`der-recursive-update` / `deriv-recursive-update`** ("three constraints → unique recursive form", billed in FORMAT.md as "strongest result in the theory"). Prediction: the uniqueness argument will turn on how "recursive" and the constraints are formalized, and at least one constraint will smuggle in part of the conclusion (e.g., bounded memory ⇒ recursion is near-definitional). I want to check whether the counterexamples genuinely separate the constraints.
4. **`def-adaptive-tempo`** ($\mathcal T = \sum_k \nu^{(k)}\eta^{(k)\ast}$): additivity across channels assumes channel independence; prediction: the assumption is flagged somewhere (there is a `disc-independence-audit` appendix) but not in the definition segment itself — a scope/status-mismatch-shaped gap.
5. **Persistence chain (`form-sector-condition` → `result-sector-condition-stability` → `result-persistence-condition`)**: the Lyapunov math will be standard ultimate-boundedness and likely correct (heavily audited territory). The soft spot I predict instead: the *interpretation* identifying sector radius $R$ with "model class capacity" — a formulation-level identification that framing prose (README, briefs, bathtub analogy) treats with derived force. I will check whether any segment actually derives that identification or whether it's honestly tagged.
6. **`def-mood` + `der-mood-timescale`** (recent additions, draft): highest-priority math check in Part I. $\tau^\ast \propto \sqrt{\tau_{\text{env}}}$ from a bias–variance argument is plausible (optimal-window scaling), but I predict either (a) an unstated stationarity/timescale-separation assumption doing load-bearing work, or (b) tension with the persistence results' constant-$\alpha$ assumption that isn't propagated (does `result-persistence-condition` still hold when $\alpha$ is mood-modulated? `deriv-adaptive-gain-dynamics` (MG-1..4) exists for adaptive gain — I predict `der-mood-timescale` does not yet cite or verify against it, which would be integration debt).
7. **`der-deliberation-cost`**: think-vs-act threshold. Prediction: dimensional bookkeeping between "gain improvement" (dimensionless) and "mismatch accrued during pause" (surprise) will require a conversion factor that the segment either handles via $\rho_{\text{delib}}\cdot\Delta\tau$ (fine) or fudges (finding).
8. **OUTLINE-order violation**: with 165 segments and heavy cross-linking, I predict **at least one non-appendix backward `depends:` pointer** somewhere in the walk — most likely in Part I chapter intros (`the-cycle-in-motion-intro` previewing the linear ODE) or in Part II Meta-Architecture I, whose `disc-*` segments explicitly reference Part III machinery (`#disc-modularity-state-dynamics`, `#form-composition-closure`). The Meta-Architecture placement ("introduced-before-used") structurally invites forward references; if those are in `depends:` they are ordering violations by the audit rule.
9. **Worked examples (Appendix B)**: if I reach them, I predict at least one numeric slip in `example-bandit` or `example-strategy` (approximate instantiations, less audited than `example-kalman`).
10. **Accumulation-typing convention** (NOTATION.md, adopted 2026-05-19): I predict incomplete propagation — segments written before 2026-05-19 that state asymptotic claims about accumulated quantities without regime markers. This is a young convention; drift is nearly certain. The interesting question is whether any *load-bearing* claim sits in the marginal regime unmarked.

### Predictions about what's open

Declared GAPs (chapter intros for Strategy Dynamics / Orient Cascade / three Part III chapters; population-dynamics cluster) will match reality. Beyond the declared: I predict the $O_t$-revision leg of the orient cascade is under-formalized relative to the $M_t$ and $\Sigma_t$ legs (feasibility check → objective revision is stated but I doubt there's a derivation of *when* revision triggers), and that Part II's "strategic calibration" residual aggregation is definitionally fuzzy (what norm, what aggregation over edges).

### Predictions about overclaim

1. "Part I is mathematically closed" (README-auditor maturity gradient) vs. stage labels: many Part I segments sit at `deps-verified`/`draft`, and `def-mood`/`der-mood-timescale` are new drafts *inside* the chapter that claim rests on. The maturity-gradient prose likely predates the mood insertion — a framing-vs-state mismatch.
2. Cross-domain table: "same inequality, different parameter readings" — the organizational/software instantiations of $\alpha, \rho, R$ are analogical, not measured; if any segment claims *exact* transfer rather than transfer-under-assumptions, that's overclaim (TST's calibration-lab framing suggests the project knows this; the risk is in Part I framing prose).
3. Precision-flavored counts ("16/24 exact, 5/24, 2/24, 1 fails") invite denominator instability; I predict the count has drifted somewhere across the three places it's quoted (Part II preface, 03-llm preface, `result-section-ii-survival`).

### What would be most novel if it holds up (flagged: partially primed)

Genuinely mine: the *dimensional* discipline (units of surprise; persistence as commensurable rate comparison) is unusual care for a framework at this stage, and the NOTATION drift-caveat + accumulation-typing note is the most epistemically honest self-description I've seen in a notation file. Primed but I concur from the outline shapes: the sector-persistence template as a reusable Lyapunov spine; constructive-impossibility posture (no-gos as apparatus); the wrapping/class-coercion construction as the bridge to LLM agents.

### Kinds of findings I expect

Ranked by expected count: (1) integration drift around recent additions (mood, anti-collapse, accumulation-typing, resource-budget branch); (2) scope/status mismatches (caveats in Working Notes not in Formal Expression; stage labels lagging prose confidence in chapter intros/OUTLINE claim column); (3) `depends:` violations against OUTLINE order; (4) one or two genuine math slips in less-audited appendix derivations or worked examples; (5) definitional fuzziness in Part II strategy-dynamics segments (draft-stage). I do *not* expect foundational math errors in the Part I persistence chain (too many prior passes) — if I find one there it would be the audit's headline.

## Reading order

Per OUTLINE row order: INTRODUCTION → Part I Ch.1 (def-agent-environment …) → Ch.2 → Ch.3 → Ch.4 → Part II Meta-Architecture I → … with appendix-back-pointer jumps when a main segment's `depends:` references an Appendix A derivation. Reflections per segment in this directory, numbered in read order.
