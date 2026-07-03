# Running Outline — Audit 731548

> **⚠ SUPERSEDED for routing.** This is the *de-novo discovery* ledger, written before the independent verification round. It contains candidate findings the verifiers later **refuted, reclassified as regressions, or corrected** (see `verify/01..06-*-verdict.md`). For the routable finding set with verified dispositions, use the FINAL: `audits/audit-731548-FINAL-2026-07-02.md` (§B / §B.1). This file is reasoning-trail archaeology only — do not route from its raw ledger. Reflection 36 (`36-impl-segments-audit.md`) covers the impl-* series added after this outline was last updated.

## PART I MAIN CHAIN COMPLETE (reflection 35) — addendum

Walked all of Part I's canonical main chain: Ch.1 (7) + Ch.2 (intro+4) + Ch.3 (intro+9, incl. appendix jumps to deriv-recursive-update, deriv-sector-condition) + Ch.4 (intro+8, incl. mood pair + form-sector-condition + der-gain-sector-bridge). Skipped per AVOID: the four `impl-*` chapter-end segments. **Not walked:** Appendix A (~40 derivation segments; hit 2 via back-pointers), Appendix B worked examples, Parts II/III entirely.

### Finding-grade (would go in §B)
- **(lxxiv) The persistence "iff" is unproven & false-in-general** — headline correctness finding. Sector generalization makes $\alpha \gt \rho/R$ *sufficient* for persistence, not necessary (slack floors; counterexample in reflection 30). Three sites: appendix Prop A.1, result-sector-condition-stability headline, result-persistence-condition summary + "below threshold" paragraph. Root: certificate/behavior conflation, true only in the linear/tight case. Repair = state sufficiency + prove necessity-under-tightness (a small strengthening). *No walked downstream derivation uses only-if; referee-visible.*
- **(viii)+(35b)+(05) $\mathcal C_t$ trichotomy / missing $M_0$** — one paragraph fixes three findings: physical trajectory (non-copyable, identity-bearing) vs accessible record (copyable) vs compressed model + endowment ($M_0$/φ/class, not from $\mathcal C_t$). Home: def-chronica + form-agent-model. Load-bearing for identity claim (scope-agent-identity) and LLM applicability.
- **(x) scope-adaptive-system exclusion equivalence** fails on fully-observed-unknown-dynamics (RL). Root fix: totality-reading paragraph in def-agent-environment ($T\subseteq\Omega$).
- **Floor-accounting family (xlix/xxx)** — "reducible" mislabel (three floors not two); class-vs-noise detection-signature conflation. **Resolution now concrete:** the residual-autocorrelation diagnostic (structured→class, white→noise) exists in result-structural-adaptation-necessity's body+gold; propagate it to def-model-class-fitness's signature. Assembles into the four-branch operator diagnostic (raise-gain/keep-learning/fix-sensors/change-class) — the corpus's single most-converged missing segment (arrivals: 13,20,21,29,33).
- **(xiii/liv/xvii) condition-4 proprioceptive weakness** — scope-agency's Formal Expression admits observation-only contrast; repair lives in Discussion not FE; CIY + post-causal-structure inherit ("exactly Level 2" overclaim; nominal-coupling membership contradiction).
- **(lxxx/lxxxi) mood integration** — τ* derived for estimator-role, def-mood assigns modulator-role (ES silent, WN acknowledges); persistence-compatibility rests on unquantified timescale-separation, MG-1..4 / temporal-nesting $\epsilon_{\max}$ machinery uninvoked. Concrete fix: place mood in the temporal-nesting ladder.

### Structural / §F
- Normative-layer reconciliation sweep; **quantifier/gloss-audit sweep** (the under-audited layer — iff/any/exactly/labels/table-cells; lxxiv is Exhibit A); age-gradient refined to *recently-integrated=woven, recently-added=locally-strong-not-woven* (mood is the proof).
- **Missing-theorem candidates:** Class-1 compression price (11); g_M calibration/confabulation bound (16); compilation-cost axis (18/27); EIG-at-CIY-prices conservation (22); IB-vs-structural-reserve tension (33); necessity-under-tightness lemma (30).
- **Shadow-catalogue (10 pairs)** — Part-I theorems with Volume-4 readings that inherit Part-I's tier. **Top §F recommendation: a half-page appendix cataloguing them** — worth more to the ELI program's defensibility than most direct Volume-4 writing.
- Legibility: Ch.1 lacks intro segment (only Part-I chapter without; others exemplary); constitutive-opacity triad unnamed; per-domain anchor tables = best legibility device, one per formulation segment; best segments now 40% non-body (WN/gold/findings) — fold-by-default render needed.

### §E (what holds) — calibration
deriv-recursive-update + deriv-sector-condition + form-sector-condition = the quality-ceiling trio (all recent, 2026-05-16→20). Corpus *anticipated* my registered attacks 4×. Integration-is-replacement executed cleanly (Model-S dichotomy; consequence-3 re-grounding). Tier-separation discipline throughout Ch.2–4. Pipeline: corrective edits execute when fix-specific+recent; the earlier "stall class" hypothesis weakened.

