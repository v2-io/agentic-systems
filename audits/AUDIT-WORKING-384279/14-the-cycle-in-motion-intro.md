# 14 — the-cycle-in-motion-intro

*Type: discussion. Status: discussion-grade. Stage: draft. Chapter intro for Ch.3.*

## Predictions vs evidence
Predicted: transitional prose previewing event-driven dynamics. Found: that, plus three math previews ($\eta^\ast = U_M/(U_M+U_o)$, $\mathcal{T} = \sum_k \nu^{(k)}\eta^{(k)\ast}$, $\|\delta\|_{ss} = \rho/\mathcal{T}$).

## **Convention articulation — partial resolution of candidate finding #2**
Line 40 of this segment **explicitly articulates the Pearl-as-external-import convention**:
> "CIY uses Pearl's $do(\cdot)$ notation — an external import (Pearl 2009; Bareinboim, Correa, Ibeling & Icard 2022; AAT's recapitulation lives at #def-pearl-causal-hierarchy in Part II Ch.2, where the framework deploys the hierarchy as machinery rather than referencing it as vocabulary)."

This means scope-agency's choice to use $do(\cdot)$ without declaring `def-pearl-causal-hierarchy` in `depends:` is *consistent with an articulated convention* — Pearl is external; the AAT segment is invoked when AAT-specific deployment matters, not just when do-operator is used.

**Update to candidate finding #2:** No longer a dep-graph violation. But the convention is only articulated here, in a chapter intro at Ch.3. **The residual finding is meta-documentation:** this convention should appear in FORMAT.md or in the segment that uses do-operator first (scope-agency), not solely in a downstream chapter intro. Severity: low. Disposition: editorial — lift the convention statement upstream.

## Math previews — verification (quick)
- $\eta^\ast = U_M / (U_M + U_o)$ — Bayesian update under Gaussian uncertainties. Standard. ✓
- $\mathcal{T} = \sum_k \nu^{(k)} \eta^{(k)\ast}$ — additive sum of channel-wise corrected rates. ✓
- $\|\delta\|_{ss} = \rho/\mathcal{T}$ — steady state of the linear ODE $\dot\delta = -\mathcal{T}\delta + \rho$ at $\dot\delta = 0$. ✓

## Prose-coherence
- "Chapter 2 left us with a static picture" (line 16) — uses Chapter terminology consistently. No Section drift here.
- "two things follow immediately... Both feel obvious in hindsight; both are *derived*, not chosen" (line 18) — this is good methodological flagging. The segment is identifying which forthcoming claims are derived from completeness vs which are independent choices.
- Working Notes line 48 records the 2026-05-12 relocation of def-pearl-causal-hierarchy from Part I Ch.1 to Part II Ch.2 with motivation. Useful archaeology.

## Watch list
- The "two derivations from completeness" framing (line 18) names der-recursive-update + der-action-selection as joint consequences of form-agent-model's completeness clause. Verify when I reach those derivations.

## Next-segment predictions
`#form-event-driven-dynamics`. Will introduce the event-driven substrate $\mathcal{E} = \{(e_i, \tau_i)\}$, event rates $\nu^{(k)}$, model-state at event boundaries $M_{\tau^-}$, $M_{\tau^+}$. Will be foundational, status probably formulation or axiomatic.

## What I'd change
Lift the Pearl-as-external-import convention upstream — either into FORMAT.md's reference-handling section or into scope-agency directly. A fresh reader walking OUTLINE order encounters do-operator in scope-agency without the convention being articulated; they need to wait until this Ch.3 intro to see the framework's stance made explicit.

## Wandering thoughts (brief)

**On the 2026-05-12 relocation history.** The fact that this segment's Working Notes records the relocation — and explains *why* the CIY-placement paragraph changed from apologetic to declarative — is exactly the kind of cross-cycle handoff documentation Joseph's CLAUDE.md commits to. A future agent walking the corpus and wondering "why is Pearl-hierarchy in Part II instead of Part I" has the answer right here. Good record.

**On the linear-ODE-as-heuristic-preview.** The chapter intro's commitment to "we'll use the linear ODE as preview, then generalize via sector condition in Ch.4" is methodologically clean — the framework is naming where its pedagogy and its rigor diverge. The linear ODE is for reading; the sector condition is for proving.
