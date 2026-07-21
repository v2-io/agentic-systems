# Batch 5 — def-adaptive-tempo, hyp-mismatch-dynamics, persistence-and-limits-intro, der-deliberation-cost, form-sector-condition (+ appendix deriv-sector-condition)

Appendix rule fired via hyp-mismatch-dynamics → deriv-sector-condition. Reading the appendix at first reference paid off enormously: the intro-chapter's claims ("containment dichotomy," "what disappears at the threshold is the certificate") only became precise there.

## Predictions vs evidence

- def-adaptive-tempo: predicted the sum form; did NOT predict `status: conditional` on a *definition* — the honest reasoning: the definition is advertised as an operationalization, and that interpretation is exact only under (1) cross-channel noise independence and (2) shared-eigenbasis/isotropy. The additivity story is deeper than I knew: the deviation from additivity is **signed** (echo-chamber overcounting with closed-form redundancy penalty and saturation under shared bias, but noise-cancelling *under*counting), so "additive tempo is an upper bound" is **refuted** — a resolved-then-refuted trail visible right in the WN (2026-07-14 adjudication → 2026-07-15 derivation refuting the bound form). Two no-gos: no sign-blind dependence measure can carry the correction; no convention-free per-channel attribution for n≥3 (PID impossibility). A tensor tempo (matrix gains, eigenvalue per-direction rates) handles anisotropy; scalar overestimates by 72% in a 5:1 anisotropic sim.
- hyp-mismatch-dynamics: as predicted (linear ODE, heuristic, fluid limit), plus the **Model D vs Model S steady-state split** I hadn't fully placed this early: $\rho/\mathcal T$ vs $\sigma_w/\sqrt{2\mathcal T}$. Correction fights drift linearly but noise only as a square root — this propagates to adversarial exponents ($b=2$ vs $3/2$).
- form-sector-condition: predicted (A1)/(A2')/(A3); the depth is the **sub-scope α/β partition**: A2' *derived* (via gain-sector bridge B1 directional fidelity) for Bayesian/exponential-family/strongly-convex-gradient/L2-regularized/linear-PD agents; *assumed per-system* for PID/rule-based/human/misspecified/variational/non-convex-beyond-basin/per-step-SGD. Plus the operator-theory positioning (A2' = one-point strong monotonicity; sub-scope α = cocoercive families; AAT as specialization+repurposing of monotone-operator theory — stated with explicit humility). The **structural Lipschitz floor**: rule-based/discontinuous correction is a *structural scope-exit* (sector bound cannot imply contraction across rule-firing jumps; hybrid-dissipative machinery is the right apparatus) with a concrete counterexample.
- deriv-sector-condition: the four anchor results in full. A.1 ($R^\ast = \rho/\alpha$; positive invariance of $\mathcal B_R$ when $\alpha R > \rho$); **Lemma A.1N** — the once-claimed fixed-agent "iff" is *false in general* (the dip counterexample: sector floor at unreachable radii; the true agent-level escape threshold is a mountain-pass quantity); necessity is *class-level*, agent-level only under radially tight sector (linear case). A.1S region-aware stopped bounds + fixed-time tail; **Corollary A.1S.1**: $P(\tau_R<\infty) \in \{0,1\}$ exactly — 0 under Model D, 1 under Model S, **α-invariant** — correction strength cannot interpolate; the kind of guarantee, not the rate, changes. A.2: $\Delta\rho^\ast = \alpha R - \rho$.
- der-deliberation-cost: as predicted (threshold inequality $\Delta\eta^\ast\cdot\Vert\delta_{post}\Vert > \rho_{delib}\Delta\tau$, conditional on local-drift assumption, finite optimum under diminishing returns). The honest scope note: the formal benefit channel is *epistemic* ($\eta^\ast$ improvement), while many canonical examples (MCTS, MPC) are action-value deliberation — acknowledged, not yet formalized.

## The big picture that assembled this batch

Part I's climax structure is now visible whole: linear ODE (heuristic) → sector condition (formulation, two-tier grounding) → Lyapunov results (exact, with class-level-not-agent-level necessity) → containment dichotomy (exact, new) → structural-adaptation genericity. The single most misquotable chain in the corpus:

1. "$\alpha > \rho/R$ is necessary and sufficient for persistence" — **wrong as stated**; sufficiency + class-level necessity; fixed-agent iff only when radially tight.
2. "Strong enough correction keeps a stochastic agent in its region" — **wrong**; exit is a.s. for any α, any A2'-satisfying F. α buys typical scale and fixed-time tails only.
3. "Below threshold, mismatch diverges" — **wrong**; the *certificate* is lost (and escape forced only for the extremal/tight cases); the dip counterexample shows condition-failure ≠ certified escape.

These three are the sharpest expert-tier quiz material in the whole volume so far — each is a strengthen-before-soften scar the corpus wears openly (the WN provenance notes document the audit → attempted-strengthening → no-go/split trail for each).

Also: the "certificate voice" is now a recognizable register. Persistence claims are claims about *what can be guaranteed and by what kind of witness*, not about what will happen to a given agent. Summary-readers systematically read certificate-voice claims as behavior-voice claims. That's the deepest single comprehension seam I've found.

## Smaller notes

- persistence-and-limits-intro's structural-vs-task-adequacy split (machinery-works vs works-well-enough; the second is a domain parameter, not derived) — category-error guard for domain transfer. Bathtub figure with 3-layer isomorphic captioning is in-corpus (the Alan Walton gloss institutionalized).
- Thermodynamic shadow: $\dot R \geq n\alpha/2$ nats/time (deriv-persistence-cost, appendix, not yet read — it's not in any depends so far; will read if/when depended or at the appendix sweep). "Survival is a sustained burn rate."
- Tempo's WN shows a *live ripple ledger*: disc-independence-audit §3 still states the refuted general inequality per the WN note — a known-unexecuted ripple. Not my finding (recorded in-corpus), but I'll verify if I reach disc-independence-audit.
- der-deliberation-cost + emp-update-gain "Open questions" blocks inside claims-verified segments — known convention-texture item.

## Watch-list updates

- Resolved: sector-condition grounding (the α demotion story is real and careful); Model-S/Model-D asymmetry.
- Carry: result-sector-condition-stability and result-persistence-condition (next batch) must carry certificate-voice + no fixed-agent iff (regression guard is in deriv WN); verify.
- Carry: does result-structural-adaptation-necessity deliver the intro's "central result" promise at inevitability grade, with the genericity handed off from Cor A.1S.1 (note sketch-structural-adaptation-genericity in appendix flags a possible mild overclaim in the hand-off — will read when referenced).
- New: mood segments (def-mood, der-mood-timescale) are `draft` insertions into this chapter — check integration texture next batch.

## Predictions for batch 6 (der-gain-sector-bridge, result-sector-condition-stability, result-persistence-condition, def-mood, der-mood-timescale)

der-gain-sector-bridge: B1 directional fidelity $\delta^T H g(\delta) \geq c_{min}\Vert\delta\Vert^2$ ⇒ A2' with $\alpha = \eta^\ast c_{min}$ (Prop B.3); five failure modes named (FM-1 rotation, gain collapse, saturation, unobservable directions, misspecification aim); Kalman/gradient equivalences in appendix deriv-gain-sector (in depends? likely — will read). result-sector-condition-stability: certificate-voice restatement of A.1/A.1S for the body. result-persistence-condition: $\alpha > \rho/R$ with the class-level necessity phrasing and adaptive reserve; probably where the bathtub Brief lives. def-mood: leaky integral of mismatch modulating gain/tempo — a slow second-order outer loop; predict conditional/draft status, OU-environment assumption in der-mood-timescale's $\tau^\ast \propto \sqrt{\tau_{env}}$ (bias-variance argument, my batch-1 prediction of a conditional sketch stands).
