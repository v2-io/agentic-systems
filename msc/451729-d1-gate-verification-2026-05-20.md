---
purpose: Independent Gate 1–4 verification adjudication for the 6 segments the 451729 extraction agent identified as Class A (genuinely promotion-ready) D.1 residuals.
adjudicator: Claude Opus 4.7 (1M context)
adjudication-date: 2026-05-20
input: audits/audit-findings-451729.md §"First-hand check of current segment state (2026-05-20 spot-check)" Class A list (6 segments)
scope: adjudication-only — no segment edits, no stage advances, no commits; reports diverging reads cleanly
disposition: report-only; recommendations go to TODO/Joseph at higher level
---

# 451729 D.1 — Independent Gate Verification (2026-05-20)

## Provenance and framing

The 451729 extraction agent (Claude Opus 4.7, 2026-05-20 parallel-sweep) recovered the per-segment cognition trail from the 451729 working dir, examined each of 8 candidate-conservatively-staged segments first-hand against current `src/`, and partitioned them into Class A (6 genuinely promotion-ready), Class B (1 genuinely-blocked: `form-consolidation-dynamics` on the F.3 upper-bound), Class C (1 already-promoted: `deriv-graph-structure-uniqueness`). This adjudication is the *independent-verify* gate over the Class A read — per `doc/audit-routing-instructions.md` §8 (Independent-verify gate: "adjudicator ≠ grad-confirmer; primary-source spot-checked by an agent *other than* the one who adjudicated them") and §0/§8 Refinement 4 ("the evidence hierarchy is proxy; truth is the arbiter").

The adjudication applies `FORMAT.md`'s Gates 1–4 promotion workflow to each segment first-hand and reports pass/fail per gate with the load-bearing observation. **Strengthen-first posture honored throughout**: where a Gate-failure ask would imply softening, I report the strengthening route the segment already covers before recommending any downgrade. The target promotion for these segments is `draft → claims-verified` (which implies `deps-verified` first); the FORMAT.md ordering is `draft → deps-verified → claims-verified → format-clean → candidate`.

**The single most-consequential cross-cutting finding**: 4 of 6 segments **fail Gate 1** on staging-monotonicity (FORMAT.md §"Gate 1: Dependency audit" criterion 3 — *"The referenced segment is itself at `deps-verified` or higher"*), and 4 of 6 **fail Gate 3** on `bin/lint-md`. Both findings narrow the actionable promotion set tighter than the extraction agent's read. Detail below.

---

## §1 — `deriv-recursive-update`

**Current state.** `stage: draft`, `status: exact`, `type: derivation`. Depends: `form-agent-model` (deps-verified), `form-event-driven-dynamics` (deps-verified), `post-causal-structure` (deps-verified), `scope-adaptive-system` (claims-verified), `def-observation-function` (deps-verified).

**Gate 1 (Dependency audit) — PASS.** All five dependencies exist; staging-monotonicity satisfied (all deps at `deps-verified` or higher); each dependency is genuine — the segment's three constraints (C1 arrow-of-time, C2 partial observability, C3 state completeness) name `post-causal-structure`, `scope-adaptive-system` + `def-observation-function`, and `form-agent-model` respectively, and `form-event-driven-dynamics` is the scope token for the event-rate framing. No missing dependencies identified; the Doob–Dynkin formalization in §"Information-Set Formalization" cites Kallenberg 2002 externally (footnote), correctly handled as external machinery, not requiring a `depends:` entry.

**Gate 2 (Content review) — PASS, with one substantive caveat noted by the segment itself.** The three triage questions: (1) prior objects — yes, the five depended segments cover C1+C2+C3 fully; (2) competing formulation — Attack 1 (simultaneous events), Attack 2 (continuous coupling), and Attack 7 (full-history retention) explicitly test alternative formulations, with each shown to either preserve the form or sit outside scope; the corollary $\dot M = g(M, u)$ for continuous coupling is named as the general form arrived at by the same argument structure (no overclaim); (3) falsifiability — the result is constraint-relative, *honestly* labeled as such in the §"What Is Derived vs. What Is Chosen" table where C3 carries Strength = "Definition" (analytical commitment), with Proved status reserved for the uniqueness claim conditional on the three-constraint set. The Doob–Dynkin information-set formalization is mathematically clean and provides the cleanest technical proof path. Label audit: `status: exact` matches — the result is mathematically exact under the stated constraints, and the segment is explicit that C3 is definitional. The "What Is Derived vs. What Is Chosen" table is a model of the FORMAT.md §"Derivation-audit table" convention.

**Gate 3 (Mechanical review) — PASS.** `bin/lint-md` returns "All clean." All cross-references resolve to existing files (verified: `#scope-adaptive-system`, `#post-causal-structure`, `#def-observation-function`, `#form-agent-model`, `#form-event-driven-dynamics`, `#form-information-bottleneck`, `#emp-update-gain`, `#def-model-sufficiency`, `#result-structural-adaptation-necessity` — all exist). Document cadence matches (frontmatter / title / summary / Formal Expression contents / Epistemic Status / Discussion / Working Notes). Equation-level tags present.

