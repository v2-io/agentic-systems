---
slug: disc-w1-structural-bound-boundary
type: discussion
status: robust-qualitative
depends:
  - der-class-coercion-via-wrapping
  - der-directed-separation
stage: draft
---

# Discussion: The W₁ Structural-Bound Boundary

The W₁ structural leakage bound of `#der-class-coercion-via-wrapping` exists if and only if the wrapped component carries no goal-correlated state across the call boundary (condition (C2′)); otherwise the goal-leak routes through a channel the wrapper cannot observe or condition on, and only a behavioral (W₂-type) bound remains. The discontinuity at the boundary is a *certifiability* discontinuity, not a behavioral one: the leakage itself is continuous — and quadratically flat — in the degree of (C2′)-violation, while what snaps at the boundary is the availability of the structural certificate.

## Formal Expression

### Setup: the two channels and the conditioning that distinguishes them

Recall from `#der-class-coercion-via-wrapping` that the W₁ regime issues a structurally goal-blind query $q_M$ to a black-box component $A$, then updates the wrapper belief $M_W$ from the response $A(q_M)$. Two distinct goal variables are in play: the wrapper's internal register $G_W$ (which $q_M$ structurally does not take as an argument; Theorem 1 closes this *processing* channel exactly), and the latent operator goal $G^{\text{op}}$ inferable from query content (the *selection* channel bounded by $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$). The structural bound is a property of the wrapper's query-selection policy because, under (C2′), $G^{\text{op}} \to q_M \to A(q_M)$ is a Markov chain — the goal can reach the response *only* through the query the wrapper chose.

### The no-go: statefulness reopens an unobservable channel

*[Discussion (w1-structural-bound-no-go)]*

Drop (C2′). Let $A$ carry hidden state $S$ — a conversation KV-cache, a retrieval buffer, adaptive context — that is correlated with $G^{\text{op}}$ through shared history (e.g. a prior goal-conditioned call in the same macro-step touched $S$). Then the response can depend on the goal *through $S$*, and this dependence survives conditioning on the query:

$$I\big(A(q_M);\, G^{\text{op}} \,\big\vert\, q_M\big) \;\ge\; 0, \qquad \text{and generically } \gt 0 \text{ when } S \not\perp G^{\text{op}}.$$

Conditioning on $q_M$ no longer closes the path, because the leak does not flow through $q_M$ — it flows through $S$. The conditioning that *would* close it, $I(A(q_M); G^{\text{op}} \mid q_M, S) = 0$, is unavailable to any wrapper-level analysis: $S$ is internal to the black-box oracle and the wrapper cannot observe or condition on it. The Markov chain $G^{\text{op}} \to q_M \to A(q_M)$ is broken — there is now a second edge $G^{\text{op}} \to S \to A(q_M)$ that bypasses the query — so the data-processing argument that yields $\kappa_{W_1}^{\text{sel}} \le I(q_M; G^{\text{op}})$ no longer holds.

**No-go statement.** For a component carrying goal-correlated cross-call state, *no bound on the belief-channel goal-leakage is derivable from the wrapper's query-selection policy alone.* The structural W₁ bound is available if and only if (C2′) holds. When (C2′) fails, the leak flows through an unobservable, unconditionable channel, and only a *behavioral* bound — estimated by monitoring $I(A(q_M); G^{\text{op}} \mid q_M)$ in the responses — remains, exactly as in the W₂ regime and for the same structural reason (an unconditionable goal-correlated channel). This locates the structural-versus-behavioral split not only in *wrapper design* (where to place the separation commitment — the W₀/W₁/W₂ regime choice) but *also* in a *component property*: statefulness across the call boundary forces a behavioral-only bound regardless of how the wrapper is built. The condition is sharp — it is not online weight-adaptation that breaks the structural bound (a frozen-weights LLM adapts nothing) but mere goal-correlated state persistence across the call boundary, which a frozen-weights LLM with a conversation cache exhibits.

### The discontinuity is in the certificate, not in the behavior

The boundary at (C2′) is best read as a *certifiability* discontinuity. Parameterize the (C2′)-violation by $\varepsilon$, the goal-correlation retained in the cross-call state ($\varepsilon = 0$ is exact statelessness-about-the-goal; $\varepsilon \gt 0$ is a sliver of goal-correlated memory). Two facts hold at the boundary, and they point in opposite directions:

- **The behavior is continuous.** The actual goal-information reaching the belief is a continuous function of $\varepsilon$ through $\varepsilon = 0$ — no jump, no threshold. Two wrappers differing only in $\varepsilon$ leak amounts that differ by an amount shrinking with $\varepsilon$; they cannot be told apart by watching their belief updates.
- **The certificate's validity is a step.** At $\varepsilon = 0$ the design-side certificate — *the goal is not in the query, the component is stateless about the goal, therefore the belief update cannot see the goal* — is true. At any $\varepsilon \gt 0$ that same certificate is still computable and still asserts the same thing, but is now *false*: the real leak is positive and took the unobservable path. The certificate's *value* (a flat selection-channel reading of $0$ under goal-blind selection) is continuous across the boundary; its *truth* is the step function. Once $\varepsilon \gt 0$ the only honest instrument is behavioral monitoring.

