# 86 - impl-unity-communication

Source: `01-aat-core/src/impl-unity-communication.md`

## First-pass understanding

This chapter-end segment is a catalog and synthesis layer for unity, shared intent, Auftragstaktik, and communication gain. Its strongest contribution is architectural: it names Ch.3 as the bandwidth/trust layer between composition closure machinery and later cooperative/adversarial coupling. That is a useful map of the framework.

The risk is status amplification. Several component segments were explicitly discussion-grade or hypothesis-grade, with unresolved metric, IB, allocation, and trust-denominator assumptions. This implications segment sometimes preserves those caveats, but elsewhere restates the sharper predictions as if the chapter has established them: structural monotonicity beyond linear-Gaussian examples, absolute bandwidth ordering, Conway's Law as a consequence, signed coupling as direct trust uncertainty, and cross-domain prescriptions for AI teams.

## Diagram attempt

I drew the chapter as a synthesis funnel. Unity, shared intent, Auftragstaktik, and communication gain enter with caveat tags; the synthesis layer can organize them, but it cannot remove the tags. The diagram highlights the burden: implications should preserve epistemic status rather than laundering local hypotheses into global framework results.

## Findings and watches

- F173 candidate: `impl-unity-communication` sometimes promotes caveated component claims into chapter-level predictions. A discussion synthesis can catalog implications, but it should preserve the proof status of unresolved unity metrics, IB encoders, bandwidth ordering, and additive trust gain.
- F174 candidate: the claim that structural monotonicity "survives more broadly" than the linear-Gaussian closure mapping still needs conditions. For arbitrary update rules and projections, monotonicity in `U_f` is not established by the worked Kalman case alone.
- F175 soft candidate: the heterogeneous-optimizer ensemble example is suggestive but under-specified. "Same content, different structural unity" needs a metric showing equivalent content while update machinery differs; different optimizers/schedules can also change learned content.
- F176 candidate: the Auftragstaktik discussion repeats `B_O > B_Sigma > B_M`, "most closure-defect reduction comes from a small objective-sharing investment," and Conway's Law as a consequence. These inherit F162-F165 and should remain marginal/conditional, not absolute or derived.
- F177 candidate: mapping cooperative coupling `gamma < 0` to `U_align -> 0` and adversarial coupling `gamma > 0` to large `U_align` is too direct. Coupling sign, objective alignment, observed source reliability, and receiver uncertainty about alignment are related but not identical variables.
- F178 soft candidate: the risk-asymmetric trust story needs an explicit loss function and evidence model before deriving "high-trust relationships build slowly and break quickly." Conservative quantiles are decision-policy choices, not consequences of the reliability posterior alone.
- F179 candidate: the cross-domain prescription that flat trust models systematically trust unreliable sources too much in low-stakes regimes and too little in high-stakes regimes does not follow from the displayed communication-gain formula without a risk/loss layer.
- F180 soft candidate: "the priority ordering is structural, not contingent" overstates the result. The segment itself notes regime reversals; the structural claim should be conditional on local observability, change rates, entropy, and communication costs.
- F181 watch: the segment imports later chapter claims (`der-team-persistence`, `der-adversarial-destabilization`, `deriv-strategic-composition`, identifiability-floor instances) as synthesis context. Keep these as forward references until the AAT outline reaches their homes.

## Local verdict

The chapter map is useful, but its final form should clearly tag each implication with the status of the weakest component it depends on. The clean mental model is "bandwidth/trust synthesis layer," not "proof that the chapter's qualitative predictions now hold."