**Gate 4 (Notes disposition) — FAIL (mild).** The `## Working Notes` section has 3 items: (a) C3's definitional character — already incorporated into Epistemic Status; this is a *resolved* item that should be deleted; (b) the continuous-coupling generalization Attack 2 — already covered in Attack 2 + the corollary; *resolved*; (c) the recommendation to make the Doob–Dynkin path the primary proof path — this is *promoted*-class (editorial reorganization). All three are editorial/resolved, not blocking research. Per FORMAT.md §"Gate 4", these should be resolved (deleted/promoted) at `candidate` stage, not at `claims-verified`. **Gate 4 is the final gate (to `candidate`), so it does not block promotion to `claims-verified`**; I flag it only because the extraction agent claimed "Working Notes are editorial polish, not blockers" — that read is *correct*, and these items would block only the further-out `candidate` promotion.

**Recommended next stage: `claims-verified`.** All four gates either pass or do not yet apply (Gate 4 applies for `candidate`, not `claims-verified`). The extraction agent's read is upheld: the segment is mature, well-derived, with the strongest mathematics in the corpus (per the 451729 auditor's first-encounter assessment that this is "the cleanest mathematical result in the theory"). **No strengthening direction necessary** — the segment is in the inevitability core (FORMAT.md §"Three rings"), the derivation is tight, the seven-attack discipline is exemplary.

**Divergence from extraction agent: none on the verdict.** Reading converges.

---

## §2 — `deriv-sector-condition`

**Current state.** `stage: draft`, `status: exact`, `type: derivation`. Depends: `def-adaptive-tempo` (claims-verified), `def-mismatch-signal` (deps-verified). The brief noted this segment is "substantively more mature now: Cor A.1S.1 dichotomy landed 2026-05-16 post-audit."

