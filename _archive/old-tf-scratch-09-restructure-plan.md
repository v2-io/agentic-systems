# TFT Restructure Plan — Session 7

## The Problem

Current TFT documents don't follow the TST "one result per document" pattern:
- TF-06 (161 lines) contains 5+ ideas and NO formal proposition
- TF-00 (185 lines) is a notation dump — definitions should live where first needed
- TF-01b, TF-06.5 have awkward numbering
- Line counts range 43–266 (6:1 ratio; TST is ~3:1)
- Navigational scaffolding (dependency DAGs, results indexes, notation appendix) was needed BECAUSE the document structure doesn't self-document

In TST, each file IS a theorem. The document structure IS the navigation. No index needed to find where theorems live.

## The TST Pattern (to emulate)

Each file contains:
1. **Definition(s)** — only those needed by this theorem, not yet defined elsewhere
2. **Central Result** — ONE theorem/axiom/hypothesis/claim with formal expression
3. **Discussion** — "Why This Matters," implications, domain instantiations
4. **Corollary(ies)** — if any

Files range 27–95 lines (mean ~63). Example: T-02.md = Definition D-01 ("Feature") → T-02 ("Implementation Time Lower Bound") → Corollary C-02.1.

## Proposed New Structure

### Mapping: Old → New

| New # | Old Source | Title | Type | Central Result | Est. Lines |
|-------|-----------|-------|------|----------------|------------|
| TF-01 | TF-01 | Scope | Scope Def | $\mathcal{S}_{\text{TFT}}$ defined | ~40 |
| TF-02 | TF-01b | Causal Structure | Axiom | Temporal ordering → causality; CIY | ~90 |
| TF-03 | TF-02 | The Model | Axiom | $M_t = \phi(\mathcal{H}_t)$ as sufficient statistic | ~80 |
| TF-04 | TF-03 | Event-Driven Dynamics | Formulation | $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ | ~60 |
| TF-05 | TF-04 | Mismatch Inevitability | Derived | Prop 5.1: $\mathbb{E}[\|\delta_t\|^2] > 0$ | ~80 |
| TF-06 | TF-05 | The Update Gain | Empirical | Claim 6.1: $\eta^* = U_M/(U_M + U_o)$ | ~80 |
| TF-07 | TF-06 §1–3 | Action Selection | Derived | $a_t = \pi(M_t)$; fluency spectrum | ~70 |
| TF-08 | TF-06 §4–7 | Exploration-Exploitation Balance | Hypothesis | $\pi^* = \arg\max[\text{value} + \lambda \cdot \text{CIY}]$ | ~90 |
| TF-09 | TF-06.5 | Deliberation Threshold | Derived | Prop 9.1: $\Delta\eta^* \cdot \|\delta_{\text{post}}\| > \rho \cdot \Delta\tau$ | ~70 |
| TF-10 | TF-07 | Structural Adaptation | Derived | Prop 10.1: $\mathcal{F}(\mathcal{M}) < 1-\epsilon$ → structural change | ~90 |
| TF-11 | TF-08 | Persistence Threshold | Hypothesis | Prop 11.1: $\mathcal{T} > \rho$ | ~90 |
| App A | App A | Lyapunov Stability | Derived | Props A.1–A.4 (nonlinear generalization) | ~200 |

**Total: 11 numbered + 1 appendix = 12 documents** (TST has 12 numbered)

### What happens to TF-00?

TF-00 (notation appendix) **shrinks dramatically or is absorbed into README**:
- Each symbol is now defined where first introduced (inline with its theorem)
- README gets: TOC, Epistemic Status Legend, Dependency Chain, Formal Results Index
- If TF-00 survives at all, it's a slim (~30 line) "Conventions" quick-reference card

### What happens to TF-06?

TF-06 is the main surgical operation. It splits into two documents:

