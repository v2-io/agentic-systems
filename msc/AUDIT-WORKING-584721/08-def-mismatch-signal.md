# Reflection 08 — def-mismatch-signal (Section I row 17)

## §4.2 dependency check

`depends: [form-agent-model, def-observation-function]`. Both upstream. **No backward-dependency finding.**

But: the Formal Expression uses $a_{t-1}$ (in $\hat o_t = \mathbb E[o_t \mid M_{t-1}, a_{t-1}]$). Tracing transitively:
- form-agent-model: depends [def-agent-environment, def-observation-function, def-chronica] — no def-action-transition
- def-observation-function: depends [def-agent-environment] — no def-action-transition

Same F-A drift again. But this prompts a *root-cause* observation worth surfacing:

### Root-cause realization on the F-A series

`def-observation-function` (Section I row 2) itself has Formal Expression $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$ — it uses $a_{t-1}$ without depending on `def-action-transition`. This means **F-A drift is rooted at row 2**. Every downstream segment whose only path to action-symbol coverage runs through `def-observation-function` (or through `form-agent-model`, which inherits from `def-observation-function`) will also be missing `def-action-transition` transitively.

Re-numbering the F-A series in OUTLINE row order:

| # | Segment | Row | Symbol used | Missing dep |
|---|---------|-----|-------------|-------------|
| F-A0 | def-observation-function | 2 | $a_{t-1}$ | def-action-transition |
| F-A1 | scope-adaptive-system | 4 | $\mathcal C_t$ | def-chronica |
| F-A2 | form-information-bottleneck | 11 | $a_{t:\infty}$ | def-action-transition (propagates from F-A0) |
| F-A3 | def-model-sufficiency | 12 | $a_{t:\infty}$ | def-action-transition (propagates from F-A0) |
| F-A4 | form-event-driven-dynamics | 14 | $M_{\tau^-}$ | form-agent-model (independent) |
| F-A5 | def-mismatch-signal | 17 | $a_{t-1}$ | def-action-transition (propagates from F-A0) |

**The structural insight**: F-A0, F-A2, F-A3, F-A5 are all the *same root-cause finding*. Adding `def-action-transition` to `def-observation-function`'s depends would fix the chain through transitivity for at least F-A2, F-A3, F-A5 (form-information-bottleneck → form-agent-model → def-observation-function would pick up the action-transition dependency).

That's one editorial change with multi-segment impact, not 4-5 separate fixes. Worth flagging as a *root-cause* finding rather than as a list.

F-A1 (scope-adaptive-system → def-chronica) and F-A4 (form-event-driven-dynamics → form-agent-model) appear to be independent drifts not solvable by the same root-cause fix.

## §4.4 prompts walk-through

**1. Predictions vs evidence.** I predicted (in reflection 07): "Row 17 = def-mismatch-signal. I expect: clean definition with the score-function variant $\tilde \delta_t$ also defined per NOTATION.md. Probably status:axiomatic. Cross-references to #form-agent-model and #der-recursive-update." Verification: ✓ on status, definition shape, score-function variant. **Mostly correct, with one miss**: depends actually lists `def-observation-function` (not `der-recursive-update`); makes sense in retrospect — the mismatch is observation-side, not update-side.

**2. Cross-segment consistency.** Forward refs to `#result-persistence-condition`, `#result-sector-condition-stability`, `#result-mismatch-decomposition`, `#def-causal-information-yield`, `#emp-update-gain`. Internal consistency holds.

**3. Math verification.** The Mahalanobis-distance normalization in the Discussion is standard. The score-function form $\tilde \delta = -\nabla_M \log P$ is the negative gradient of the log-likelihood — that's the standard score (Fisher's). Under Gaussian likelihoods, score is proportional to prediction error scaled by precision; segment claims "they coincide up to scaling" — accurate.

**4. What direction will the theory take next?** Excitement: a clean derivation connecting the two mismatch forms ($\delta_t$ in observation space, $\tilde \delta_t$ in tangent space $T_M \mathcal M$) under a broader class than just Gaussian. Useful because downstream segments will need the mapping. Disappointment: if $\tilde \delta_t$ is mentioned but never actually used in downstream derivations (dangling formalism). The notation foreshadows information-geometric machinery; whether it's actually used is the test.