---

## (earlier) Ch.3→Ch.4 boundary consolidation

Updated at the Ch.3→Ch.4 boundary (reflection 24). This consolidates the ledger scattered across reflections 01–24 and sketches the FINAL's shape. Roman numerals = ledger items as numbered in the reflections.

## Walk position

INTRODUCTION + Part I Ch.1 (7 segs) + Ch.2 (intro + 4) + Ch.3 (intro + 9, incl. appendix jump to deriv-recursive-update) = 24 reflections. Next: appendix jump `#deriv-sector-condition`, then Ch.4 (persistence — the heart), whose `impl-persistence-and-limits` row is **skipped** (AVOID list: chapter-end impl segments).

## Strategic-loop revision (§4.5)

Initial predictions ~60% confirmed / ~25% falsified in the corpus's favor / ~15% pending. The falsifications cluster on recently-reworked segments → **age-gradient hypothesis** (quality tracks recency-of-rework, not depth/importance) has survived every test. Audit focus for Ch.4: deliberate gain-reset; pre-registered checks in reflection 24 §4–6. The audit's highest-value products so far are compositional (cross-segment), not local — consistent with the front-of-outline being locally audited-out.

## Candidate findings ledger (for §B triage)

### A. Floor-accounting family (likely one structured finding, strongest of the walk)
- **(xlix)** `result-mismatch-decomposition` labels term (i) "reducible" — but the Bayes/state-uncertainty floor $\mathbb E[\mathrm{Var}(\bar o\mid\mathcal C)]$ inside it is irreducible by any modeling; three floors, not two. Verify against `#internal-external-decomposition`. [mine, strong]
- **(xxx)** `def-model-class-fitness` detection signature ("persistent mismatch despite learning") conflates class-ceiling with noise floor; $S/\mathcal F$ are normalized while the signature is absolute. Check Ch.4's `#result-structural-adaptation-necessity` hypothesis statement. [mine, med-high]
- **(xlvii)** `def-mismatch-signal` Mahalanobis normalizer uses noise-only covariance; innovation covariance ($U_M+U_o$ — which the *gain* segment uses) is the coherent choice. [mine, med-high]

### B. Boundary-adjudication family (Ch.1 species: formal layer permissive, Discussion adjudicates, siblings inherit different sides)
- **(x)** `scope-adaptive-system` exclusion equivalence fails on natural reading (fully-observed-unknown-dynamics excluded; $T\subseteq\Omega$ never stated). Root fix: one totality-reading paragraph in `def-agent-environment`. [mine, high; claims-verified segment]
- **(xiii)+(liv)** `scope-agency` condition 4 proprioceptively satisfiable (repair exists in Discussion, not Formal Expression); CIY inherits ("exactly Level 2" overclaim). [mine, med-high]
- **(xvii)+(xviii)** `post-causal-structure` vs `scope-agency`: query-only coupling inside vs at-boundary of agency scope; "interventional" with two referents. Drift from the newer boundary paragraph. [mine, high on referent split]
- **(v)** Ch.1 opacity atoms (transition/epistemic opacity as constitutive) vs Kalman-known-model instances — **resolution exists** at `emp-update-gain` (endogenous estimation); residual = propagation debt to Ch.1. [mine+4 prior substrates; downgraded]
- **(viii)** No $M_0$/endowment slot: chronica "only raw material," LLM realization omits weights, $\mathcal F$'s class-identity undefined for pretrained agents. Three independent routes; one-paragraph fix in `form-agent-model`. [convergent; my top structural repair]

### C. Certified-shape singletons
- **(xix→certified)** `post-causal-structure`'s causal-downstream *update-weighting* norm unsupported; machinery prices provenance at *selection* (CIY), informativeness at *update* (gain). Precise rewording available; two-line dominance lemma plausible. [mine]
- **(xxiv)** `form-information-bottleneck`: exact-status vs deterministic-encoder special case; closed-loop stochastic-encoder chain failure makes the two halves of the warrant mutually exclusive. One-paragraph fix. [mine+526815]
- **(li)** `emp-update-gain` type outgrown (Fisher-local exact derivation landed; type still `empirical`) — a *deflation fossil*. [mine]
- **(lii)** $U_M$ symbol collision (model uncertainty vs Part-III epistemic unity) inside NOTATION. [endorsed 266847, elevated]
- **(xlii)** Attack 6 timestamp-field vs event-tuple mismatch — one field from settling the clock ontology. [mine]
- **(xl)** Two-clocks reconciliation *available*: record ordinal, dynamics metric (g_M flow) — proposal, not problem. [mine]
- **(ix)** THREAD-E gold counterfactual (injective φ ⇒ introspectively detectable forks) is false — detection is relational, needs external channel. Guard `#scope-agent-identity` against importing it. [mine, finding-about-the-gold]
- **(lx)** 3/2 adversarial exponent channel-dependent (drift-injection assumption unstated); derivation sketch in reflection 24. [verify-at-target]
- **(vii)** $a_0$/$t{=}1$ boundary; **(xxxv)** ES misattribution in form-event-driven; **(xxxvi)** expected-vs-realized $\mathcal I(e_\tau)$; **(xliv)** fluency formalization borrows update-gain for action-quality (test at der-deliberation-cost); **(xlv)** where fixed goals live in Part I; **(xxix)** elementwise-sup type error in $\mathcal F$; **(xxxi)** unbound $\varepsilon$; **(lxi)** Model-D equality vs ultimate bound. [small/mechanical]