So the wall is in the epistemics, not in the world: the leakage the structural certificate would have bounded is continuous in the (C2′)-violation, and the discontinuity is in what is *provable*, not in what the agent *does*. This pre-empts the natural objection — *surely a tiny bit of state can only leak a tiny bit?* — by agreeing with it and relocating the bite: the leak is indeed tiny, but the structural guarantee is gone entirely.

### What is solid versus suggestive

Two parts of the picture are exact and carry the no-go:

1. **The behavioral identity at the limit.** At exact statelessness-about-the-goal the structural certificate's zero reading is the truth (the leak is zero); the Markov chain holds and $\kappa_{W_1}^{\text{sel}} \le I(q_M; G^{\text{op}})$ is valid.
2. **The certificate-validity step.** The structural certificate is available iff (C2′) holds; at any (C2′)-violation it asserts a false zero and only the behavioral monitor remains valid. This is forced by the unobservability of $S$ and does not depend on the magnitude of the violation.

What is *suggestive but not proven in general* is the global *continuity-and-flatness* of the leakage past the boundary. In an exact-enumeration toy (single bit, single call, a state-bends-the-answer mechanism) the leak is monotone, smooth, and $\Theta(\varepsilon^2)$ — flat to first order — throughout the violation range. That is moderately strong evidence for the continuity reading and against a behavior-discontinuity reading, but it is a deliberately simple toy: a component whose retained state *amplifies* (state that controls the response gain, or multi-step accumulation across many calls) could in principle exhibit super-linear or threshold leakage, and that is not ruled out. The continuity claim is therefore stated as *robust qualitative* — the certifiability step is the exact load-bearing content; the smoothness of the leak past the boundary is the toy-suggested, not-fully-general, companion.

## Epistemic Status

*Robust qualitative.* The no-go itself — *the structural W₁ bound is available iff (C2′) holds; under goal-correlated cross-call state the belief-channel leak is unconditionable at the wrapper level and only a behavioral bound remains* — is exact: it follows directly from the unobservability of the component's internal state $S$ and the consequent breaking of the $G^{\text{op}} \to q_M \to A(q_M)$ Markov chain. The certifiability-discontinuity framing (behavior continuous, certificate-validity a step) rests on (a) the exact behavioral identity at the (C2′) limit and (b) the certificate-validity step, both solid. The *general* continuity-and-flatness of the leakage in the degree of (C2′)-violation is *suggestive, not proven*: it is exhibited cleanly in an exact-enumeration toy ($\Theta(\varepsilon^2)$ flatness), but a component with an amplifying state mechanism could in principle break smoothness, and that case is not closed. Hence the segment as a whole sits at robust qualitative rather than exact: the boundary's *existence and location* are exact; the boundary's *shape past it* is qualitatively characterized.

Max attainable: robust qualitative for the continuity-shape claim absent a general continuity proof; the no-go's existence-and-location is already exact.

## Discussion

**Why this is a sharpening, not a softening, of W₁.** The W₁ regime's structural guarantee is not undercut by this boundary — it is given a precise domain of validity. Theorem 1 of `#der-class-coercion-via-wrapping` (exact directed separation under (C1)–(C3)) is untouched; the selection-channel bound is untouched within (C2′). What this segment adds is the honest statement of *when the structural bound stops existing* and *what replaces it* (a behavioral bound), together with the recognition that the replacement is forced by a component property orthogonal to wrapper design. A no-go with an explicit boundary characterization is more useful than a structural bound asserted without a stated domain.

**Practical reading.** The $\Theta(\varepsilon^2)$ flatness of the toy carries a counter-intuitive design implication: a near-stateless component is *operationally* almost as safe as an exactly-stateless one (a little cross-call memory leaks very little goal-information), but it is *certificationally* not safe at all (the structural guarantee is lost entirely the instant statelessness fails). The value of enforcing exact (C2′)-statelessness across the call boundary is concentrated almost entirely in what it lets you *prove*, not in the marginal leakage it prevents. When deciding whether the engineering cost of true call-boundary state-resetting is worth it over "mostly reset," the thing being bought is a proof, not a meaningful behavioral delta.

**Relation to the Class 2 sub-typology.** This boundary is the agent-level companion to the $\Sigma$-channel observation in `#disc-partial-coupling-pathways`: a $\Sigma$-source coupling in a stateful component can undermine W₁'s structural commitment via strategy-context that persists across calls, which is precisely a (C2′)-violation. The sub-typology names the component-internal form of the coupling; this segment names the call-boundary condition under which W₁'s structural certificate survives it.