**5. What errors should I now watch for?** 
- Future segments that conflate $\delta$ and $\tilde \delta$ without specifying which space they're in.
- Claims that "low $\delta$ = good model" without acknowledging the zero-aporia ambiguity (cases a/b/c here are clean — adequacy / confirmation bias / channel noise).
- The Mahalanobis normalization is footnoted in Discussion but not in the Formal Expression; downstream segments using $\Vert \delta \Vert$ should cite which norm.

**6. Predictions for next segments.** Row 18 = `result-mismatch-decomposition`. I expect a result decomposing $\delta_t$ into model-error and observation-noise components. Status:exact (it's listed in CLAUDE.md / now in CLAUDE-2.md as inevitability-core). Depends on def-mismatch-signal + likely GA-1 (fresh noise). Likely a bias-variance-style identity.

**7. What would I change?** Add `def-action-transition` to depends — root-cause fix for the F-A series. Also consider whether the Discussion's "TF-06's update rule writes $M_t = M_{t-1} + \eta \cdot g(\delta_t)$" is best as Discussion content or should be moved to a Working Notes provenance trail. Not a finding, just style.

**8. What am I now curious about?** The "zero-aporia ambiguity" framing — three cases for $\delta_t \approx 0$: (a) genuine adequacy, (b) confirmation bias, (c) channel-noise-too-high. Does this connect to detection-latency machinery? `#deriv-detection-latency` (per CLAUDE-2.md, recently added) gives $\Omega((n_{\min}+1)/\varepsilon)$ as the floor for within-class regime change with footprint $\varepsilon$. If $\varepsilon$ is small (case b — silent confirmation bias) or noise dominates (case c — deafness), detection latency blows up. The connection between zero-aporia ambiguity and detection-latency might be tighter than the segment surfaces.

Also curious: the "active testing" framing at the end of the Discussion ("choosing actions to generate informative aporia") points to CIY (#def-causal-information-yield). This is the agent fighting the case-b/c ambiguity by intervening. Worth tracking how strong that connection becomes.

**9. What new knowledge does this enable?** With $\delta$ defined formally, downstream becomes: mismatch dynamics ODE, sector condition, persistence, decomposition. With $\tilde \delta$, information-geometric treatments (Fisher metric, natural gradient). The combination enables both control-theoretic and information-theoretic routes to the same persistence-condition target.

**10. Should the audit process change?** The root-cause-realization move I just did (recognizing F-A0 → F-A2/3/5 via transitivity) is a useful audit move — surface root-causes when a pattern reaches 3+ instances rather than just listing instances. Worth noting as a self-discipline going forward: if 3+ instances of a finding-pattern, look for a single upstream cause.

**11. Outline updates for final report.** Section B should now have a *root-cause finding* for the F-A0 → F-A series rather than a flat enumeration. Re-shape:

```
F-A (root-cause): def-observation-function (Section I row 2) uses $a_{t-1}$ in 
   its Formal Expression but does not list def-action-transition in depends. 
   This drift propagates through form-agent-model (which depends on 
   def-observation-function but also doesn't carry def-action-transition) 
   and downstream into form-information-bottleneck, def-model-sufficiency, 
   def-mismatch-signal, and any segment whose action-symbol coverage 
   transits through def-observation-function. 
   Root-cause fix: add def-action-transition to def-observation-function's depends.
   
   Independent drifts not addressed by the root-cause fix:
   - F-A1: scope-adaptive-system missing def-chronica (row 4).
   - F-A4: form-event-driven-dynamics missing form-agent-model (row 14).
```

## Status-label / discipline

`status: axiomatic`, `stage: deps-verified`. Both appropriate — except (per F-A0 root-cause) the deps-verified stage is technically aspirational; the depends list is incomplete relative to Formal Expression usage.

## Cadence check

One Read → 11-prompt walk-through → reflection → next Read. Holding.

Next: Section I row 18 = `result-mismatch-decomposition`.