**Gate 1 (Dependency audit) — PASS, with a missing-deps concern.** Both listed dependencies are at `claims-verified` / `deps-verified`. **However**, the segment's mathematical content depends on machinery from `#der-gain-sector-bridge` (Prop B.3 / DA2'-inc — explicitly named in the "Grounding of GA-3 — sub-scope $\alpha$" paragraph, and the operator-family classification depends on this segment + bridge bidirectionally), and on `#deriv-stochastic-non-exit` (the no-go subderivation referenced from Cor A.1S.1's proof). The `#deriv-stochastic-non-exit` segment exists (verified) and is structurally an *appendix* to this one. Neither `der-gain-sector-bridge` nor `deriv-stochastic-non-exit` appears in `depends:`. **FORMAT.md §"Gate 1" criterion 4**: *"if the Formal Expression uses a quantity defined elsewhere, that slug appears in `depends:`."* The sub-scope α/β partition (load-bearing in the §"Grounding" paragraphs, §"Sub-scope β" structural-Lipschitz-floor result, and the "What Is Derived" row 5) genuinely uses Prop B.3 from `der-gain-sector-bridge`. The Cor A.1S.1 proof genuinely cites `#deriv-stochastic-non-exit` as the load-bearing no-go demonstration.

This is a **dependency-completeness fault**, not a softening recommendation. Strengthen-first posture: the fix is *additive* — add `der-gain-sector-bridge` and `deriv-stochastic-non-exit` to `depends:`. Both targets exist; neither is at a lower stage than `draft` (so no cascade). **Verdict: PASS-with-fixup** — Gate 1 is repaired by a frontmatter edit; the staging-monotonicity check would then need to confirm `deriv-stochastic-non-exit` is at `deps-verified` or higher before this segment can promote to `claims-verified`.

**Gate 2 (Content review) — PASS.** The Cor A.1S.1 dichotomy landing is the canonical worked example of strengthen-before-soften + integration-is-replacement (per `doc/audit-routing-instructions.md` §6, the corrected-rule version). Triage: (1) priors complete (modulo Gate 1 fixup); (2) competing formulation thoroughly addressed — Khalil's deterministic Lyapunov machinery vs. Khasminskii's stochastic recurrence are both classical, the AAT contribution is the *categorical α-invariant dichotomy* labeled honestly as "Synthesis — exact result built from classical components" in the Findings Novelty Claim; (3) falsifiability — under bounded Model D the assertion is testable by counterexample (find an interior trajectory that exits), under Model S the assertion is by-construction (recurrence of non-degenerate diffusion is well-established). Derivation check: each step of the Itô-Lyapunov computation, the stopping-time localization at $\tau_R$, the Markov-tail (iii′) chain, and the (iv) finite-horizon sup-bound are all traceable; the Model-S half of Cor A.1S.1 invokes the Khasminskii ch. 3–4 recurrence fact, which is correctly handled as *formal antecedent* in the Related-Work table rather than re-derived. The §"What Is Derived vs. What Is Chosen" table is detailed and accurate — Cor A.1S.1 is labeled **Proved — new exact result**, consistent with the integration-is-replacement landing posture. Sub-scope α/β handling is rigorous: the operator-theoretic re-statement (Rockafellar / Bauschke-Combettes / Baillon-Haddad / Amari) is correctly framed as "specialization + repurposing rather than strict generalization."

**Gate 3 (Mechanical review) — FAIL.** `bin/lint-md` reports **13 issues** — primarily bare Greek (`α`, `β`) used outside `$...$` math spans in prose like "the α/β epistemic labeling" and "sub-scope β rule-based". Per FORMAT.md §"Math Formatting" + project-CLAUDE.md §6 Self-reminder, bare Unicode math in prose violates the document-wide LaTeX-in-files rule. This is the known recurring failure mode named in CLAUDE.md §6(a). The fix is mechanical (`\(\alpha\)` / `\(\beta\)` or `$\alpha$` / `$\beta$`); the lint-fix mode may handle some automatically. **Gate 3 blocks promotion to `format-clean`; it does NOT block promotion to `claims-verified`**, but it is on the critical path before any further advance.

**Gate 4 — N/A at `claims-verified` target.** Working Notes are extensive but mostly *landing-context provenance* (the Cor A.1S.1 landing trail, the spike-routing cycle disconfirmation of the 628401 optimism prediction) and *low-confidence ideation* glimpses (the dichotomy as candidate instance-family for SP-23). These are legitimate Working-Notes content per FORMAT.md §"Voice and provenance".

**Recommended next stage: `claims-verified` (with the Gate-1 frontmatter fixup as prerequisite).** Lint cleanup is required before `format-clean`, not before `claims-verified`. The mathematical substance is exceptional — this is the most mathematically rich segment in the corpus by some margin (the auditor's first-encounter assessment was "Highest value of any segment I've read" and the Cor A.1S.1 landing has only added to that).

**Strengthening direction noticed.** The "low-confidence ideation" Working Note flagging Cor-A.1S.1-shaped dichotomies at `#deriv-discrete-sector-condition`, `#deriv-matrix-persistence-condition`, `#deriv-adaptive-gain-dynamics`, possibly `#result-per-dimension-persistence` is a candidate instance-family for the theorem-import-architecture meta-segment (PROPOSALS SP-23) or a sibling of `#disc-identifiability-floor`. This is **post-promotion** strengthening work — not blocking; tracked correctly in Working Notes per `doc/sop/spikes.sop.md` §1.

**Divergence from extraction agent.** Extraction agent said "No blockers." My read: **Gate 1 has a substantive missing-dependency fault** (`der-gain-sector-bridge` and `deriv-stochastic-non-exit` should be in `depends:`), and **Gate 3 has 13 lint issues**. Both are *additive fixups* rather than substantive blockers, but they are real and the extraction agent missed them. Neither blocks `claims-verified` per the strict FORMAT.md gate semantics (Gate 1 is repaired by the frontmatter edit; Gate 3 blocks only `format-clean`), but both should be folded into any promotion sweep.

---

## §3 — `der-gain-sector-bridge`

**Current state.** `stage: draft`, `status: conditional`, `type: derived`. Depends: `emp-update-gain` (claims-verified), `def-mismatch-signal` (deps-verified), `deriv-sector-condition` (**draft** — this is the staging-monotonicity blocker), `deriv-gain-sector` (deps-verified).

**Gate 1 (Dependency audit) — FAIL.** `deriv-sector-condition` is currently at `stage: draft` (verified `head -10 01-aat-core/src/deriv-sector-condition.md`), which fails FORMAT.md §"Gate 1" criterion 3 — *"The referenced segment is itself at `deps-verified` or higher."* The bridge derivation **uses** the sector condition framework from `deriv-sector-condition` (its result is the bridge from B1 directional fidelity → GA-3 / A2'), so the dependency is genuine. The staging-monotonicity blocker is real. **Resolution path**: promote `deriv-sector-condition` first (or in coordination — but no monotonicity violation per FORMAT.md §"Ordering: promote in topological order"). This is not a defect of `der-gain-sector-bridge` per se — it is a topological-order claim about which segment promotes first.

**Strengthening posture honored**: the *fix* is to promote `deriv-sector-condition` first (which my §2 verdict supports). I am NOT recommending a status downgrade on `der-gain-sector-bridge`; I am flagging the topological ordering. Per `doc/audit-routing-instructions.md` §2, effort to land the dependency promotion is "false constraint" — the right move is to promote in topological order.

**Gate 2 (Content review) — PASS.** Triage: (1) priors — yes, the five rows of the "Verified Instances" table (scalar Kalman, matrix Kalman, Beta-Bernoulli, exponential family in natural parameters, gradient on strongly convex, gradient on locally convex) each cite their domain machinery cleanly; (2) competing formulation — the B1 directional fidelity vs strong convexity equivalence is explicitly handled in two forms (one-point ⇐ strong convexity, with the $L'(x) = x(1 + \tfrac{1}{2}\sin(10x))$ counterexample showing the reverse fails; two-point ⇔ strong convexity full equivalence via Nesterov 2004 Thm 2.1.10); (3) falsifiability — the five named failure modes (FM-1 through FM-5) are concrete tests; the sub-scope α / sub-scope β partition makes the bridge's claim domain explicit. `status: conditional` matches — the bridge holds conditional on B1 (or strong convexity, or one of the other operator-family structural conditions). The "Weighted-norm subtlety" paragraph and the "Fisher-metric cases under parameterization-invariance" paragraph are model treatments of when AAT-internal axioms ((PI) + Čencov) upgrade conditional → forced. The connection to `#disc-additive-coordinate-forcing` is correctly named.

**Gate 3 (Mechanical review) — FAIL.** `bin/lint-md` reports **6 issues**: bare Greek `α-T relationship` (line 121), two `raw < in math — use \lt` (line 129, twice), plus three more (I'd verify visually but they cluster in the discussion section). Same failure class as `deriv-sector-condition`. **Gate 3 blocks `format-clean`, not `claims-verified`.**

**Gate 4 — N/A and remarkably, *no* `## Working Notes` section exists**. The segment uses a Discussion-only structure. Per FORMAT.md §"Document cadence," Working Notes is optional — its absence is fine and means the segment is closer to candidacy than segments with WN debris. Gate 4 is trivially satisfied if there are no working notes.

**Recommended next stage: HOLD on staging-monotonicity (Gate 1 blocker).** Promote `deriv-sector-condition` first, then this segment can advance to `claims-verified` (Gate 3 lint cleanup needed before `format-clean`).

**Strengthening direction noticed.** None additional — the segment is already a strengthening landing (the bridge transforms GA-3 from "opaque global assumption" to "structurally derived for sub-scope α", landed across multiple cycles). The (PI)/Čencov upgrade path is named in the Discussion and tracked in `#disc-additive-coordinate-forcing` — appropriate.

**Divergence from extraction agent.** Extraction agent said "No `## Working Notes` section at all (segment uses Discussion-only structure). Still appears conservatively-staged. No blockers." My read: the **Gate 1 staging-monotonicity violation with `deriv-sector-condition` (draft)** is a real blocker that the extraction agent missed — the segment cannot promote past `draft` until its dependency does, per FORMAT.md's promotion-in-topological-order rule. The fix is to promote `deriv-sector-condition` first, not to forcibly co-promote both. The extraction agent's underlying read of segment-content maturity is correct.

---

## §4 — `deriv-edge-credence-dynamics`

**Current state.** `stage: draft`, `status: conditional`, `type: derivation`. Depends: `schema-strategy-persistence` (**draft**), `hyp-edge-update-via-gain` (**draft**), `deriv-sector-condition` (**draft**), `scope-and-or` (**draft**). The Prop B.4 fix landed (verified at line 220).

**Gate 1 (Dependency audit) — FAIL.** All four dependencies are at `stage: draft`. This is the worst staging-monotonicity violation among the six segments. Verdict mechanism: the segment cannot promote to `claims-verified` until every dependency is at `deps-verified` or higher. The dependencies are genuine — `scope-and-or` provides the AND/OR DAG semantics (load-bearing throughout), `hyp-edge-update-via-gain` provides the Beta-Bernoulli edge dynamics, `deriv-sector-condition` provides Prop A.1, and `schema-strategy-persistence` is the parent schema being instantiated.

**The dependency chain.** `schema-strategy-persistence` itself has `deriv-sector-condition` and friends as dependencies — the staging cascade goes:
- `deriv-sector-condition` (draft) → `schema-strategy-persistence` (draft) → `deriv-edge-credence-dynamics` (draft)
- The 451729 D.1 list is a coordinated promotion target precisely because of this topological chain; advancing any single one without its dependencies advancing first would violate FORMAT.md's order.

**Strengthening posture**: the fix is *coordinated promotion in topological order*, not status-downgrade. The extraction agent's "Class A coordinated promotion sweep" framing in `audits/audit-findings-451729.md` Part II is exactly this — a sweep that respects topology.

**Gate 2 (Content review) — PASS, with a substantive observation.** Triage: (1) priors — yes; (2) competing formulation — extensively, with Props B.1 / B.2 / B.3 / B.4 / B.6 / B.7 each handling a distinct topology with stated formulation choices; B.5d (gradient-based attribution) is explicitly proved as the minimal SA1-preserving scheme for coupled edges, addressing what would otherwise be an alternative-formulation concern; (3) falsifiability — each Prop is testable algebraically, and the B.4 subscript fix that landed 2026-05-12 is itself the falsifier-having-fired evidence the segment is verifiable. Derivation check: Prop B.4's optimal exploration rate at line 220 (`$\varepsilon^\ast = (n_2+1)/(n_1+n_2+2)$`) is correct (the 451729 auditor's hand-derived value); the corollary $\alpha_\Sigma^\ast = 1/(n_1+n_2+2)$ follows by substitution; the $k$-arm generalization and (SA3) minimum exploration rate follow. The `## What Is Derived vs. What Is Chosen` table is comprehensive (39 rows). The B.7 / refutation-under-unobservable-$C$ is a clean instance of the integration-is-replacement landing pattern — refutation stated as positive result, not softened.

**Substantive caveat**: there is no `## Working Notes` section, and the §"Epistemic Status" §"What remains open" list still has 2 active items (continuous outcomes; adaptive exploration) and 3 resolved items (struck through). The 2 active items are research-seeds, not segment-content blockers — per FORMAT.md §"Working Notes" the location for active items would normally be Working Notes; here they live in Epistemic Status §"What remains open" which is also legitimate. The segment's Discussion-only structure works.

**Gate 3 (Mechanical review) — FAIL.** `bin/lint-md` reports **3 issues**: lines 346, 501, 507 — *"2 inline math spans with emphasis-vulnerable `_`."* Per project-CLAUDE.md §6 footnote, this is the GitHub emphasis-parser-can-match-`_`-across-spans failure mode; the lint's `--fix` mode handles the brace-removal automatically. **Gate 3 blocks `format-clean`, not `claims-verified`.**

**Gate 4 — N/A.** No `## Working Notes` section.

**Recommended next stage: HOLD on staging-monotonicity (Gate 1 blocker).** All four dependencies must promote first; in particular, `schema-strategy-persistence` and `deriv-sector-condition` are the load-bearing ones — a coordinated promotion in topological order, per FORMAT.md §"Ordering: promote in topological order."

**Strengthening direction noticed.** The §"Epistemic Status" item 2 (continuous outcomes) and item 5 (adaptive exploration — UCB, Thompson sampling) are post-promotion research directions, not strengthening-of-current-claims work. No softening-disguised-as-strengthening risk.

**Divergence from extraction agent.** Extraction agent said "No blockers. Still appears conservatively-staged." My read: **Gate 1 fails on all four dependencies at draft**, and **Gate 3 has 3 lint issues**. The extraction agent's "no blockers" judgment is correct for *segment-content maturity*, but it misses the staging-monotonicity requirement: this segment depends on three other Class A segments + `scope-and-or`, all at draft. The right disposition is *coordinated topological-order promotion*, which the extraction agent's Class A framing implicitly endorses but doesn't make explicit.

---

## §5 — `form-strategy-complexity-cost`

**Current state.** `stage: draft`, `status: discussion-grade`, `type: formulation`. Depends: `def-strategic-tempo` (**draft**), `form-information-bottleneck` (**draft**), `norm-explicit-strategy-condition` (**draft**), `der-chain-confidence-decay` (claims-verified), `form-structural-change-as-parametric-limit` (**draft**), `def-value-object` (deps-verified), `form-objective-functional` (deps-verified).

**Gate 1 (Dependency audit) — FAIL.** Four of seven dependencies are at `stage: draft` (`def-strategic-tempo`, `form-information-bottleneck`, `norm-explicit-strategy-condition`, `form-structural-change-as-parametric-limit`). Staging-monotonicity violated. Each dependency is genuine — the IB framework comes from `form-information-bottleneck`, the strategic-tempo definition from `def-strategic-tempo`, the maintenance-cost framing from `norm-explicit-strategy-condition`, and the compression-operations from `form-structural-change-as-parametric-limit`.

**Gate 2 (Content review) — PASS, with substantive engagement.** Triage: (1) priors — yes, the seven dependencies cover the conceptual machinery; the segment also adopts standard MDL (cited correctly) and the IB framework from Tishby (correctly cited via `form-information-bottleneck`); (2) competing formulation — the segment makes its formulation status explicit ("description length formulation is a *formulation*"); the KL direction is *derived* from a regret-bound argument via Pinsker (Csiszár 1991 Thm 3 corollary + Aczél-Daróczy 1975 chain-rule axiom for the uniqueness-of-reverse-KL-within-f-divergences upgrade); the IB direction-forcing is the strengthening the segment landed (cf. the deriv-strategy-cost-regret-bound link, which the segment references). (3) Falsifiability — testable at the depth-bound level (the $d^\ast$ formula is concrete and predictive). Label audit: `status: discussion-grade` matches the formulation-character of the segment overall; the maximum-useful-depth $d^\ast$ is labeled "Derived (Conditional on Beta-Bernoulli, per-edge persistence)" at the equation tag, which is internally consistent with the segment-level discussion-grade. The Pinsker / reverse-KL / Bretagnolle-Huber treatment in Epistemic Status is rigorous.

**Strengthening direction noticed (important).** The segment's `status: discussion-grade` is interesting: parts of it are *derived* (the depth-bound $d^\ast$, the KL-direction regret-bound argument). The §"Max attainable" line says *"robust-qualitative for the IB objective with the direction-forced derivation."* A reasonable interpretation: the segment could potentially promote to `robust-qualitative` once the dependency chain stabilizes — its current `discussion-grade` is conservative. **This is a strengthening direction worth flagging**: when the dependency staging clears, a status-upgrade attempt from `discussion-grade` → `robust-qualitative` should be made before `claims-verified` promotion. Strengthen-first per `doc/audit-routing-instructions.md` §2.

**Gate 3 (Mechanical review) — PASS.** `bin/lint-md` returns "All clean." Cross-references all resolve. Document cadence matches.

**Gate 4 — `## Working Notes` has 4 active items**, all forward-research:
- Mixed topologies (the $d^\ast$ generalization to mixed AND/OR DAGs)
- Optimal topology (combinatorial optimization, likely NP-hard)
- Dynamic complexity (compression-by-convergence)
- Stochastic $\mathcal T_\Sigma$ (Model S version)

These are *deferred* or *promoted* (each is candidate for its own future segment or research-seed entry). Per FORMAT.md §"Gate 4 — Notes disposition," at `candidate` they would each need explicit routing. **Not a blocker for `claims-verified`.**

**Recommended next stage: HOLD on staging-monotonicity (Gate 1 blocker), then *first try strengthening* to `robust-qualitative` before promoting to `claims-verified`.** The status-upgrade attempt is the strengthening-first move; if it succeeds, the segment promotes to `claims-verified` at status `robust-qualitative`; if it fails honestly (status holds at `discussion-grade`), promote at `discussion-grade`.

**Divergence from extraction agent.** Extraction agent: "Still appears conservatively-staged. Working Notes items are research-seeds, not blockers." My read: agrees on Working-Notes assessment; **Gate 1 staging-monotonicity is a 4-dependency block** (extraction agent missed); and the segment's `status: discussion-grade` is **possibly itself conservative** — a strengthening attempt to `robust-qualitative` is owed before the promotion sweep, per the project's strengthen-first discipline. This is a *strengthening recommendation*, not a softening — the extraction agent did not surface it.

---

## §6 — `schema-strategy-persistence`

**Current state.** `stage: draft`, `status: sketch`, `type: proposed-schema`. Depends: `result-sector-condition-stability` (claims-verified), `result-sector-persistence-template` (**draft**), `def-strategic-calibration` (**draft**), `def-strategy-dag` (**draft**). Brief noted: *"§D.3 strengthen-first landing record in its WN should trigger promotion attempt per 451729 extraction agent."*

**Gate 1 (Dependency audit) — FAIL.** Three of four dependencies are at `stage: draft` (`result-sector-persistence-template`, `def-strategic-calibration`, `def-strategy-dag`). Staging-monotonicity violated. Each is genuine — the schema instantiates the sector-persistence template (`result-sector-persistence-template`); the forgetting-prerequisite analysis uses the `def-strategic-calibration` framework via `δ_{\text{strategic}}`; the L0/L1 mismatch-state distinction uses `def-strategy-dag`'s Correlation Hierarchy.

**Gate 2 (Content review) — PASS, with substantive note on the §D.3 landing.** Triage: (1) priors — yes; (2) competing formulation — the schema's `type: proposed-schema` correctly tags the segment as a *framework for future verification* with verified instances; the §D.3 landing strengthened it from sketch with a hidden hard ceiling (linear approximation $\alpha_\Sigma^{ss} \approx 1-\lambda$) to an exact form $(1-\lambda)/(2-\lambda)$ with the hard ceiling at $\rho_\Sigma \geq R_\Sigma/2$ surfaced. This is a canonical instance of strengthen-before-soften operating on a polish-class finding (per Working Notes "Audit 451729 (D.3) strengthen-first edit, 2026-05-12"); (3) falsifiability — each verified instance (Props B.1–B.6 from `deriv-edge-credence-dynamics`) is a testable instantiation. **The §D.3 strengthening is significant**: it converts the schema's instantaneous check into a trajectory guarantee, surfaces a previously-hidden hard ceiling, and connects to NeurIPS Paper 2's structural-class theorem on gain-decay updates.

**Strengthening direction — major.** The brief flagged that "§D.3 strengthen-first landing record in its WN should trigger promotion attempt." **My read: agreed, and stronger than that.** The §D.3 landing did three things: (i) replaced the linear approximation with the exact form; (ii) surfaced the hard ceiling at $\rho_\Sigma \geq R_\Sigma/2$; (iii) connected to NeurIPS Paper 2's $\mathcal{A}_{\text{decay}}$ structural class. **The combined effect is that the segment is now strictly more mature than the `status: sketch` label captures.** A strengthening attempt could plausibly promote it to `robust-qualitative` or even `conditional` (the exact form is mathematically exact, the hard ceiling is a class-level no-go). Per `doc/audit-routing-instructions.md` §2, the strengthening attempt is owed before any promotion to `claims-verified` — and per the integration-is-replacement landing discipline of `doc/audit-routing-instructions.md` §4–6, **the status label tracks current truth, not provenance**: down-tiering an exact result for being new is a category error.

**Specifically**: the formal expression now states the threshold *exactly* (line 50: $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$), and the hard-ceiling is *exactly* derivable (line 58 says when $\rho_\Sigma \ge R_\Sigma/2$ *no* $\lambda$ satisfies the prerequisite, regardless of forgetting design — a class-level no-go). The segment's `status: sketch` undercounts what is now provably *exact* in the schema's load-bearing claims. Strengthening attempt: ask whether `status: conditional` (the exact threshold conditional on Beta-Bernoulli + exponential forgetting) is achievable; if so, promote to that status before `claims-verified`.

**Gate 3 (Mechanical review) — FAIL.** `bin/lint-md` reports **4 issues**: two `raw > in math — use \gt` (line 142), plus 2 emphasis-vulnerable `_` (line 144). Same lint-fix-mode-handles-it failure mode.

**Gate 4 — `## Working Notes` has 5 active items** (mostly resolved or landing-context-provenance items, including the §D.3 audit-trail entry and the NeurIPS Paper 2 cross-reference). Per the segment-voice rule (FORMAT.md §"Voice and provenance"), the §D.3 audit-trail line in Working Notes is correctly placed there (process history, not present-truth-of-the-theory) — exemplary integration-is-replacement landing. Not a blocker for `claims-verified`.

**Recommended next stage: HOLD on staging-monotonicity (Gate 1 blocker), then *strengthening attempt* to `conditional` (or higher) before promotion to `claims-verified`.** The brief's read is correct that this is the promotion-attempt trigger; my read sharpens it: this is the *strongest* strengthening direction in the 6-segment set.

**Divergence from extraction agent.** Extraction agent: "Still appears conservatively-staged given the strengthening landing. The §D.3 landing should arguably *trigger* a promotion attempt." My read: **agreed but stronger** — the segment is sufficient for `status: conditional` *now* (exact form + hard ceiling derived; both load-bearing for the schema's trajectory guarantee). The strengthening attempt to status `conditional` should be made before promotion. Gate 1 is a topological-order blocker (3 deps at draft), Gate 3 has 4 lint issues.

---

## §7 — Summary table

| Segment | Gate 1 | Gate 2 | Gate 3 | Gate 4 | Recommended next stage |
|---|---|---|---|---|---|
| `deriv-recursive-update` | PASS | PASS | PASS | N/A (3 editorial items; Gate 4 applies for `candidate`) | **`claims-verified`** |
| `deriv-sector-condition` | PASS-with-fixup (add `der-gain-sector-bridge` + `deriv-stochastic-non-exit` to `depends:`) | PASS | FAIL (13 lint) | N/A | **`claims-verified`** after frontmatter fixup; lint cleanup needed before `format-clean` |
| `der-gain-sector-bridge` | FAIL (`deriv-sector-condition` is draft) | PASS | FAIL (6 lint) | N/A (no Working Notes) | **HOLD** — promote `deriv-sector-condition` first |
| `deriv-edge-credence-dynamics` | FAIL (4 deps at draft) | PASS | FAIL (3 lint) | N/A (no Working Notes) | **HOLD** — coordinated topological-order promotion |
| `form-strategy-complexity-cost` | FAIL (4 deps at draft) | PASS | PASS | N/A (4 research-seed WN items; not blocking `claims-verified`) | **HOLD** + *attempt strengthening* `discussion-grade` → `robust-qualitative` |
| `schema-strategy-persistence` | FAIL (3 deps at draft) | PASS | FAIL (4 lint) | N/A (Working Notes correctly populated with §D.3 landing trail) | **HOLD** + *strengthening attempt* `sketch` → `conditional` (or higher) before promotion |

---

## §8 — Honest coverage statement

**Deep Gate-3 mathematical verification (full re-derivation by hand)**: not conducted in this adjudication pass for any of the 6 segments. The mathematical maturity of the Lyapunov / Itô-Lyapunov / Khasminskii / Pinsker / Csiszár / Doob-Dynkin / Bareinboim-Pearl machinery exceeds what a single adjudication pass can re-derive; the 451729 first-encounter auditor (Sonnet 4.6, full corpus walk) did spot-derivation of key results (the Prop B.4 fix; the schema-strategy-persistence approximation surfacing) — that prior work is upstream evidence for Gate 2. My Gate 2 reads are based on (a) structural-coherence check (does the derivation chain make sense end-to-end? do the equation tags match the claims?); (b) label-audit (does `status:` match what the segment claims?); (c) cross-reference resolution (do dependencies and citations resolve to real segments / real papers?); (d) Working-Notes / landing-trail consistency. **I did not re-derive Prop B.4's optimal exploration rate, Prop A.1S's stopped Grönwall bound, the Pinsker / Bretagnolle-Huber regret bound, the Cor A.1S.1 dichotomy, or the §D.3 exact threshold $(1-\lambda)/(2-\lambda)$ from scratch in this pass.** The 451729 auditor's first-hand work + the strengthen-first landing trails (Cor A.1S.1, §D.3 sharpening) + the segment-internal "What Is Derived" tables stand as the verification substrate.

**Lighter Gate-pattern matching**: this is what was actually run for Gates 1, 3, and 4 — frontmatter / depends-stage / cross-reference / `bin/lint-md` / Working-Notes-disposition. These mechanics are checkable; the Gate-1 finding (4 of 6 segments fail staging-monotonicity) and the Gate-3 finding (4 of 6 segments fail lint) are reliable.

**Deferred items flagged**:
- A full Gate-2 mathematical-derivation re-check of any of Prop B.4 / A.1S / Cor A.1S.1 / §D.3 / KL-direction-via-Pinsker would be a separate substantive review — not impossible in a single pass but not what this pass delivered. The first-hand 451729 audit provided prior coverage; a *second* independent mathematical re-derivation pass on the strongest claims would be the strict-form independent-verify per `doc/audit-routing-instructions.md` §0/§8 Refinement 4. Recommend if any single promotion (especially `deriv-sector-condition` carrying Cor A.1S.1) lands as `claims-verified`, a second independent mathematician (Joseph or a fresh sub-agent) re-derives Cor A.1S.1's Model-S half + the §D.3 exact form before any further status elevation.
- The strengthening direction on `schema-strategy-persistence` (`sketch` → `conditional`) is sketched here but not executed. Honest deferral.
- The strengthening direction on `form-strategy-complexity-cost` (`discussion-grade` → `robust-qualitative`) is sketched here but not executed. Honest deferral.

---

## §9 — Cross-cutting findings

1. **Gate 1 (staging-monotonicity) is the binding constraint on the Class A promotion sweep.** 4 of 6 segments fail Gate 1 because their dependencies are at `stage: draft`. The right disposition is **coordinated topological-order promotion** (FORMAT.md §"Ordering: promote in topological order"); not single-segment promotion. This is what the extraction agent's "Class A coordinated promotion sweep" framing implicitly endorses — my adjudication confirms the topology must be respected explicitly.

2. **Gate 3 (`bin/lint-md`) fails on 4 of 6 segments — total 26 issues across the set.** This is mostly the bare-Greek-in-prose failure mode (CLAUDE.md §6 "Self-reminder" footnote — *"a recurring kindness-to-future-me note, not pedantry"*) plus a few `raw <`/`raw >` and emphasis-vulnerable `_` cases. The lint's `--fix` mode handles the brace-removal automatically; the bare-Greek-in-prose requires hand edits. **Gate 3 does NOT block promotion to `claims-verified`** (it blocks promotion to `format-clean`), but it should be folded into the next mechanical-pass after Gate-2 promotions land. The pattern that 4 of 6 segments share this failure mode is itself signal: the lint-before-claim habit (CLAUDE.md §6) is not running across this segment family.

3. **`deriv-sector-condition` has a missing-dependency fault**: `der-gain-sector-bridge` (cited extensively for the sub-scope α derivation) and `deriv-stochastic-non-exit` (cited as the load-bearing no-go) should be in `depends:`. Strict Gate-1 read says this is a content-completeness fault, not a softening recommendation; fix is additive. Note: adding `der-gain-sector-bridge` creates a bidirectional dependency between the two — the bridge depends on the sector-condition, and the sector-condition's sub-scope α partition uses the bridge — which is structurally a co-dependency that promotion should treat as a single batch.

4. **`schema-strategy-persistence`'s `status: sketch` is the *most* understated label in the set.** The §D.3 strengthening landed an exact threshold form AND surfaced a hard-ceiling class-level no-go. The current sketch label may be the equivalent of the "down-tier exact result because it is new" category error named in `doc/audit-routing-instructions.md` §4–6. Strongest strengthening direction in the 6-segment set.

5. **The promotion sweep should be staged as**:
   - (Phase 1, monotonicity-leaves) Promote `deriv-recursive-update` → `claims-verified` (clean). Promote the lower-level draft deps that are blocking: `result-sector-persistence-template`, `scope-and-or`, `def-strategy-dag`, `def-strategic-tempo`, `def-strategic-calibration`, `form-information-bottleneck`, `norm-explicit-strategy-condition`, `form-structural-change-as-parametric-limit`, `hyp-edge-update-via-gain` — these are not in the D.1 list but they are the staging-monotonicity blockers. (Some may be appropriate-at-draft; those should be verified individually before forcing promotion. Joseph's judgment recommended.)
   - (Phase 2) Promote `deriv-sector-condition` → `claims-verified` (after frontmatter fixup adding the two missing deps).
   - (Phase 3) Promote `der-gain-sector-bridge` → `claims-verified` (now that `deriv-sector-condition` has promoted).
   - (Phase 4) **Strengthening attempts** on `schema-strategy-persistence` (sketch → conditional) and `form-strategy-complexity-cost` (discussion-grade → robust-qualitative) per strengthen-first discipline; if they succeed, promote at the strengthened status.
   - (Phase 5) Promote `deriv-edge-credence-dynamics` → `claims-verified`.
   - (Phase 6, separate) Lint cleanup pass on the 4 failing segments before any of them promote to `format-clean`.

---

## §10 — Disposition (per `doc/audit-routing-instructions.md` §8 enum)

The 6 segments collectively constitute a **`coordinated-topological-promotion`** disposition (not in the canonical enum; submitting as a candidate refinement of `actionable-open`). Each individual segment's disposition:

- `deriv-recursive-update` → `actionable-open` (clean single-segment promotion to `claims-verified` co-owner direct-fix).
- `deriv-sector-condition` → `actionable-open` (with frontmatter-fixup); `claims-verified` after fixup, co-owner direct-fix.
- `der-gain-sector-bridge` → `actionable-open` (blocked-on-topology); promotes after `deriv-sector-condition`.
- `deriv-edge-credence-dynamics` → `actionable-open` (blocked-on-topology); promotes after coordinated dep chain.
- `form-strategy-complexity-cost` → `architectural` → strengthening attempt → `actionable-open` once status-upgrade attempted.
- `schema-strategy-persistence` → `architectural` → strengthening attempt → `actionable-open` once status-upgrade attempted.

**Soft / sentiment / considered-declined**: none — the 6 segments are all genuinely promotion-candidates per the extraction agent's read; the divergence is in *what gates fire* and *what topological ordering is required*, not in whether they're promotable.

**Independent-verify gate fired**: yes. This adjudication is the second-eye check on the 451729 extraction agent's "Class A coordinated promotion sweep" framing. The extraction agent's substantive read holds for `deriv-recursive-update` and `deriv-sector-condition`; for the other 4 segments, my read adds the Gate-1 topology blocker and (for 2 segments) a strengthening-attempt-owed-before-promotion finding. Both readings converge on "do not do single-segment promotion without topological coordination."

---

*Adjudication complete 2026-05-20. Output for Joseph / parent agent: per-segment Gate verdicts above, recommended phased promotion sweep §9.5, deferred-Gate-2-mathematical-redrivation flagged honestly §8. No edits made to any segment, no TODO modifications, no commits.*
