---
kind: item
owner: G.2
opened: 2026-10-30T21:21:17Z
opened-by: Claude Opus 5.5 (item rechecker, lane p-process)
concerns: [segment:deriv-mismatch-budget-attribution]
---

# spikes/spike-rho-additive-variance-strengthening-2026-04-24.md is held at spikes/ root with payload not in canon. Its variance-additive core has a canon counterpart: #deriv-mismatch-budget-attribution (landed 2026-08-22) carries an additive variance decomposition and its first-order attenuation reading. What canon does not carry is the spike's three multiplicative sub-structures (the Poisson-driven multiplicative-cascade regime, the large-deviation regime, and the third it names) and the appendix it recommended (#rho-decomposition, never written). Compare the spike against #deriv-mismatch-budget-attribution, land what is true and new at honest tier or set it aside with a reason, then file the spike.

Carried only by spikes/ROUTING.md's 'Next actions' item 4, a numbered line the tracker import did not take; ROUTING is being deleted.

Source added 2026-10-30 by Claude Opus 5.5 (spike drain fork A), after reading spikes/spike-rho-additive-variance-strengthening-2026-04-24.md §§1-6 against #deriv-mismatch-budget-attribution and #internal-external-decomposition at HEAD. Most of the payload is superseded by canon; one piece becomes a canon defect, now its own item.
- (AV), §2, should not land, and re-landing it would be a regression. As defined, rho*^2 + Delta_M^2 + Delta_pi^2 already telescopes to rho^2 exactly, so the extra 2 chi double-counts and the 'theorem' is either a definitional identity or wrong. Canon's corrected form, #deriv-mismatch-budget-attribution Prop 1 and Cor 1a, says the policy is the measure, 'not a fourth term'. The PID-rho refinement (§3.3) refines a cross term canon shows does not exist, and the multiplicative-noise note (§3.4) is a coordinate remark. Both are set aside.
- The §4.1 no-go rests on a false premise: the Bayes-optimal innovation variance depends on process and observation noise separately (P* + R from the Riccati fixed point), not only on their sum. Its conclusion (no single scalar environmental volatility) is canon, by a different argument, at #internal-external-decomposition:59.
- The §3.1 multiplicative-cascade regime is exact arithmetic (independent Poisson thinning, Kingman 1993 ch. 2), and with no channel floor it is a counterexample to the no-go as canon states it. That defect is item:internal-external-decomposition-59-states-the-co (C.1), which also carries the exact separability criterion and the policy-invariant exception.
- The §3.2 tail regime is the classical contraction principle for sums of independent contributions, so it needs the independence that canon's Prop 1 denies in general. Set aside unless a client needs tail diagnostics.

Suggested disposition, for a second mind to confirm: close this item once the C.1 item is taken, and file the spike to spikes/.archived/ with this reason (its no-go conclusion is canon by another route; its (AV) is correctly superseded).
