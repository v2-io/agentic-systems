# 03 — def-observation-function

`type: definition · status: axiomatic · stage: deps-verified · depends: [def-agent-environment, def-action-transition]`

## Dep-graph / OUTLINE-order check
Both deps are segments 01, 02 — already read in order. `depends:` on
`def-action-transition` is *genuine* (the $a_{t-1}$ argument of $h$ uses it),
so Gate-1 dependency is real, not "merely mentioned." No violation. B7 alive.

## Prompt walk (light segment — brief by design, not by neglect)

**1 Predictions vs evidence.** Segment-02 prediction landed exactly:
$o_t=h(\Omega_t,a_{t-1},\varepsilon_t)$, `axiomatic`, deps = agent-env +
action-transition. No surprise.

**2 Cross-segment consistency.** Consistent with 01 (lossiness = the
constitutive boundary, here *localized to $h$*) and with NOTATION. Mild
watch-note (**THREAD-C**, low priority): $\varepsilon_t$ is introduced here as
"noise or limits of perception," distribution unknown to the agent; GA-1
("fresh noise": $\varepsilon_t \perp \mathcal C_{t-1}\mid(\Omega_t,a_{t-1})$)
will later constrain its *conditional independence* and is load-bearing for
`result-mismatch-decomposition`. Check there that GA-1 is flagged as the
assumption doing the cross-term-killing work, not absorbed silently. (This is
the segment-01 prediction about `result-mismatch-decomposition` re-stated with
the specific mechanism now named.)

**3 Math.** None. Reduction "$a_{t-1}$ absent $\Rightarrow h(\Omega_t,
\varepsilon_t)$" is consistent with NOTATION.

**6 Next-segment prediction.** OUTLINE next: `def-chronica` — the interaction
history $\mathcal C_t=(o_1,a_1,\dots,a_{t-1},o_t)$; `axiomatic`/definitional;
`depends:` on the three primitives so far (agent-env, action-transition,
observation-function). It is the object $\phi$ compresses into $M_t$, so it is
the bridge from primitives to the reality model.

**7 What I'd change.** Nothing. The segment is correctly minimal. The
active-perception remark ("what the agent sees may depend on where it looked")
is a strong, cheap intuition that pays off later (CIY, exploration); fine
where it is.

**9/13 Enables.** Localizing the loss to a named map $h$ is what makes the
*amount* of loss a later first-class quantity (the $U_o$ machinery). Active
perception ($a_{t-1}\to h$) is the seed of "observation quality partly under
agent control" → causal information yield, the exploration drives. Light file,
structurally load-bearing for the CIY line.

**12 Felt value.** Low magnitude, foundational-confirming. The triple
(01,02,03) is a clean, honest primitive layer; positive §E calibration that
the discipline holds at the foundation.

## Wandering thoughts (≤2 ¶)

The thing worth one paragraph: AAT splits the world→agent corruption into
*structural loss* ($h$ many-to-one) and *stochastic noise* ($\varepsilon_t$),
and makes both opaque to the agent. This is the same two-channel decomposition
that will reappear as model-error vs observation-noise in the mismatch
decomposition — so the segment is quietly pre-installing the bias/variance
split at the *definitional* layer rather than introducing it as a derivation
artifact later. That is good architecture: the decomposition you want to
derive is already latent in how you defined the primitive, so the later
"derivation" is really an *unfolding* of a definitional choice. The auditor's
note-to-self: when I reach `result-mismatch-decomposition`, ask whether it is
a genuine identity or a restatement of this definitional two-channel split —
either is fine, but the epistemic label should match which it is.

The active-perception clause is the most generative seed in this otherwise
inert segment. By letting $o_t$ depend on $a_{t-1}$, AAT makes "looking" an
action with epistemic consequence *at the definitional layer*, which is
exactly what later licenses treating exploration as a first-class control
variable rather than a heuristic add-on. It is a small inclusion with a long
shadow; I will watch whether the later CIY / exploration segments actually
cash this dependence in (use the $a_{t-1}$ argument of $h$ structurally) or
merely gesture at it.

## Diagram

Isomorphic content: $h$ is a **many-to-one** (lossy) map — distinct $\Omega$
states collapse to the same $o$ — *steered* by $a_{t-1}$ (active perception
re-partitions what is resolvable) and *jittered* by $\varepsilon_t$. Perturb
by making $h$ injective ⇒ no collapse ⇒ ties back to seg-01 degeneracy. The
fan-in collapse is the load-bearing picture of "information is destroyed."
See `03-def-observation-function.tex`.
