# 16 — der-recursive-update

*Type: derived. Status: conditional (in frontmatter). Body Epistemic Status says "Exact, with a partly definitional character." Stage: claims-verified. Depends: [form-agent-model, form-event-driven-dynamics, deriv-recursive-update].*

## Predictions vs evidence
Predicted: derivation that update must be recursive from completeness + temporal-ordering + partial-observability. Found: exactly that — three constraints (C1 temporal ordering, C2 partial observability, C3 completeness commitment) force recursive form. Seven counterexample attacks live in #deriv-recursive-update.

## **Candidate finding — status-label drift**
Frontmatter `status: conditional` but body Epistemic Status (line 41) reads `*Exact, with a partly definitional character.*` These differ:
- FORMAT.md `exact`: "Mathematically validated under stated assumptions"
- FORMAT.md `conditional`: "Depends on explicitly named local assumptions"

The constraints C1 (temporal-ordering, postulate-grade), C2 (partial-observability, scope condition), C3 (completeness commitment, definitional) are *all framework-internal commitments* — not external conditions that might not hold. So the result is exact *within the framework*; "conditional" is a slight underclaim. **Severity: low. Type: scope/status mismatch. Disposition: editorial — either align frontmatter to "exact" matching the body, or align the body to "conditional" matching the frontmatter.** Anchor: 01-aat-core/src/der-recursive-update.md frontmatter line 4 + body line 41.

## Math verification
- $M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$ — event-driven recursive form. ✓
- $\frac{dM}{d\tau} = g_M(M_\tau)$ — between-event ODE evolution. ✓

The appendix derivation (`#deriv-recursive-update`) is claimed to verify by seven counterexample attacks. I'll need to verify when I reach it — high-leverage check given this is *the* first derived result.

## Prose-coherence
- Line 16: "This is not a weakness; it is the precise character of the claim." — borderline. Could be (a) defensive ghost per integration-is-replacement discipline, or (b) pedagogical clarification. Reading it cold, it seems more pedagogical: it preempts the question "doesn't completeness-as-definitional make recursive-update trivial?" by clarifying what kind of claim this is. **Not a finding, but observable.** A future audit could check whether "not a weakness" language is the integration-is-replacement ghost or genuine pedagogy.
- The "two derivations from completeness" framing from the chapter intro (line 18 of the-cycle-in-motion-intro) names this segment + der-action-selection as joint consequences. This segment doesn't reciprocally name der-action-selection — that's fine because der-action-selection comes next in OUTLINE order.

## Cross-segment consistency
Forward-refs `#deriv-recursive-update` (appendix), `#def-model-sufficiency`, `#emp-update-gain`, `#form-consolidation-dynamics`, `#schema-strategy-persistence`. Internal coherence good.

## Watch list (update)
- Status-label drift in der-recursive-update is the *first* status-label inconsistency I've found. Mild signal that the broader corpus may have more of these. **Watch.**
- The "consolidation regime" foreshadowing (line 47) connecting to #form-consolidation-dynamics is interesting — this is the kind of "named open regime with its own scope condition" that the framework will rely on later for plasticity-stability tradeoffs.

## Next-segment predictions
`#der-action-selection`. Second of "two derivations from completeness." Will derive that action depends on $M_t$ alone — not directly on $\mathcal{C}_t$. Same epistemic character (partly definitional).

## What I'd change
Align status field. Either:
- Frontmatter status → `exact`, OR
- Body Epistemic Status → "Conditional under C1+C2+C3 (which are framework-internal commitments rather than external assumptions)"

## Brief wandering

**On the "partly definitional" honesty.** The framework explicitly names that C3 (completeness) cannot be violated — it's definitional. So the recursive-update result is, in some sense, baked-in by the modeling choice. The framework is honest about this. The methodological alternative would be to *not* commit to $M_t$ as complete (allow auxiliary state outside $M_t$) and then have non-recursive updates as a possibility; the framework's choice is to commit to completeness and recover recursion as a derived consequence. This is a valid trade-off; what matters is naming it.