**TF-07 (Action Selection)** gets:
- "Action as Model Function" (the derived consequence of TF-03's model axiom)
- "Implicit vs. Explicit Action Selection"
- "Action Fluency vs. Model Sufficiency"
- "The Temporal Advantage of Implicit Action"
- Domain instantiations (implicit/explicit columns only)

**TF-08 (Exploration-Exploitation Balance)** gets:
- "The Exploration-Exploitation Trade-off"
- "Action as Information Generation"
- "Query Actions: Accessing External Models"
- "The Adversarial Mirror: Deception and Model Corruption"
- "Toward a Unified Policy Objective" (promoted to central result)
- Domain instantiations (probing/query columns)

### Where adversarial material lives

Currently scattered across TF-06, TF-08, and Appendix A. Under restructure:
- **Conceptual** adversarial (deception, OODA interference, trust meta-model) → **TF-08** (it's about the CIY framework in adversarial settings)
- **Formal** adversarial dynamics (tempo competition, mismatch ratios, coupling coefficients) → **TF-11** (it's about persistence under adversarial ρ)
- **Lyapunov** adversarial (Props A.3, A.3.1) → **Appendix A** (stays)

### Appendix A treatment

Stays as appendix. Rationale:
- It's a GENERALIZATION of TF-11's result, not a new primary line of reasoning
- The 4 propositions share a Lyapunov setup — splitting them would require repeating it 4×
- Academic convention: main result in body, generalization in appendix
- Appendix A remains the longest document (~200 lines) but this is acceptable for a technical appendix

## Dependency Chain (new numbering)

```
TF-01 (Scope) → TF-02 (Causality) → TF-03 (Model) → TF-04 (Events)
  → TF-05 (Mismatch) → TF-06 (Gain) → TF-07 (Action) → TF-08 (Policy)
  → TF-09 (Deliberation) → TF-10 (Structural) → TF-11 (Persistence)
  → Appendix A (Lyapunov)

Cross-links:
  TF-02 ←→ TF-08 (CIY drives exploration)
  TF-03 ←→ TF-05 (sufficiency → mismatch proof)
  TF-06 ←→ TF-09 (gain → deliberation threshold)
  TF-03 ←→ TF-10 (model class fitness)
  TF-06 ←→ TF-11 (gain → tempo)
  TF-04 ←→ TF-11 (event rates → tempo)
  TF-11 → App A (linear → nonlinear generalization)
```

## Document-Level Format (TST-aligned)

Each document follows this template:

```markdown
# [Definition D-XX: Name (if introducing new definitions)]

[Definition text]

# TF-XX: Title (Epistemic Type)

[1-2 sentence plain-language statement of the central result]

**Epistemic status**: [Brief note on what is derived vs. hypothesized vs. discussion]

## Formal Expression

[LaTeX equations with variable definitions]

## [Discussion Section(s)]

[Why this matters, implications, etc. — 1-3 sections]

## Corollary C-XX.Y: Name (if any)

[Statement and brief discussion]

## Domain Instantiations

[Table mapping the result to specific domains]

## Open Questions

[If any]
```

## Definitions Placement

Each definition appears where FIRST NEEDED:

| Definition | First Used | Currently In |
|------------|-----------|-------------|
| Ω, O, A, h, T, ε | TF-01 (Scope) | TF-01 ✓ |
| H_t (interaction history), do(·), CIY | TF-02 (Causality) | TF-01b ✓ |
| M_t, M, φ, f, S(M_t), F(M), β | TF-03 (Model) | TF-02 ✓ |
| e, τ, E, ν^(k), U_o^(k), ν_eff | TF-04 (Events) | TF-03 ✓ |
| ô_t, δ_t | TF-05 (Mismatch) | TF-04 ✓ |
| η, η*, U_M, g | TF-06 (Gain) | TF-05 ✓ |
| π, action fluency | TF-07 (Action) | TF-06 (part) |
| λ(M_t), unified policy | TF-08 (Policy) | TF-06 (part) |
| Δτ, Δη* | TF-09 (Deliberation) | TF-06.5 ✓ |
| Φ (structural update) | TF-10 (Structural) | TF-07 ✓ |
| T, ρ, |δ|_ss | TF-11 (Persistence) | TF-08 ✓ |

Good news: definitions already live roughly where they're first used. The main change is that TF-00 stops being the canonical definition location.

## Proposition Renumbering

| Old | New | Name |
|-----|-----|------|
| Prop 4.1 | Prop 5.1 | Mismatch Inevitability |
| Claim (TF-05) | Claim 6.1 | Uncertainty Ratio Principle |
| — (TF-06 discussion) | Hypothesis 8.1 | Unified Policy Objective |
| Prop 6.5.1 | Prop 9.1 | Deliberation Threshold |
| Prop 7.1 | Prop 10.1 | Structural Adaptation Necessity |
| Prop 8.1 | Prop 11.1 | Persistence Threshold |
| Props A.1–A.4 | Props A.1–A.4 | (unchanged — appendix numbering independent) |

## Execution Plan

### Phase 1: Create new files (parallelizable)

Each document can be written independently since the mapping is fixed:

1. **Agent A**: Write new TF-01.md through TF-04.md (straightforward renumber — content barely changes, just update cross-refs)
2. **Agent B**: Write new TF-05.md and TF-06.md (renumber from old TF-04/TF-05, update cross-refs)
3. **Agent C**: Write new TF-07.md and TF-08.md (SPLIT old TF-06 — this is the surgical operation)
4. **Agent D**: Write new TF-09.md through TF-11.md (renumber from old TF-06.5/TF-07/TF-08, update cross-refs)
5. **Agent E**: Update Appendix-A-Lyapunov.md cross-references
6. **Agent F**: Rewrite README.md (new TOC, dependency chain, absorb TF-00's indexes)

### Phase 2: Verify (sequential)

7. **Verification agent**: Check all cross-references, proposition numbers, definition consistency

### Phase 3: Cleanup

8. Remove old files (TF-00.md, TF-01b.md, TF-06.5.md — the ones whose names change)
9. Update scratch/additional-feedback.md with new numbering
10. Commit

### Risk: Cross-reference breakage

Every document references every other. Mitigation:
- All agents receive the SAME old→new mapping
- Each agent is responsible for updating ALL cross-refs within its assigned documents
- Verification agent does a final sweep

## What This Achieves

| Metric | Before | After |
|--------|--------|-------|
| Documents | 11 + appendix | 11 + appendix |
| Line range | 43–266 (6:1) | ~40–200 (5:1) |
| Mean lines (excl. appendix) | ~113 | ~76 |
| Docs with formal proposition | 5 of 11 | 7 of 11 |
| Docs with >1 central idea | 3 (TF-06, TF-00, TF-08) | 0 |
| Separate notation document | Yes (185 lines) | No (or slim 30-line conventions) |
| Awkward numbering (01b, 06.5) | 2 | 0 |
| Navigational indexes needed | 3 (TOC, dep DAG, results index) | 1 (README TOC) |
