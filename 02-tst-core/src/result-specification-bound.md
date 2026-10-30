---
slug: result-specification-bound
type: result
status: conditional
depends:
  - post-temporal-optimality
  - def-feature
  - scope-evolving-software
stage: draft
---

# Result: Specification Bound

The minimum time to implement a feature is bounded below by the time required to transmit enough information for the implementer to distinguish the intended feature from competing possibilities. Written specification and demonstration are special cases of this more general transmission bound.

## Formal Expression

*[Derived (Conditional on S1–S2; specification-bound)]*

$$\forall \text{ feature } F: \quad \text{time}_{\min}(F) \geq \inf_{c \in \mathcal{C}_{\text{suff}}(F)} \text{time}_{\text{transmit}}(F, c, M_{\text{shared}})$$

where:
- $\mathcal{C}_{\text{suff}}(F)$ is the set of communication channels or transmission paths sufficient to convey feature $F$ to the implementer
- $M_{\text{shared}}$ is the context shared by specifier and implementer
- $\text{time}_{\text{transmit}}(F, c, M_{\text{shared}})$ is the time required for channel $c$ to transmit enough information, given that shared context

**Derivation.** Two premises:

- **(S1) Distinguishability premise.** The implementer reliably produces the *intended* feature $F$ — rather than some competing implementation consistent with what has been received so far — only if information sufficient to distinguish $F$ from the alternatives admissible under $M_{\text{shared}}$ has arrived through some channel $c \in \mathcal{C}_{\text{suff}}(F)$. "Reliably" excludes success by lucky guessing; a correct guess does not violate the bound in expectation, only in a lucky sample.
- **(S2) Temporal ordering.** Reliable implementation of $F$ cannot *complete* before that transmission completes: as long as distinguishing information remains untransmitted, some implementation decision remains underdetermined by everything the implementer has, so any completed artifact resolves it by chance rather than by intent.

Given S1–S2, any successful reliable implementation used some $c \in \mathcal{C}_{\text{suff}}(F)$ and took at least the transmission time of that channel; minimizing over admissible executions gives the infimum over the sufficient-channel set. The bound's existence therefore rests on S1–S2 (near-definitional unpacking of "intended" and "sufficient") plus the standard information-theoretic fact that distinguishing among alternatives requires receiving the distinguishing information; what is *not* derived is any closed form for the transmission time itself.

*[Derived (two-channel special case)]*

If the only admissible sufficient channels are written specification and demonstration, the general bound reduces to:

$$\text{time}_{\min}(F) \geq \min\!\big(\text{time}_{\text{specify}}(F, M_{\text{shared}}),\; \text{time}_{\text{demo}}(F, M_{\text{shared}})\big)$$

*[Formulation (specification-time, first-order approximation)]*

$$\text{time}_{\text{specify}}(F, M_{\text{shared}}) \approx \frac{H_{\text{req}}(F \mid M_{\text{shared}})}{R_{\text{spec}}}$$

where:
- $H_{\text{req}}(F \mid M_{\text{shared}})$ is the residual information that must still be communicated once shared context is taken into account
- $R_{\text{spec}}$ is the effective information rate of the specification channel

Shared context acts as compression by reducing $H_{\text{req}}$, not by appearing as a free-standing divisor.

**Assumptions.** The feature $F$ is within #scope-evolving-software (non-negligible future change probability). A channel is "sufficient" if it transmits enough information for the implementer to produce the intended feature, not merely approximate it.

### Corollary: Communication as Bottleneck

*[Derived (communication-bottleneck)]*

As actual implementation time approaches $\text{time}_{\min}(F)$, communication speed and quality become the limiting factor.

This follows directly: if implementation overhead shrinks (for example, through automation or stronger tools), the remaining irreducible time is the cheapest sufficient transmission path. In many real settings that path is still dominated by communication and context-building.

## Epistemic Status

The bound's *existence* is *derived*, conditional on the two named premises S1–S2 in the Formal Expression: you cannot reliably implement what has not been sufficiently distinguished from competing implementations, and that distinction requires transmitting enough residual information through some admissible channel. The conditions gating the `conditional` status are: (i) S1's notion of channel *sufficiency* is stated intuitively rather than operationalized (see Working Notes for the intended operationalization); (ii) the bound covers *reliable* implementation — success by lucky guessing is excluded by premise, not proved impossible. Within those conditions the general infimum-over-channels statement is the strongest version currently justified. The approximation $\text{time}_{\text{specify}} \approx H_{\text{req}} / R_{\text{spec}}$ is a *formulation*, not a derivation — a first-order modeling choice patterned on Shannon's entropy-over-rate form, exact only under a formalization (of $H_{\text{req}}$ as a conditional entropy and $R_{\text{spec}}$ as a channel capacity) that has not been carried out here. Neither the exact form of $H_{\text{req}}$ nor the effective rate $R_{\text{spec}}$ is derived within AAT. The Discussion's consequence for effort–schedule laws of Putnam's form, that they must fail under enough compression, is derived under one further condition, a sufficient transmission time that effort does not shorten; reading observed compression limits as this bound is a hypothesis.

## Discussion

**Shared context as compression.** Domain-specific languages, established conventions, examples, and shared mental models reduce the residual information $H_{\text{req}}(F \mid M_{\text{shared}})$. "Make it like Twitter but for dogs" is an efficient specification only because the receiver already has a rich model of what "Twitter" implies. Without that context, the same feature would require far more transmission time.

