# Reflection 15 — der-gain-sector-bridge (Section I row 24)

Trying to preserve more thinking-trail this round.

## §4.2 dependency check — F-C3 and F-C4

Walking through depends as I read the frontmatter: `[emp-update-gain, def-mismatch-signal, deriv-sector-condition, deriv-gain-sector]`. Two of these are Appendix A — both downstream of where I am in OUTLINE.

So this segment triggers two F-C critical findings simultaneously: F-C3 (deriv-sector-condition) and F-C4 (deriv-gain-sector). 

Realization mid-walking: every Section I derived/result segment with an appendix derivation will trigger this. So far: der-recursive-update (F-C1), hyp-mismatch-dynamics (F-C2), now der-gain-sector-bridge with TWO. Likely upcoming: result-sector-condition-stability, result-persistence-condition, result-structural-adaptation-necessity each will probably point to deriv-sector-condition or some other Appendix A segment.

This is going to be many many F-C instances. The honest move for the report is *not* to enumerate them as separate findings but to surface the *architectural pattern* once. The report's Section B should have something like: "F-C: Appendix-A-back-pointer pattern. Section I/II/III result segments routinely list Appendix A derivations in their `depends:`, even though Appendix A comes after Sections I-III in the OUTLINE walk. Strict reading of §4.2 makes each instance a critical finding; pragmatic reading recognizes the convention. Either the OUTLINE row order should be revised (move Appendix A derivations upstream of the segments that depend on them, which would make Appendix A read as 'context for what follows' rather than as 'proofs of the foregoing'), or §4.2's verification target should explicitly accept appendix-back-pointers as a recognized exception. This is an architectural decision for Joseph to make, not the audit."

