# 16 - der-recursive-update

Segment: `01-aat-core/src/der-recursive-update.md` (`#der-recursive-update`)

Dependencies: `form-agent-model`, `form-event-driven-dynamics`, and appendix `deriv-recursive-update`, all read by this point. The appendix dependency was handled via the appendix-back-pointer exception, though I noticed it after pulling the main segment into context.

## Segment Read

This main-section segment states the result backed by the appendix: model updates must be recursive, $M_{\tau^+}=f_M(M_{\tau^-},e_\tau)$, and between events the model evolves autonomously, $dM/d\tau=g_M(M_\tau)$. It gives the reader-facing explanation and leaves the full uniqueness proof to the appendix.

The segment also introduces `epistrophe` as the corrective turning toward reality, but I will wait for the cycle-phase defining context before voting on that term.

## Predictions Vs Evidence

I predicted a recursive-update result after event-driven dynamics. This is exactly the next move. The surprise is that the segment already points toward consolidation dynamics and stability-plasticity, which are downstream and not yet votable for me.

## Cross-Segment Consistency

The main segment and appendix are consistent. The main segment's status is `conditional`, while the appendix status is `exact`; the main Epistemic Status says "Exact, with a partly definitional character." That mismatch may be intentional because the main segment includes event-driven and finite-agent claims not fully exact, but it is a small status-label ambiguity. For naming, it does not affect the term.

## Naming Notes

`recursive update` is a strong keep. It is the standard name for the update form and remains accurate whether the update is event-driven or serial-discrete.

`event-driven update` is a useful subphrase for the displayed form, but not a replacement. `Between-event dynamics` is descriptive and likely worth keeping if targeted.

`epistrophe` should not be voted from this segment alone, even though the gloss is beautiful; the cycle vocabulary should be judged as a set.

## What This Enables

The recursive update form makes update gain local: gain modulates a single-step correction from current model plus new event. It also enables mismatch dynamics and later consolidation as autonomous or pseudo-event-driven evolution between observations.

## Watchlist

- Whether card targets distinguish main result `recursive update` from appendix `recursive update derivation`.
- Whether `f_M` gets a prose alias; it is the update function, but "epistemic update function" may be more precise once $G_t$ exists.
- Whether consolidation terms are defined later rather than inferred from this passing reference.

## Wandering Thoughts

The main/appendix split works well here. The main segment says the result in a way a reader can carry forward; the appendix carries the burden of proof and counterexample handling.

For naming, this is a case where the current term is enough. "Recursive update" is not especially memorable, but it does not need to be. The memorable term in this neighborhood is probably `epistrophe`, which names the cycle phase rather than the function form.

The status mismatch between main and appendix is worth remembering as a process observation. It may be harmless, but fresh readers will notice if one file says conditional and the other says exact. Names cannot fix that, but clean derivation-audit conventions can make it less confusing.

I also see why `f_M` will need a precise alias. Once $G_t$ and strategy updates arrive, "update function" alone may be ambiguous. The subscript already says model/epistemic; prose should probably follow.