**Specification is one channel among many.** Natural language requirements, demonstrations, examples, tests, partial implementations, and prior conventions are all candidate transmission paths. The lower bound is on the cheapest *sufficient* path, not specifically on prose. This is why showing a user a working prototype, giving a failing test, or pointing to an analogous feature can outperform a long written brief.

**Connection to AAT.** In AAT terms, the specification bound constrains how fast $O_t$ ( #form-objective-functional) can be communicated from specifier to implementer. Shared context corresponds to the overlap between specifier's $M_t$ and implementer's $M_t$. When this overlap is small, even a simple objective requires extensive specification.

*[Discussion]* This suggests that $M_t$ quality ( #form-agent-model) and observation infrastructure ( #der-code-quality-as-observation-infrastructure) are load-bearing for the specification bound: shared context built through good code (documentation, naming, structure) reduces specification time for future features. *This connection is structurally motivated but the quantitative relationship between code quality and specification time has not been empirically measured.*

**Putnam's software equation.** *[Empirical Claim — Putnam's fit.]* Putnam (1978, "A general empirical solution to the macro software sizing and estimating problem," *IEEE Trans. Software Eng.* SE-4(4), 345–361) fitted project data to $\text{LOC} = C \cdot E^{1/3} \cdot t^{4/3}$, with $E$ the life-cycle effort, $t$ the development time and $C$ a "technology constant" that lumps tooling, process, team skill and domain familiarity. Solved for time, $t = (\text{LOC}/C)^{3/4} E^{-1/4}$: at fixed size and technology constant, time falls only as the fourth root of effort, so halving the schedule costs sixteen times the effort. The equation itself sets no floor; $t \to 0$ as $E \to \infty$. Putnam's minimum development time comes from a second empirical relation: the effort an organization can bring to bear grows no faster than $\lvert\nabla D\rvert\, t^3$, where the "difficulty gradient" $\lvert\nabla D\rvert$ is fitted for each class of system (Putnam 1978, "Example of an early sizing, cost and schedule estimate for an application software system," *Proc. Third Summer Software Engineering Workshop*, NASA Goddard Space Flight Center; NTRS 19820068869). Substituting gives $t_{\min} = \big(\text{LOC}/(C\,\lvert\nabla D\rvert^{1/3})\big)^{3/7}$. His worked example, 98,475 source statements with $C = 10040$ and $\lvert\nabla D\rvert = 15$, gives 1.81 years.

*[Derived (Conditional on S1–S2 and on a sufficient transmission time that does not fall with effort).]* The specification bound has no effort term. Let $\tau = \inf_{c} \text{time}_{\text{transmit}}(F, c, M_{\text{shared}})$ for a system specified as one feature $F$, and suppose adding effort does not shorten it: the distinguishing information comes from a source whose rate does not grow with the team, such as a single customer. Then $t \geq \tau$ at every effort, and the software equation, which puts $t$ below any positive constant once $E$ is large enough, can hold only while

$$E \leq \left(\frac{\text{LOC}}{C}\right)^{3} \tau^{-4}.$$

Beyond that effort the bound, not the fit, sets the schedule. So any law of Putnam's form must stop holding under compression, whatever the staffing limit. *[Hypothesis.]* That observed compression limits, Putnam's difficulty-gradient limit among them, are in part this transmission limit is a conjecture of this theory. It predicts that projects of equal size, technology constant and staffing gradient have longer minimum schedules when the specification carries more distinguishing information or reaches the team through a slower channel. Putnam's $\lvert\nabla D\rvert$, which he relates to how much of the work can proceed concurrently, does not represent either. The prediction is untested.

**Lineage of the existence argument.** Premise S1 is the software instance of the basic lower-bound argument of communication complexity: to distinguish one of $N$ admissible alternatives, a receiver must be sent at least $\log_2 N$ bits by some protocol (Kushilevitz & Nisan 1997, *Communication Complexity*, Cambridge University Press). The specification bound adds the claim that this transmission takes time, and the observation that shared context shrinks the admissible set.

## Working Notes

- 2026-07-14 label adjudication: the general bound's derivation is now exhibited explicitly (premises S1–S2) rather than asserted; the $H_{\text{req}}/R_{\text{spec}}$ line was retagged Derived→Formulation (it is a Shannon-patterned modeling choice, not derived here); the `conditional` status's gating conditions (sufficiency informal; reliability premise) are now named in Epistemic Status. Promoting the Formulation back to Derived requires formalizing $H_{\text{req}}$ as a conditional entropy and $R_{\text{spec}}$ as a capacity.
- The strongest next tightening would be to define "sufficient" more formally: e.g. the channel must reduce the implementer's posterior uncertainty over acceptable implementations below some task-dependent threshold. Right now sufficiency is intuitive rather than operationalized.
- This segment was written by an earlier agent with less context (noted in WORKBENCH). Needs a review pass during Part I/IV tightening — particularly to connect to the AAT communication framework ( #hyp-communication-gain) and to make the information-theoretic derivation more explicit.
- The $H_{\text{req}} / R_{\text{spec}}$ expression is still a first-order approximation. A tighter version would separate encoding efficiency, channel noise, and interactive back-and-forth — but that may be over-engineering for a bound that is primarily conceptual.