### D. Watches pending (test in Ch.4+)
(xli) tempo blind to interior corrective work → der-deliberation-cost; (xxxii) class-transition cost unpriced; (xxxiv) events-only vs consolidation pseudo-events; (liii) short-stream gain-estimation transient → deriv-adaptive-gain-dynamics; (lviii) $\rho$ under-defined at load-bearing moment; (i) Model D/S dichotomy overlap → deriv-sector-condition [imminent]; $R$-as-capacity identification [imminent]; scalar-$\mathcal T$ anisotropy exposure in headline persistence results.

### E. Meta-findings (for §F/§G)
1. **Normative-layer reconciliation sweep** (Ch.1 pattern): for every Discussion boundary-adjudication, check the Formal Expression encodes it.
2. **Gloss-audit sweep**: labels/underbraces/table-cells checked against math (the "reducible" case is Exhibit A).
3. **Pipeline directional bias**: corrective edits execute when neutral/strengthening (≥6 specimens); stall when they'd weaken constitutive-sounding claims (opacity atoms, nominal-coupling, expected-vs-realized). State candidate explanations honestly.
4. **Gold-lift vs de-novo tension** (§G): prior-audit gold embedded in segment bodies primes every future auditor; Joseph's contrarian-stance instruction works and should enter the SOP; gold items need re-verification before action (stale specimens found).
5. **Age-gradient**: retrofit priority = oldest-untouched, not most-important (Ch.1 needs the Ch.2/3 treatment).
6. **Attack-section/well-definedness-clause as one genus** — mandate a minimal version corpus-wide (FORMAT).
7. **Missing-theorem candidates**: Class-1 compression price (goal-blindness has an IB cost — with possible optimal $\kappa^\ast>0$); $g_M$ calibration constraint (interior dynamics may not decrease expected calibration — confabulation bound); compilation-cost axis (goals→π, deliberation→fluency, knowledge→weights — one unpriced cost family); EIG-at-CIY-prices conservation (formulation cost smuggles EIG's intractability back in).
8. **Missed-elegance candidates**: learnability budget = sufficiency denominator (closes Ch.1 gap beautifully); interior-invariance meta-theorem (fork-undetectability, curation-blindness, sandbox ceiling as one statement — check M1 subsumes); epistemic-attack-surfaces assembly (silence-engineering / noise-inflation / yield-spoofing as Part-I roots of Part III); record-vs-state duality (chronica/M_t); three-currencies note (error/surprise/information); Red-Queen endogenization of ρ seeded at hyp-mismatch-dynamics; tempo-doubling diagnostic; iso-tempo cost contours.
9. **Legibility ledger** (Joseph's ask): Ch.1 lacks an intro segment (Ch.2/3's are exemplary); constitutive-opacity triad unnamed across three segments; "Constraint C3"-style forward labels; $r^{(j)}$ unglossed; defensive-armor paragraphs mid-formulation (IB segment); punchline-trailing in long boundary paragraphs; per-domain anchor tables are the best legibility device in the corpus — one per formulation segment would be the single highest-yield policy.
10. **§E (what holds)**: deriv-recursive-update as the quality ceiling; emp-update-gain's opacity-resolution; def-model-sufficiency's pre-emptive hygiene; def-adaptive-tempo's self-armored caveats; tier-separation discipline throughout Ch.2–3; corpus repeatedly *anticipated* registered attacks (4×).

## FINAL shape (draft)

§A scope/method (walk order, appendix jumps, gold-contrarian protocol, priming bleed). §B: A-family floor-accounting (structured), B-family boundary-adjudication (structured), then singletons by severity. §B.1 rescinded candidates (running: axiomatic-vs-definitional nit rescinded; constraint-separation want withdrawn; cyclic-SCM tension rescinded; batch of gold items refuted — dogfooding the contrarian instruction). §C coverage honesty (Ch.1–4 + appendix sample; Parts II–III untouched → continuation offer). §D hypothesis-tier (learnability floor, ρ endogenization, channel-dependence of 3/2). §E per item 10. §F missing-theorems + missed-elegance + proportionality (exemplar-diet monotony; coupling taxonomy uncashed vs learnability floor missing; tables hide best unexploited claims). §G process (gold-lift tension, impl-skip note, chapter-intro under-audit, instantiate-and-check as cheap Gate-2 addition).