**Relation to the action-side bounded-signaling assumption.** The unobservable-channel structure here is the belief-side twin of the action-side bounded-signaling assumption named in `#der-directed-separation` — both are "a goal-correlated channel the formalism does not see." Whether they are the same phenomenon viewed from two sides is left open.

## Findings

### The W₁ Structural-Bound Boundary (Certifiability Discontinuity at (C2′))

**Brief:** Imagine a scaffold that keeps a language model honest about its beliefs by only ever asking it goal-blind questions — "summarize this diff," never "summarize this diff so we can ship the fix." The promise of strict wrapping (W₁) is that you can *certify from the design alone* that the operator's goal cannot bend the belief update: the goal is structurally not an input to the belief-side query. That promise holds exactly when the component forgets everything about the goal between the goal-blind question and the goal-conditioned one. The moment the component keeps a sliver of goal-touched memory across that boundary — a conversation cache, a retrieval buffer — the goal can sneak into the answer through the memory, on a path the scaffold cannot see, and the design-side certificate becomes false even though it still computes the same reassuring number. The striking part is *how* it fails: the actual amount of goal that leaks is continuous and, near the boundary, quadratically tiny — you can get a near-stateless component arbitrarily close in behavior to a stateless one. What snaps, all-or-nothing, is not the behavior but the *provability*: you lose the entire structural guarantee for an almost-invisible behavioral cost. You were buying a proof, not a meaningful safety margin.

**Impact:** Locates the structural-versus-behavioral leakage split of `#der-class-coercion-via-wrapping` in a *component property* (goal-correlated cross-call statefulness) independent of wrapper design, complementing the W₀/W₁/W₂ regime choice that locates it in wrapper construction. Promotes the $\Sigma$-channel-suppressed-W₁ Working Note of the wrapping segment to a named, load-bearing condition (C2′) and gives the precise reason it is needed. Frames the no-go as a certifiability discontinuity — sharpening the CS-norm practice of characterizing *what kind* of boundary a no-go draws — and supplies the practical corollary that exact call-boundary statelessness buys a certificate, not a behavioral delta.

**Novelty Claim:** *Claim recognition* that the W₁ structural leakage bound's availability is governed by a sharp component-side condition (no goal-correlated cross-call state), with the boundary characterized as a discontinuity in the *validity of the structural certificate* rather than in the agent's leakage behavior — the leakage being continuous, and second-order flat, in the degree of condition-violation.

**Related Work:**
- Cover & Thomas, *Elements of Information Theory* (2nd ed., 2006), data-processing inequality (published 2006, found 2026-05-31) — *formal antecedent* — the DPI along $G^{\text{op}} \to q_M \to A(q_M)$ is what holds under (C2′) and breaks when an unobservable $S$ adds a bypassing edge.
- Pearl, *Causality* (2nd ed., 2009), d-separation / unobservable-confounder structure (published 2009, found 2026-05-31) — *adjacent literature* — the broken-Markov-chain reading (a hidden $S$ confounding $G^{\text{op}}$ and $A(q_M)$ that the wrapper cannot condition on) is the causal-graph idiom for the no-go.

**Search Log:**
- 2026-05-31 (*intuition-only*): No dedicated literature search for the certifiability-discontinuity framing as such; the underlying tools (DPI, unobservable-confounder structure) are standard and cited. A targeted search for prior art on "certifiable goal-blindness under stateful components" / structural-vs-behavioral verifiability boundaries in scaffolded-agent design has not been conducted.

## Working Notes

- Reasoning trail: the correction that produced this no-go is `spikes/spike-w1-leakage-vacuity-2026-05-31.md` (§4 the embedded no-go; §3 the corrected selection-channel bound it sharpens); the certifiability-discontinuity framing and the exact-enumeration toy exhibiting the $\Theta(\varepsilon^2)$ flatness are in `spikes/spike-w1-w2-boundary-intuition-2026-05-31.md` (companion sim `spikes/sim-w1-w2-boundary.py`).
- **Open: amplifying-state mechanisms.** The general continuity-and-flatness of the leak past the boundary is toy-suggested, not proven. A component whose retained state controls the response gain, or accumulates across many calls, could exhibit super-linear or threshold leakage. Closing this would lift the continuity-shape claim from robust qualitative toward exact; it connects to the M4 "amplification under high component fidelity" thread in `#disc-modularity-state-dynamics` and the accuracy-vs-inference-effect decomposition in `#der-class-coercion-via-wrapping` §Discussion "Two senses of component competence."
- **Open: behavioral-monitor construction.** Past the boundary only the behavioral bound $I(A(q_M); G^{\text{op}} \mid q_M)$ remains; constructing a consistent estimator for it (and for the latent $G^{\text{op}}$ it conditions on) is the same open follow-on as the $\hat\kappa_{\text{processing}}$ estimator of `#der-directed-separation` and the decomposed-estimator spike candidate recorded in `#der-class-coercion-via-wrapping` Working Notes.
