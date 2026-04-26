# 16 — deriv-recursive-update

Appendix jump from `der-recursive-update`.
Dependencies checked: `form-agent-model`, `form-event-driven-dynamics`, `post-causal-structure`, `scope-adaptive-system`, and `def-observation-function` already read.

## Reflection

The appendix proof is stronger and more honest than the main segment summary.
It explicitly separates the eliminative constraints (arrow of time, partial observability) from the definitional constraint (state completeness).
That is the right epistemic posture.

The Doob-Dynkin formulation is a clean technical proof path:
if the agent's information set at $\tau$ is $\sigma(M_{\tau^-},e_\tau)$, then $M_{\tau^+}$ is a measurable function of $(M_{\tau^-},e_\tau)$.
This proves the representation given the information-set restriction.

The "uniqueness" claim is valid in a representation-theoretic sense, not in an independently discovered dynamics sense.
The appendix acknowledges this:
C3 is definitional and can absorb apparent counterexamples by expanding $M$.
That makes the result exact under the modeling commitment, but it should not be oversold as a physical theorem about all possible cognitive architectures.

Important limitation surfaced by the appendix itself:
Attack 2 says continuous environmental influence is a genuine limitation of the event-driven formulation and the more general form is $\dot M=g(M,u)$.
This means the event-driven recursive update is exact for event/sampled systems, while continuous coupling needs the control-theoretic generalization.
The main segment's between-event corollary $dM/d\tau=g_M(M_\tau)$ should probably carry the same caveat more prominently.

Status reconciliation:
The appendix frontmatter says `status: exact`; the main `der-recursive-update` frontmatter says `conditional`; the main Epistemic Status says "Exact, with a partly definitional character."
After reading the appendix, I think the strongest accurate label is "exact conditional on C1-C3 and event-driven/sampled representation; continuous coupling generalizes the input form."
The mismatch is not fatal, but the status language should be harmonized.

Dependency / upstream issue:
Because `deriv-recursive-update` depends on `scope-adaptive-system`, it inherits the unresolved issue that adaptive scope is using action-coupled primitives and an initially missing chronica definition.
The derivation itself also uses action-completion events; passive observers can be represented with observation-only events, but that should be stated.

Math verification:
No algebra error found.
The proof is mostly information-set elimination; I find it sound under its definitions.

What this enables:
It gives the rest of AAD permission to operate on local update functions rather than full histories, while making the cost of that permission explicit: $M$ must be complete relative to the analysis.

Prediction after returning to main outline:
`der-action-selection` should define policy as a function of $M_t$ and possibly mark action selection as exact only after agency scope.
I will watch whether it depends on `scope-agency` or only on adaptive primitives.

Running report update:
- Candidate status/style finding: harmonize exact vs conditional recursive-update labels and carry continuous-coupling caveat into main segment.
- No math error in the recursive-update derivation under stated constraints.
