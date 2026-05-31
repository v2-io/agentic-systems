# 15 — form-event-driven-dynamics

*Type: formulation. Status: robust-qualitative. Depends: [post-causal-structure, def-observation-function, def-action-transition, form-agent-model].*

## Predictions vs evidence
Predicted: event-stream substrate with rates $\nu^{(k)}$, $M_{\tau^-}$/$M_{\tau^+}$ pre/post-event states. Found: that, plus event-information-content $\mathcal{I}(e_\tau) = I(e_\tau; \Omega_\tau \mid M_{\tau^-})$ and channel-specific observation uncertainty $U_o^{(k)}$.

## Math verification
- $\mathcal{I}(e_\tau) = I(e_\tau; \Omega_\tau \mid M_{\tau^-})$ — well-typed conditional MI. ✓
- $\nu_\text{eff} = \sum_k \nu^{(k)} \eta^{(k)*}$ — additive over channels. ✓
- Note: $\nu_\text{eff}$ is introduced here as the name of the sum but immediately said to be "identical to adaptive tempo $\mathcal{T}$" (line 67). Two names for the same thing — small wartiness but not a finding.

## Prose-coherence
Clean. Software-channels table (line 71-79) is a nice domain instantiation but doesn't carry an AAT-internal claim. The cross-component TST-side note at line 80 explicitly defers the three-part tempo decomposition to 02-tst-core.

## Cross-segment consistency
Forward-refs `#def-mismatch-signal`, `#def-adaptive-tempo`, `#emp-update-gain`, `#der-recursive-update`. All coherent. The line 51 statement that "discrete-time form $M_t = f(M_{t-1}, o_t, a_{t-1})$ from #der-recursive-update is a special case" previews the next segment.

## Watch list
- The "$M_{\tau^-}$ / $M_{\tau^+}$" notation introduced via the event-information-content uses $M_{\tau^-}$ (model just before event). NOTATION.md preserves this. ✓
- Small redundancy: $\nu_\text{eff}$ vs $\mathcal{T}$. Pick one canonical symbol going forward — likely $\mathcal{T}$ per NOTATION.md.

## Next-segment predictions
`#der-recursive-update`. The first of the "two derivations from completeness" (per the chapter intro line 18). Will derive that the update from $M_{\tau^-}$ to $M_{\tau^+}$ depends *only* on prior model + incoming event. Status likely robust-qualitative or exact.

## What I'd change
The two-symbols-for-one-quantity ($\nu_\text{eff}$ + $\mathcal{T}$) is minor; lift to $\mathcal{T}$ throughout if the framework is decided.

## Brief wandering
The framework's commitment to event-driven dynamics rather than fixed-clock-tick is methodologically interesting. Most adaptive-control literature uses fixed time steps; AAT's choice to make event-rate first-class lets the framework span thermostats (slow events) through compiler-feedback (fast events) within one formalism. The cost is notational complexity (need to track $\nu^{(k)}$, $M_{\tau^-}$, $M_{\tau^+}$, etc.); the benefit is that the multi-rate generalization that real agents face is built-in rather than bolted-on.
