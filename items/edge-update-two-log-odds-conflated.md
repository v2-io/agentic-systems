---
kind: item
owner: C.1
opened: 2026-10-31T02:15:11Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:hyp-edge-update-via-gain]
---

# #hyp-edge-update-via-gain conflates two log-odds coordinates (526815 F54/F55, checked at HEAD 4175aae7). Line 45 defines lambda_ij = log(p_ij/(1-p_ij)), the logit of the Bernoulli success probability p_ij. Line 49 updates it by l(y) = log[P(y | edge true)/P(y | edge false)], the likelihood ratio for the hypothesis that the edge is true. Those are the log-odds of two different propositions: success on a trial, and truth of the causal link. The conjugate Beta-Bernoulli update of line 43 is not additive in the logit of p_ij. Separately, eta_edge = U_edge/(U_edge + U_obs) (lines 31-34) divides a Beta variance in probability space by an observation-noise proxy with no common metric. Strengthen first: state which proposition the coordinate is about and derive the additive update for that one (#deriv-edge-update-natural-parameter's evidential-additivity axiom applies to the edge-truth hypothesis). Source: the segment's gold Follow-up (WN line 94), routed there as certified-track.
