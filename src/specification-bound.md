---
slug: specification-bound
type: result
status: conditional
depends:
  - temporal-optimality
  - feature-definition
  - software-scope
---

# Result: Specification Bound

The minimum time to implement a feature is bounded below by the time required to transmit enough information for the implementer to distinguish the intended feature from competing possibilities. Written specification and demonstration are special cases of this more general transmission bound.

## Formal Expression

*[Derived (specification-bound)]*

$$\forall \text{ feature } F: \quad \text{time}_{\min}(F) \geq \inf_{c \in \mathcal{C}_{\text{suff}}(F)} \text{time}_{\text{transmit}}(F, c, M_{\text{shared}})$$

where:
- $\mathcal{C}_{\text{suff}}(F)$ is the set of communication channels or transmission paths sufficient to convey feature $F$ to the implementer
- $M_{\text{shared}}$ is the context shared by specifier and implementer
- $\text{time}_{\text{transmit}}(F, c, M_{\text{shared}})$ is the time required for channel $c$ to transmit enough information, given that shared context

*[Derived (two-channel special case)]*

If the only admissible sufficient channels are written specification and demonstration, the general bound reduces to:

$$\text{time}_{\min}(F) \geq \min\!\big(\text{time}_{\text{specify}}(F, M_{\text{shared}}),\; \text{time}_{\text{demo}}(F, M_{\text{shared}})\big)$$

*[Derived (specification-time, first-order approximation)]*

$$\text{time}_{\text{specify}}(F, M_{\text{shared}}) \approx \frac{H_{\text{req}}(F \mid M_{\text{shared}})}{R_{\text{spec}}}$$

where:
- $H_{\text{req}}(F \mid M_{\text{shared}})$ is the residual information that must still be communicated once shared context is taken into account
- $R_{\text{spec}}$ is the effective information rate of the specification channel

Shared context acts as compression by reducing $H_{\text{req}}$, not by appearing as a free-standing divisor.

**Assumptions.** The feature $F$ is within #software-scope (non-negligible future change probability). A channel is "sufficient" if it transmits enough information for the implementer to produce the intended feature, not merely approximate it.

### Corollary: Communication as Bottleneck

*[Derived (communication-bottleneck)]*

As actual implementation time approaches $\text{time}_{\min}(F)$, communication speed and quality become the limiting factor.

This follows directly: if implementation overhead shrinks (for example, through automation or stronger tools), the remaining irreducible time is the cheapest sufficient transmission path. In many real settings that path is still dominated by communication and context-building.

## Epistemic Status

The bound's *existence* is *derived* from information theory: you cannot implement what has not been sufficiently distinguished from competing implementations, and that distinction requires transmitting enough residual information through some admissible channel. The general infimum-over-channels statement is the strongest version currently justified. The approximation $\text{time}_{\text{specify}} \approx H_{\text{req}} / R_{\text{spec}}$ is *first-order* — the actual relationship depends on channel characteristics, encoding efficiency, and interaction structure. Neither the exact form of $H_{\text{req}}$ nor the effective rate $R_{\text{spec}}$ is derived within ACT.

## Discussion

**Shared context as compression.** Domain-specific languages, established conventions, examples, and shared mental models reduce the residual information $H_{\text{req}}(F \mid M_{\text{shared}})$. "Make it like Twitter but for dogs" is an efficient specification only because the receiver already has a rich model of what "Twitter" implies. Without that context, the same feature would require far more transmission time.

**Specification is one channel among many.** Natural language requirements, demonstrations, examples, tests, partial implementations, and prior conventions are all candidate transmission paths. The lower bound is on the cheapest *sufficient* path, not specifically on prose. This is why showing a user a working prototype, giving a failing test, or pointing to an analogous feature can outperform a long written brief.

**Connection to ACT.** In ACT terms, the specification bound constrains how fast $O_t$ ( #objective-functional) can be communicated from specifier to implementer. Shared context corresponds to the overlap between specifier's $M_t$ and implementer's $M_t$. When this overlap is small, even a simple objective requires extensive specification.

*[Discussion]* This suggests that $M_t$ quality ( #agent-model) and observation infrastructure ( #code-quality-as-observation-infrastructure) are load-bearing for the specification bound: shared context built through good code (documentation, naming, structure) reduces specification time for future features. *This connection is structurally motivated but the quantitative relationship between code quality and specification time has not been empirically measured.*

**Empirical indication.** Putnam (1978) empirically discovered implementation time bounds that may approximate $t_{\min} \approx (\text{time}_{\text{specify}})^{3/4}$.
*[Empirical Claim — historical observation, not derived within ACT. The exponent 3/4 is Putnam's empirical finding, not a theoretical prediction.]*

## Working Notes

- The strongest next tightening would be to define "sufficient" more formally: e.g. the channel must reduce the implementer's posterior uncertainty over acceptable implementations below some task-dependent threshold. Right now sufficiency is intuitive rather than operationalized.
- This segment was written by an earlier agent with less context (noted in WORKBENCH). Needs a review pass during Section I/IV tightening — particularly to connect to the ACT communication framework ( #communication-gain) and to make the information-theoretic derivation more explicit.
- The $H_{\text{req}} / R_{\text{spec}}$ expression is still a first-order approximation. A tighter version would separate encoding efficiency, channel noise, and interactive back-and-forth — but that may be over-engineering for a bound that is primarily conceptual.