I'll keep noting individual F-C instances briefly to maintain the count, but I won't expand them into full burden-of-proof writeups anymore. The pattern is clear at N=4.

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted (from reflection 13's "predictions for next segments" through 14): "der-gain-sector-bridge connects gain principle to sector condition. Likely depends emp-update-gain, def-mismatch-signal, deriv-sector-condition. Third dep would be Appendix A → F-C-class finding." Verification: ✓ all correct. Plus a fourth dep on deriv-gain-sector that I didn't predict — that one is also Appendix A, so two F-C instances at once. Better than expected on the F-C prediction (the segment is more F-C-rich than I anticipated).

**2. Cross-segment consistency.** This is where it gets interesting. The "(PI) parameterization-invariance" subsection late in the segment is *the* place where the recently-added (2026-04-23 per CLAUDE-2.md) (PI) axiom propagates into a Section I derivation. The propagation upgrades two Verified Instance rows (matrix-Kalman and exponential-family-natural-parameters) from "derived (conditional on inner-product choice)" to "derived (AAD-internally forced)." Cross-refs to #disc-additive-coordinate-forcing place this as the metric-layer instance of the meta-pattern.

This is exactly what §5.2 ("cross-segment consistency around recent additions") prescribes watching. The propagation lands here cleanly. ✓

**3. Math verification.**
- Bridge: $\alpha = \eta^* \cdot c_{\min}$ where $c_{\min} = \inf [\delta^T H g(\delta) / \|\delta\|^2]$. If B1 says the inner product is bounded below by $c \|\delta\|^2$, then the sector parameter is $\eta^* c$. Trivial. ✓
- Gradient equivalence: $\alpha = \eta \cdot \mu$, $\mu = \inf \lambda_{\min}(\nabla^2 L)$. Standard convex-optimization result for gradient descent on $\mu$-strongly-convex losses. Contraction rate $\eta\mu$ near the optimum. ✓
- The basin-radius $R$ as the convexity radius of $L$ is correct.

The (PI) / Čencov subsection: under (PI), Fisher metric is uniquely forced on statistical-manifold sub-cases of $M_t$. The matrix-Kalman case in Fisher-metric-form removes the $\kappa(P^-)$ Euclidean-transfer penalty. Sounds right structurally — Fisher metric is the "natural" inner product on a statistical manifold and Čencov's theorem says it's the unique invariant one. I'll spot-check Čencov when I do citation verification.

**4. What direction next?** Excitement: the Appendix A derivations themselves (deriv-sector-condition, deriv-gain-sector) — these are the load-bearing proofs that the bridge is delegating to. Reading them out of OUTLINE order (F-C-class issue) means I'll see the proofs after the result; that may give me a different vantage. Disappointment: if the sub-scope α/β partition's coverage gap (β = PID, rule-based, variational, etc.) is too large for the framework to apply meaningfully to important agent classes (LLMs are arguably in β).

**5. What errors should I now watch for?**
- Future segments using GA-3 / sector condition without acknowledging the sub-scope α vs β distinction. The whole point of this segment is to ground GA-3 *for sub-scope α* — claiming GA-3 holds universally would be a finding.
- The (PI) adoption is conditional. Under non-adoption, Fisher-metric cases stay Euclidean-with-penalty. Future segments asserting Fisher-metric statements as if forced without flagging (PI) = finding.
- The B1 directional fidelity assumption — if any segment treats it as automatic (rather than as a constraint that excludes pathological updates) = finding.

**6. Predictions for next segments.** Row 25 = `result-sector-condition-stability`. The Lyapunov persistence theorem. Probably status:claims-verified, depends `[deriv-sector-condition, hyp-mismatch-dynamics, ...]` — at least one Appendix A back-pointer → F-C5.

**7. What would I change?** The "Verified Instances" table is a great pedagogical device — concrete agent classes with their derived sector parameters. The sub-scope α/β partition is honest. The (PI) subsection is well-structured. I'd consider one small change: making the F-C-class issue (depends listing deriv-sector-condition + deriv-gain-sector while these are downstream) more visible by adding a brief Working Notes line about the convention. But that's a documentation move on the framework's part, not a content fix.

**8. What am I now curious about?**

The α/β partition is the framework's main scope-honesty move at the persistence-machinery level. Sub-scope α: Bayesian + gradient-on-strongly-convex + variants. Sub-scope β: PID, rule-based, variational, severely-misspecified, non-convex-beyond-basin, per-step-SGD. Logogenic agents (LLMs) — where do they sit? They're variational-ish (transformer attention as approximate posterior over latent states is a stretch but not unreasonable) and potentially severely-misspecified relative to the world. So they'd land in β. That means GA-3 / sector condition / persistence machinery applies to LLMs only as a *posit*, not as a derived consequence. Worth tracking when I reach 03-logogenic.

Also curious: the failure mode FM-1 (directional infidelity, $\delta^T g(\delta) \leq 0$) — the segment says "for optimal Bayesian updates, B1 holds by construction" but offers a counterexample for "pathological update rules" without giving the counterexample. The "spikes/spike-a2-prime-strengthening.md" reference would have it; I can't read msc/ at this stage.

The "gain collapse → α → 0 → persistence fails" failure mode (FM-2) is the same agent pathology I noted in emp-update-gain. So FM-2 here = "gain collapse" in emp-update-gain Discussion = "stability-induced myopia" / detection-latency-blowup per CLAUDE-2.md priming. Multiple segments converging on the same pathology under different names. Section D (bigger-picture pondering) candidate: this pathology has multiple descriptions; should they be unified under a single name?

**9. What new knowledge enabled.**
- GA-3 grounded (not floating) for sub-scope α agents.
- Sub-scope α/β partition explicit — a key piece of scope-honesty per the framework's "epistemic architecture as distinctive contribution" reframe.
- (PI)-axiom-driven upgrade of Fisher-metric cases.
- α-T relationship structurally derived for the important cases.
- Bridge to discrete-time framework with Lipschitz constraint $c_{\max} < 2/\eta^*$.

**10. Should audit process change?** I think the F-C-class pattern can now be batched: just note instances in passing rather than expanding each. Going forward, when I hit an appendix-back-pointer dep, I'll log it as F-C(N) but not expand. The meta-finding is the audit's contribution; instance count is just the supporting evidence.

**11. Outline updates.** F-C count: 4 (F-C1 through F-C4). Section E (calibration): this segment lives up to inevitability-core — clean derivation, sub-scope honesty, (PI) propagation lands cleanly. Section D (bigger-picture pondering) candidate: gain-collapse / stability-induced-myopia / detection-latency-blowup are three names for what may be the same pathology; unification candidate.

## Status-label / discipline

`status: conditional` for the bridge theorem (conditional on B1 directional fidelity). Within-segment `*[Derived (...)]*` tags are tier-stratified honestly. `stage: draft` — interesting; the Epistemic Status is meaty, content is well-developed. Why draft? Maybe Gate 1 audit hasn't run since the (PI) addition. The F-C-class issues might be why it hasn't promoted further.

## Cadence check

Holding. Next: row 25 = `result-sector-condition-stability`.
