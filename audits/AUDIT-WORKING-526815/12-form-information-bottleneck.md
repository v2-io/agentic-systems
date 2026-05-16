# 12 - form-information-bottleneck

Segment: `01-aat-core/src/form-information-bottleneck.md`
Dependencies: `form-agent-model`, `def-action-transition` - satisfied.
Status observed: `type: formulation`, `status: exact`, `stage: draft`.
External spot-check: Tishby, Pereira & Bialek 1999 / arXiv physics/0004057 after segment read.

## Reflection

The core AAT binding is natural: `X = C_t`, bottleneck variable `T = M_t`, relevance variable `Y = future observations conditioned on future actions`. The objective shape `I(X;T) - beta I(T;Y)` checks against the original IB paper. I also like the policy-relativity caveat; future observations are not a neutral target when the agent's actions alter what it will see.

The main concern is exactness of the stated optimization object. The original IB variational problem optimizes over conditional encoders `p(\tilde{x}|x)`; this segment writes `phi^* = argmin_phi` and inherits `phi: C^* -> M` from `form-agent-model`, which reads deterministic. A deterministic map is a special case or a different deterministic-IB formulation, not the full standard theorem. If `phi` is intended as shorthand for a stochastic Markov kernel from histories to model states, the segment should say so. If not, the "exact applied external theorem" status is overstated for the displayed equation even though the mutual-information trade-off itself is correct.

## Prompt pass

Predictions vs evidence: I predicted an IB objective targeted at future observations. Correct. I also predicted possible operational-measurability and status issues; the deterministic-vs-stochastic encoder issue is sharper than expected.

Cross-segment consistency: consistent with `form-agent-model` if `phi` is just a generic compression. But the exact theorem import strains against `form-agent-model`'s deterministic-looking map. Forward references to many downstream compression/strategy segments are discussion-level; unlike F2, they are not necessary to understand the local core.

Math / citation verification: sampled the original paper. The paper's functional is `L[p(tilde{x}|x)] = I(tilde X;X) - beta I(tilde X;Y)` and the self-consistent solution is for conditional distributions `p(tilde{x}|x)`. So the segment's objective has the right information terms but appears to narrow the encoder class without saying so.

Direction next: `def-model-sufficiency` should define a ratio against full-history predictive power. I will watch whether it uses the deterministic `M_t` state or a distribution over model states.

Errors to watch: exact theorem labels where the AAT binding changes the theorem's optimization domain; beta/rho qualitative claims living under a frontmatter `status: exact`; policy-conditioning on future action sequences being under-specified before value/continuation conventions exist.

What I would change: replace `argmin_phi` with an optimization over encoders/kernels `p(M_t | C_t)` or explicitly state that AAT restricts to deterministic encoders and is using the deterministic special case. Also consider a frontmatter status that exposes mixed exact/robust-qualitative layers.

Curiosity: whether the deterministic map is deliberate because `M_t` is the actual realized state of a concrete agent. If so, the segment may need two layers: agent-realization `M_t = phi(C_t)` and optimal-reference encoder `q(M|C)`.

New knowledge enabled: model sufficiency and class fitness can be grounded in retained predictive information rather than vague model quality.

Audit process change: keep external theorem checks focused on whether AAT preserves theorem hypotheses and optimization objects, not merely whether the formula resembles the theorem.

Running outline change: add F3 candidate: IB exact theorem imported over stochastic encoders but segment displays deterministic `phi`.

Value feel: high. This is a powerful segment, and the candidate issue is fixable but important because the segment's status is `exact`.

## Diagram thought

The diagram should contrast two encoders: the segment's displayed `phi: C -> M` and the IB theorem's stochastic `p(M|C)`. The visual should not imply the segment is wrong wholesale; it should show that the exact theorem lives at the kernel level, while deterministic `phi` is a restricted lane inside it.
